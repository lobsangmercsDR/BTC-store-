<template>
  <div class="flex flex-wrap place-items-center h-2/6">
    <section class="relative mx-auto">
      <!-- navbar -->
      <nav class="flex justify-between bg-gray-900 w-screen">
        <div class="px-5 xl:px-12 py-6 flex w-full items-center text-white">
          <a class="text-3xl font-bold font-heading" href="#">Logo Here.</a>
          <!-- Nav Links -->
          <ul class="hidden md:flex px-4 mx-auto font-semibold font-heading space-x-12" :class="{ 'hidden': !menuOpen }">
            <li><a class="hover:text-gray-200" href="#">Home</a></li>
            <li><a class="hover:text-gray-200" href="#">Category</a></li>
            <li><a class="hover:text-gray-200" href="#">Shop</a></li>
            <li><a class="hover:text-gray-200" href="#">Be a seller!</a></li>
          </ul>
          <!-- Header Icons -->
          <div class="relative hidden xl:flex items-center space-x-5">
            <!-- Cart -->
            <div @click="toggleCart" class="relative cursor-pointer">
              <a class="hover:text-gray-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                <span class="absolute -top-2 -right-2 block w-5 h-5 rounded-full text-white bg-red-500 text-center font-bold">{{ cart.length }}</span>
              </a>
              <!-- Cart Dropdown -->
              <div class="absolute right-0 mt-12 bg-white w-64 rounded shadow-lg p-6 z-10 text-gray-800" v-if="cartOpen">
                <h2 class="font-bold mb-4">Your Cart for Fisical Products</h2>
                <div v-for="product in cart" :key="product.id" class="flex justify-between items-center mb-2">
                  <div>{{ product.name }}</div>
                  <div class="flex items-center">
                    <div class="text-gray-500">${{ product.price }}</div>
                    <button @click="removeProduct(product)" class="ml-2 text-red-500">Remove</button>
                  </div>
                </div>
                <div class="border-t mt-4 pt-4 flex justify-between items-center font-bold">
                  <div>Total:</div>
                  <div>${{ total }}</div>
                </div>
                <h2 class="font-bold mb-4">Your Cart For Digital Products</h2>
                <div v-for="product in cart" :key="product.id" class="flex justify-between items-center mb-2">
                  <div>{{ product.name }}</div>
                  <div class="flex items-center">
                    <div class="text-gray-500">${{ product.price }}</div>
                    <button @click="removeProduct(product)" class="ml-2 text-red-500">Remove</button>
                  </div>
                </div>
                <div class="border-t mt-4 pt-4 flex justify-between items-center font-bold">
                  <div>Total:</div>
                  <div>${{ total }}</div>
                </div>
              </div>
            </div>
            <!-- User -->
            <div class="relative cursor-pointer" @click="toggleUserMenu">
              <a class="flex items-center hover:text-gray-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span class="ml-2">{{ username }}</span>
              </a>
              <!-- User Dropdown -->
              <div class="absolute right-0 mt-12 bg-white w-64 rounded shadow-lg p-6 z-10 text-gray-800" v-if="userMenuOpen">
                <h2 class="font-bold mb-4">User Menu</h2>
                <h2 class="font-bold mb-4">Your Balance: 0 BTC</h2>
                <ul class="space-y-2">
                  <li><a href="" class="hover:text-blue-500"><router-link to="/profile">Perfil</router-link></a></li>
                  <li><a href="#" class="hover:text-blue-500">Logout</a></li>
                </ul>
              </div>
            </div>
          </div>
          <!-- Responsive navbar -->
          <a class="md:hidden flex mr-6 items-center" href="#" @click="toggleMenu">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </a>
        </div>
      </nav>
    </section>
  </div>
</template>


<script>
import axios from 'axios';
import { request } from 'http';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      menuOpen: false,
      cartOpen: false,
      userMenuOpen: false,
      username: '',
      cart: [
        { id: 1, name: 'Product 1', price: 100 },
        { id: 2, name: 'Product 2', price: 200 },
        { id: 3, name: 'Product 3', price: 300 },
      ],
    };
  },
  computed: {
    total() {
      return this.cart.reduce((sum, product) => sum + product.price, 0);
    },

    created() {
      this.getUserData()
    }
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    toggleCart() {
      this.cartOpen = !this.cartOpen;
    },
    toggleUserMenu() {
      this.userMenuOpen = !this.userMenuOpen;
    },
    removeProduct(product) {
      this.cart = this.cart.filter((p) => p.id !== product.id);
    },
    async getUserData(id) {
      console.log(id)
       await axios.get('http://127.0.0.1:8000/api/users', {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`,
          },
        }).then(response => {console.log(response);})
        .catch(error=> {console.log(error); })
        console.log(id),
        this.username = response.data.username;
    },
  },
  mounted() {
    this.getUserData();
  },
};
</script>

<style scoped>
.absolute {
  position: absolute;
}
</style>
