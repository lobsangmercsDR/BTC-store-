<template>
  <TopBar @open-modal="receivEmit"/>
  <homeview ref="homeViewRef" />
</template>

<script>
import TopBar from '@/components/headerNav.vue';
import realtimelastbuy from '@/components/realtimelastbuy.vue';
import realtimenewproduct from '@/components/realtimenewproduct.vue';
import newsbox from '@/components/newsbox.vue';
import SingleProduct from '@/components/SingleProduct.vue';
import SingleDigitalProduct from '@/components/SingleDigitalProduct.vue';
import AddDigitalProduct from '@/components/creators/AddDigitalProduct.vue';
import AddProduct from '@/components/creators/AddProduct.vue';
import DigitalCategoriesCreator from '@/components/admintoolscomponentes/DigitalCategoriesCreator.vue';
import invitationcodetool from '@/components/admintoolscomponentes/invitationcodetool.vue';
import usermanages from '@/components/admintoolscomponentes/usermanages.vue';
import rechar from '@/components/payments/rechar.vue';
import inventory from '@/components/payments/inventory.vue'
import productCard from '@/components/productCard.vue';
import homeview from '@/components/homeview.vue';
import users_profile_component from '@/components/usersdashboard/users_profile_component.vue';
import digital_product_view from '@/components/digital_product_view.vue';
import user_shopVue from '@/components/usersdashboard/user_shop.vue';




export default {
  name: 'HomePageEcommerce',
  components: {
    TopBar,
    realtimelastbuy,
    realtimenewproduct,
    newsbox,
    SingleProduct,
    SingleDigitalProduct,
    AddDigitalProduct,
    AddProduct,
    DigitalCategoriesCreator,
    invitationcodetool,
    usermanages,
    rechar,
    inventory,
    productCard,
    homeview,
    users_profile_component,
    digital_product_view,
    user_shopVue,


  },
  data() {
    return {
      showModal:true,
      product1: {
        title: 'Backpack',
        description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit In odit exercitationem fuga id nam quia',
        image: 'https://images.unsplash.com/photo-1494726161322-5360d4d0eeae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
        rating: 3,
        price: 220,
      },
      product2: {
        title: 'Sneakers',
        description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit In odit exercitationem fuga id nam quia',
        image: 'https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80',
        rating: 4,
        price: 120,
      },
      product3: {
        title: 'Watch',
        description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit In odit exercitationem fuga id nam quia',
        image: 'https://images.unsplash.com/photo-1521737711862-5a810fda9665?ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80',
        rating: 5,
        price: 300,
      },
    };
  },
  methods: {
    receivEmit(params) {
      console.log(params)
      this.$refs.homeViewRef.openModal(params.id, params.type);
    },

    addToCart(product) {
      console.log('Product added to cart:', product);
      // Implementar la lógica para agregar el producto al carrito aquí
    },
  },
};
</script>


<style>
.div6 {
  display: none;
}

.bg-light-gray {
  background-color: #fff;
}

.homepage-container {

    margin: 0 auto;
    padding: 20px;  
}

.grid-container {
  display: grid;
  grid-template-columns: minmax(0, 2fr);
  /* Crea 3 columnas de tamaño igual */
  grid-gap: 20px;
  /* Espacio entre las celdas */
  max-width: 5000px;
  margin: auto;

}

.table-container {
  grid-column: span 2;
  /* Ocupa 2 columnas */
}

.newsbox-container {
  grid-column: span 1;
  /* Ocupa 1 columna */
}

.table-fixed {
  width: 100%;
}

.espacio {
  height: 20px;
  /* Ajusta la altura del espacio según tus necesidades */
}

/* Estilos adicionales según sea necesario para los componentes */</style>