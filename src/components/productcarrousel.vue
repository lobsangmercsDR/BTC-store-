<template>
  <div class="flex max-w-screen-sm bg-gray-100 shadow-lg rounded-lg overflow-hidden">
    <div class="w-1/3 bg-cover" :style="'background-image: url(' + product.image + ')'">
    </div> 
    <div class="w-2/3 p-4">
      <h1 class="text-gray-900 font-bold text-2xl">{{ product.title }}</h1>
      <p class="mt-2 text-gray-600 text-sm">{{ product.description }}</p>
      <div class="flex item-center mt-2">
        <svg v-for="index in 5" :key="index" class="w-5 h-5 fill-current" :class="index <= product.rating ? 'text-gray-700' : 'text-gray-500'" viewBox="0 0 24 24">
          <path d="M12 17.27L18.18 21L16.54 13.97L22 9.24L14.81 8.63L12 2L9.19 8.63L2 9.24L7.46 13.97L5.82 21L12 17.27Z"/>
        </svg>
      </div>
      <div class="flex item-center justify-between mt-3">
        <h1 class="text-gray-700 font-bold text-xl">${{ product.price }}</h1>
        <button class="px-3 py-2 bg-gray-800 text-white text-xs font-bold uppercase rounded" @click="addToCart">Add to Card</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  methods: {
    addToCart() {
      this.$emit('add-to-cart', this.product);
    }
  }
};
</script>
