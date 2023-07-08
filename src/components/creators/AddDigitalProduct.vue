<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 1100px; max-height: 900px;">
      <h2 class="text-3xl font-semibold mb-4">Agregar Nuevo Producto Digital</h2>
      <form class="grid grid-cols-2 gap-4">
        <div>
          <label for="productName" class="text-lg font-semibold">Nombre del Producto:</label>
          <input v-model="newProduct.name" id="productName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
        </div>

        <div>
          <label for="productPriceUSD" class="text-lg font-semibold">Precio del Producto:</label>
          <div class="flex items-center">
            <input v-model="newProduct.price" id="productPriceUSD" type="number" step="0.01" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceBTC">
          </div>
        </div>

        <div>
          <label for="productCategories" class="text-lg font-semibold">Subcategorías del Producto:</label>
          <select v-model="newProduct.subCategory" id="productCategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" multiple required>
            <option v-for="subCategory in ListsubCategories" :key="subCategory.id" :value="subCategory.id">{{ subCategory.nameSubCategory }}</option>
          </select>
        </div>
        <div>
          <label for="productPlainText" class="text-lg font-semibold">Descripcion:</label>
          <textarea v-model="newProduct.description" id="productPlainText" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
        </div>

        <div>
          <label for="productPlainText" class="text-lg font-semibold">Muestra de checker:</label>
          <textarea v-model="newProduct.checkerText" id="productPlainText" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
        </div>
        <div>
          <label for="productPlainText" class="text-lg font-semibold">Texto Plano:</label>
          <textarea v-model="newProduct.additional_details" id="productPlainText" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
        </div>

        <div>
          <label class="text-lg font-semibold">Vista Previa del Texto:</label>
          <div class="bg-gray-100 p-2 rounded-lg border border-gray-300 overflow-auto text-left" style="max-height: 200px; white-space: pre-line">{{ getPreviewText() }}</div>
          <p v-if="!hasPurchased" class="text-red-500 text-sm mt-2">Solo se mostraran en la web las primeras 10 lineas del contenido</p>
        </div>

        <div class="col-span-2">
          <button @click="addProduct()" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 self-end">
            Agregar Producto
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      newProduct: {
        name: '',
        description: '',
        checkerText: '',
        additional_details: '',
        price: 0,
        subCategory: null,
      },
      ListsubCategories: null,
      btcPrice: 0,
      hasPurchased: false,
    };
  },

  created() {
    this.fetchSubCategories()
  },
  methods: {
    addProduct() {
      console.log('Agregando nuevo producto:', this.newProduct);
      this.createDigitalProduct()
    },

    async fetchSubCategories() {
      await axios.get(`http://127.0.0.1:8000/api/categorias?formC=true`, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        this.ListsubCategories = response.data[1].subCategories
        console.log(this.subCategories)
      })
    },
    
    async createDigitalProduct() {
      await axios.post(`http://127.0.0.1:8000/api/productos/digit`, this.newProduct)
      .then(response => console.log(response.data))
      .catch(error => {console.log(error.response.data)})
    },

    getPreviewText() {
      const lines = this.newProduct.additional_details.split('\n');
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
