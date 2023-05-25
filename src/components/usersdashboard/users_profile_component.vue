<template>
    <div class="min-h-screen w-full bg-gray-100 text-gray-700">
      <!-- Encabezado -->
 
      <!-- Contenido principal -->
      <div class="flex">
        <!-- Barra lateral -->
        <aside class="flex w-72 flex-col space-y-2 border-r-2 border-gray-200 bg-white p-2" :class="{ 'hidden': !asideOpen }" style="height: 90.5vh">
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'home'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Pefil</span>
          </a>
  
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'wallet'">
            <span class="text-2xl"><i class="bx bx-cart"></i></span>
            <span>Wallet</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'orders'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Ordenes de compra</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'sells_orders'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Ordenes de venta</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'buy_categories'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Comprar Categorias de Venta</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'checker_panel'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Checker Panel</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'p_product_add'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Subir Producto</span>
          </a>
          <a href="#" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'd_product_add'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Subir Producto Digital</span>
          </a>
  
          <!-- Agrega más opciones de sidebar aquí -->
  
        </aside>
  
        <!-- Área principal -->
        <div class="w-full p-4">
          <template v-if="selectedOption === 'home'">
           <profile_modification/>
          </template>
  
          <template v-if="selectedOption === 'wallet'">
            <rechar/>
          </template>
          <template v-if="selectedOption === 'orders'">
            <orders/>
          </template>
          <template v-if="selectedOption === 'sells_orders'">
            <sell_orders/>
          </template>
  
          <!-- Agrega más opciones de panel aquí -->
  
        </div>
      </div>
    </div>
  </template>
  
  <script>
import AddDigitalProduct from '../creators/AddDigitalProduct.vue';
import AddProduct from '../creators/AddProduct.vue';
import rechar from '../payments/rechar.vue';
import profile_modification from './profile_modification.vue';
import orders from './orders.vue';
import sell_orders from './sell_orders.vue';
  
  export default {
    data() {
      return {
        profileOpen: false,
        asideOpen: true,
        selectedOption: 'dashboard',
      };
    },
    components: {
        AddDigitalProduct,
        AddProduct,
        rechar,
        profile_modification,
        orders,
        sell_orders,
    },
  };
  </script>
  
  <style>
  /* Agrega los estilos de Tailwind CSS aquí */
  </style>
  