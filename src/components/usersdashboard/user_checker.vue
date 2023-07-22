<template>
    <div class="order-review">
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4 fontHeader">Aprobadas</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('active')">
            <button class="accordion-button"  :class="{ 'active': activeAccordion === 'active' }">
              Aprobadas
            </button>
          </h3>
          <div v-show="activeAccordion === 'active'"  class="accordion-collapse" :class="{'keyup':activeAccordion  === 'keyup'}">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">Fecha de aprobación</th>
                  <th class="py-2">Comision</th>
                  <th class="py-2">Opciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in activeOrders" :key="order.checkerId">
                  <td class="py-2">{{ order.product.id }}</td>
                  <td class="py-2">{{ order.product.name   }}</td>
                  <td class="py-2">{{ order.dateCreated }}</td>
                  <td class="py-2">{{ order.product.comisionCheck }}</td>
                  <td><button @click.stop="openDetailsModal(order.product.id, 'checker',order.status,order.id)" class="px-2 py-1 bg-orange-500 text-white rounded ml-2" style="margin:0px">Ver detalles</button></td>

                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
      
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4 fontHeader">Pendientes de Revisión</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('pending')">
            <button class="accordion-button" :class="{ 'active': activeAccordion === 'pending' }">
              Pendientes de Revisión
            </button>
          </h3>
          <div v-show="activeAccordion === 'pending'" class="accordion-collapse">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">Fecha de solicitud</th>
                  <th class="py-2">No. Solicitudes</th>
                  <th class="py-2">Comision</th>
                  <th class="py-2">Opciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in pendingOrders" :key="order.id">
                  <td class="py-2">{{ order.product.id }}</td>
                  <td class="py-2">{{ order.product.name }}</td>
                  <td class="py-2">{{ order.dateCreated }}</td>
                  <td class="py-2">{{ order.product.no_solicitud }}</td>
                  <td class="py-2">{{ order.product.comisionCheck }}</td>
                  <td><button @click="openDetailsModal(order.product.id, 'checker',order.status,order.id)" class="px-2 py-1 bg-orange-500 text-white rounded ml-2" style="margin:0px">Ver detalles</button></td>

                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
        <SingleDigitalProduct :modalInfo="modalData" @updated="handleUpdateChecking"></SingleDigitalProduct>
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4 fontHeader  ">Rechazadas</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('expired')">
            <button class="accordion-button" :class="{ 'active': activeAccordion === 'expired' }">
              Rechazadas
            </button>
          </h3>
          <div v-show="activeAccordion === 'expired'" class="accordion-collapse">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">Fecha de rechazo</th>
                  <th class="py-2">No. Solicitudes</th>
                  <th class="py-2">Precio</th>
                  <th class="py-2">Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in expiredOrders" :key="order.checkerId">
                  <td class="py-2">{{ order.product.id }}</td>
                  <td class="py-2">{{ order.product.name }}</td>
                  <td class="py-2">{{ order.dateCreated }}</td>
                  <td class="py-2">{{ order.product.no_solicitud }}</td>
                  <td class="py-2">{{ order.product.price }}</td>
                  
                  <td><button @click="openDetailsModal(order.product.id, 'checker',order.status,order.id)" class="px-2 py-1 bg-orange-500 text-white rounded ml-2" style="margin:0px">Ver detalles</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
    </div>
  </template>
  
  <script>
import axios from 'axios';
import SingleDigitalProduct from '../SingleDigitalProduct.vue';

  export default {
    components: {
    SingleDigitalProduct,
},

    created() {
      this.getSolicPendingOrders()
      this.getSolicRefusedOrders()
      this.getSolicActiveOrders()
    },



    data() {
      return {
        activeOrders: [],
        pendingOrders: [],
        modalData: null,
        expiredOrders: [],
        activeAccordion: "",
        showModal: false
      };
    },
    methods: {
      handleUpdateChecking() {
        this.$emit('updated')
      },

      openDetailsModal(id, type, status, idOrd) {
            console.log(id)
            console.log(type);
            console.log(status);
            if(type == "checker") {
                this.modalData = {showDigitModal: true,typeProd: type, objID: id, status:status,order:idOrd }
            }
        },

      async getSolicPendingOrders() {
        console.log(2222)
       await axios.get(`http://127.0.0.1:8000/api/solicChecker?pending=true`)
       .then(response => {
        this.pendingOrders = response.data
        console.log(this.pendingOrders)
      })
       .catch(error => {console.log(error.response.data)})
      },

      async getSolicActiveOrders() {
       await axios.get(`http://127.0.0.1:8000/api/solicChecker?approved=true`)
       .then(response => {
        this.activeOrders = response.data
        console.log(this.activeOrders)
      })
       .catch(error => {console.log(error.response.data)})
      },

      async getSolicRefusedOrders() {
       await axios.get(`http://127.0.0.1:8000/api/solicChecker?canceled=true`)
       .then(response => {
        this.expiredOrders = response.data
        console.log(this.expiredOrders)
      })
       .catch(error => {console.log(error.response.data)})
      },

      toggleAccordion(accordionName) {
        if (this.activeAccordion === accordionName) {
          this.activeAccordion = "keyup";
        } else {
          this.activeAccordion = accordionName;
        }
      }
    }
  };
  </script>
  
  <style scoped>

  .fontHeader {
    color: #ad3700;
  }
  .column {
    flex-grow: 1;
  }
  .order-review {
    max-width: 800px;
    padding: 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(561px, 1fr));
    grid-gap: 49px;
    min-width: 100%;
  }
  
  .table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #fffbf7;
  }
  
  .table th,
  .table td {
    border: 1px solid #fffbf7;
    padding: 0.75rem;
  }
  
  .accordion {
    border: 1px solid #e2d1c7;
    border-radius: 0.375rem;
    overflow: hidden;
  }
  
  .accordion-item {
    border-bottom: 1px solid #fffbf7;
  }
  
  .accordion-header {
    padding: 1rem;
    background-color: #fffbf7;
    border-bottom: 1px solid #e2e8f0;
    cursor: pointer;
  }
  
  .accordion-button {
    background-color: transparent;
    border: none;
    text-align: center;
    width: 100%;
    transition: background-color 0.4s ease;
  }
  
  .accordion-button:focus {
    outline: none;

  }
  
  .accordion-button.active {
    background-color: #ffebd8;
    text-align: center;
  }
  
  .accordion-collapse {
    background-color: #fffbf7;
    display: none;
    animation: displayXY 0.8s ease;
  }

  

  @keyframes displayXY {
    from {
      max-height: 0;
      opacity: 0;
    }
    to {
      max-height: 1000px;
      opacity: 1;
    }
  }
  
  .accordion-collapse[style] {
    display: block;
  }
  
  .accordion-body {
    padding: 1rem;
  }
  </style>
  