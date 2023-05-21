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
           

            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu1">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Ordenes
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu1">
              <router-link to="/products_fis" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Historial de Ordenes
              </router-link>
              <router-link to="/product_dig" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Tickets
              </router-link>
            </div>

            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu2">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Carteras
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu2">
              <router-link to="/products_fis" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Cripto Concuurrencia
              </router-link>
              <router-link to="/product_dig" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Carteras
              </router-link>
              <router-link to="/categories_manage" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Movimientos
              </router-link>
            </div>

            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu3">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Usuarios
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu3">
              <router-link to="/products_fis" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Usuarios Registrados
              </router-link>
              <router-link to="/product_dig" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Administrador de codigos de invitacion
              </router-link>
            </div>
            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu3">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-three-dots"
                viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3 7.5A1.5 1.5 0 014.5 6h11A1.5 1.5 0 0117 7.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 7.5zm0 5A1.5 1.5 0 014.5 11h11A1.5 1.5 0 0117 12.5a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 013 12.5z" />
              </svg>
              Productos y categorias
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu3">
              <router-link to="/products_fis" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Agregar Producto Fisico
              </router-link>
              <router-link to="/product_dig" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Agregar Productos Digitales
              </router-link>
              <router-link to="/categories_manage" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Creador y editor de Categorias
              </router-link>
              <router-link to="/inventory_general" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Inventario
              </router-link>
            </div>


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
      showSubMenu2: false,
      showSubMenu3: false,
      showSubMenu4: false,
    };
  },
  methods: {
    toggleSubMenu() {
      this.showSubMenu = !this.showSubMenu;
    },
    toggleSubMenu1() {
      this.showSubMenu1 = !this.showSubMenu1;
    },
    toggleSubMenu2() {
      this.showSubMenu2 = !this.showSubMenu2;
    },
    toggleSubMenu3() {
      this.showSubMenu3 = !this.showSubMenu3;
    },
    toggleSubMenu4() {
      this.showSubMenu4 = !this.showSubMenu4;
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
.submenu2 {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu2.show {
  display: block;
}

.submenu2 ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu2 li {
  margin-bottom: 5px;
}

.submenu2 li:last-child {
  margin-bottom: 0;






}







.submenu3 {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu3.show {
  display: block;
}

.submenu3 ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu3 li {
  margin-bottom: 5px;
}

.submenu3 li:last-child {
  margin-bottom: 0;
}




</style>
