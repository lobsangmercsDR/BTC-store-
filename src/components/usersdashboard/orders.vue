<template>
  <div class="bg-white rounded shadow">
    <div class="px-4 py-3 border-b">
      <h2 class="text-lg font-semibold">Mis órdenes</h2>
    </div>
    <div class="p-4">
      <div v-if="ordersPhisics.length === 0" class="text-gray-600">
        No hay órdenes disponibles.
      </div>
      <div v-for="(orderList, orderType) in ordersByType" :key="orderType" >
        <h3 @click="toggleOrderSection(orderType)" class="text-lg font-semibold mt-4 cursor-pointer">
          Órdenes de productos {{ orderType === 'physical' ? 'físicos' : 'digitales' }}
          <span v-if="isOrderSectionOpen(orderType)" class="text-sm ml-2">[-]</span>
          <span v-else class="text-sm ml-2">[+]</span>
        </h3>
        <table v-show="isOrderSectionOpen(orderType)" class="table-auto w-full text-left">
          <thead>
            <tr>
              <th class="px-4 py-2">ID de orden</th>
              <th class="px-4 py-2">Fecha</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in orderList" :key="order.id" class="cursor-pointer">
              <td class="border px-4 py-2">{{ order.id }}</td>
              <td class="border px-4 py-2">{{ order.dateTransact }}</td>
              <td class="border px-4 py-2">{{ order.status }}</td>
              <td class="border px-4 py-2">
                
                <button @click.stop="openReportModal(order)" class="px-2 py-1 bg-orange-500 text-white rounded mt-0">Reportar problema</button>
                <button @click.stop="openDetailsModal(order)" class="px-2 py-1 bg-blue-500 text-white rounded ml-2 mt-0">Ver detalles</button>
                <button class="px-2 py-1 bg-red-500 text-white rounded ml-2 mt-0" @click="removeOrder(order.id)" v-show="orderType  != 'virtual'">Retirar</button>
              </td>
            </tr>
          </tbody>
        </table>
        <section v-if="orderType == 'virtual' && isOrderSectionOpen(orderType)" class="nav-arrows">
              
              <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,-1)" :style="{color:previousArrowColor}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 18l-6-6 6-6"/>
              </svg> 
              <div  class="pageCounter"> <span>{{ pageInfoD.actualPage }}</span></div>
 
              <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,1)" :style="{color:nextArrowColor}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 18l6-6-6-6"/>
              </svg>
        </section>

        <section v-if="orderType == 'physical' && isOrderSectionOpen(orderType)" class="nav-arrows">
              
              <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,-1)" :style="{color:previousArrowColorF}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 18l-6-6 6-6"/>
              </svg> 
              <div  class="pageCounter"> <span>{{pageInfo.actualPage}}</span></div>
 
              <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,1)" :style="{color:nextArrowColorF}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 18l6-6-6-6"/>
              </svg>
        </section>
      </div>
      
    </div>
    <transition name="modal">
      <div class="fixed z-10 inset-0 overflow-y-auto" v-if="detailsModalOpen">
        <div class=" items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4 modal-details" v-if="selectedOrder.productDigit != null">
              <h2 class="">Detalles de la orden</h2>
              <hr>
              <p><b>Fecha: </b> {{ selectedOrder.dateTransact }}</p>
              <p><b>Estado: </b> {{ selectedOrder.status}}</p>
              <h3 style="font-size: 18px; margin: 4px 11px; text-decoration: underline;"><b>Producto:</b></h3>
              <p><b>Nombre: </b> {{ selectedOrder.productDigit.name}}</p>
              <p><b>Precio: </b> {{ selectedOrder.productDigit.price}}</p>
              <p><b>Comision de Checker: </b> {{ selectedOrder.productDigit.comisionCheck}}</p>
              <p><b>Precio Total: </b> {{ parseInt(selectedOrder.productDigit.price) + parseInt(selectedOrder.productDigit.comisionCheck)}}.00</p>
              <p><b>Verificado: </b> {{(selectedOrder.productDigit.needChecker ===true) ? 'Si' : 'No'}}</p>
              <p><b>Tienda: </b> {{ selectedOrder.productDigit.store_id.nameStore}}</p>
              <p><b>Contacto de vendedor: </b>809-555-2222 </p>

            </div>
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4 modal-details" v-if="selectedOrder.productFisic != null">
              <h2 class="">Detalles de la orden</h2>
              <hr>
              <p><b>Fecha: </b> {{ selectedOrder.dateTransact }}</p>
              <p><b>Estado: </b> {{ selectedOrder.status}}</p>
              <p><b>Cantidad Pedida: </b> {{ selectedOrder.quantity_asked}}</p>
              <p><b>Dirección: </b> {{ selectedOrder.sendDirection}}</p>
              <p><b>Precio Total: </b> {{ (parseInt(selectedOrder.productFisic.price) * parseInt(selectedOrder.quantity_asked)).toFixed(2) }}</p>
              <h3 style="font-size: 18px; margin: 4px 11px; text-decoration: underline;"><b>Producto:</b></h3>
              <p><b>Nombre: </b> {{ selectedOrder.productFisic.nameProduct}}</p>
              <p><b>Precio: </b> {{ parseInt(selectedOrder.productFisic.price).toFixed(2)}}</p>
              <p><b>Marca: </b> {{ selectedOrder.productFisic.brand}}</p>
              <p><b>Categoria: </b> {{ selectedOrder.productFisic.subCategory.nameSub}}</p>
              <!-- <p><b>Precio Total: </b> {{ parseInt(selectedOrder.productDigit.price) + parseInt(selectedOrder.productDigit.comisionCheck)}}.00</p>
              <p><b>Verificado: </b> {{(selectedOrder.productDigit.needChecker ===true) ? 'Si' : 'No'}}</p>
              <p><b>Tienda: </b> {{ selectedOrder.productDigit.store_id.nameStore}}</p> -->
              <p><b>Contacto de vendedor: </b>809-555-2222 </p>

            </div>
            <div class="px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button @click.stop="closeDetailsModal" type="button" class="px-4 py-2 bg-blue-500 text-white rounded ">Cerrar</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="modal">
      <div class="fixed z-10 inset-0 overflow-y-auto" v-if="reportModalOpen">
        <div class="items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4" style="padding-bottom: 0px;">
              <h3 class="text-lg leading-6 font-medium text-gray-900">Reportar problema</h3>
              <p>{{ selectedOrder.productFisic != null  ? 'Quejas de productos físicos' : 'Quejas de productos digitales' }}</p>
              <textarea maxlength="401" v-model="rMessage" @input="updateTextLength" class="txt-complains"></textarea>
              <p>{{ textlength }}/400</p>
            </div>
            <div class="px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse" style="padding-top: 8px;">
              <button @click.stop="closeReportModal" type="button" class="px-4 py-2 bg-red-500 text-white rounded ml-3">Cerrar</button>
              <button @click.stop="SendReport(selectedOrder.id)" type="button" class="px-4 py-2 bg-blue-500 text-white rounded">Enviar</button>
            </div>
            <div v-if="detailsReportModal" class="modal">
                <div class="modal-content">
                  <div class="modal-header">
                    <h2>Detalles de reporte</h2>
                      <p style="text-align: center;">Su reporte ha sido enviado con exito</p>
                    <hr style="margin:10px 0px ;">
                    <p><b>No. de orden:  </b>{{ reportObj.noReporte  }}</p>
                    <p><b>Fecha: </b>{{ reportObj.dateReport }}</p>
                    <p><b>Estado: </b>{{ reportObj.status }}</p>
                  </div>
                  <button @click.stop="closeReportModal" type="button" class="px-4 py-2 bg-red-500 text-white rounded ml-3 INTbutton">Cerrar</button>
                </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>

