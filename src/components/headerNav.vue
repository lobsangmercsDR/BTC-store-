<template>
  <div>
    <nav class="navbar bg-orange-500 text-white fixed w-full">
      <div class="flex items-center justify-between p-6">
        <div class="firsSNav flex items-center">
          <!-- Logo del sitio -->
  
          <div>
            <p class="font-semibold text-xl mr-2 icon-log">Logo</p>
          </div>


          <!-- Buscador -->
          <div class="relative mr-6 flex w-550px border rounded-lg overflow-hidden">
            <Dropdown v-model="selectedCategory" :options="categories" option-label="name" option-value="name"
              placeholder="Categorias" class="h-12 rounded -l-lg text-sm focus:outline-none"></Dropdown>
            <InputText v-model="searchText" @input="this.isOpenAcc=true; seek()" class="h-12  rounded-r-lg text-sm focus:outline-none flex-grow"
              placeholder=""></InputText>
              
          </div>
          <div class="accordion-dfg" v-show="isOpenAcc"  @blur="this.isOpenAcc=false">
            <p v-show="results==0" style="color: black;">No hay productos con ese nombre</p>
            <tr v-for="result in results">
              <td><span>{{ result.name }}</span></td>
              <td><button class="mt-0" @click="openModal(result.id, 'digits',result)">Ver</button></td>
            </tr>
          </div>
          <button class="button-top mt-0" @click="isOpenAcc=false">
              x
            </button>

          


            


          <!-- Menú -->
          <div class="flex items-center mr-6">
            <Button label="Home" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(1)"></Button>
            <Button label="¡Unete a nosotros!" v-show="authenticated != true" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(2)"></Button>
            <router-link to="/profile/categories_store"> <Button label="¡Vuelvete Seller!" v-show="authenticated" class="mr-6 p-button-text" style="color: white !important;"></Button></router-link>
            <Button label="Contacto" class="mr-6 p-button-text" style="color: white !important;" @click="redirect(4)"></Button>
            
          </div>
        </div>
        <div class="Resp-day">
        <button class="block   p-button-text menu" @click="menuOpen = !menuOpen">
          <i class="pi pi-bars text-white h-6 w-6"></i>
        </button>
                <div>
            <p class="font-semibold text-xl ml-2 icon-log-ext">Logo</p>
          </div>
        </div>
            <div v-show="menuOpen" class="">
          <div class="fixed inset-0 flex z-50">
            <!-- Fondo oscuro -->
            <div class="fixed inset-0 bg-black opacity-50"></div>
    
            <!-- Menú lateral -->
            <div class="relative latnav"  style="background-color: white; margin-top: 80px;" :class="{'latnav-showed': menuOpen}">
              <!-- Botón para cerrar el menú -->
              <button class="absolute top-0 right-0 mt-4 mr-4 p-button-text" @click="menuOpen=false">
                <i class="pi pi-times text-orange-500 h-6 w-6"></i>
              </button>
    
              <!-- Contenido del menú -->
              <div class="p-6 flex flex-col" >
                <!-- Buscador -->
                <div class="relative mb-6 flex w-full border rounded-lg overflow-hidden" style="top:20px">
                  <Dropdown v-model="selectedCategory" :options="categories" option-label="name" option-value="name"
              placeholder="Categorias" class="h-12 rounded -l-lg text-sm focus:outline-none"></Dropdown>
            <InputText v-model="searchText" @input="this.isOpenAcc=true; seek()" class="h-12  rounded-r-lg text-sm focus:outline-none flex-grow"
              placeholder=""></InputText>
                </div>

                <div class="accordion-lat" v-show="isOpenAcc"  @blur="this.isOpenAcc=false">
            <p v-show="results==0" style="color: black;">No hay productos con ese nombre</p>
            <tr v-for="result in results">
              <td><span>{{ result.name }}</span></td>
              <td><button class="mt-0" @click="openModal(result.id, 'digits',result); ">Ver</button></td>
            </tr>
            <p style="color: #000; cursor: pointer;" @click="this.isOpenAcc=false"><b>X</b></p>
          </div>
    
                <!-- Menú principal -->
                <div class="flex flex-col">
                  <Button label="Home" @click="this.$router.push('/homePageEcommerce')" class="mb-2 p-button-text" style="color: black;"></Button>
                  <Button label="¡Unete a nosotros!" v-show="authenticated != true" class="mb-2 p-button-text" style="color: black;"></Button>
                  <Button label="¡Vuelvete Seller!" v-show="authenticated" class="mb-2 p-button-text" style="color: black;"></Button>
                  <Button label="Contacto" class="mb-2 p-button-text" style="color: black;"></Button>
                </div>
    
                <!-- Botones de inicio de sesión y registro -->
                <div class="mt-auto flex flex-col">
                  <Button class="mb-2 p-button-text" v-show="authenticated != true" @click="handleUserAnon(1)">
                    <span class="p-button-label">Iniciar Sesión</span>
                  </Button>
                  <Button class="p-button-text" v-show="authenticated != true" @click="handleUserAnon(2)">
                    <span class="p-button-label">Registrarse</span>
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Iconos -->
        <div class="flex items-center relative" v-show="authenticated">

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
        <div class="flex items-center relative" v-show="authenticated != true">
          <div class="relative flex items-center">
            <Button class="flex items-center ml-4 p-button-text" @click="handleUserAnon(1)">
              <span class="ml-2 text-white"> Iniciar Sesión </span>
            </Button>
            <span class="ml-2 text-white"> | </span>
            <Button class="flex items-center ml-4 p-button-text" @click="handleUserAnon(2)">
              <span class="ml-2 text-white"> Registrarse </span>
            </Button>

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
import { isAuthenticated } from '../../utils/auth';

