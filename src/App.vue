<template>
  <div id="app">
    <router-view />
    <ProductCard  v-if="ShowCard"/>
  </div>
</template>

<script>
import ProductCard from './components/productCard.vue';

export default {
  name: 'App',
  components: {
    ProductCard,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
