<template >
  <div class="modal" v-show="showFisicModal" :class="{'modal-transition':showFisicModal}" >
    <div class="bg-white rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto card-container" style="padding: 20px 32px; max-height: 645px;  min-width: 435px; width: 860px;">
      <div class="close-button-cont">
        <button @click="closeModal" class="close-button">
          <svg class="w-6 h-6 fill-current text-gray-500 hover:text-gray-700" xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24">
            <path
              d="M18.364 5.636a2 2 0 0 0-2.828 0L12 9.172 8.464 5.636a2 2 0 1 0-2.828 2.828L9.172 12l-3.536 3.536a2 2 0 1 0 2.828 2.828L12 14.828l3.536 3.536a2 2 0 1 0 2.828-2.828L14.828 12l3.536-3.536a2 2 0 0 0 0-2.828z" />
          </svg>
        </button>
      </div>
      <div v-if="productFisic" class="flex flex-col md:flex-row" >
        <div class="w-full md:w-1/2">
          <div class="max-w-[200px] mx-auto md:max-w-none">
            <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]" style="display: flex;">
              <img class="container-img" :src="'http://127.0.0.1:8000/api' + productFisic.image"  alt="">
            </div>
          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8 modCont" style="overflow: auto;">
          <div class="content">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300 ">
            {{ productFisic.name }}
          </h2>
          <span class="text-gray-600 text-lg mr-2 font-semibold"></span>

          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad:</span>
            <input v-model="quantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="1" />
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Marca:</span>
            <span class="text-lg">{{ productFisic.brand }}</span>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Tienda:</span>
            <span class="text-lg">{{ productFisic.store.nameStore }}</span>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad Disponible:</span>
            <span class="text-lg">{{ productFisic.actQuantity }}</span>
          </div>
          <div class="flex items-center mb-4" style="display: block;">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Zona de entrega:</span>  <br>
            <span class="text-lg">{{ productFisic.address_direction }}</span>
          </div>
          <div class="flex mb-2">
            <p class="text-2xl font-semibold mr-2"> Precio: {{ productFisic.price }}</p>
          </div>
          <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2 text-left">Detalles adicionales:</h3>
            <p class="text-gray-600 text-lg text-left">{{ productFisic.aditional_details }}</p>
          </div>
          <div class="flex mb-4 space-x-4 justify-end">
            <button @click="buyNow"
              class="bg-[#ac15c1] hover:bg-[#d836e8] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#ac15c1]">
              Comprar ahora
            </button>
          </div>
          </div>
        </div>
      </div>
      <div v-if="method" class="flex flex-col md:flex-row" style="    height: 500px;">

        <div class="w-full md:w-1/2">
          <div class="max-w-[200px] mx-auto md:max-w-none">
            <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]" style="display: flex;">
              <img class="container-img" :src="'http://127.0.0.1:8000/api' + method.image"  alt="">
            </div>
          </div>
          <div class="flex justify-center mt-4 space-x-2 overflow-x-auto scrollbar-hide">

          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8 modCont" style="overflow: auto;">
          <div class="content">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300 ">
            {{ method.nameProduct }}
          </h2>
          <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Tienda:</span>
            <span class="text-lg">{{ method.store.nameStore }}</span>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad Disponible:</span>
            <span class="text-lg">Infinity</span>
          </div>
          <div class="flex mb-2">
            <p class="text-2xl font-semibold mr-2"> Precio: {{ method.price }}</p>
          </div>
          <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2 text-left">Detalles adicionales:</h3>
            <p class="text-gray-600 text-lg text-left" style="word-wrap: break-word;">{{ method.description}}</p>
          </div>
          <div class="flex mb-4 space-x-4 justify-end">
            <button @click="buyNow"
              class="bg-[#ac15c1] hover:bg-[#d836e8] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#ac15c1]">
              Comprar ahora
            </button>
          </div>
          </div>
        </div>
      </div>
      <!-- <div v-else class="text-center py-8">
        <p class="text-lg text-gray-600">Cargando datos del producto...</p>
      </div> -->
      
    </div>

    <!-- Ventana emergente de pago -->
    <transition name="modal">
      <div v-if="showPaymentModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div v-if="productFisic" class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Confirmar compra</h2>
          <p>Producto: {{ productFisic.name}}</p>
          <p>Marca: {{ productFisic.brand }}</p>
          <p>Tienda: {{ productFisic.store.nameStore }}</p>
          <p>Cantidad: {{quantity }}</p>
          <p>Precio total: {{  (productFisic.price * quantity)}} </p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible: <span class="text-green-500">{{ user.balance }}</span></p>
          <input v-model="transactInfo.sendDirection" type="text"
            class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-full mt-4"
            placeholder="Dirección de envío" required />
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="processFisicPayment"
              class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Confirmar</button>
          </div>
        </div>
        <div v-if="method" class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Confirmar compra</h2>
          <p>Producto: {{ method.nameProduct }}</p>
          <p>Precio: {{ method.price }}</p>
          <p>Tienda: {{ method.store.nameStore }}</p>
          <p>Precio total: {{  (method.price * quantity)}} </p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible: <span class="text-green-500">{{ user.balance }}</span></p>
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="processMethodPayment"
              class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Confirmar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de transacción en proceso -->
    <transition name="modal">
      <div v-if="processingTransaction" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Procesando transacción</h2>
          <p>Por favor, espera mientras se procesa tu transacción...</p>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de transacción fallida -->
    <transition name="modal">
      <div v-if="showTransactionFailedModal"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Transacción fallida</h2>
          <p>Tu transacción ha sido rechazada debido a fondos insuficientes o cantidad inexistente.</p>
          <div class="flex justify-end mt-4">
            <button @click="showTransactionFailedModal = false"
              class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de factura generada -->
    <transition name="modal">
      <div v-if="showInvoiceModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div v-if="productFisic" class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Factura generada</h2>
          <p>Número de orden: {{ orderNumber }}</p>
          <p>Fecha de compra: {{ formattedDate }}</p>
          <p>Estado: En espera</p>
          <p>Nombre del producto: {{ productFisic.name }}</p>
          <p>Marca: {{ productFisic.brand }}</p>
          <p>Tienda: {{ productFisic.store.nameStore }}</p>
          <p>Cantidad comprada: {{ quantity }}</p>
          <p>Total a pagar: {{ (productFisic.price * quantity).toFixed(2) }} </p>
          <button class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded mt-4"
            @click="downloadInvoice">Descargar factura</button>
          <div class="flex justify-end mt-4">
            <button @click="showInvoiceModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
          </div>
        </div>
        <div v-if="method" class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Factura generada</h2>
          <p>Número de orden: {{ orderNumber }}</p>
          <p>Fecha de compra: {{ formattedDate }}</p>
          <p>Estado: En espera</p>
          <p>Nombre del producto: {{ method.nameProduct }}</p>
          <p>Tienda: {{ method.store.nameStore }}</p>
          <p>Cantidad comprada: {{ quantity }}</p>
          <p>Total a pagar: {{ (method.price * quantity).toFixed(2) }} </p>
          <button class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded mt-4"
            @click="downloadInvoice">Descargar factura</button>
          <div class="flex justify-end mt-4">
            <button @click="showInvoiceModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import Cookies from 'js-cookie';
