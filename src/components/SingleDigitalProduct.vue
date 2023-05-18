<template>
    <div class="container">
      <div class="bg-white rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto">
        <div v-if="product" class="flex flex-col md:flex-row">
          <div class="w-full md:w-1/2">
            <div v-if="product.image" class="max-w-[200px] mx-auto md:max-w-none">
              <img
                class="w-full h-auto object-contain rounded-lg transform hover:scale-105 transition-transform duration-300"
                :src="product.image"
                :alt="product.name"
              />
            </div>
            <div v-else class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]"></div>
            <div class="flex justify-center mt-4 space-x-2 overflow-x-auto scrollbar-hide">
              <div v-for="placeholderImage in placeholderImages" :key="placeholderImage.id">
                <img
                  class="w-10 h-10 object-contain rounded-lg mx-1"
                  :src="placeholderImage.image"
                  :alt="placeholderImage.name"
                />
              </div>
            </div>
          </div>
          <div class="w-full md:w-1/2 md:pl-8">
            <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300 ">
              {{ product.name }}
            </h2>
            <p class="text-gray-600 text-lg mb-4">{{ product.description }}</p>
            <div class="mt-8 flex items-center">
              <h3 class="text-xl font-semibold mb-2 text-left mr-4">Variante:</h3>
              <select class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
                <option v-for="option in product.variants" :key="option">{{ option }}</option>
              </select>
            </div>
            <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
  
            <div class="flex items-center mb-4">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad:</span>
              <input
                v-model="quantity"
                type="number"
                class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20"
                min="1"
              />
            </div>
            <div class="flex items-center mb-4">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Marca:</span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-4">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Vendedor:</span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-4">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Likes:</span>
              <span class="text-lg">{{ product.likes }}</span>
              <button
                @click="incrementLikes"
                class="text-green-500 hover:text-green-600 focus:outline-none"
              >
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
            <div class="flex items-center mb-4">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Dislikes:</span>
              <span class="text-lg">{{ product.dislikes }}</span>
              <button
                @click="incrementDislikes"
                class="text-red-500 hover:text-red-600 focus:outline-none"
              >
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
            <div class="flex mb-2">
              <p class="text-2xl font-semibold mr-2">{{ productPriceBTC.toFixed(8) }} BTC</p>
              <p class="text-green-500 text-lg font-extrabold">
                ${{ convertToDollars(productPriceBTC).toFixed(2) }} USD
              </p>
            </div>
            <div class="mt-8">
              <h3 class="text-xl font-semibold mb-2 text-left">Detalles adicionales:</h3>
              <p class="text-gray-600 text-lg text-left">{{ product.additionalDetails }}</p>
            </div>
            <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
            <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
            <div class="flex mb-4 space-x-4 justify-end">
              <!-- Aquí se aplica justify-end para alinear los botones a la derecha -->
              
              <button
                @click="addToCart"
                class="bg-[#f76108] hover:bg-[#fa7328] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#f76108]"
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
        <div v-else class="text-center py-8">
          <p class="text-lg text-gray-600">Cargando datos del producto...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        product: null,
        quantity: 1,
        placeholderImages: [
          { id: 1, name: 'Placeholder 1', image: 'https://via.placeholder.com/50x50' },
          { id: 2, name: 'Placeholder 2', image: 'https://via.placeholder.com/50x50' },
          { id: 3, name: 'Placeholder 3', image: 'https://via.placeholder.com/50x50' },
        ],
        btcPrice: 27.419, // Precio ficticio del BTC en USD
        productPriceBTC: 0,
      };
    },
    mounted() {
      this.product = {
        name: 'PUFFY 2G - Girls (Super Blends)',
        description: 'Super Blends were carefully crafted to mimic the live resin experience',
        price: 0.011, // Precio ficticio en BTC
        image: 'https://via.placeholder.com/100x100',
        brand: 'Puffy',
        shipping: 'Envío gratis',
        likes: 0,
        dislikes: 0,
        variants: ['Chocolate Sativa', 'Berry Hibrida', 'Indica Girlscout Cookies'],
        additionalDetails:
          'Super Blends were carefully crafted to mimic the live resin experience. We drew our inspiration from the cannabis plant. Creating unique cannabinoid formulas with terpene profiles that mirror today’s most popular strains.',
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
        console.log(`Comprando ${this.quantity} unidades del producto`);
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
  </style>
  