<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto">
      <div v-if="product" class="flex flex-col md:flex-row">
        <div class="w-full md:w-1/2">
          <div v-if="product.image" class="max-w-[200px] mx-auto md:max-w-none">
            <img class="w-full h-auto object-contain rounded-lg transform hover:scale-105 transition-transform duration-300"
              :src="product.image" :alt="product.name" />
          </div>
          <div v-else class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]"></div>
          <div class="flex justify-center mt-4 space-x-2 overflow-x-auto scrollbar-hide">
            <div v-for="placeholderImage in placeholderImages" :key="placeholderImage.id">
              <img class="w-10 h-10 object-contain rounded-lg mx-1" :src="placeholderImage.image"
                :alt="placeholderImage.name" />
            </div>
          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8">
          <h2 class="text-3xl font-semibold mb-4 text-blue-600 hover:text-blue-800 transition-colors duration-300">{{ product.name }}</h2>
          <p class="text-gray-600 text-lg mb-4">{{ product.description }}</p>
          <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2">Variante:</h3>
            <select class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-full">
              <option v-for="option in product.variants" :key="option">{{ option }}</option>
            </select>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2">Marca:</span>
            <span class="text-lg">{{ product.brand }}</span>
          </div>
          <div class="flex mb-2">
            <p class="text-2xl font-semibold mr-2">{{ product.price }} BTC</p>
            <p class="text-green-500 text-lg">${{ convertToDollars(product.price) }}</p>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2">Envío:</span>
            <span class="text-lg">{{ product.shipping }}</span>
          </div>
          <div class="flex items-center mb-4">
            <span class="text-gray-600 text-lg mr-2">Rating:</span>
            <div class="flex">
              <template v-for="star in 5" :key="star">
                <svg class="w-6 h-6 fill-current text-yellow-500" :class="{ 'text-gray-400': star > product.rating }"
                  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                  <path
                    d="M19.906 7.319a.708.708 0 0 0-.621-.446L13.61 6.288 11.548.982a.73.73 0 0 0-1.372 0L6.39 6.288.715 6.873a.71.71 0 0 0-.394 1.212l4.343 4.234-1.03 6.004a.73.73 0 0 0 1.06.769L10 16.835l5.366 2.247a.732.732 0 0 0 .352.089.722.722 0 0 0 .71-.601l1.03-6.0044.343-4.234a.71.71 0 0 0 .198-.766z" />
                </svg>
              </template>
            </div>
          </div>
          <div class="mt-8">
            <h3 class="text-xl font-semibold mb-2">Detalles adicionales:</h3>
            <p class="text-gray-600 text-lg">{{ product.additionalDetails }}</p>
          </div>
          <div class="flex mb-4 space-x-4">
            <button @click="addToCart"
              class="bg-[#f76108] hover:bg-[#fa7328] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#f76108]">
              Agregar al carrito
            </button>
            <button @click="buyNow"
              class="bg-[#ac15c1] hover:bg-[#d836e8] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#ac15c1]">
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
    };
  },
  mounted() {
    setTimeout(() => {
      this.product = {
        name: 'PUFFY 2G - Girls (Super Blends)',
        description: 'Super Blends were carefully crafted to mimic the live resin experience',
        price: 0.0125,
        image: 'https://via.placeholder.com/100x100',
        brand: 'Puffy',
        shipping: 'Envío gratis',
        rating: 4,
        variants: ['Chocolate Sativa', 'Berry Hibrida', 'Indica Girlscout Cookies'],
        additionalDetails: 'Super Blends were carefully crafted to mimic the live resin experience. We drew our inspiration from the cannabis plant. Creating unique cannabinoid formulas with terpene profiles that mirror today’s most popular strains.',
      };
    }, 2000);
  },
  methods: {
    addToCart() {
      console.log(`Agregando ${this.quantity} unidades del producto al carrito`);
    },
    buyNow() {
      console.log(`Comprando ${this.quantity} unidades del producto`);
    },
    convertToDollars(price) {
      const conversionRate = 4000;
      return (price * conversionRate).toFixed(2);
    },
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Ajusta esta altura según tus necesidades */
}

.bg-white {
  margin: 0 auto;
  margin-left: 300px;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.button {
  background-color: #4a86e8;
  color: #fff;
  transition: all 0.3s ease;
}

.button:hover {
  background-color: #0058a3;
  transform: scale(1.05);
}

.select-variant {
  text-align: left;
  width: 100%;
}
</style>