import  axios  from 'axios';
import SingleDigitalProduct from './SingleDigitalProduct.vue';
export default {
  components: {
    SingleDigitalProduct
  },
  props: {
    modalInfo : Object
  },

  created()  {
    this.takeUserInfo();

  },
  watch: {
    modalInfo(newValue) {
      console.log(newValue)
      this.showFisicModal = newValue.showFisicModal
      let id = newValue.objID
      if (newValue.typeProd == 'fisic') {
        this.renderProductFisicData(id.split('.')[1])
        
      }
      else if(newValue.typeProd== 'method') {
        this.renderMethodData(id)
      }
    }
  },
  data() {
    return {

      showModal: false,
      showFisicModal:false,
      productFisic: null,
      productDigital: {
        id: "1",
        name:"señor amparame"
      },
      method:null,
      quantity: 1,
      selectedVariant: '',
      productPriceBTC: 0,
      showPaymentModal: false,
      processingTransaction: false,
      showTransactionFailedModal: false,
      showInvoiceModal: false,
      transactInfo: { 
        productDigit_id: 0,
        quantity_asked: 0,
        sendDirection:""
      },
      user: {
        username: 'JohnDoe',
        balance: 10000, // Saldo ficticio en BTC
      },
      shippingAddress: '',
      orderNumber: '',
      liked: false,
      disliked: false,
    };
  },
  mounted() {
    this.product = {
      id: 1,
      name: 'Producto',
      price: 0.011, // Precio ficticio en BTC
      brand: 'Marca de producto',
      likes: 0,
      dislikes: 0,
      variants: ['Chocolate Sativa', 'Berry Hibrida', 'Indica Girlscout Cookies'],
      additionalDetails:
        'sssssssssssssssssssssssss ssssssss sssssssssss sssssssssssssss sdsa s dsd sssss     sdsd sd dsd     sd  ',
      sellerUsername: 'JohnSeller',
    };
    this.productPriceBTC = this.product.price * this.btcPrice;
  },

  computed: {
    OpenModal(){
      value = this.modalInfo
      console.log(value)
      return value
    },
  },
  methods: {
    async renderProductFisicData(id) {
      console.log(id)
      await axios.get(`http://127.0.0.1:8000/api/productos/${id}`)
        .then(response => {
          this.productFisic = response.data;
          this.transactInfo.productDigit_id =id
        })
        .catch(error => console.log(error.response.data))
    },

    async renderMethodData(id) {
      await axios.get(`http://127.0.0.1:8000/api/productos/methods/${id}`)
        .then(response => {
          this.method = response.data;
          this.transactInfo.productDigit_id = response.data.id

        })
        .catch(error => console.log(error.response.data))
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

    incrementLikes() {
      if (!this.liked && !this.disliked) {
        this.product.likes++;
        this.liked = true;
      }
    },
    closeModal(){
      this.showFisicModal = false
      this.productFisic = null
      this.method = null
    },



    incrementDislikes() {
      if (!this.liked && !this.disliked) {
        this.product.dislikes++;
        this.disliked = true;
      }
    },
    addToCart() {
      const item = {
        id: this.product.id,
        name: this.product.name,
        price: this.product.price,
        quantity: this.quantity,
        variant: this.selectedVariant,
      };
      this.addToCartLocal(item); // Modificamos la llamada a `addToCartLocal`
      this.showPaymentModal = true;
    },
    removeProduct(product) {
      this.removeFromCart(product.id);
    },
    buyNow() {
      if(Cookies.get('token') == null) {
        console.log(2222)
        this.$router.push('/login')
      }
      this.showPaymentModal = true;
    },
    processFisicPayment() {
      this.processingTransaction = true;
      setTimeout(() => {
        if ((this.user.balance >= this.productFisic.price * this.quantity) && (this.productFisic.actQuantity != 0)) {
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.orderNumber = Math.floor(Math.random() * 1000000).toString().padStart(6, '0');
          this.transactInfo.quantity_asked = this.quantity
          this.makeTransact()
        } else {
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.showTransactionFailedModal = true;
        }
      }, 2000);
    },

    processMethodPayment() {
      this.processingTransaction = true;
      setTimeout(() => {
        console.log(this.user.balance);
        let balance = this.user.balance
        let price = this.method.price
        console.log(typeof(balance), typeof(price));
        if ( parseInt(balance) >= parseInt(price)) {
          console.log("AAAw");
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.showInvoiceModal = true;
          this.orderNumber = Math.floor(Math.random() * 1000000).toString().padStart(6, '0');
          this.transactInfo.quantity_asked = this.quantity
          this.makeMethodTransact()
        } else {
          console.log(this.user.balance, this.method.price);
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.showTransactionFailedModal = true;
        }
      }, 2000);
    },

    async makeTransact() {
      console.log("llegue")
      await axios.post(`http://127.0.0.1:8000/api/transacts`,this.transactInfo, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
        }})
        .then(response => {
          this.showInvoiceModal = true
          this.takeUserInfo()
        })
        .catch(error =>
        {
          console.log(error.response.data)
        })
    },

    async makeMethodTransact() {
      console.log("llegue")
      delete this.transactInfo.sendDirection 
      await axios.post(`http://127.0.0.1:8000/api/productos/transacts/methods`,this.transactInfo, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
        }})
        .then(response => {
          console.log(response)
          this.takeUserInfo()
        })
        .catch(error =>
        {
          console.log(error.response.data)
        })
    },
    downloadInvoice() {
      const invoiceData = {
        product: this.product.name,
        variant: this.selectedVariant,
        brand: this.product.brand,
        sellerUsername: this.product.sellerUsername,
        quantity: this.quantity,
        totalPriceBTC: (this.product.price * this.quantity * this.btcPrice).toFixed(8),
        totalPriceUSD: (this.product.price * this.quantity).toFixed(2),
        shippingAddress: this.shippingAddress,
        date: this.formattedDate,
        orderNumber: this.orderNumber,
      };

      const invoiceText = `
        Factura de compra
        
        Número de orden: ${invoiceData.orderNumber}
        Fecha de compra: ${invoiceData.date}
        
        Producto: ${invoiceData.product}
        Variante: ${invoiceData.variant}
        Marca: ${invoiceData.brand}
        Username del vendedor: ${invoiceData.sellerUsername}
        Cantidad: ${invoiceData.quantity}
        Precio total: ${invoiceData.totalPriceBTC} BTC / $${invoiceData.totalPriceUSD} USD
        
        Dirección de envío: ${invoiceData.shippingAddress}
        
        Gracias por usar nuestra web.
      `;

      const element = document.createElement('a');
      const file = new Blob([invoiceText], { type: 'text/plain' });
      element.href = URL.createObjectURL(file);
      element.download = 'factura.txt';
      document.body.appendChild(element);
      element.click();
    },
  },
  computed: {
    cartTotal() {
      return this.$store.getters['cart/cartTotal'];
    },
    formattedDate() {
      return new Date().toLocaleDateString();
    },
  },
};
</script>


<style scoped>
.modal-transition {
    opacity: 0;
    animation: modalT 0.4s forwards;
}




@keyframes modalT{
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@media (max-width: 768px){
  .card-container {
    max-width: 475px !important;
  }
}


.card-container {
  max-width: 951px;
  overflow: auto;
}
.container-img {
      width: 100%;

    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.modCont::-webkit-scrollbar {
  width: 0;
}

.bg-white {
  margin: 0 auto;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.close-button {
    margin-bottom: 20px;
}

.close-button-cont {
  display: flex;
  justify-content: flex-end;
}


.close-button svg:hover {
  color: rgb(212, 0, 255) !important;
}

.select-variant {
  width: 200px;
}
</style>
