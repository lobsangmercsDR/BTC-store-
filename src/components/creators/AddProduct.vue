<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 1100px; max-height: 900px;">
      <h2 class="text-3xl font-semibold mb-4">Agregar Nuevo Producto</h2>
      <form class="grid grid-cols-2 gap-4" @submit.prevent="handle">
        <div>
          <label for="productName" class="text-lg font-semibold">Nombre del Producto:</label>
          <input v-model="newProduct.nameProduct" id="productName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('nameProduct')}">
          <div v-if="error && error.hasOwnProperty('nameProduct')" class="text-red-500 errorText"> 
            <small>{{ error.nameProduct[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productDescription" class="text-lg font-semibold">Descripción del Producto:</label>
          <textarea v-model="newProduct.description" id="productDescription" :class="{'errorInput': error && error.hasOwnProperty('description')}" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4"   ></textarea>
          <div v-if="error && error.hasOwnProperty('description')" class="text-red-500 errorText"> 
              <small>{{ error.description[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productPriceBTC" class="text-lg font-semibold">Precio del Producto (BTC):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceBTC" id="productPriceBTC" type="number" step="0.001" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" :class="{'errorInput':error && error.hasOwnProperty('priceProduct')}"  @input="updatePriceUSD">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(2) }} USD</p>
          </div>
          <div v-if="error && error.hasOwnProperty('priceProduct')" class="text-red-500 errorText"> 
              <small>{{ error.priceProduct[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productPriceUSD" class="text-lg font-semibold">Precio del Producto (USD):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceUSD" id="productPriceUSD" type="number" step="0.01" :class="{'errorInput':error && error.hasOwnProperty('priceProduct')}" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceBTC">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(8) }} BTC</p>
          </div>
        </div>
        <div>
          <label for="productImage" class="text-lg font-semibold">Imagen del Producto:</label>
          <input type="file" style="border-radius:15px" accept="image/*" @change="handleImageUpload"  :class="{'errorInput': error && error.hasOwnProperty('image_product')}">
          <div v-if="error && error.hasOwnProperty('image_product')" class="text-red-500 errorText"> 
            <small>{{ error.image_product[0] }}</small>
          </div>
        </div>
        <div v-if="newProduct.image">
          <label class="text-lg font-semibold">Vista Previa de la Imagen:</label>
          <img :src="newProduct.image" class="w-40 h-auto mt-2 rounded-lg">
        </div>
        <div>
          <label for="productBrand" class="text-lg font-semibold">Marca del Producto:</label>
          <input v-model="newProduct.brand" id="productBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" >
        </div>
        <div>
          <label for="productVariants" class="text-lg font-semibold">Variantes del Producto:</label>
          <textarea v-model="newProduct.variants" id="productVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2" ></textarea>
        </div>
        <div>
          <label for="productCategories" class="text-lg font-semibold">Categorías del Producto:</label>
          <select v-model="newProduct.category" id="productCategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('subcategory_id')}" >
            <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.nameCategory }}</option>
          </select>
          <div v-if="error && error.hasOwnProperty('categor')" class="text-red-500 errorText"> 
            <small>{{ error.image_product[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productSubcategories" class="text-lg font-semibold">Subcategorías del Producto:</label>
          <select v-model="newProduct.subcategory_id" id="productSubcategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('subcategory_id')}" >
            <option v-for="subcategory in getSubcategories(newProduct.category)" :key="subcategory" :value="subcategory.id">{{ subcategory.nameSubCategory }} </option>
          </select>
          <div v-if="error && error.hasOwnProperty('subcategory_id')" class="text-red-500 errorText"> 
            <small>{{ error.subcategory_id[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productQuantity" class="text-lg font-semibold">Cantidad del Producto:</label>
          <input v-model="newProduct.quantity" id="productQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" min="1" >
        </div>
        <div>
          <label for="productDetails" class="text-lg font-semibold">Detalles Adicionales:</label>
          <textarea v-model="newProduct.aditional_details" id="productDetails" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" ></textarea>
        </div>
        <div class="col-span-2">
          <button @click="CreateProduct" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 self-end">
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
        nameProduct: '',
        description: '',
        priceProduct: 0,
        priceUSD: 0,
        priceBTC: 0,
        image_product: null,
        image: null,
        is_digital: null,
        brand: '',
        variants: '',
        subcategory_id: 0,
        quantity: 1,
        aditional_details: '',
      },
      error: null, 
      btcPrice: 0
    };
  },

  created() {
    this.fetchCategoriesForCreate();
  },

  mounted() {
    this.fetchBTCPrice();
  },
  methods: {
    async fetchProducts() {
      await axios.get('http://127.0.0.1:8000/api/productos', {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {})
      .catch(error => {console.log(error)})
    },

    async fetchCategoriesForCreate() {
      await axios.get("http://127.0.0.1:8000/api/categorias", {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => { this.categories = response.data;})
      .catch(error => {console.log(error)})
    },
    

    async CreateProduct() {
      const formData= new FormData();
      const ObjCopy = Object.assign({}, this.newProduct)

      delete ObjCopy.subcategory
      delete ObjCopy.priceUSD 
      console.log(ObjCopy)
      ObjCopy.priceProduct = ObjCopy.priceBTC
      if (ObjCopy.image_product == null) {
        delete ObjCopy.image_product
      }
      delete ObjCopy.priceBTC
      delete ObjCopy.image
      console.log(ObjCopy)

      let properties = Object.keys(ObjCopy)
      for (let i = 0; i < properties.length; i++) {
        let clave = properties[i]
        let Obj = ObjCopy[clave]
        formData.append(clave, Obj)
      }
      await axios.post('http://127.0.0.1:8000/api/productos',formData,{
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response=> {console.log(response)})
      .catch(error => {
        this.error = error.response.data; 
        console.log(this.error)})
      .finally(res => {this.cleanForm()})
    },

    async fetchBTCPrice() {
      try {
        const response = await axios.get('https://api.coinbase.com/v2/prices/spot?currency=USD');
        this.btcPrice = parseFloat(response.data.data.amount);
      } catch (error) {
        console.error('Error al obtener el precio del BTC:', error);
      }
    },
    cleanForm() {
      console.log('Agregando nuevo producto:', this.newProduct);
      this.newProduct.subcategory_id = 0
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
    getSubcategories(category) {
      // console.log(category)
      if (category != null) {
        const selectedCategory = this.categories.find((c) => c.id == category)
        return selectedCategory.subCategories
      }
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
