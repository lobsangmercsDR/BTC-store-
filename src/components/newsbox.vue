<template>
    <div class="mx-auto max-w-500 w-full px-4 overflow-x-auto">
      <div class="border-collapse border-gray-300 rounded-lg overflow-hidden bg-blue-900 text-white">
        <div class="py-2 text-center">
          <h2 class="text-lg font-medium">s</h2>
        </div>
        <div v-for="(noticia, index) in noticias" :key="index"
          :class="index % 2 === 0 ? 'bg-white hover:bg-gray-200' : 'bg-gray-50 hover:bg-gray-200'">
          <div class="w-full px-2 py-0.5 border-b border-gray-300">
            <div class="text-xs font-medium text-gray-500 uppercase tracking-wider font-bold">{{ noticia.fecha }}</div>
            <a :href="noticia.url" class="text-xs font-medium hover:underline text-black">{{ noticia.titulo }}</a>
            <div class="text-xs text-black">{{ noticia.contenido }}</div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        noticias: [],
      };
    },
    mounted() {
      this.cargarNoticias();
    },
    methods: {
      cargarNoticias() {
        axios.get('https://mi-api.com/noticias')
          .then(response => {
            this.noticias = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
    },
  };
  </script>
  