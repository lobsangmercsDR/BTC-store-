<template >
  <div class="modal" v-if="showModal" >
    <div class="bg-white rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto" style="padding: 20px 32px;">
      <button @click="closeModal" class="close-button">
          <svg class="w-6 h-6 fill-current text-gray-500 hover:text-gray-700" xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24">
            <path
              d="M18.364 5.636a2 2 0 0 0-2.828 0L12 9.172 8.464 5.636a2 2 0 1 0-2.828 2.828L9.172 12l-3.536 3.536a2 2 0 1 0 2.828 2.828L12 14.828l3.536 3.536a2 2 0 1 0 2.828-2.828L14.828 12l3.536-3.536a2 2 0 0 0 0-2.828z" />
          </svg>
        </button>
      <div v-if="product" class="flex flex-col md:flex-row" style="    height: 500px;
    width: 875px;">

        <div class="w-full md:w-1/2">
          <div class="max-w-[200px] mx-auto md:max-w-none">
            <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]" style="display: flex;">
              <img class="container-img" :src="'http://127.0.0.1:8000/api' + product.image_product"  alt="">
            </div>
          </div>
          <div class="flex justify-center mt-4 space-x-2 overflow-x-auto scrollbar-hide">

          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8" style="overflow: auto;">
          <div class="content">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300 ">
            {{ product.nameProduct }}
          </h2>
          <span class="text-gray-600 text-lg mr-2 font-semibold"></span>

          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad:</span>
            <input v-model="quantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="1" />
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Marca:</span>
            <span class="text-lg">{{ product.brand }}</span>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Vendedor:</span>
            <span class="text-lg">{{ product.seller.name }}</span>
          </div>
          <div class="flex items-center mb-4" style="display: block;">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Zona de entrega:</span>  <br>
            <span class="text-lg">{{ product.address_direction }}</span>
          </div>
          <!-- <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Likes:</span>
            <span class="text-lg">{{ product.likes }}</span>
            <button @click="incrementLikes" class="text-green-500 hover:text-green-600 focus:outline-none"
              :disabled="liked">
              <svg class="w-6 h-6 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path
                  d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8s3.589-8 8-8 8 3.589 8 8-3.589 8-8 8z" />
                <path
                  d="M15.707 9.293l-4 4a.997.997 0 0 1-1.414 0l-2-2a.999.999 0 1 1 1.414-1.414L11 10.586l3.293-3.293a.999.999 0 1 1 1.414 1.414z" />
              </svg>
            </button>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2 font-semibold">Dislikes:</span>
            <span class="text-lg">{{ product.dislikes }}</span>
            <button @click="incrementDislikes" class="text-red-500 hover:text-red-600 focus:outline-none"
              :disabled="disliked">
              <svg class="w-6 h-6 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path
                  d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8s3.589-8 8-8 8 3.589 8 8-3.589 8-8 8z" />
                <path d="M8 8h8v8H8z" />
              </svg>
            </button>
          </div> -->
          <div class="flex mb-2">
            <p class="text-2xl font-semibold mr-2"> Precio: {{ product.price }}</p>
          </div>
          <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2 text-left">Detalles adicionales:</h3>
            <p class="text-gray-600 text-lg text-left">{{ product.aditional_details }}</p>
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
      <div v-else class="text-center py-8">
        <p class="text-lg text-gray-600">Cargando datos del producto...</p>
      </div>
      
    </div>

    <!-- Ventana emergente de pago -->
    <transition name="modal">
      <div v-if="showPaymentModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Confirmar compra</h2>
          <p>Producto: {{ product.nameProduct }}</p>
          <p>Marca: {{ product.brand }}</p>
          <p>Tienda: {{ product.seller.name }}</p>
          <p>Cantidad: {{ quantity }}</p>
          <p>Precio total: {{  (product.price * quantity)}} </p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible: <span class="text-green-500">{{ user.balance.toFixed(2) }}</span></p>
          <input v-model="shippingAddress" type="text"
            class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-full mt-4"
            placeholder="Dirección de envío" required />
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="processPayment"
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
          <p>Tu transacción ha sido rechazada debido a fondos insuficientes.</p>
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
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Factura generada</h2>
          <p>Número de orden: {{ orderNumber }}</p>
          <p>Fecha de compra: {{ formattedDate }}</p>
          <p>Estado: En espera</p>
          <p>Nombre del producto: {{ product.nameProduct }}</p>
          <p>Marca: {{ product.brand }}</p>
          <p>Tienda: {{ product.seller.name }}</p>
          <p>Cantidad comprada: {{ quantity }}</p>
          <p>Total a pagar: {{ (product.price * quantity).toFixed(2) }} </p>
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
import  axios  from 'axios';

export default {
  props: {
    modalInfo : Object
  },
  watch: {
    modalInfo(newValue) {
      this.showModal = newValue.showModal
      if (newValue.typeProd == 'fisic') {
        this.renderProductData(newValue.objID)
      }
    }
  },
  data() {
    return {

      showModal: false,
      product: null,
      quantity: 1,
      selectedVariant: '',
      productPriceBTC: 0,
      showPaymentModal: false,
      processingTransaction: false,
      showTransactionFailedModal: false,
      showInvoiceModal: false,
      user: {
        username: 'JohnDoe',
        balance: 10000, // Saldo ficticio en BTC
      },
      shippingAddress: '',
      orderNumber: '',
      formattedDate: '',
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
    }
  },
  methods: {
    async renderProductData(id) {
      await axios.get(`http://127.0.0.1:8000/api/productos/${id}`)
        .then(response => {this.product = response.data; console.log(this.product)})
        .catch(error => console.log(error.response.data))
    },


    incrementLikes() {
      if (!this.liked && !this.disliked) {
        this.product.likes++;
        this.liked = true;
      }
    },
    closeModal(){
      this.showModal = false
    },



    incrementDislikes() {
      if (!this.liked && !this.disliked) {
        this.product.dislikes++;
        this.disliked = true;
      }
    },
    convertToDollars(price) {
      return price * this.btcPrice;
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
      this.showPaymentModal = true;
    },
    processPayment() {
      this.processingTransaction = true;
      setTimeout(() => {
        if (this.user.balance >= this.product.price * this.quantity) {
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.showInvoiceModal = true;
          this.orderNumber = Math.floor(Math.random() * 1000000).toString().padStart(6, '0');
        } else {
          this.showPaymentModal = false;
          this.processingTransaction = false;
          this.showTransactionFailedModal = true;
        }
      }, 2000);
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

.bg-white {
  margin: 0 auto;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.close-button {
  margin-left: 53.5em;
    margin-bottom: 20px;
    margin-top: 0px;
}


.close-button svg:hover {
  color: rgb(212, 0, 255) !important;
}

.select-variant {
  width: 200px;
}
</style>
