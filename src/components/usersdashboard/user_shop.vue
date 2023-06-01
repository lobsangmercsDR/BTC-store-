<template>
    <div class="container mx-auto px-4 py-8 bg-white rounded-lg border-4 border-gray-300">
      <!-- Store Registration -->
      <div v-if="!storeRegistered" class="mb-8">
        <h2 class="text-2xl font-bold text-gray-800">Welcome Vendor, please register your store</h2>
        <form @submit.prevent="registerStore" class="flex flex-col bg-gray-100 p-4 rounded-lg">
          <label class="mb-2">
            Upload Avatar:
            <input type="file" @change="previewImage" accept="image/*">
          </label>
          <label class="mb-2">
            Upload Banner:
            <input type="file" @change="previewBanner" accept="image/*">
          </label>
          <label class="mb-2">
            Store Name:
            <input v-model="storeName" type="text" required class="border-2 border-gray-200 rounded p-1"/>
          </label>
          <label class="mb-2">
            Store Description:
            <textarea v-model="storeDescription" required class="border-2 border-gray-200 rounded p-1"></textarea>
          </label>
          <button type="submit" class="bg-blue-500 text-white rounded p-2 mt-2">Register</button>
        </form>
      </div>
      <!-- Store Details -->
      <div v-else>
        <div class="relative mb-8">
          <img :src="banner" class="w-full h-64 object-cover rounded-t-lg" alt="Banner">
          <img :src="avatar" class="w-32 h-32 rounded-full border-4 border-white animate-pulse absolute bottom-0 transform -translate-y-1/2" alt="Avatar">
        </div>
        <div class="flex flex-col items-center">
          <h2 class="text-2xl font-bold text-gray-800">{{ storeName }}</h2>
          <p class="text-gray-600">{{ storeDescription }}</p>
          <!-- Likes and Dislikes -->
          <div class="flex justify-between mt-4">
            <div class="flex items-center">
              <h3 class="font-bold mr-2 text-gray-800">Likes:</h3>
              <p class="text-green-500 text-xl">{{ likes }}</p>
            </div>
            <div class="flex items-center">
              <h3 class="font-bold mr-2 text-gray-800">Dislikes:</h3>
              <p class="text-red-500 text-xl">{{ dislikes }}</p>
            </div>
          </div>
          <!-- Subcategories -->
          <div class="mb-8">
            <h3 class="font-bold mb-2 text-gray-800">Subcategories:</h3>
            <div class="grid grid-cols-3 gap-4">
              <div v-for="subCategory in subCategories" :key="subCategory.id" class="sub-category bg-f66305 text-white font-bold rounded-full px-2 py-1 transition-all duration-300 hover:bg-ab16be hover:scale-105 hover:shadow-lg">
                {{ subCategory.name }}
              </div>
            </div>
          </div>
          <!-- Total Sold Products -->
          <div class="mb-8">
            <h3 class="font-bold mb-2 text-gray-800">Total Sold Products:</h3>
            <div class="grid grid-cols-3 gap-4">
              <div v-for="(sold, index) in soldProducts" :key="index" class="sold-product bg-ab16be text-white font-bold rounded-full px-2 py-1 transition-all duration-300 hover:bg-f66305 hover:scale-105 hover:shadow-lg">
                {{ sold.subCategory }}: {{ sold.count }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        avatar: '',
        banner: '',
        storeName: 'Nombre de la tienda',
        storeDescription: 'Breve descripción de la tienda',
        subCategories: [
          { id: 1, name: 'Subcategoría 1' },
          { id: 2, name: 'Subcategoría 2' },
          { id: 3, name: 'Subcategoría 3' },
          { id: 4, name: 'Subcategoría 4' },
          { id: 5, name: 'Subcategoría 5' },
          { id: 6, name: 'Subcategoría 6' }
        ],
        likes: 100,
        dislikes: 20,
        soldProducts: [
          { subCategory: 'Subcategoría 1', count: 50 },
          { subCategory: 'Subcategoría 2', count: 30 },
          { subCategory: 'Subcategoría 3', count: 20 },
          { subCategory: 'Subcategoría 4', count: 40 },
          { subCategory: 'Subcategoría 5', count: 10 },
          { subCategory: 'Subcategoría 6', count: 15 }
        ],
        storeRegistered: false
      };
    },
    mounted() {
      this.getRandomAvatar();
      this.getRandomBanner();
    },
    methods: {
      getRandomAvatar() {
        fetch('https://source.unsplash.com/random/200x200')
          .then(response => {
            this.avatar = response.url;
          })
          .catch(error => {
            console.error(error);
          });
      },
      getRandomBanner() {
        fetch('https://source.unsplash.com/random/1024x576')
          .then(response => {
            this.banner = response.url;
          })
          .catch(error => {
            console.error(error);
          });
      },
      previewImage(event) {
        const file = event.target.files[0];
        if (file) {
          this.avatar = URL.createObjectURL(file);
        }
      },
      previewBanner(event) {
        const file = event.target.files[0];
        if (file) {
          this.banner = URL.createObjectURL(file);
        }
      },
      registerStore() {
        if (this.hasPurchasedSubCategory()) {
          this.storeRegistered = true;
        }
      },
      hasPurchasedSubCategory() {
        // Logic to check if the user has purchased any subcategory goes here
        // Returning true for the purpose of this demo
        return true;
      }
    }
  };
  </script>
  
  <style>
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
  </style>
  