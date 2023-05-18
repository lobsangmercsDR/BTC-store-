<template>
  <div class="bg-light-gray">
    <TopBar />
    <div class="d-flex flex-row justify-content-between margin-top">
      <div class="flex-1 mr-4">
        <table class="table-fixed w-2/5">
          <realtimelastbuy />
        </table>
      </div>
      <div class="flex-1">
        <newsbox />
      </div>
      <div class="flex-1">
        <table class="table-fixed w-2/5">
          <realtimenewproduct />
        </table>
      </div>
    </div>
   
     <SingleProduct />
     <SingleDigitalProduct />
     <productCard />
     <AddDigitalProduct/>


  </div>
</template>
  
<script>
import TopBar from '@/components/headerNav.vue';
import realtimelastbuy from '@/components/realtimelastbuy.vue';
import realtimenewproduct from '@/components/realtimenewproduct.vue';
import newsbox from '@/components/newsbox.vue';
import productCard from '@/components/productCard.vue';
import SingleProduct from '@/components/SingleProduct.vue';
import SingleDigitalProduct from '@/components/SingleDigitalProduct.vue';
import AddDigitalProduct from '@/components/creators/AddDigitalProduct.vue';


export default {
  name: 'HomePageEcommerce',
  components: {
    TopBar,
    realtimelastbuy,
    realtimenewproduct,
    newsbox,
    productCard,
    SingleProduct,
    SingleDigitalProduct,
    AddDigitalProduct,
  },
  data() {
    return {
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
    addToCart(product) {
      console.log('Product added to cart:', product);
      // Implementar la lógica para agregar el producto al carrito aquí
    },
  },
};
</script>
  
<style>
.bg-light-gray {
  background-color: #f2f2f2;
}

.d-flex {
  display: flex;
}

.flex-row {
  flex-direction: row;
}

.justify-content-between {
  justify-content: space-between;
}

.realtimelastbuy {
  margin-right: 50px;
}

.realtimenewproduct {
  margin-left: 100px;
}

.margin-top {
  margin-top: 16px;
}
</style>