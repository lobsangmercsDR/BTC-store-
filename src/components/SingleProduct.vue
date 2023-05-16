<template>
    <div class="bg-gray-100">
      <div class="container mx-auto p-8">
        <div v-if="product" class="flex flex-col md:flex-row">
          <div class="w-full md:w-1/2">
            <img class="w-full rounded-lg" :src="product.image" :alt="product.name" />
          </div>
          <div class="w-full md:w-1/2 md:pl-8">
            <h2 class="text-3xl font-bold mb-4">{{ product.name }}</h2>
            <p class="text-gray-600 mb-4">{{ product.description }}</p>
            <p class="text-2xl font-bold mb-4">${{ product.price }}</p>
            <div class="flex items-center mb-4">
              <span class="text-gray-600">Cantidad:</span>
              <input
                v-model="quantity"
                type="number"
                min="1"
                class="w-16 ml-2 py-2 px-4 rounded border-gray-300 border"
              />
            </div>
            <button
              @click="addToCart"
              class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors duration-200"
            >
              Agregar al carrito
            </button>
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
      };
    },
    mounted() {
      this.fetchProductData();
    },
    methods: {
      async fetchProductData() {
        try {
          const response = await fetch('https://api.example.com/products/1');
          const data = await response.json();
          this.product = data;
        } catch (error) {
          console.error(error);
        }
      },
      addToCart() {
        // Lógica para agregar el producto al carrito
        console.log(`Agregando ${this.quantity} unidades del producto al carrito`);
      },
    },
  };
  </script>
  