<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto">
      <div v-if="product" class="flex flex-col md:flex-row">
        <div class="w-full md:w-1/2">
          <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]">
            <h3 class="text-xl font-semibold mb-2 text-left">Preview:</h3>
            <p class="text-gray-600 text-lg text-left">{{ product.additionalDetails }}</p>
            <p v-if="!hasPurchased" class="text-red-500 text-sm mt-2">For complete view buy the product</p>
          </div>
          <div class="flex items-center mb-2">
            <p class="text-2xl font-semibold mr-2">Categorias:</p>
            <p class="text-green-500 text-lg font-extrabold">Subcate</p>
          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8 text-left">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300">
            {{ product.name }}
          </h2>
          <div class="mt-8 flex items-center space-x-4"></div>
          <div class="mt-4">
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Vendedor:</span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Fecha de Publicacion:</span>
              <span class="text-lg">{{ product.release_data }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad</span>
              <span class="text-lg">{{ product.quantity }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Likes:</span>
              <span class="text-lg">{{ product.likes }}</span>
              <button @click="incrementLikes" class="text-green-500 hover:text-green-600 focus:outline-none">
                <svg
                  class="w-6 h-6 fill-current"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8s3.589-8 8-8 8 3.589 8 8-3.589 8-8 8z"
                  />
                  <path
                    d="M15.707 9.293l-4 4a.997.997 0 0 1-1.414 0l-2-2a.999.999 0 1 1 1.414-1.414L11 10.586l3.293-3.293a.999.999 0 1 1 1.414 1.414z"
                  />
                </svg>
              </button>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Dislikes:</span>
              <span class="text-lg">{{ product.dislikes }}</span>
              <button @click="incrementDislikes" class="text-red-500 hover:text-red-600 focus:outline-none">
                <svg
                  class="w-6 h-6 fill-current"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8s3.589-8 8-8 8 3.589 8 8-3.589 8-8 8z"
                  />
                  <path d="M8 8h8v8H8z" />
                </svg>
              </button>
            </div>
            <div class="flex items-center mb-2">
              <p class="text-2xl font-semibold mr-2">{{ productPriceBTC.toFixed(8) }} BTC</p>
              <p class="text-green-500 text-lg font-extrabold">
                ${{ convertToDollars(productPriceBTC).toFixed(2) }} USD
              </p>
            </div>

            <div class="flex mt-4 justify-end">
              <button
                @click="addToCart"
                class="bg-[#f76108] hover:bg-[#fa7328] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#f76108] mr-2"
              >
                Agregar al carrito
              </button>
              <button
                @click="buyNow"
                class="bg-[#ac15c1] hover:bg-[#d836e8] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#ac15c1]"
              >
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
          <p>Producto: {{ product.name }}</p>
          <p>Cantidad: {{ quantity }}</p>
          <p>Precio total: {{ (product.price * quantity * btcPrice).toFixed(8) }} BTC / ${{ (product.price * quantity).toFixed(2) }} USD</p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible en BTC: <span class="text-green-500">{{ user.balanceBTC.toFixed(8) }} BTC</span></p>
          <p>Equivalente en USD: ${{ (user.balanceBTC * btcPrice).toFixed(2) }} USD</p>
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="confirmPayment" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Confirmar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de descarga -->
    <transition name="modal">
      <div v-if="showDownloadModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">{{ product.name }}</h2>
          <p class="text-gray-600">{{ product.additionalDetails }}</p>
          <div class="flex justify-end mt-4">
            <button @click="showDownloadModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
            <button @click="downloadPreview" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Descargar</button>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      product: null,
      quantity: 1,
      btcPrice: 27.419,
      productPriceBTC: 0,
      user: {
        username: "Djangolapara",
        balanceBTC: 2.345,
      },
      showPaymentModal: false,
      showDownloadModal: false,
      showDeclinedModal: false,
    };
  },
  mounted() {
    this.product = {
      name: 'PUFFY 2G - Girls (Super Blends)',
      description: 'Super Blends were carefully crafted to mimic the live resin experience',
      price: 0.011,
      brand: 'Puffy',
      likes: 0,
      dislikes: 0,
      additionalDetails:
        'Super Blends were carefully crafted to mimic the live resin experience. We drew our inspiration from the cannabis plant. Creating unique cannabinoid formulas with terpene profiles that mirror today’s most popular strains.',
      release_data: "Aqui fecha",
      quantity: 0,
      category: [],
      subcategory: [],
      seller_username: "Djangolapara"
    };
    this.productPriceBTC = this.product.price * this.btcPrice;
  },
  methods: {
    incrementLikes() {
      this.product.likes++;
    },
    incrementDislikes() {
      this.product.dislikes++;
    },
    convertToDollars(price) {
      return price * this.btcPrice;
    },
    addToCart() {
      console.log(`Agregando ${this.quantity} unidades del producto al carrito`);
    },
    buyNow() {
      this.showPaymentModal = true;
    },
    confirmPayment() {
      // Verificar si el usuario tiene fondos suficientes
      if (this.user.balanceBTC >= this.product.price * this.quantity) {
        console.log(`Comprando ${this.quantity} unidades del producto`);

        // Lógica adicional para procesar el pago

        // Mostrar el modal de descarga
        this.showPaymentModal = false;
        this.showDownloadModal = true;
      } else {
        // Mostrar el modal de transacción declinada
        this.showPaymentModal = false;
        this.showDeclinedModal = true;
      }
    },
    downloadPreview() {
      const text = this.product.additionalDetails;

      const element = document.createElement("a");
      const file = new Blob([text], { type: "text/plain" });
      element.href = URL.createObjectURL(file);
      element.download = "preview.txt";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
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
  background-color: rgba(0, 0, 0, 0.5);
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-8 {
  padding: 2rem;
}

.text-2xl {
  font-size: 1.5rem;
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.my-4 {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.text-gray-500 {
  color: #a0aec0;
}

.hover:text-gray-700:hover {
  color: #4a5568;
}

.text-white {
  color: #fff;
}

.bg-blue-500 {
  background-color: #4299e1;
}

.hover:bg-blue-700:hover {
  background-color: #2b6cb0;
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

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter,
.modal-leave-to {
  opacity: 0;
}

.modal-enter {
  transform: translate(-50%, -50%);
}

.modal-leave-to {
  transform: translate(-50%, -60%);
}
</style>