import axios from "axios";
import Cookies from "js-cookie";

export default {


  data() {
    return {
      ordersPhisics: [],
      ordersDigits: [],
      reportObj: null,
      pageInfo: {
          actualPage: 1,
          available_page:0
        },
      pageInfoD: {
          actualPage: 1,
          available_page:0
        },
      orderSections: {
        physical: true,
        virtual: true,
      },
      detailsModalOpen: false,
      textlength:0,
      detailsReportModal: false,
      rMessage: '',
      reportModalOpen: false,
      selectedOrder: null,
    };
  },

  created() {
    this.renderOrdersDigitData()
    this.renderOrdersPhisicsData()
  },

  computed: {
    previousArrowColor() {
            const page = this.pageInfoD.actualPage;
            if (page === 1) {
                return '#c2c2c2'; 
            } else {
                return ''; 
            }
        },
      
        previousArrowColorF() {
            const page = this.pageInfo.actualPage;
            console.log(page)
            if (page === 1) {
                return '#c2c2c2'; 
            } else {
                return ''; 
            }
        },

        nextArrowColor() {
            const pageNext = this.pageInfoD.available_page

            if (pageNext == 0) {
                return '#c2c2c2'
            } else {
                return ''
            }
        },

        nextArrowColorF() {
            const pageNext = this.pageInfo.available_page
          console.log(pageNext)
            if (pageNext == 0) {
                return '#c2c2c2'
            } else {
                return ''
            }
        },

    ordersByType() {
      return {
        physical: this.ordersPhisics,
        virtual: this.ordersDigits,
      };
    }
  },
  methods: {
    async renderOrdersPhisicsData(pageF=1) {
      await axios.get(`http://127.0.0.1:8000/api/transacts?fisics=true&page=${pageF}&pw=5`, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      }) 
        .then(response => {
          console.log(response.data)
          this.ordersPhisics  = response.data.data
          this.pageInfo.actualPage = response.data.actual_page
          this.pageInfo.available_page = response.data.available_pages
          console.log(this.pageInfo);

        })
        .catch(error => {
          console.log(error.response.data)
        });
      },

     async renderOrdersDigitData(pageD=1) {
      await axios.get(`http://127.0.0.1:8000/api/transacts?digitals=true&pw=5&page=${pageD}`, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        this.ordersDigits = response.data.data
        this.pageInfoD.actualPage = response.data.actual_page
        this.pageInfoD.available_page = response.data.available_pages
      })
      .catch(error => {
        console.log(error)
      })
     }, 

    async removeOrder(id) {
      if(!confirm('¿Esta seguro que desea retirar esa orden?')) {
        console.log('no');
        return ''
      }
      console.log(id);
      await axios.delete(`http://127.0.0.1:8000/api/transacts/${id}`)
      .then(response => {
        this.renderOrdersPhisicsData(this.pageInfo.actualPage)
        console.log(response.data)
      })
      .catch(error => {
        console.log(error.response.data)
      })
    },

    async handleChangePage(type,steps) {
      console.log(type);
      if(type=='virtual') {
        if(this.pageInfoD.actualPage+steps != 0) {
          this.renderOrdersDigitData(this.pageInfoD.actualPage+steps)
        }
      }
      else if (type == 'physical') {
        console.log(steps)
        console.log('fisical');
        if(this.pageInfo.actualPage+steps != 0)  {
          this.renderOrdersPhisicsData(this.pageInfo.actualPage+steps)
        }
      }
    },

    async SendReport(transactID) {
      console.log(transactID)
      console.log(this.rMessage);
      await axios.post(`http://127.0.0.1:8000/api/reports/${transactID}`,{rMessage:this.rMessage}, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        this.reportObj = response.data
        this.detailsReportModal = true
      })
      .catch(error => {
        console.log(error)
      })
      
    }, 

    updateTextLength() {
      this.textlength = this.rMessage.length
    },

    toggleOrderSection(orderType) {
      this.orderSections[orderType] = !this.orderSections[orderType];
    },
    isOrderSectionOpen(orderType) {
      return this.orderSections[orderType];
    },
    openDetailsModal(order) {
      this.selectedOrder = order;
      this.detailsModalOpen = true;
    },
    closeDetailsModal() {
      this.selectedOrder = null;
      this.detailsModalOpen = false;
    },
    openReportModal(order) {
      this.selectedOrder = order;
      this.reportModalOpen = true;
    },
    closeReportModal() {
      this.selectedOrder = null;
      this.reportModalOpen = false;
      this.detailsReportModal = false;
      this.rMessage = ""
      this.textlength = 0
      this.reportObj = null
    },
  }
}
</script>


