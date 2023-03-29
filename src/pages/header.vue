<template>
  <div class="flex flex-wrap justify-center">
    <div class="w-full md:w-1/3 p-4">
      <h2 class="font-bold mb-2 text-center">Artículos vendidos recientemente</h2>
      <ul class="list-disc pl-5">
        <li v-for="item in soldItems" :key="item.id" class="mb-2">{{ item.name }}</li>
      </ul>
    </div>
    <div class="w-full md:w-1/3 p-4">
      <h2 class="font-bold mb-2 text-center">Noticias</h2>
      <ul class="list-disc pl-5">
        <li v-for="news in latestNews" :key="news.id" class="mb-2">{{ news.title }}</li>
      </ul>
    </div>
    <div class="w-full md:w-1/3 p-4">
      <h2 class="font-bold mb-2 text-center">Artículos recién subidos</h2>
      <ul class="list-disc pl-5">
        <li v-for="item in newItems" :key="item.id" class="mb-2">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      soldItems: [
        { id: 1, name: 'Artículo 1' },
        { id: 2, name: 'Artículo 2' },
        { id: 3, name: 'Artículo 3' },
      ],
      latestNews: [
        { id: 1, title: 'Noticia 1' },
        { id: 2, title: 'Noticia 2' },
        { id: 3, title: 'Noticia 3' },
      ],
      newItems: [
        { id: 1, name: 'Artículo 4' },
        { id: 2, name: 'Artículo 5' },
        { id: 3, name: 'Artículo 6' },
      ],
    };
  },
};
</script>

<style>
/* Estilos personalizados */
li {
  color: #333;
  font-size: 16px;

  
}
</style>
