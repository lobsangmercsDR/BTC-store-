<template>
      <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 1100px; max-height: 1100px;">
      <h2 class="text-3xl font-semibold mb-4">Agregar Nuevo Producto</h2>
      <div class="flex typProd">
          <label for="productType" class="text-lg font-semibold">Tipo de Producto:</label>
          <select name="productType" v-model="isMethod" @change="selectProductType()">
            <option value=f>Fisico</option>
            <option value=t>Metodo</option>
          </select>
        </div>
      <form class="grid grid-cols-2 gap-4 form-add" @submit.prevent>
        <div>
          <label for="productName" class="text-lg font-semibold">Nombre del Producto:</label>
          <input v-model="newProduct.name" id="productName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('nameProduct')}">
          <div v-if="error && error.hasOwnProperty('nameProduct')" class="text-red-500 errorText"> 
            <small>{{ error.name[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productPriceBTC" class="text-lg font-semibold">Precio del Producto:</label>
          <div class="flex items-center">
            <input v-model="newProduct.price" id="productPriceBTC" type="number" step="0.001" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" :class="{'errorInput':error && error.hasOwnProperty('price')}"  @input="updatePriceUSD">
          </div>
          <div v-if="error && error.hasOwnProperty('price')" class="text-red-500 errorText"> 
              <small>{{ error.price[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productImage" class="text-lg font-semibold">Imagen del Producto:</label>
          <input type="file" style="border-radius:15px" accept="image/*" @change="handleImageUpload"  :class="{'errorInput': error && error.hasOwnProperty('image_product')}">
          <div v-if="error && error.hasOwnProperty('image_product')" class="text-red-500 errorText"> 
            <small>{{ error.image_product[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productBrand" class="text-lg font-semibold">Lugares disponibles:</label>
          <input v-model="newProduct.address_direction" id="productBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('address_direction')}">
          <div v-if="error && error.hasOwnProperty('address_direction')" class="text-red-500 errorText"> 
            <small>{{ error.address_direction[0] }}</small>
          </div>
        </div>
        <div v-if="newProduct.image" style="margin-bottom:20px ;">
          <label class="text-lg font-semibold">Vista Previa de la Imagen:</label>
          <img :src="newProduct.image" class="w-40 h-auto mt-2 rounded-lg">
        </div>
        <div v-if="isMethod === 'f'">
          <label for="productSubcategories" class="text-lg font-semibold">Subcategorías del Producto:</label>
          
          <select v-model="newProduct.subCat_id" id="productSubcategories" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('subCat_id')}" >
            <option style="margin:auto;"> </option>
            <option style="margin:auto;" v-for="subcategory in this.categories" :key="subcategory" :value="subcategory.id">{{ subcategory.nameSubCategory }} </option>
          </select>
          <div v-if="error && error.hasOwnProperty('subCat_id')" class="text-red-500 errorText"> 
            <small>{{ error.subCat_id[0] }}</small>
          </div>
        </div>
        <div>
          <label for="productBrand" class="text-lg font-semibold">Marca del Producto:</label>
          <input v-model="newProduct.brand" id="productBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" :class="{'errorInput': error && error.hasOwnProperty('brand')}">
          <div v-if="error && error.hasOwnProperty('brand')" class="text-red-500 errorText"> 
            <small>{{ error.brand[0] }}</small>
          </div>
        </div>
        
        <div>
          <label for="productQuantity" class="text-lg font-semibold">Cantidad del Producto:</label>
          <input v-model="newProduct.quantity" id="productQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" min="1" :class="{'errorInput': error && error.hasOwnProperty('quantity')}">
          <div v-if="error && error.hasOwnProperty('quantity')" class="text-red-500 errorText"> 
              <small>{{ error.quantity[0] }}</small>
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
          <label for="productDetails" class="text-lg font-semibold">Detalles Adicionales:</label>
          <textarea v-model="newProduct.aditional_details" id="productDetails" :class="{'errorInput': error && error.hasOwnProperty('aditional_details')}" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4" ></textarea>
          <div v-if="error && error.hasOwnProperty('aditional_details')" class="text-red-500 errorText"> 
            <small>{{ error.aditional_details[0] }}</small>
          </div>
        </div>
      </form>
      <button @click="CreateProduct" style="margin:auto; margin-top: 20px;" class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 self-end">
            Agregar Producto
          </button>
    </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      isMethod: "f",
      newProduct: {
        name:"martinis",
        price:99.8
      },
      error: {}, 
      btcPrice: 0,
      categories:null
    };
  },

  created() {
    this.fetchCategoriesForCreate();
  },

  methods: {
    selectProductType() {
      console.log(typeof(this.isMethod))
    },

    async fetchCategoriesForCreate() {
      await axios.get("http://127.0.0.1:8000/api/categorias?formC=true", {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => { this.categories = response.data[0].subCategories; console.log(response.data,  this.categories)})
      .catch(error => {console.log(error)})
    },
    

    async CreateProduct() {
      const formData= new FormData();
      const ObjCopy = Object.assign({}, this.newProduct)
      console.log(ObjCopy)
      if (ObjCopy.image_product == null)  {
        delete ObjCopy.image_product
      }
      if (ObjCopy.subCat_id == 0)  {
        delete ObjCopy.subCat_id
      }
      if(ObjCopy.image) {
        delete ObjCopy.image
      }
      
      console.log(ObjCopy)

      let properties = Object.keys(ObjCopy)
      for (let i = 0; i < properties.length; i++) {
        let clave = properties[i]
        let Obj = ObjCopy[clave]
        formData.append(clave, Obj)
      }

      let url = ""
      if(this.isMethod) {
        url = 'http://127.0.0.1:8000/api/productos/methods'        
      }else {
         url = 'http://127.0.0.1:8000/api/productos'

      }
      
      await axios.post(url,formData,{
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response=> {console.log(response)})
      .catch(error => {
        this.error = error.response.data; 
        console.log(this.error)})
    },

    handleImageUpload(event) {
      const file = event.target.files[0];

      this.newProduct.image_product = file;
      console.log(this.image_product)
      const reader = new FileReader();
      reader.onload = () => {
        this.newProduct.image = reader.result;
      };
      reader.readAsDataURL(file);
    },
  },
};
</script>

<style>

.typProd {
  justify-content: center;
  gap: 12px;
  font-size: 19px;
}

.typProd label {
  font-size: 19px;
}


.container {
  display: flex;
  justify-content: row;
  align-items: center;
  height: 100vh;
}

@media (max-width: 768px) {
  .form-add {
    display: block;
  }
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
