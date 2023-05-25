<template>
  <div>
    <headerNav/>
    <users_profile_component/>
    <profile_modification/>
    <orders/>
    <sell_orders/>
  </div>
</template>

<script>
import headerNav from '@/components/headerNav.vue';
import users_profile_component from '@/components/usersdashboard/users_profile_component.vue';
import profile_modification from '@/components/usersdashboard/profile_modification.vue';
import orders from '@/components/usersdashboard/orders.vue';
import sell_orders from '@/components/usersdashboard/sell_orders.vue';




export default {
  components: {
    headerNav,
    users_profile_component,
    profile_modification,
    orders,
    sell_orders,

  },
};
</script>

<style>
/* Estilos específicos para la página de lista de productos */
</style>
