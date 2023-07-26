<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import ProductCard from './components/productCard.vue';
import homeview from './components/homeview.vue';

export default {
  name: 'App',
  components: {
    ProductCard,
    homeview,
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
  overflow: visible;
}
</style>
