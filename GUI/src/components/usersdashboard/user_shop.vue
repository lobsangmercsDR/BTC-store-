<template>
    <div class="container mx-auto px-4 py-8 bg-white rounded-lg border-4 border-gray-300 " style="height: 750px; overflow: auto;">
      <!-- Store Registration -->
      <div v-if="!storeRegistered && loaded" class="mb-8">
        <h2 class="text-2xl font-bold text-gray-800">Registrar tienda</h2>
        <form class="flex flex-col bg-gray-100 p-4 rounded-lg">
          <label class="mb-2">
            Imagen de Avatar
            <input type="file" @change="previewImage" accept="image/*">
          </label>
          <label class="mb-2">
            Imagen de Banner:
            <input type="file" @change="previewBanner" accept="image/*">
          </label>
          <label class="mb-2">
            Nombre de tienda:
            <input v-model="storeCreateInformation.name" type="text"  class="border-2 border-gray-200 rounded p-1" />
          </label>
          <label class="mb-2">
            Descripcion de tienda:
            <textarea v-model="storeCreateInformation.description"  class="border-2 border-gray-200 rounded p-1"></textarea>
          </label>
          <button type="button" @click="registerStore()" class="bg-blue-500 text-white rounded p-2 mt-2">Registrar</button>
        </form>
        
      </div>
      <!-- Store Details -->
      <div v-if="storeRegistered && loaded" style="width: 100%" >
        <div class="relative mb-8">
          <img :src="'http://127.0.0.1:8000/api/'+ storeInformation.banner_img" class="w-full h-64 object-cover rounded-t-lg" alt="Banner">
          <div class="avatar-container">
            <img
              :src="'http://127.0.0.1:8000/api/'+ storeInformation.avatar_img"
              class="w-32 h-32 rounded-full border-4 border-white  absolute bottom-0 transform -translate-y-1/2"
              alt="Avatar"
            >
          </div>
        </div>
        <div class="flex flex-col items-center">
          <h2 class="text-2xl font-bold text-gray-800">{{ storeInformation.name }}</h2>
          <p class="text-gray-600">{{ storeInformation.description }}</p>

          <!-- Subcategories -->
          <div class="mb-8">
            <h3 class="font-bold mb-2 text-gray-800">Subcategorias:</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
              <div
                v-for="subCategory in storeInformation.buyed_categories"
                :key="subCategory.id"
                class="sub-category bg-f66305 text-white font-bold rounded-full px-2 py-1 transition-all duration-300 hover:bg-ab16be hover:scale-105 hover:shadow-lg"
              >
                {{ subCategory.nameSubCategory }}
              </div>
            </div>
          </div>
          <!-- Total Sold Products -->
          <div class="mb-8">
            <h3 class="font-bold mb-2 text-gray-800">Productos vendidos por categoría:</h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
              <div
                v-for="subCat in storeInformation.buyed_categories"
                :key="index"
                class="sold-product bg-ab16be text-white font-bold rounded-full px-2 py-1 transition-all duration-300 hover:bg-f66305 hover:scale-105 hover:shadow-lg"
              >
                {{ subCat.nameSubCategory }}: {{ subCat.selled_products_user_based }}
              </div>
            </div>
          </div>

          <div>
            <inventory :sell-view="true"></inventory>
          </div>
          
        </div>
        
      </div>

    </div>
  </template>
  
  <script>
 import axios from 'axios';
 import Cookies from 'js-cookie';
 import inventory from '../payments/inventory.vue';

  export default {
    data() {
      return {
        avatar: '',
        banner: '',
        storeCreateInformation: {
          name: '',
          description: '',
          banner_img: null,
          avatar_img: null
        },
        storeInformation: {},
        subCategories: [
          { id: 1, name: 'Subcategoría 1' },
          { id: 2, name: 'Subcategoría 2' },
        ],
        soldProducts: [
          { subCategory: 'Subcategoría 1', count: 50 },
          { subCategory: 'Subcategoría 2', count: 30 },
        ],
        loaded:false,
        storeRegistered: false,
        loggedIn: true, 
      };
    },
    created() {
      this.getStoreData()
    },
    components: {
      inventory
    },
    methods: {
      previewImage(event) {
        const file = event.target.files[0];
        this.storeCreateInformation.avatar_img = file
      },
      previewBanner(event) {
        const file = event.target.files[0];
        this.storeCreateInformation.banner_img = file;
      },
      async registerStore() {
        const newStore = this.storeCreateInformation
        let formData = new FormData()
        for(let item in this.storeCreateInformation) {
          console.log(item, newStore[item])
          formData.append(item, newStore[item])
        }
        await axios.post('http://127.0.0.1:8000/api/store',formData, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        })
        .then( response => {
          console.log(response.data)
          this.getStoreData()
        })
        .catch(error => {
          console.log(error.response.data)
        })
      
      },
      hasPurchasedSubCategory() {
        return true;
      },

      async getStoreData() {
        await axios.get(`http://127.0.0.1:8000/api/store/${Cookies.get('svg')}`, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        })
        .then(response => {
          console.log(response.data)
          this.storeRegistered = response.data.success
          this.storeInformation = response.data.store
          this.loaded = true
        })
        .catch(error => {
          console.log(error.response.data)
        })
      }
    }
  };
  </script>
  
  <style scoped>
  /* ... estilos anteriores ... */
  
  .animate-pulse {
    animation: pulse 2s infinite;
  }
  
  @keyframes pulse {
    0% {
      opacity: 0.5;
    }
    50% {
      opacity: 1;
    }
    100% {
      opacity: 0.5;
    }
  }
  
  .sub-category {
    background-color: #f66305;
  }
  
  .sold-product {
    background-color: #ab16be;
  }
  
  @media (max-width: 640px) {
    .container {
      padding: 2rem;
    }
    .sub-category,
    .sold-product {
      font-size: 0.8rem;
      padding: 0.5rem;
    }
  }
  
  /* Estilos adicionales para tabletas */
  @media (min-width: 641px) and (max-width: 1024px) {
    .container {
      max-width: 768px;
      margin: 0 auto;
    }
  }
  
  .avatar-container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    top: 50px;
  }
  
.container {
  align-items: flex-start !important;
}

  </style>
  