export default {
  components: {
    Button,
    Dropdown,
    InputText
  },
  created() {
    this.takeUserInfo()
    this.authenticated = isAuthenticated()
  },
  
  data() {
    return {
      isOpenAcc:false ,
      hasToken: false,
      logoImage: '',
      categories: [
        {id: 0, name:"Todas"},
        {id: 1, name:"Fisicas"},
        {id: 2, name:"Digitales"},
        {id: 3, name:"Metodos"}
      ],
      menuOpen: false,
      results: [],
      selectedCategory: null,
      authenticated: false,
      searchText: '',
      cartOpen: false,
      userMenuOpen: false,
      user: {
        name: '',
        balance: ''
      }, 
      showAccordion:false,
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
    openModal(id, type,obj) {
      this.isOpenAcc = false
      this.menuOpen = false
      if(obj.hasOwnProperty('comisionCheck')) {
        type = 'digits'
      }
      else if(obj.hasOwnProperty('variants')) {
        type='fisic'
      }
      else {
        console.log(obj)
        type='method'
      }
      this.$emit('open-modal',{id:id, type:type});
    },

    closeUserMenu() {
      this.userMenuOpen = false
    },

    async seek() {
    let url = 'http://127.0.0.1:8000/api/seeker?query=' + this.searchText;
    if (this.selectedCategory) {
      url += '&tip=' + this.selectedCategory;
    }
  await axios.get(url)
    .then(response=> {
      const data = response.data;
      const responseData =data.slice(0, 10).map(item => {
        if(item.hasOwnProperty('nameProduct')) {   
      return {
        ...item,
        name: item.nameProduct,
      };
    } else {
      return item
    }
    }); 
      this.results =  responseData
      console.log(responseData);
    })

    .catch(error => {
      console.error(error)
    })
    
    // Manipular los datos obtenidos en la respuesta

    },

    async takeUserInfo() {
      let token = Cookies.get('token')
      if (token != null) {
        this.hasToken = true 
        await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(response => {
          this.user.name = response.data.name; 
          this.user.balance = response.data.userBalance
        })
        .catch(error => {console.log(2)})
      }
      
    },

    handleUserAnon(type) {
      if(type==1) {
        this.$router.push('/login')
      }
      else {
        this.$router.push('/signup')
      }
    },

    toggleUserMenu() {
      this.userMenuOpen = !this.userMenuOpen
    },

    toggleCart() {
      this.cartOpen = !this.cartOpen;
      if (this.userMenuOpen) this.userMenuOpen = false;
    },
    closeCart() {
      this.cartOpen = false;
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
      if(id==2) {
        this.$router.push('/signup')
      }
      if(id==3) {
        this.$router.push({
          path: '/profile',
          query: {option: 'buy_categories'}
        })
      } 
    }
  }
};
</script>


<style>

.menu {
  display: none;
}

@media (max-width: 640px) {

}

@media (max-width: 1160px) {
  .menu {
    display: block;
  }

  .Resp-day {
    display: flex;
  }
  .firsSNav {
    display: none !important;
  }

  .latnav {
    opacity: 9;
  }

  .accordion-lat {
    position: absolute;
    top: 97px;
    left: 23px;
    width: 334px;
    background-color: #fff;
    border: 1px solid #ccc;
    /* margin-left: 80px; */
    padding: 1rem;
    border-radius: 7px;
    display: block;
    z-index: 2;
}

.icon-log-ext {
  display: block !important;
  margin-top: 10px;
}

.accordion-lat tr {
  color:black;
  margin-top: 8px;
  text-align: left;
  align-items: center;
  display: flex;
  justify-content: space-between;
}
.accordion-lat tr td button {
  padding:5px 12px;
  border-radius: 10px;
  background-color: #e55a00;
  color: #fff;
  font-weight: bold;
}

}

.icon-log-ext {
  display: none;
}

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

.button-top {
  margin-top: 0 rem !important;
    background-color: #e55a00;
    padding: 11px 9px;
    border-radius: 10px;
    /* border: 2px #ffaf7b solid; */
    margin-left: -12px;
    margin-right: 42px;
}

.accordion-dfg {
  position: absolute;
    top: 93%;
    left: 0;
    width: 409px;
    background-color: #fff;
    border: 1px solid #ccc;
    margin-left: 80px;
    padding: 1rem;
    border-radius: 7px;
    display: block;
}

.accordion-dfg tr {
  color:black;
  margin-top: 8px;
  text-align: left;
  align-items: center;
  display: flex;
  justify-content: space-between;
}
.accordion-dfg tr td button {
  padding:5px 12px;
  border-radius: 10px;
  background-color: #e55a00;
  color: #fff;
  font-weight: bold;
}



.show-accordion .accordion-dfg {
  display: block;
}


.button-top:hover {
  transition: all 0.1s ease-out;
  scale: 1.09;
}
</style>