<style scoped>

.nav-arrows {
    display: flex;
    justify-content: flex-end;
    margin-top: auto;
}
.pageCounter {
  display: flex;
  align-items: center;
  padding: 1px 10px;
  border: 2px gray solid;
  border-radius: 5px;
}

.pageCounter span {
  user-select: none;
}

.arrow-icon {
  height: 35px;
  user-select: none;
}

button {
  margin-top: 0px;
}

.INTbutton {
  width: 83px;
    display: right;
    margin-left: auto;
}
.button {
  margin-top: 0px !important;
}

.txt-complains {
    padding: 15px;
    margin-top:15px;
    border: 2px black solid;
    border-radius: 11px;
    width: 100%;
    min-height: 216px;
}

.table-auto {
  width: 100%;
  max-width: 100%;
  margin-bottom: 1rem;
  border-collapse: collapse;
}

.modal-content {
  max-width: 340px;
    min-height: 291px;
  
    display: flex;
    flex-direction: column;
    justify-content: space-between;

}

.modal-header h2{
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}

.modal-header p {
  padding: 5px;
}

.modal-details h2{
  text-align: center;
    margin-bottom: 9px;
    font-size: 19px;
    font-weight: bold;
}

.modal-details p {
  margin: 11px 10px;
    font-size: 16px;
}

.table-auto th,
.table-auto td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table-auto thead th {
  border-bottom: 2px solid #dee2e6;
}

.table-auto tbody+tbody {
  border-top: 2px solid #dee2e6;
}
</style>
