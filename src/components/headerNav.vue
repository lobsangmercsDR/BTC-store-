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
            <Button label="Home" class="mr-6 p-button-text"></Button>
            <Button label="Become Seller" class="mr-6 p-button-text"></Button>
            <Button label="Categorías" class="mr-6 p-button-text"></Button>
            <Button label="FAQ" class="mr-6 p-button-text"></Button>
          </div>
        </div>

        <!-- Iconos -->
        <div class="flex items-center relative">
          <!-- Icono de carrito de compras -->
          <div class="relative flex items-center">
            <Button @click="toggleCart" class="relative mr-6 p-button">
              <i class="pi pi-shopping-cart text-white-500 h-100 w-100 cart-icon"></i>
              <span class="ml-1 text-sm font-medium" v-show="cartOpen">
                <span class="cart-total text-white">
                  Cantidad total:{{ getTotalItems() }}||
                  <span class="cart-total-price">Total del carrito:{{ getTotalPrice() }}</span>
                </span>
              </span>
            </Button>
            <!-- Desplegable del carrito -->
            <div v-show="cartOpen" class="cart">
              <div class="w-80 bg-white rounded-lg shadow-xl overflow-hidden">
                <div class="flex items-center justify-between p-4 text-sm font-semibold text-gray-900 bg-orange-500">
                  <span>Carrito de Compras</span>
                  <Button @click="closeCart" class="text-white">
                    <i class="pi pi-times-circle h-6 w-6"></i>
                  </Button>
                </div>
                <!-- Productos físicos -->
                <div class="px-4 py-2 text-sm font-semibold text-gray-900 bg-gray-100">
                  Productos físicos (Total: {{ totalPhysical }})
                </div>
                <ul class="px-4 py-2 text-black">
                  <li v-for="product in physicalProducts" :key="product.id">
                    {{ product.name }} ({{ product.quantity }} x {{ product.price }})
                    <Button @click="decreaseQuantity(product, 'physical')" class="ml-2 p-button-danger p-button-rounded"
                      icon="pi pi-minus"></Button>
                    <Button @click="increaseQuantity(product, 'physical')" class="ml-2 p-button-success p-button-rounded"
                      icon="pi pi-plus"></Button>
                  </li>
                </ul>
                <!-- Productos digitales -->
                <div class="px-4 py-2 text-sm font-semibold text-gray-900 bg-gray-100">
                  Productos digitales (Total: {{ totalDigital }})
                </div>
                <ul class="px-4 py-2 text-black">
                  <li v-for="product in digitalProducts" :key="product.id">
                    {{ product.name }} ({{ product.quantity }} x {{ product.price }})
                    <Button @click="decreaseQuantity(product, 'digital')" class="ml-2 p-button-danger p-button-rounded"
                      icon="pi pi-minus"></Button>
                    <Button @click="increaseQuantity(product, 'digital')" class="ml-2 p-button-success p-button-rounded"
                      icon="pi pi-plus"></Button>
                  </li>
                </ul>
                <!-- Botón de pago -->
                <div class="flex items-center justify-end px-4 py-2 bg-gray-100">
                  <Button @click="pay" class="p-button-success" label="Pagar"></Button>
                </div>
              </div>
            </div>
          </div>

          <!-- Icono de usuario -->
          <div class="relative flex items-center">
            <Button @click="toggleUserMenu" class="flex items-center ml-4 p-button-text">
              <i class="pi pi-user text-white h-100 w-100"></i>
              <span class="ml-2 text-white">{{ username }}|</span>
              <span class="ml-2 text-white">Balance: 00</span>
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
                    <Button @click="handleUserOption(option)" class="p-button-text" label="{{ option.label }}"></Button>
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

export default {
  components: {
    Button,
    Dropdown,
    InputText
  },
  data() {
    return {
      logoImage: '',
      categories: [],
      selectedCategory: null,
      searchText: '',
      cartOpen: false,
      userMenuOpen: false,
      username: 'John Doe',
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
      console.log(option);
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
  background-color: #f66305 !important;
}
</style>