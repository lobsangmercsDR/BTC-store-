<template>
  <div class="card shadow-lg max-w-xs rounded overflow-hidden">
    <div class="card-header" :style="{ backgroundColor: primaryColor }"></div>
    <img :src="image" :alt="title" class="w-full">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ title }}</div>
      <p class="text-gray-700 text-base">{{ description }}</p>
      <p class="text-gray-700 text-base">{{ price }}</p>
    </div>
    <div class="px-6 pt-4 pb-2">
      <button class="button" @click="addToCart()">
        <span>Add to Cart</span>
        <span class="button-icon" :style="{ backgroundColor: secondaryColor }"></span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: 'Product Title'
    },
    image: {
      type: String,
      default: 'https://via.placeholder.com/300x200'
    },
    description: {
      type: String,
      default: 'Some text about the product...'
    },
    price: {
      type: String,
      default: '$0.00'
    }
  },
  data() {
    return {
      primaryColor: '#ac15c1',
      secondaryColor: '#f96207'
    };
  },
  methods: {
    addToCart() {
      // Aquí se puede agregar la lógica para agregar el producto al carrito
    }
  }
};
</script>

<style scoped>
.card {
  background-color: #fff;
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease-in-out;
}

.card:hover {
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

.card-header {
  height: 10px;
}

.card img {
  object-fit: cover;
  object-position: center;
  height: 200px;
  transition: transform 0.3s ease-in-out;
}

.card:hover img {
  transform: scale(1.05);
}

.button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 10px 20px;
  background-color: #f96207;
  border: none;
  border-radius: 20px;
  color: #fff;
  font-weight: bold;
  text-transform: uppercase;
  position: relative;
  overflow: hidden;
  transition: background-color 0.3s ease-in-out;
}

.button:hover {
  background-color: #ac15c1;
}

.button span {
  z-index: 2;
}

.button-icon {
  position: absolute;
  top: 0;
  right: -50%;
  bottom: 0;
  width: 50%;
  background-color: #ac15c1;
  transform-origin: right center;
  transform: scaleX(0);
  transition: transform 0.3s ease-in-out;
}

.button:hover .button-icon {
  transform: scaleX(1);
}
</style>
