<template>
  <div>
    <nav class="navbar bg-blue-500 text-white fixed w-full">
      <div class="flex items-center justify-between p-6">
        <div class="flex items-center">
          <!-- Logo del sitio -->
          <div v-if="logoImage">
            <img :src="logoImage" alt="logo" class="h-10 w-10 mr-2"/>
          </div>
          <div v-else>
            <p class="font-semibold text-xl mr-2">Logo</p>
          </div>

          <!-- Buscador -->
          <div class="relative mr-6 flex w-550px border rounded-lg overflow-hidden">
            <select class="bg-white h-12 px-5 rounded-l-lg text-sm focus:outline-none"
                    v-model="selectedCategory">
              <option disabled value="">Selecciona una categoría</option>
              <option v-for="category in categories" :key="category.value" :value="category.value">
                {{ category.name }}
              </option>
            </select>
            <input class="bg-white h-12 px-5 rounded-r-lg text-sm focus:outline-none flex-grow"
                   type="search" name="search" v-model="searchText" placeholder="Buscar...">
          </div>

          <!-- Menú -->
          <div class="flex items-center mr-6">
            <a href="#" class="mr-6">Home</a>
            <a href="#" class="mr-6">Become Seller</a>
            <a href="#" class="mr-6">Categorías</a>
            <a href="#" class="mr-6">FAQ</a>
          </div>
        </div>

        <!-- Iconos -->
        <div class="flex items-center relative">
          <!-- Icono de carrito de compras -->
          <div class="relative flex items-center">
            <button @click="toggleCart" class="relative mr-6">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.9 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293-.707M17 16a2 2 0 112-2 2 2 0 01-2 2zm-8 0a2 2 0 112-2 2 2 0 01-2 2z" />
              </svg>
              <span class="ml-1 text-sm font-medium" v-show="cartOpen">
                {{ getTotalItems() }}
                <span class="animate-ping absolute inline-flex h-2 w-2 rounded-full bg-blue-400 opacity-75"></span>
              </span>
            </button>
            
            <!-- Desplegable del carrito -->
            <transition name="fade">
              <div v-show="cartOpen" class="cart">
                <div class="w-80 bg-white rounded-lg shadow-xl overflow-hidden">
                  <div class="flex items-center justify-between p-4 text-sm font-semibold text-gray-900 bg-blue-500">
                    <span>Carrito de Compras</span>
                    <button @click="closeCart" class="text-white">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  </div>

                  <!-- Productos físicos -->
                  <div class="px-4 py-2 text-sm font-semibold text-gray-900 bg-gray-100">
                    Productos físicos (Total: {{ totalPhysical }})
                  </div>
                  <ul class="px-4 py-2 text-black">
                    <li v-for="product in physicalProducts" :key="product.id">
                      {{ product.name }} ({{ product.quantity }} x {{ product.price }})
                      <button @click="decreaseQuantity(product, 'physical')" class="ml-2 text-red-500">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                        </svg>
                      </button>
                      <button @click="removeProduct(product, 'physical')" class="ml-2 text-red-500">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </li>
                  </ul>

                  <!-- Productos digitales -->
                  <div class="px-4 py-2 text-sm font-semibold text-gray-900 bg-gray-100">
                    Productos digitales (Total: {{ totalDigital }})
                  </div>
                  <ul class="px-4 py-2 text-black">
                    <li v-for="product in digitalProducts" :key="product.id">
                      {{ product.name }} ({{ product.quantity }} x {{ product.price }})
                      <button @click="decreaseQuantity(product, 'digital')" class="ml-2 text-red-500">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                        </svg>
                      </button>
                      <button @click="removeProduct(product, 'digital')" class="ml-2 text-red-500">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </li>
                  </ul>
                </div>
              </div>
            </transition>
          </div>

          <!-- Icono de usuario -->
          <div class="relative flex items-center">
            <button @click="toggleUserMenu" class="flex items-center ml-4">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              <span class="ml-2 text-white">{{ username }}</span>
            </button>

            <!-- Desplegable del usuario -->
            <transition name="fade">
              <div v-show="userMenuOpen" class="user-menu">
                <div class="w-40 bg-white rounded-lg shadow-xl" style="z-index: 9999;">
                  <ul class="py-2">
                    <li>
                      <a href="#" class="text-black">Profile</a>
                    </li>
                    <li>
                      <a href="#" class="text-black">Cerrar sesión</a>
                    </li>
                  </ul>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </nav>

    <!-- Contenido adicional -->
    <div class="mt-20">
      <!-- Agrega aquí el contenido adicional de tu página -->
      <!-- Ejemplo de contenido adicional -->
      <div class="p-6">
        <h1 class="text-3xl font-semibold mb-4">Bienvenido a mi sitio web</h1>
        <p>Este es un ejemplo de contenido adicional en tu página.</p>
        <p>Puedes agregar más elementos HTML y estilos según tus necesidades.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      logoImage: null,
      username: 'Usuario',
      searchText: '',
      selectedCategory: '',
      categories: [
        { value: 'category1', name: 'Categoría 1' },
        { value: 'category2', name: 'Categoría 2' },
        // Agrega más categorías aquí
      ],
      cartOpen: false,
      physicalProducts: [
        { id: 'p1', name: 'Producto físico 1', quantity: 2, price: 100 },
        { id: 'p2', name: 'Producto físico 2', quantity: 3, price: 200 },
        // Agrega más productos físicos aquí
      ],
      digitalProducts: [
        { id: 'd1', name: 'Producto digital 1', quantity: 1, price: 300 },
        { id: 'd2', name: 'Producto digital 2', quantity: 4, price: 400 },
        // Agrega más productos digitales aquí
      ],
      userMenuOpen: false
    }
  },
  computed: {
    totalPhysical() {
      return this.physicalProducts.reduce((total, product) => total + product.quantity * product.price, 0);
    },
    totalDigital() {
      return this.digitalProducts.reduce((total, product) => total + product.quantity * product.price, 0);
    }
  },
  methods: {
    decreaseQuantity(product, type) {
      if (product.quantity > 1) {
        product.quantity--;
      }
    },
    removeProduct(product, type) {
      const productList = type === 'physical' ? this.physicalProducts : this.digitalProducts;
      const index = productList.findIndex(p => p.id === product.id);
      if (index !== -1) {
        productList.splice(index, 1);
      }
    },
    getTotalItems() {
      let totalItems = 0;
      for (const product of this.physicalProducts) {
        totalItems += product.quantity;
      }
      for (const product of this.digitalProducts) {
        totalItems += product.quantity;
      }
      return totalItems;
    },
    toggleCart() {
      this.cartOpen = !this.cartOpen;
    },
    closeCart() {
      this.cartOpen = false;
    },
    toggleUserMenu() {
      this.userMenuOpen = !this.userMenuOpen;
    }
  }
}
</script>

<style>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 100px;
  background-color: #3B82F6;
  color: #FFFFFF;
  z-index: 9999;
}

.cart,
.user-menu {
  position: absolute;
  top: 100%;
  left: -100%;

  width: 100%;
  max-width: 550px;
  z-index: 9999;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
  transform: translateX(100%);
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

.mt-20 {
  margin-top: 64px;
}

.w-550px {
  width: 550px;
}
</style>
