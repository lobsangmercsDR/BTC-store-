<template>
            <section @click="this.showSide=!this.showSide" v-show="!this.showSide" style="margin: 20px; position: absolute;">
          <svg width="30" height="30" id="icoOpen">
            <path d="M0,5 30,5" stroke="#000" stroke-width="5"/>
            <path d="M0,14 30,14" stroke="#000" stroke-width="5"/>
            <path d="M0,23 30,23" stroke="#000" stroke-width="5"/>
          </svg>
        </section>
  <div class="w-screen h-screen flex" style="overflow: auto;">
    <!-- Side bar -->
    <div class="w-[400px] h-full bg-gray-200 text-white" v-show="showSide" style="position: absolute; z-index: 10;">
      <div class="h-[50px] bg-gray-900 flex justify-start items-center ">
        <div class="px-[20px] header-menu">
          <h3 class="font-bold text-xl">Admin Dashboard</h3>
          <button @click="this.showSide = false" class="close-button">
          <svg class="w-6 h-6 fill-current text-gray-500 hover:text-gray-700" xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24">
            <path
              d="M18.364 5.636a2 2 0 0 0-2.828 0L12 9.172 8.464 5.636a2 2 0 1 0-2.828 2.828L9.172 12l-3.536 3.536a2 2 0 1 0 2.828 2.828L12 14.828l3.536 3.536a2 2 0 1 0 2.828-2.828L14.828 12l3.536-3.536a2 2 0 0 0 0-2.828z" />
          </svg>
        </button>
        </div>
      </div>
      <div class=" bg-gray-800 py-[20px]" style="height: inherit; ">
        <div class="flex flex-col justify-between h-full px-[20px] space-y-[10px] menuCont" style="overflow: auto;">
          <div class=" flex flex-col justify-between space-y-[10px]">
            <router-link to="/home"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-200 hover:text-gray-800  transition duration-400 ease-in-out">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-house"
                viewBox="0 0 20 20">
                <path
                  d="M10 3L2 9v8a1 1 0 0 0 1 1h4v-6h6v6h4a1 1 0 0 0 1-1V9l-8-6zm8 10h-3v-6a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v6H2v-7l8-6 8 6v7z" />
                <path d="M9 14h2v2H9v-2z" />
              </svg>

              Home
            </router-link>












            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu1">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-cart-check"
                viewBox="0 0 20 20">
                <path
                  d="M14.473 1.334a1 1 0 0 1 .859.502l3.333 5a1 1 0 0 1 .04 1.006l-2.666 5a1 1 0 0 1-.946.623H3.667a1 1 0 0 1-.944-.65l-2-5a1 1 0 0 1 .044-1.002l3.333-5a1 1 0 0 1 .86-.492h9.924zM10 16a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm4-2a3.999 3.999 0 0 1-6.657 2.915L4.559 14H15z" />
                <path
                  d="M9 15a1 1 0 0 0 .707-1.707l-4-4a1 1 0 1 0-1.414 1.414L8.586 15A1 1 0 0 0 9 15zm6-12h-3V1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1z" />
              </svg>
              Ordenes
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu1">
              <router-link to="/cases" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Historial de Ordenes
              </router-link>
            </div>











            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu2">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-wallet2"
                viewBox="0 0 20 20">
                <path d="M2 5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1H2V5zm16 2H2v8h16V7zM2 13v2h16v-2H2z" />
                <path fill-rule="evenodd" d="M2 5v2h16V5H2zm0 2h16v1H2V7z" />
              </svg>

              Carteras
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu2">
              <router-link to="/Wallet" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Solicitudes de Retiro
              </router-link>
              <router-link to="/deposit_coins" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Depositos
              </router-link>
            </div>








            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu3">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-people"
                viewBox="0 0 20 20">
                <path
                  d="M6 6a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm8 0a3 3 0 1 1 0-6 3 3 0 0 1 0 6zM3.5 16a6.519 6.519 0 0 1 2-4.803A7.49 7.49 0 0 1 10 11a7.49 7.49 0 0 1 4.5 1.197A6.519 6.519 0 0 1 16.5 16H3.5zm12.033-4.207a5.48 5.48 0 0 0-1.108-.957 5.488 5.488 0 0 0-3.867-.24 5.46 5.46 0 0 0-1.912 1.34A4.528 4.528 0 0 0 9.525 14h5.01a5.458 5.458 0 0 0 1.008-1.207z" />
                <path fill-rule="evenodd"
                  d="M10 11a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zm4 2a4 4 0 1 1-8 0 4 4 0 0 1 8 0zm-8-1a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" />
              </svg>

              Usuarios
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu3">
              <router-link to="/user_control" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Usuarios Registrados
              </router-link>
              <router-link to="/invitation_code_manager" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Administrador de codigos de invitacion
              </router-link>
            </div>






            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu4">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-box-seam"
                viewBox="0 0 20 20">
                <path
                  d="M7 6.5a1.5 1.5 0 0 1-3 0V4a1.5 1.5 0 0 1 1.5-1.5h8A1.5 1.5 0 0 1 16 4v2.5a1.5 1.5 0 0 1-3 0V4h-1v2.5a2.5 2.5 0 0 0 5 0V4a2.5 2.5 0 0 0-2.5-2.5h-8A2.5 2.5 0 0 0 3 4v2.5H2V4a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v2.5h-1V4A2.5 2.5 0 0 0 12 1.5h-8A2.5 2.5 0 0 0 1.5 4v2.5h-1V4a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v2.5h-1V4A2.5 2.5 0 0 0 12 1.5h-8A2.5 2.5 0 0 0 1.5 4v2.5H0V4a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v2.5h-1V4a2.5 2.5 0 0 0-2.5-2.5h-8A2.5 2.5 0 0 0 1 4v2.5H0V4a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v2.5h-1V4A2.5 2.5 0 0 0 12 1.5h-8A2.5 2.5 0 0 0 1.5 4v2.5H0V4z" />
                <path fill-rule="evenodd"
                  d="M12.5 9.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0 0 1h9a.5.5 0 0 0 .5-.5zm1.5 4a.5.5 0 0 0-.5-.5h-11a.5.5 0 1 0 0 1h11a.5.5 0 0 0 .5-.5zm.5-4a1.5 1.5 0 0 0-1.5-1.5h-9A1.5 1.5 0 0 0 2 9.5v1A1.5 1.5 0 0 0 3.5 12h9A1.5 1.5 0 0 0 14 10.5v-1zm-1.5.5a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 1 0v1zm-9 0a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 1 0v1zm9-3a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 1 0v1zm-9 0a.5.5 0 0 1-1 0v-1a.5.5 0 0 1 1 0v1z" />
              </svg>

              Productos y categorias
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu4">
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








            <button
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out"
              @click="toggleSubMenu5">
              <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor"
                class="bi bi-check2-square" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                  d="M3.5 9a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zm13.5-7H14a2 2 0 0 0-1.555.746L6.232 11H5.5a.5.5 0 0 0 0 1H6l6.212.001a2 2 0 0 0 1.554-.746L16 4H17.5a.5.5 0 0 0 0-1zm-4 10a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1 0-1h9a.5.5 0 0 1 .5.5zm0-7a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1 0-1h9a.5.5 0 0 1 .5.5zm0 3a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1 0-1h9a.5.5 0 0 1 .5.5zm2-8h-11a2 2 0 0 0-1.85 1.21L.268 10.71a.5.5 0 0 0 .053.518l3 3.5a.5.5 0 0 0 .857-.514L2.464 12H17.5a2 2 0 0 0 1.85-1.21l1-2.5A.5.5 0 0 0 20 8.5v-4a.5.5 0 0 0-.5-.5zm-12 9.293l-2-2.333V6.04l2 2.334V12.29zm3 0V8.375l2-2.334V9.96l-2 2.333zm3-4.626V6.04l2-2.333v4.041l-2 2.334z" />
              </svg>

              Checker Panel
            </button>
            <div class="mt-2 bg-gray-300 rounded-md overflow-hidden" v-show="showSubMenu5">
              <router-link to="/user_checker" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Solicitudes de Checker
              </router-link>  
            </div>






            <router-link to="/homePageEcommerce"
              class="inline-flex relative items-center py-[10px] px-[10px] w-full text-sm font-medium rounded-md border-gray-200 hover:bg-gray-300  hover:text-gray-800 transition duration-400 ease-in-out">
              <svg aria-hidden="true" class="mr-2 w-[25px] h-[25px] fill-current" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z">
                </path>
              </svg>
              Home
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
              <!-- <router-link to="/settings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-400">
                Configuraciones
              </router-link> -->
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
      showSide: false,
      showSubMenu: false,
      showSubMenu1: false,
      showSubMenu2: false,
      showSubMenu3: false,
      showSubMenu4: false,
      showSubMenu5: false,
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
    toggleSubMenu5() {
      this.showSubMenu5 = !this.showSubMenu5;
    },
  },
};
</script>

<style scoped>

.menuCont::-webkit-scrollbar {
  width: 0
}


.header-menu {
    display: flex;
    justify-content: space-between !important;
    width: 100%;
}
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



.submenu4 {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu4.show {
  display: block;
}

.submenu4 ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu4 li {
  margin-bottom: 5px;
}

.submenu4 li:last-child {
  margin-bottom: 0;
}


.submenu5 {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 10;
}

.submenu5.show {
  display: block;
}

.submenu5 ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.submenu5 li {
  margin-bottom: 5px;
}

.submenu5 li:last-child {
  margin-bottom: 0;
}</style>
