<template>
  <div>
    <nav class="navbar bg-orange-500 text-white fixed w-full">
      <div class="flex items-center justify-between p-6">
        <div class="flex items-center">
          <!-- Logo del sitio -->
          <div v-if="logoImage">
            <img :src="logoImage" alt="logo" class="h-10 w-10 mr-2" />
          </div>
          <div v-else>
            <p class="font-semibold text-xl mr-2">Logo</p>
          </div>

          <!-- Buscador -->
          <div class="relative mr-6 flex w-550px border rounded-lg overflow-hidden">
            <Dropdown v-model="selectedCategory" :options="categories" option-label="name" option-value="value"
              placeholder="Selecciona una categoría" class="h-12 rounded -l-lg text-sm focus:outline-none"></Dropdown>
            <InputText v-model="searchText" class="h-12  rounded-r-lg text-sm focus:outline-none flex-grow"
              placeholder="Buscar..."></InputText>
          </div>

          <!-- Menú -->
          <div class="flex items-center mr-6">
            <Button label="Home" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(1)"></Button>
            <Button label="Become Seller" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(2)"></Button>
            <Button label="Categorías" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(3)"></Button>
            <Button label="FAQ" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(4)"></Button>
          </div>
        </div>

        <!-- Iconos -->
        <div class="flex items-center relative">

          <!-- Icono de usuario -->
          <div class="relative flex items-center">
            <Button @click="toggleUserMenu" class="flex items-center ml-4 p-button-text">
              <i class="pi pi-user text-white h-100 w-100"></i>
              <span class="ml-2 text-white">{{ user.name }}|</span>
              <span class="ml-2 text-white">Balance: {{ user.balance }}</span>
            </Button>
            <!-- Desplegable del usuario -->
            <div v-show="userMenuOpen" class="user-menu">
              <div class="w-80 bg-white rounded-lg shadow-xl overflow-hidden">
                <div class="flex items-center justify-between p-4 text-sm font-semibold text-gray-900 bg-orange-500">
                  <span>Mi perfil</span>
                  <Button @click="closeUserMenu" class="text-white">
                    <i class="pi pi-times-circle h-6 w-6"></i>
                  </Button>
                </div>
                <ul class="px-4 py-2 text-black">
                  <li v-for="option in userOptions" :key="option.id">
                    <Button @click="handleUserOption(option)" class="p-button-text">{{ option.label }}</Button>
                  </li>
                </ul>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import InputText from 'primevue/inputtext';
import Cookies from 'js-cookie';
import axios from 'axios';

export default {
  components: {
    Button,
    Dropdown,
    InputText
  },
  created() {
    this.takeUserInfo()
  },
  
  data() {
    return {
      hasToken: false,
      logoImage: '',
      categories: [],
      selectedCategory: null,
      searchText: '',
      cartOpen: false,
      userMenuOpen: false,
      user: {
        name: '',
        balance: ''
      }, 
      physicalProducts: [],
      digitalProducts: [],
      userOptions: [
      { id: 1, label: 'Mi perfil' },
      { id: 2, label: 'Mi tienda' },
      { id: 3, label: 'Cerrar sesión' }


      ]
    };
  },
  methods: {
    async takeUserInfo() {
      console.log("aaa");
      let token = Cookies.get('token')
      console.log(token);
      if (token != null) {
        this.hasToken = true 
        await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(response => {
          console.log("aaaee");
          console.log(response);
          this.user.name = response.data.name; 
          this.user.balance = response.data.userBalance
        })
        .catch(error => {console.log(2)})
      }
      
    },

    toggleCart() {
      this.cartOpen = !this.cartOpen;
      if (this.userMenuOpen) this.userMenuOpen = false;
    },
    closeCart() {
      this.cartOpen = false;
    },
    toggleUserMenu() {
      this.userMenuOpen = !this.userMenuOpen;
      if (this.cartOpen) this.cartOpen = false;
    },
    closeUserMenu() {
      this.userMenuOpen = false;
    },
    handleUserOption(option) {
      if(option.id == 3) {
        this.$router.push('/logout')
      }
      else if(option.id == 1) {
        this.$router.push('/profile')
      }
    },
    decreaseQuantity(product, type) {
      // Decrease quantity
    },
    increaseQuantity(product, type) {
      // Increase quantity
    },
    pay() {
      // Payment process
    },
    getTotalItems() {
      // Calculate total items
    },
    getTotalPrice() {
      // Calculate total price
    },
    redirect(id) {
      if(id==1) {
        this.$router.push('/homePageEcommerce')
      }
    }
  }
};
</script>


<style>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 80px;
  background-color: #f66305;
  color: #FFFFFF;
  z-index: 9999;
}

.cart,
.user-menu {
  position: absolute;
  top: 100%;
  right: 0;
  transition: all 0.3s ease-in-out;
  z-index: 9998;
}

.pi-shopping-cart {
  color: white !important;
  outline: none;
  /* Remover el contorno azul */
  box-shadow: none;
  /* Remover el contorno sombreado */
}

.cart-icon {
  outline: none; /* Remover el contorno azul */
  box-shadow: none; /* Remover el contorno sombreado */
}

.search-bar {
  width: 5000px !important;
}

.button {
  background-color: #d9d9d9 !important;
}
</style>