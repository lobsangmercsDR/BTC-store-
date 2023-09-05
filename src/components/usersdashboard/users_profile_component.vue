<template>
    <div class="min-h-screen w-full bg-gray-100 text-gray-700">
      <!-- Encabezado -->
 
      <!-- Contenido principal -->
      <div class="flex" style="margin-top: 80px;">
        <section @click="this.showAsideMenu=!this.showAsideMenu" v-show="!this.showAsideMenu" style="margin: 20px; position: absolute;">
          <svg width="30" height="30" id="icoOpen">
            <path d="M0,5 30,5" stroke="#000" stroke-width="5"/>
            <path d="M0,14 30,14" stroke="#000" stroke-width="5"/>
            <path d="M0,23 30,23" stroke="#000" stroke-width="5"/>
          </svg>
        </section>
        <!-- Barra lateral -->
        <aside v-show="this.showAsideMenu" class="flex w-72 flex-col space-y-2 border-r-2 border-gray-200 bg-white p-2" :class="{ 'hidden': !asideOpen }" style="min-height: 1165px; position: absolute; z-index: 2;">
          <div class="close-button-cont">
            <button @click="this.showAsideMenu = false" class="close-button">
              <svg class="w-6 h-6 fill-current text-gray-500 hover:text-gray-700" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24">
                <path
                  d="M18.364 5.636a2 2 0 0 0-2.828 0L12 9.172 8.464 5.636a2 2 0 1 0-2.828 2.828L9.172 12l-3.536 3.536a2 2 0 1 0 2.828 2.828L12 14.828l3.536 3.536a2 2 0 1 0 2.828-2.828L14.828 12l3.536-3.536a2 2 0 0 0 0-2.828z" />
              </svg>
            </button>
          </div>
          <router-link to="/profile/modificate" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'home'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Editar Perfil</span>
          </router-link>
  
          <router-link to="/profile/rechar" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600">
            <span class="text-2xl"><i class="bx bx-cart"></i></span>
            <span>Wallet</span>
          </router-link>
          <router-link to="/profile/buying_orders" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'orders'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Ordenes de compra</span>
          </router-link>
          <router-link to="/profile/sell_orders" v-show="this.typeUser != 'buyers'" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'sells_orders'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Ordenes de venta</span>
          </router-link>
          <router-link to="/profile/categories_store" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'buy_categories'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Comprar Categorias de Venta</span>
          </router-link>
          <router-link to="/profile/Pchecker" v-show="this.typeUser != 'buyers' && this.typeUser != 'sellers'" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Checker Panel</span>
          </router-link>
          <router-link to="/profile/add_product_f" v-show="this.typeUser != 'buyers'" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Subir Producto</span>
          </router-link>
          <router-link to="/profile/add_product_d" v-show="this.typeUser != 'buyers'" class="flex items-center space-x-1 rounded-md px-2 py-3 hover:bg-gray-100 hover:text-blue-600" @click="selectedOption = 'd_product_add'">
            <span class="text-2xl"><i class="bx bx-home"></i></span>
            <span>Subir Producto Digital</span>
          </router-link>
  
          <!-- Agrega más opciones de sidebar aquí -->
  
        </aside>
  
        <!-- Área principal -->
        <div class="w-full p-4">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import AddDigitalProduct from '../creators/AddDigitalProduct.vue';
import AddProduct from '../creators/AddProduct.vue';

import profile_modification from './profile_modification.vue';
import orders from './orders.vue';
import sell_orders from './sell_orders.vue';
import buy_categories from './buy_categories.vue';
import user_checker from './user_checker.vue';
import { validateGroup } from '../../../utils/auth';
  
  export default {
    created() {
      const urlParams = new URLSearchParams(window.location.search);
      const option = urlParams.get('option');

      if (option === 'checker_panel') {
        this.selectedOption = 'checker_panel';

      }
    },


    created() {
      let Obj = this.$route.query
      if(Obj.option == null) {

        this.selectedOption = 'home'
      }
      else {
        this.selectedOption = Obj.option
      }



      this.IsAuthorized()
    }, 
    data() {
      return {
        profileOpen: false,
        asideOpen: true,
        selectedOption: 'home',
        typeUser:"",
        showAsideMenu:false
      };
    },
    components: {
        AddDigitalProduct,
        AddProduct,
        profile_modification,
        orders,
        sell_orders,
        buy_categories,
        user_checker,
    },

  methods: {
    returnRoute(route) {

      if (route === 'checker_panel') {
        const newUrl = window.location.origin + window.location.pathname + '?option=checker_panel';
        window.location.href = newUrl;
      }
    },
    async IsAuthorized() {
      let result = await validateGroup()
      this.typeUser = result
    }
  }
  };


  </script>
  
  <style>
  /* Agrega los estilos de Tailwind CSS aquí */
  </style>
  