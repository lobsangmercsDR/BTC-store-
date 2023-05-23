<template>
    <div class="parent">
      <div class="div1">
        <!-- Table 1 -->
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
              <tr v-for="(product, index) in productsTable1" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">{{ product.name }}</td>
                <td class="p-2">{{ product.quantitySold }}</td>
                <td class="p-2">{{ product.dateSold }}</td>
                <td class="p-2">{{ product.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="div2">
        <!-- Table 2 -->
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
              <tr v-for="(product, index) in productsTable2" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">{{ product.name }}</td>
                <td class="p-2">{{ product.quantitySold }}</td>
                <td class="p-2">{{ product.dateSold }}</td>
                <td class="p-2">{{ product.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="div3">
        <!-- Slider -->
        <div class="slider-container">
          <agile :options="sliderOptions" @afterChange="handleAfterChange" ref="agile">
            <div v-for="(product, index) in productsSlider" :key="index" class="slider-item">
              <div class="product-info">
                <div class="product-image">
                  <img :src="product.image" alt="Product Image">
                </div>
                <h4 class="product-name">{{ product.name }}</h4>
                <p class="product-price">$ {{ product.price }}</p>
                <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
              </div>
            </div>
          </agile>
        </div>
      </div>
      <div class="div4">
        <div class="slider-container">
          <agile :options="sliderOptions1" @afterChange="handleAfterChange" ref="agile">
            <div v-for="(product, index) in productsSlider" :key="index" class="slider-item">
              <div class="product-info">
                <div class="product-image">
                  <img :src="product.image" alt="Product Image">
                </div>
                <h4 class="product-name">{{ product.name }}</h4>
                <p class="product-price">$ {{ product.price }}</p>
                <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
              </div>
            </div>
          </agile>
        </div>
      </div>
      <div class="div5">
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
              <tr v-for="(product, index) in productsTable2" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">{{ product.name }}</td>
                <td class="p-2">{{ product.quantitySold }}</td>
                <td class="p-2">{{ product.dateSold }}</td>
                <td class="p-2">{{ product.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="div6">
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
              <tr v-for="(product, index) in productsTable2" :key="index" class="bg-gray-200 text-gray-700">
                <td class="p-2">{{ product.name }}</td>
                <td class="p-2">{{ product.quantitySold }}</td>
                <td class="p-2">{{ product.dateSold }}</td>
                <td class="p-2">{{ product.price }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { VueAgile } from 'vue-agile'
  
  export default {
    components: {
      'agile': VueAgile,
    },
    data() {
      return {
        sliderOptions: {
          infinite: true,
          slidesToShow: 4,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 3000,
          dots: true,
          initialSlide: 0,
        },
        sliderOptions1: {
          infinite: true,
          slidesToShow: 4,
          slidesToScroll: -1,
          autoplay: true,
          autoplaySpeed: 3000,
          dots: true,
          initialSlide: 0,
        },
        productsTable1: [
          { name: 'Product A', quantitySold: '20', dateSold: '2023-05-21', price: '200' },
          { name: 'Product B', quantitySold: '10', dateSold: '2023-05-21', price: '150' },
          { name: 'Product C', quantitySold: '5', dateSold: '2023-05-21', price: '100' },
        ],
        productsTable2: [
          { name: 'Product X', quantitySold: '15', dateSold: '2023-05-22', price: '250' },
          { name: 'Product Y', quantitySold: '12', dateSold: '2023-05-22', price: '180' },
          { name: 'Product Z', quantitySold: '8', dateSold: '2023-05-22', price: '120' },
        ],
        productsSlider: [
          { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
          { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
          { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
          { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
          { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
          { id: 2, name: 'Product Slider 2', price: '180', image: 'product2.jpg' },
          { id: 3, name: 'Product Slider 3', price: '120', image: 'product3.jpg' },
          { id: 4, name: 'Product Slider 4', price: '300', image: 'product4.jpg' },
          { id: 5, name: 'Product Slider 5', price: '220', image: 'product5.jpg' },
          { id: 6, name: 'Product Slider 6', price: '150', image: 'product6.jpg' },
        ],
      }
    },
    methods: {
      goToProduct(productId) {
        this.$router.push({ name: 'Product', params: { id: productId } })
      },
      handleAfterChange(currentSlide) {
        if (currentSlide === this.productsSlider.length - 1) {
          this.$refs.agile.goTo(0)
        }
      },
    }
  }
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
    grid-area: 1 / 2 / 3 / 5;
    align-self: start;
    overflow: hidden;
  }
  
  .div4 {
    grid-area: 2 / 2 / 3 / 5;
    align-self: start;
    overflow: hidden;
  }
  
  .div5 {
    grid-area: 1 / 5 / 4 / 6;
  }
  
  .div6 {
    grid-area: 2 / 6 / 3 / 5;
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
  
  .slider-items-wrapper {
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    margin: -10px;
  }
  
  .slider-item {
    height: 220px;
    width: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
    transition: transform 0.3s ease;
  }
  
  .slider-item:hover {
    transform: scale(1.02);
  }
  
  .product-info {
    text-align: center;
  }
  
  .product-image img {
    width: 100%;
    max-height: 120px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
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
  