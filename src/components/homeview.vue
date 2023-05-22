<template>
    <div class="parent">
      <div class="div1">
        <div class="component-container component-container-color1">
          <table class="table text-gray-400 border-separate space-y-4 text-sm">
            <thead class="bg-gray-800 text-gray-500">
              <tr>
                <th class="p-2">Product</th>
                <th class="p-2">Quantity Sold</th>
                <th class="p-2">Date Sold</th>
                <th class="p-2">Price</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">
                  {{ product.name }}
                </td>
                <td class="p-2">
                  {{ product.quantitySold }}
                </td>
                <td class="p-2">
                  {{ product.dateSold }}
                </td>
                <td class="p-2">
                  {{ product.price }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="div2">
        <div class="component-container component-container-color2">
          <table class="table text-gray-400 border-separate space-y-4 text-sm">
            <thead class="bg-gray-800 text-gray-500">
              <tr>
                <th class="p-2">Product</th>
                <th class="p-2">Quantity Sold</th>
                <th class="p-2">Date Sold</th>
                <th class="p-2">Price</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">
                  {{ product.name }}
                </td>
                <td class="p-2">
                  {{ product.quantitySold }}
                </td>
                <td class="p-2">
                  {{ product.dateSold }}
                </td>
                <td class="p-2">
                  {{ product.price }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="div3">
        <div class="slider-container">
          <div class="slider-wrapper">
            <div class="swiper-container" ref="swiper">
              <div class="swiper-wrapper">
                <div class="swiper-slide" v-for="(product, index) in products" :key="index">
                  <div class="slider-item">
                    <div class="product-info">
                      <h4 class="product-name">{{ product.name }}</h4>
                      <p class="product-price">{{ product.price }}</p>
                      <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="swiper-pagination"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="div4"></div>
      <div class="div5"></div>
      <div class="div6"></div>
    </div>
  </template>
  
  <script>
  import Swiper from 'swiper';
  
  export default {
    data() {
      return {
        products: [
          { id: 1, name: 'Product 1', price: '$10.00' },
          { id: 2, name: 'Product 2', price: '$15.00' },
          { id: 3, name: 'Product 3', price: '$20.00' },
          { id: 4, name: 'Product 4', price: '$10.00' },
          { id: 5, name: 'Product 5', price: '$15.00' },
          { id: 6, name: 'Product 6', price: '$20.00' },
          { id: 7, name: 'Product 7', price: '$10.00' },
          { id: 8, name: 'Product 8', price: '$15.00' },
          { id: 9, name: 'Product 9', price: '$20.00' },
        ],
      };
    },
    mounted() {
      this.initSwiper();
    },
    methods: {
      initSwiper() {
        this.swiper = new Swiper(this.$refs.swiper, {
          slidesPerView: 4,
          spaceBetween: 5,
          loop: true,
          autoplay: {
            delay: 3000,
            disableOnInteraction: false,
          },
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
          effect: 'slide',
          speed: 800,
        });
      },
      goToProduct(productId) {
        // Implement your logic to navigate to the product page
      },
    },
  };
  </script>
  
  <style>
  .parent {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(5, 1fr);
    grid-column-gap: 30px;
    grid-row-gap: 0px;
    align-items: start;
  }
  
  .div1 {
    grid-area: 1 / 1 / 2 / 2;
  }
  
  .div2 {
    grid-area: 2 / 1 / 3 / 2;
  }
  
  .div3 {
    grid-area: 1 / 2 / 3 / 3;
    align-self: start;
  }
  
  .div4 {
    grid-area: 2 / 2 / 3 / 3;
  }
  
  .div5 {
    grid-area: 1 / 3 / 2 / 4;
  }
  
  .div6 {
    grid-area: 2 / 3 / 3 / 4;
  }
  
  .component-container {
    padding: 10px;
    border-radius: 8px;
    text-align: center;
  }
  
  .component-container-color1 {
    background-color: #f66305;
    color: white;
  }
  
  .component-container-color2 {
    background-color: #ab16be;
    color: white;
  }
  
  .slider-container {
    height: 100%;
  }
  
  .slider-wrapper {
    width: 100%;
    max-width: 600px;
    height: 100%;
  }
  
  .swiper-container {
    width: 100%;
    height: 100%;
  }
  
  .slider-item {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f3f3f3;
  }
  
  .product-info {
    text-align: center;
  }
  
  .product-name {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .product-price {
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .product-button {
    background-color: #fff;
    color: #333;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .product-button:hover {
    background-color: #eee;
  }
  
  .table {
    border-spacing: 0 10px;
  }
  
  .table tr {
    border-radius: 4px;
  }
  
  .bg-gray-200 {
    background-color: rgba(255, 255, 255, 0.8);
  }
  </style>
  