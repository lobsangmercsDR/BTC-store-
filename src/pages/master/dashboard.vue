<template>
  <div class="w-screen h-screen flex">
    <!-- Side bar -->
    <div class="w-[400px] h-full bg-gray-200 text-white" v-show="showSide">
      <div class="h-[50px] bg-gray-900 flex justify-start items-center">
        <div class="px-[20px]">
          <h3 class="font-bold text-xl">Admin Dashboard</h3>
        </div>
      </div>
      <div class="h-[calc(100vh-50px)] bg-gray-800 py-[20px]">
        <div class="flex flex-col justify-between h-full px-[20px] space-y-[10px]">
          <div class=" flex flex-col justify-between space-y-[10px]">
            <router-link to="/home"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-200 hover:text-gray-800  transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                  clip-rule="evenodd"></path>
              </svg>
              Home
            </router-link>
            <router-link to="/profile"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z">
                </path>
              </svg>
              Noticias
            </router-link>
            <router-link to="/cases"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z"
                  clip-rule="evenodd"></path>
              </svg>
              Casos y ordenes por aprobar
            </router-link>
            <router-link to="/CriptoView"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md rounded-b-lg hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-wallet"
                viewBox="0 0 20 20">
                <path
                  d="M0 3a2 2 0 0 1 2-2h13.5a.5.5 0 0 1 0 1H15v2a1 1 0 0 1 1 1v8.5a1.5 1.5 0 0 1-1.5 1.5h-12A2.5 2.5 0 0 1 0 12.5V3zm1 1.732V12.5A1.5 1.5 0 0 0 2.5 14h12a.5.5 0 0 0 .5-.5V5H2a1.99 1.99 0 0 1-1-.268zM1 3a1 1 0 0 0 1 1h12V2H2a1 1 0 0 0-1 1z" />
              </svg>
              Cripto Concurrencia
            </router-link>




            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu1">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Productos
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu1">
              <router-link to="/products_fis" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Agregar Productos Fisicos
              </router-link>
              <router-link to="/product_dig" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Agregar Productos Digitales
              </router-link>
              <router-link to="/categories_manage" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Creador de Categorias
              </router-link>
              <router-link to="/inventory_general" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Inventario
              </router-link>
            </div>




            <router-link to="/inventario"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md rounded-b-lg hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z"
                  clip-rule="evenodd"></path>
              </svg>
              Inventario
            </router-link>
            <router-link to="/users"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md rounded-b-lg hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-people-fill"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M7 4a4 4 0 100 8 4 4 0 000-8zm7 0a4 4 0 100 8 4 4 0 000-8z" />
                <path fill-rule="evenodd"
                  d="M7 10a3 3 0 113-3 3.003 3.003 0 01-3 3zm7 0a3 3 0 113-3 3.003 3.003 0 01-3 3z" />
                <path fill-rule="evenodd" d="M9.5 12a5.5 5.5 0 0011 0H9.5z" />
              </svg>
              Usuarios
            </router-link>
          </div>
          <div>
            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Opciones
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu">
              <router-link to="/settings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Configuraciones
              </router-link>
              <router-link to="/logout" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Cerrar Sesión
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main content -->
    <div class="flex-1 bg-gray-100">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showSide: true,
      showSubMenu: false,
      showSubMenu1:false,
    };
  },
  methods: {
    toggleSubMenu() {
      this.showSubMenu = !this.showSubMenu;
    },
    toggleSubMenu1() {
      this.showSubMenu1 = !this.showSubMenu1;
    },
  },
};
</script>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 240px auto;
  min-height: 100vh;
}

.sidebar {
  background-color: #2b2b2b;
  color: #ffffff;
}

.sidebar-logo {
  font-size: 24px;
  font-weight: 700;
  padding: 20px;
  text-align: center;
}

.sidebar-nav {
  padding-top: 20px;
}

.sidebar-nav a {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: #ffffff;
}

.sidebar-nav a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.sidebar-nav a svg {
  margin-right: 10px;
  vertical-align: middle;
}

.sidebar .sub-menu {
  display: none;
  background-color: #1f1f1f;
}

.sidebar .sub-menu a {
  padding-left: 30px;
}

.sidebar .sub-menu a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.sidebar .sub-menu.show {
  display: block;
}

.content {
  padding: 20px;
}

.submenu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu.show {
  display: block;
}

.submenu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu li {
  margin-bottom: 5px;
}

.submenu li:last-child {
  margin-bottom: 0;
}


.submenu1 {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu1.show {
  display: block;
}

.submenu1 ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu1 li {
  margin-bottom: 5px;
}

.submenu1 li:last-child {
  margin-bottom: 0;
}


</style>
