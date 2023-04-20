<template>
    <div>
      <TopBar />
      <h1>Welcome to my eCommerce store</h1>
      <p>This is the home page of my store</p>
    </div>
  </template>
  
  <script>
  import TopBar from '@/components/headerNav.vue';
  
  export default {
    name: 'HomePageEcommerce',
    components: {
      TopBar,
    },
  };
  </script>
  