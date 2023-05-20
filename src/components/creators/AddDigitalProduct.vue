<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 1100px; max-height: 900px;">
      <h2 class="text-3xl font-semibold mb-4">Agregar Nuevo Producto Digital</h2>
      <form @submit.prevent="addProduct" class="grid grid-cols-2 gap-4">
        <div>
          <label for="productName" class="text-lg font-semibold">Nombre del Producto:</label>
          <input v-model="newProduct.name" id="productName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
        </div>

        <div>
          <label for="productImage" class="text-lg font-semibold">Imagen del Producto:</label>
          <input type="file" accept="image/*" @change="handleImageUpload" required>
        </div>

        <div>
          <label for="productPriceUSD" class="text-lg font-semibold">Precio del Producto (USD):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceUSD" id="productPriceUSD" type="number" step="0.01" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceBTC">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(8) }} BTC</p>
          </div>
        </div>

        <div>
          <label for="productPriceBTC" class="text-lg font-semibold">Precio del Producto (BTC):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceBTC" id="productPriceBTC" type="number" step="0.001" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceUSD">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(2) }} USD</p>
          </div>
        </div>

        <div v-if="newProduct.image">
          <label class="text-lg font-semibold">Vista Previa de la Imagen:</label>
          <img :src="newProduct.image" class="w-40 h-auto mt-2 rounded-lg">
        </div>

        <div>
          <label for="productCategories" class="text-lg font-semibold">Categorías del Producto:</label>
          <select v-model="newProduct.categories" id="productCategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" multiple required>
            <option v-for="category in categories" :key="category.id" :value="category">{{ category.name }}</option>
          </select>
        </div>

        <div v-for="category in newProduct.categories" :key="category.id">
          <label :for="`productSubcategories_${category.id}`" class="text-lg font-semibold">Subcategorías de {{ category.name }}:</label>
          <select v-model="category.subcategories" :id="`productSubcategories_${category.id}`" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" multiple required>
            <option v-for="subcategory in category.subcategories" :key="subcategory">{{ subcategory }}</option>
          </select>
        </div>

        <div>
          <label for="productPlainText" class="text-lg font-semibold">Texto Plano:</label>
          <textarea v-model="newProduct.plainText" id="productPlainText" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
        </div>

        <div>
          <label class="text-lg font-semibold">Vista Previa del Texto:</label>
          <div class="bg-gray-100 p-2 rounded-lg border border-gray-300 overflow-auto text-left" style="max-height: 200px; white-space: pre-line">{{ getPreviewText() }}</div>
          <p v-if="!hasPurchased" class="text-red-500 text-sm mt-2">Solo se mostraan el la web las primeras 10 lineas del contenido</p>
        </div>

        <div>
          <label for="productQuantity" class="text-lg font-semibold">Cantidad:</label>
          <input v-model="newProduct.quantity" id="productQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
        </div>

        <div class="col-span-2">
          <button type="submit" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 self-end">
            Agregar Producto
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newProduct: {
        name: '',
        description: '',
        priceBTC: 0,
        priceUSD: 0,
        image: '',
        brand: '',
        variants: '',
        categories: [],
        subcategories: [],
        plainText: '',
        quantity: 0,
      },
      btcPrice: 0,
      categories: [
        {
          id: 1,
          name: 'Credit/Debit Cards',
          subcategories: ['Visa', 'Mastercard', 'American Express'],
        },
        // Resto de las categorías existentes
      ],
      hasPurchased: false,
    };
  },
  mounted() {
    this.fetchBTCPrice();
  },
  methods: {
    async fetchBTCPrice() {
      try {
        const response = await axios.get('https://api.coinbase.com/v2/prices/spot?currency=USD');
        this.btcPrice = parseFloat(response.data.data.amount);
      } catch (error) {
        console.error('Error al obtener el precio del BTC:', error);
      }
    },
    addProduct() {
      console.log('Agregando nuevo producto:', this.newProduct);
      this.newProduct = {
        name: '',
        description: '',
        priceBTC: 0,
        priceUSD: 0,
        image: '',
        categories: [],
        subcategories: [],
        plainText: '',
        quantity: 0,
        checker_needed_product: false,
      };
    },
    updatePriceUSD() {
      const btcPriceUSD = this.btcPrice * this.newProduct.priceBTC;
      this.newProduct.priceUSD = btcPriceUSD.toFixed(2);
    },
    updatePriceBTC() {
      const usdPriceBTC = this.newProduct.priceUSD / this.btcPrice;
      this.newProduct.priceBTC = usdPriceBTC.toFixed(8);
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.newProduct.image = reader.result;
      };
      reader.readAsDataURL(file);
    },
    getPreviewText() {
      const lines = this.newProduct.plainText.split('\n');
      return lines.slice(0, 5).join('\n');
    },
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: row;
  align-items: center;
  height: 100vh;
}

.bg-white {
  margin: 0 auto;
}

form label {
  display: block;
  margin-bottom: 0.5rem;
}

form input[type="text"],
form textarea,
form input[type="number"],
form input[type="file"],
form select {
  width: 100%;
}

form input[type="file"] {
  padding: 0.5rem;
}

form p {
  margin-top: 0.5rem;
}

button {
  margin-top: 1rem;
}
</style>
