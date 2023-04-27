<template>
    <div class="card shadow-lg max-w-xs rounded overflow-hidden">
      <img :src="image" :alt="title" class="w-full">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">{{ title }}</div>
        <p class="text-gray-700 text-base">{{ description }}</p>
        <p class="text-gray-700 text-base">{{ price }}</p>
      </div>
      <div class="px-6 pt-4 pb-2">
        <button class="bg-gray-800 hover:bg-gray-900 text-white font-bold py-2 px-4 rounded-full" @click="addToCart()">Add to Cart</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: {
        type: String,
        default: 'Product Title'
      },
      image: {
        type: String,
        default: 'https://via.placeholder.com/300x200'
      },
      description: {
        type: String,
        default: 'Some text about the product...'
      },
      price: {
        type: String,
        default: '$0.00'
      }
    },
    methods: {
      addToCart() {
        // aquí se puede agregar la lógica para agregar el producto al carrito
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    background-color: #fff;
  }
  
  .card img {
    object-fit: cover;
    object-position: center;
    height: 200px;
  }
  
  .card button {
    width: 100%;
  }
  
  </style>