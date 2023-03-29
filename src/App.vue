<template>
  <div>
    <router-view />
  </div>
</template>

<script>
import header from './components/header.vue'
export default {
  name: 'App',
  components: {
    header

  }
}
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
