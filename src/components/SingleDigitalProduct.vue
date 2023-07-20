<template>


  <div class="modal modal-transition" v-show="showModal" >
    <div class="bg-white product-card card rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto">
      <div class="close-button-cont">
        <button @click="closeModal" class="close-button">
          <svg class="w-6 h-6 fill-current text-gray-500 hover:text-gray-700" xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24">
            <path
              d="M18.364 5.636a2 2 0 0 0-2.828 0L12 9.172 8.464 5.636a2 2 0 1 0-2.828 2.828L9.172 12l-3.536 3.536a2 2 0 1 0 2.828 2.828L12 14.828l3.536 3.536a2 2 0 1 0 2.828-2.828L14.828 12l3.536-3.536a2 2 0 0 0 0-2.828z" />
          </svg>
        </button>
      </div>
      <div v-if="productDigit" class="flex flex-col md:flex-row">
        <div class="w-full md:w-1/2" >
          <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]" style="height: 460px;">
            <h3 class="text-xl font-semibold mb-2 text-left">Preview:</h3>
            <p class="text-gray-600 text-lg text-left">{{ productDigit.additional_details }}</p>
            <p v-if="!hasPurchased" class="text-red-500 text-sm mt-2">For complete view buy the product</p>
          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8 text-left card-content" style="overflow: auto; height: 460px;">
          <div style="box-sizing: border-box;">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300">
            {{ productDigit.name}}
          </h2>
          <div class="mt-4">
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-l-show mr-2 font-semibold">Tienda:</span>
              <span class="text-lg">{{ productDigit.store_id.nameStore }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Fecha de Publicacion:</span>
              <span class="text-lg">{{ productDigit.dateCreated }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad</span>
              <span class="text-lg">{{ product.quantity }}</span>
            </div>
            <div class="flex items-center mb-2">
              <p class="text-2xl font-semibold mr-2">{{ productDigit.price}}</p>
              <p v-if="productDigit.needChecker" class="ml-2 text-gray-600 text-sm">(+{{ product.checkerPrice.toFixed(2) }} del Checker)</p>
            </div>
            <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2 text-left">Detalles adicionales:</h3>
            <p class="text-gray-600 text-lg text-left">asdasdasdasdasdasdasfasdfgvsdfgasdfgsdfgasg awetge g erg d dsyhsd erty eg sdfy gery eryw5t egrtgserth sertsertg erer erg e esyweg e aqt efawevrw fweterferwr54t  t eart ergser b et ert ertwet ert  ertge gegerge   r geg eg eret  ergey asg hreruy e eythrdhedghr sh erthrt sr sdryh seyher thsrt se yesy seysr hfhgjdhkrtu  seg hsrthdrh rhsrtuy sdtdryjsdhdrfth f</p>
          </div>

            <!-- Botón Need checker -->
            <div class="flex items-center mb-2" v-if="!checkerView">
              <button
                v-if="productDigit.needChecker"
                @click="openCheckerModal"
                class="bg-red-500 hover:bg-green-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500 mr-2"
              >
                Necesita verificacion
              </button>
              <button
                v-else
                class="bg-green-500 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 mr-2"
                disabled
              >
                Verificado
              </button>
            </div>

            <div class="flex items-center mb-2" v-if="checkerView ">
              <button
                v-if = "status != 'active'" 
                @click="makeActionInChecking(this.productDigit.id,'approve',this.orderS)"
                class="bg-green-500 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 mr-2"
              >
                Aprobar
              </button>
              <button
              @click="makeActionInChecking(this.productDigit.id,'refuse',this.orderS)"
                v-if="status != 'canceled'"
                class="bg-red-500 hover:bg-green-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500 mr-2"
              >
                Retirar
              </button>
            </div>

            <div class="flex mt-4 justify-end" v-if="!checkerView">
              <button
                @click="buyNow"
                class="bg-[#f76108] hover:bg-[#fa7328] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#f76108] mr-2"
              >
                Comprar ahora
              </button> 
            </div>
            <div class="espacio"></div>
          </div>
        </div>
        </div>
      </div>
      <div v-else class="text-center py-8">
        <p class="text-lg text-gray-600">Cargando datos del producto...</p>
      </div>
    </div>

    <!-- Ventana emergente de pago -->
    <transition name="modal">
      <div v-if="showPaymentModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Confirmar compra</h2>
          <p>Producto: {{ productDigit.name }}</p>
          <p>Cantidad: 1</p>
          <p>Precio total: {{ productDigit.price}}</p>
          <p v-if="addChecker" class="text-red-500 text-sm">Los productos digitales comprados sin checker no tienen derecho a garantía.</p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible: <span class="text-green-500">{{ user.balance }}</span></p>
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="confirmPayment(productDigit.id)" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Confirmar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de pago exitoso -->
    <transition name="modal">
      <div v-if="showSuccessModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Pago Exitoso</h2>
          <p>¡Gracias por tu compra!</p>
          <div class="mt-4">
            <h3 class="text-xl font-semibold mb-2">Factura:</h3>
            <p>Orden: {{ orderNumber }}</p>
            <p>Producto: {{ productDigit.name }}</p>
            <p>Cantidad: 1</p>
            <p>Tienda: {{ productDigit.store_id.nameStore }}</p>
          </div>
          <div class="flex justify-end mt-4">
            <button @click="showSuccessModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
            <button @click="downloadInvoice" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Descargar Factura</button>
            <button @click="downloadContent" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Descargar Contenido</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de transacción declinada -->
    <transition name="modal">
      <div v-if="showDeclinedModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Transacción declinada</h2>
          <p>Lo sentimos, no tienes fondos suficientes para completar la compra.</p>
          <div class="flex justify-end mt-4">
            <button @click="showDeclinedModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de Need Checker -->
    <transition name="modal">
      <div v-if="showCheckerModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Solicitud de checking</h2>
          <p class="text-red-500">Este producto requiere el uso de un checker.</p>
          <p style="margin-top: 10px;">
          Mediante esta solicitud, el usuario tendra verificacion validada de que el producto existe, sin embargo, el precio sumado sera de <b>+{{ priceChecker.toFixed(2) }}</b>
          </p>
          <div class="flex justify-end mt-4">
            <button @click="closeCheckerModal" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
            <button v-if="productDigit.needChecker" @click="sendCheckerRequest(productDigit.id)" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Solicitar</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";
import jsPDF from "jspdf";
import Cookies from "js-cookie";

export default {
  props : {
    modalInfo: Object
  },
  
  watch : {
    modalInfo(newValue) {
      if (newValue.typeProd == 'digits') {
        this.showModal = newValue.showDigitModal
        this.status = newValue.status
        this.orderS = newValue.order
        this.renderDigitProductData(newValue.objID, newValue.typeProd)
      }  
    }
  },

  created() {
    this.takeUserInfo();
  },

  

  data() {
    return {
      pagesFisic: 0,
      orderS:0,
      status:"",
      showModal:false,
      checkerView: false,
      productDigit: null,
      hasPurchased: false,
      quantity: 1,
      btcPrice: 40000,
      showDigitModal: false,
      user: {
        name: "",
        balance: 0,
      },
      priceChecker: 22.00,
      showPaymentModal: false,
      showSuccessModal: false,
      showDeclinedModal: false,
      showCheckerModal: false,
      checkerInput: "",
      addChecker: false,
      orderNumber: "",
      transactionAddress: "",
    };
  },

  mounted() {
    this.product = {
      name: '',
      description: '',
      price: 0,
      likes: 0,
      dislikes: 0,
      additionalDetails:'',
      release_data: "",
      quantity: 0,
      category: [],
      subcategory: [],
      seller_username: "",
      checkerPrice: 0, // Precio adicional del checker
    };
  },
  methods: {
    async makeActionInChecking(id, type,ordID) {
      console.log(ordID);
      if(type=='approve') {
        await axios.put(`http://127.0.0.1:8000/api/productos/digit/${id}/${ordID}`,{status:true})
        .then(response => {
          console.log(response.data)
          this.$emit('updated')
        })
        .catch(error => {
          console.log(error)
        })
      }else if (type == 'refuse'){
        await axios.put(`http://127.0.0.1:8000/api/productos/digit/${id}/${ordID}`,{status:false})
        .then(response => {
          console.log(response.data)
          this.$emit('updated')
        })
        .catch(error => {
          console.log(error)
        })
      }
    },

    buyNow() {
      if(Cookies.get('token') == null) {
        console.log(2222)
        this.$router.push('/login')
      }
      this.showPaymentModal = true;
    },
    confirmPayment(id) {
      console.log(id, this.user.balance, this.productDigit.price)
      if (parseInt(this.user.balance) >= parseInt(this.productDigit.price)) {
        this.showPaymentModal = false;
        this.showSuccessModal = true;
        this.orderNumber = Math.floor(Math.random() * 1000000);
        this.quantity = 1;
        this.makeTransact(id)
        this.addChecker = false;
      } else {
        this.showPaymentModal = false;
        this.showDeclinedModal = true;
      }
    },
    async renderDigitProductData(id,type) {
      await axios.get(`http://127.0.0.1:8000/api/productos/digit/${id}`)
      .then(response => {
        if( type == 'checker') { 
          this.checkerView = true
        }
          this.productDigit = response.data
      })
      .catch(error => {
        console.log(error.response.data)
      })
    },

    async makeTransact(id) {
      await axios.post(`http://127.0.0.1:8000/api/productos/transacts/digits`,{productDigit_id:id}, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      }) 
      .then( response => {
        console.log(response.data)
      })
      .catch (error => {
        console.log(error.response.data)
      })
    },

    async takeUserInfo() {
      let token = Cookies.get('token')
      if (token != null) {
        this.hasToken = true 
        await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(response => {
          this.user.username = response.data.name; 
          this.user.balance = response.data.userBalance
        })
        .catch(error => {})
      }
      
    },

    downloadInvoice() {
      const doc = new jsPDF();
      doc.setFontSize(18);
      doc.text("Factura de Compra", 20, 20);
      doc.setFontSize(12);
      doc.text(`Orden: ${this.orderNumber}`, 20, 30);
      doc.text(`Producto: ${this.product.name}`, 20, 40);
      doc.text(`Cantidad: ${this.quantity}`, 20, 50);
      doc.text(`Tienda: ${this.product.brand}`, 20, 60);
      doc.text(`Dirección de la Transacción: ${this.transactionAddress}`, 20, 70);
      doc.save("invoice.pdf");
    },
    downloadContent() {
      const text = this.product.additionalDetails;
      const element = document.createElement("a");
      const file = new Blob([text], { type: "text/plain" });
      element.href = URL.createObjectURL(file);
      element.download = "content.txt";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    },
    closeCheckerModal() {
      this.showCheckerModal = false;
    },
    openCheckerModal() {
      this.showCheckerModal = true;
    },
    closeModal(){
      this.showModal = false
      this.productFisic = null
      this.method = null
    },
    async sendCheckerRequest(id) {
      console.log(id)
      await axios.post(`http://127.0.0.1:8000/api/solicChecker/${id}`,null,{
        headers:{
            Authorization:`Token ${Cookies.get('token')}`
        }})
      .then(response=> {console.log(response.data)})
      .catch(error => {console.log(error.response.data)})
      this.showCheckerModal = false;
    },
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.close-button-cont {
  display: flex;
  justify-content: flex-end ;
}

.close-button {
    margin-bottom: 8px;
    margin-top: 0px;
}

@media (max-width: 768px) {
  .product-card {
    max-width: 500px;
    max-height: 750px;
    margin-top: 78px !important;
    overflow: auto;
  }

  .product-card::-webkit-scrollbar {
    width: 0;
  }
  .component-container-color2::-webkit-scrollbar {
    width: 0;
  }

  .slider-container {
    max-width: 277px !important;
  }

  .card-content { 
    overflow: unset !important;
  }
}


.bg-white {
  margin: 0 auto;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.select-variant {
  text-align: left;
  width: 100%;
}

.fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.bg-black {
  background-color: #000;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-4 {
  padding: 1rem;
}

.md\:p-8 {
  padding: 2rem;
}

.transition-colors {
  transition-property: color;
  transition-duration: 0.5s;
}

.hover\:bg-blue-50:hover {
  background-color: #f0f4ff;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.text-left {
  text-align: left;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.card {
  width: 985px;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-orange-600 {
  color: #fb923c;
}

.hover\:text-purple-800:hover {
  color: #6b46c1;
}

.mt-8 {
  margin-top: 2rem;
}

.space-x-4 > * {
  margin-right: 1rem;
}

.mt-4 {
  margin-top: 1rem;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.mr-2 {
  margin-right: 0.5rem;
}

.text-green-500 {
  color: #84cc16;
}

.font-extrabold {
  font-weight: 800;
}

.text-red-500 {
  color: #f87171;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.mt-4 {
  margin-top: 1rem;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
  margin-top:20px ;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-[#f76108] {
  background-color: #f76108;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #fa7328;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.text-white {
  color: #fff;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #d836e8;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.modal-transition {
    opacity: 0;
    animation: modalT 0.4s forwards;
}


@keyframes modalT{
0%{
  opacity: 0;
}
100% {
  opacity: 1;
}

}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

</style>
