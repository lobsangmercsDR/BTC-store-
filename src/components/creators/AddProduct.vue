<template>
  <div class="container">
    <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 1100px; max-height: 900px;">
      <h2 class="text-3xl font-semibold mb-4">Agregar Nuevo Producto</h2>
      <form @submit.prevent="addProduct" class="grid grid-cols-2 gap-4">
        <div>
          <label for="productName" class="text-lg font-semibold">Nombre del Producto:</label>
          <input v-model="newProduct.name" id="productName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
        </div>
        <div>
          <label for="productDescription" class="text-lg font-semibold">Descripción del Producto:</label>
          <textarea v-model="newProduct.description" id="productDescription" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
        </div>
        <div>
          <label for="productPriceBTC" class="text-lg font-semibold">Precio del Producto (BTC):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceBTC" id="productPriceBTC" type="number" step="0.001" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceUSD">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(2) }} USD</p>
          </div>
        </div>
        <div>
          <label for="productPriceUSD" class="text-lg font-semibold">Precio del Producto (USD):</label>
          <div class="flex items-center">
            <input v-model="newProduct.priceUSD" id="productPriceUSD" type="number" step="0.01" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required @input="updatePriceBTC">
            <p class="text-gray-500 text-sm ml-2">Precio actual del BTC: {{ btcPrice.toFixed(8) }} BTC</p>
          </div>
        </div>
        <div>
          <label for="productImage" class="text-lg font-semibold">Imagen del Producto:</label>
          <input type="file" accept="image/*" @change="handleImageUpload" required>
        </div>
        <div v-if="newProduct.image">
          <label class="text-lg font-semibold">Vista Previa de la Imagen:</label>
          <img :src="newProduct.image" class="w-40 h-auto mt-2 rounded-lg">
        </div>
        <div>
          <label for="productBrand" class="text-lg font-semibold">Marca del Producto:</label>
          <input v-model="newProduct.brand" id="productBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
        </div>
        <div>
          <label for="productVariants" class="text-lg font-semibold">Variantes del Producto:</label>
          <textarea v-model="newProduct.variants" id="productVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2" required></textarea>
        </div>
        <div>
          <label for="productCategories" class="text-lg font-semibold">Categorías del Producto:</label>
          <select v-model="newProduct.category" id="productCategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
            <option v-for="category in categories" :key="category.id" :value="category.name">{{ category.name }}</option>
          </select>
        </div>
        <div>
          <label for="productSubcategories" class="text-lg font-semibold">Subcategorías del Producto:</label>
          <select v-model="newProduct.subcategory" id="productSubcategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" required>
            <option v-for="subcategory in getSubcategories(newProduct.category)" :key="subcategory" :value="subcategory">{{ subcategory }} </option>
          </select>
        </div>
        <div>
          <label for="productQuantity" class="text-lg font-semibold">Cantidad del Producto:</label>
          <input v-model="newProduct.quantity" id="productQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" min="1" required>
        </div>
        <div>
          <label for="productDetails" class="text-lg font-semibold">Detalles Adicionales:</label>
          <textarea v-model="newProduct.aditional_details" id="productDetails" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" required></textarea>
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
        nameProduct: 'Ayuda',
        description: 'IDK',
        price: 0,
        priceUSD: 11231,
        image_product: null,
        image: null,
        is_digital: true,
        brand: 'Huae',
        variants: '13123123',
        subcategory_id: 0,
        quantity: 13,
        aditional_details: '131231231sd3',
      },
      btcPrice: 0,
      categories: [
        {
          id: 1,
          name: 'Electrónica',
          subcategories: ['Teléfonos', 'Computadoras', 'Accesorios'],
        },
        {
          id: 2,
          name: 'Ropa',
          subcategories: ['Hombres', 'Mujeres', 'Niños'],
        },
        {
          id: 3,
          name: 'Hogar',
          subcategories: ['Decoración', 'Electrodomésticos', 'Muebles'],
        },
        {
          id: 4,
          name: 'Deportes',
          subcategories: ['Fútbol', 'Baloncesto', 'Natación'],
        },
        {
          id: 5,
          name: 'Alimentación',
          subcategories: ['Frutas', 'Verduras', 'Carnes'],
        },
      ],
    };
  },
  mounted() {
    this.fetchBTCPrice();
  },
  methods: {
    ChangeSubCategory(event) {
      this
    },


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
      .then(response => {this.categories = response.data})
      .catch(error => {console.log(error.response.data)})
    },
    

    async CreateProduct() {
      const formData= new FormData();
      const ObjCopy = Object.assign({}, this.newProduct)

      delete ObjCopy.subcategory
      delete ObjCopy.priceUSD 
      ObjCopy.priceProduct = ObjCopy.priceBTC
      console.log(ObjCopy)
      delete ObjCopy.priceBTC
      delete ObjCopy.image
      ObjCopy.subcategory_id = this.Indsubcategory.id
      console.log(this.newProduct)
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
      .catch(error => {console.log(error.response.data)})
    },

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
        nameProduct: '',
        description: '',
        priceBTC: 0,
        priceUSD: 0,
        image: '',
        images_bank: '',
        brand: '',
        variants: '',
        category: '',
        subcategory: '',
        quantity: 0,
        aditional_details: '',
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
    getSubcategories(category) {
      if (category !== null && this.category !== null) {
        const selectedCategory = this.categories.find((c) => c.id == category )
        console.log(selectedCategory.subCategories)
        console.log(this.newProduct.subcategory_id)

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
