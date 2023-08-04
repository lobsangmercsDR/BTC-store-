<template>
  <div>
    <h2 class="text-3xl font-semibold mb-4">Inventario</h2>

    <!-- Filtros -->
    <div class="flex items-center mb-4">
      <div>
        <label for="categoryFilter" class="text-lg font-semibold">Categoría:</label>
        <select v-model="selectedCategory" id="categoryFilter" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
          <option value="">Todas las Categorías</option>
          <option v-for="category in categories" :key="category.id" :value="category.nameCategory">{{ category.nameCategory }}</option>
        </select>
      </div>
      <div class="ml-4">
        <label for="subcategoryFilter" class="text-lg font-semibold">Subcategoría:</label>
        <select v-model="selectedSubcategory" id="subcategoryFilter" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
          <option value="">Todas las Subcategorías</option>
          <option v-for="subcategory in getSubcategories(selectedCategory)" :key="subcategory.id" :value="subcategory.nameCategory">{{ subcategory.nameSubCategory }}</option>
        </select>
      </div>
      <div class="ml-auto">
        <label for="searchInput" class="text-lg font-semibold">Buscar:</label>
        <input v-model="searchTerm" id="searchInput" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
      </div>
    </div>

    <!-- Tabla de productos -->
    <table class="table-auto w-full">
      <thead>
        <tr>
          <th class="px-4 py-2">ID</th>
          <th class="px-4 py-2">Producto</th>
          <th class="px-4 py-2">Categoria</th>
          <th class="px-4 py-2">Subcategoria</th>
          <th class="px-4 py-2">Cantidad</th>
          <th class="px-4 py-2">Precio</th>
          <th class="px-4 py-2">Tienda</th>
          <th class="px-4 py-2">Usuario</th>
          <th class="px-4 py-2">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in filteredProducts" :key="product.id">
          <td class="border px-4 py-2">{{ product.id }}</td>
          <td class="border px-4 py-2">{{ product.name }}</td>
          <td class="border px-4 py-2">{{ product.subCategory.category }}</td>
          <td class="border px-4 py-2">{{ product.subCategory.nameSub }}</td>     
          <td class="border px-4 py-2">{{ product.quantity }}</td>
          <td class="border px-4 py-2">{{ product.price }}</td>
          <td class="border px-4 py-2">{{ product.store.nameStore }}</td>
          <td class="border px-4 py-2">{{ product.store.seller.name }}</td>
          <td class="border px-4 py-2 ">
            <button @click="openEditModal(product)" class="mx-1 bg-blue-500 hover:bg-blue-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
              Ver
            </button>
            <button @click="deleteProduct(product.id)" class="mx-1 bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500">
              Retirar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal de Edición de Producto -->
    <div v-if="isEditModalOpen" class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-gray-800 bg-opacity-75">
      <div class="bg-white rounded-lg shadow-md p-8" style="max-width: 800px; width: 90%">
        <h2 class="text-3xl font-semibold mb-4">Editar Producto</h2>
        <form @submit.prevent="updateExistingProduct">
          <div class="grid grid-cols-3 gap-4">
            <div v-if="editedProduct.subCategory.category === 'Fisicos'">
              <label for="editProductName" class="text-lg font-semibold">Imagen:</label>
              <div class="product-image">
                <img :src="'http://127.0.0.1:8000/api'+editedProduct.image_product"  alt="Product Image">
              <input @change="handleImageUpload" id="src-file" type="file" accept="image/*" class=" file-select">
              </div>
              
            </div>
            <div>
              <label for="editProductName" class="text-lg font-semibold">Nombre del Producto:</label>
              <input v-model="editedProduct.nameProduct" id="editProductName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
            </div>
            <div>
              <label for="editProductQuantity" class="text-lg font-semibold">Cantidad del Producto:</label>
              <input v-model="editedProduct.quantity" id="editProductQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" min="1">
            </div>
            <div>
              <label for="editProductDescription" class="text-lg font-semibold">Descripción del Producto:</label>
              <textarea v-model="editedProduct.description" id="editProductDescription" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4"></textarea>
            </div>
            <div>
              <label for="editProductPriceUSD" class="text-lg font-semibold">Precio del Producto</label>
              <input v-model="editedProduct.priceProduct" id="editProductPriceUSD" type="number" step="0.01" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required>
            </div>
            <div>
              <label for="editProductBrand" class="text-lg font-semibold">Marca del Producto:</label>
              <input v-model="editedProduct.brand" id="editProductBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
            </div>
            <div>
              <label for="editProductVariants" class="text-lg font-semibold">Variantes del Producto:</label>
              <textarea v-model="editedProduct.variants" id="editProductVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2"></textarea>
            </div>
            <div>
              <label for="editProductDetails" class="text-lg font-semibold">Detalles Adicionales:</label>
              <textarea v-model="editedProduct.aditional_details" id="editProductDetails" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4"></textarea>
            </div>
          </div>
          <div class="flex justify-end mt-4">
            <button @click="closeEditModal" class="bg-gray-500 hover:bg-gray-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500">
              Cancelar
            </button>
            <button @click="updateExistingProduct" class="ml-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
              Guardar Cambios
            </button>
            <button @click="saveAsNewProduct" class="ml-2 bg-green-500 hover:bg-green-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500">
              Guardar como Nuevo Producto
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';
import { filter } from 'lodash';

export default {
  data() {
    return {
      products: [],
      categories: [],
      subcategories: [],
      selectedCategory: '',
      selectedSubcategory: '',
      searchTerm: '',
      isEditModalOpen: false,
      editedProduct: {
        id: null,
        nameProduct: '',
        description: '',
        price: 0,
        image: null,
        brand: '',
        variants: '',
        category: '',
        subCategory: '',
        quantity: 0,
        aditional_details: '',
        username: ''
      },
      selectedProduct: null
    };
  },

  created() {
    this.fetchProducts();
    this.fetchCategories();
  },

  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/inventory`, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        });
        console.log(response.data)
        this.products = response.data;
      } catch (error) {
        console.error('Error al obtener los productos:', error);
      }
    },

    async fetchCategories() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/categorias', {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        });
        this.categories = response.data;
      } catch (error) {
        console.error('Error al obtener las categorías:', error);
      }
    },

    openEditModal(product) {
      this.editedProduct = product
      this.isEditModalOpen = true;
      this.selectedProduct = product.subCategory
    },

    closeEditModal() {
      this.isEditModalOpen = false;
      this.editedProduct = null
    },

    updateExistingProduct() {
      const updatedProduct = product

      // Lógica para enviar los cambios del producto existente al servidor
      axios.put(`http://127.0.0.1:8000/api/productos/${this.editedProduct.id}`, updatedProduct, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        this.fetchProducts();
      })
      .catch(error => {
        console.error('Error al actualizar el producto:', error);
      })
      .finally(() => {
        this.closeEditModal();
      });
    },

    saveAsNewProduct() {
      console.log(this.selectedProduct)
      const newProduct = this.selectedProduct

  // Lógica para guardar los cambios como un nuevo producto
axios.post('http://127.0.0.1:8000/api/productos', newProduct, {
      headers: {
        Authorization: `Token ${Cookies.get('token')}`
      }
    })
    .then(response => {
      // Agregar el nuevo producto a la lista
      this.fetchProducts();

      // Restaurar los campos de edición a sus valores predeterminados
      this.editedProduct = {
        id: null,
        nameProduct: '',
        description: '',
        priceBTC: 0,
        priceUSD: 0,
        image: null,
        brand: '',
        variants: '',
        category: '',
        subcategory: '',
        quantity: 0,
        aditional_details: '',
        username: ''
      };
    })
    .catch(error => {
      console.error( error.response.data);
    })
    .finally(() => {
      this.closeEditModal();
    });
},


    getSubcategories(category) {
      if (category !== '') {
        const selectedCategory = this.categories.find((c) => c.nameCategory === category);
        return selectedCategory.subCategories;
      }
      return [];
    },

    async deleteProduct(id) {
      console.log(id)
      if(!confirm("¿Está seguro de que quiere retirar este producto del sistema?")) {
        return null
      }
      const idSplited = id.split('.')
      const tipo = idSplited[0]
      const idOrg = idSplited[1] 
      let url = ""
      console.log(tipo)
      if(tipo == 1) {
       url = `http://127.0.0.1:8000/api/productos/${idOrg}`
      }
      else if(tipo ==2) {
        console.log(idOrg)
        url = `http://127.0.0.1:8000/api/productos/digit/${idOrg}`
      }
        await axios.delete(url,
        {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        } 
        )
        .then(
          response => {
            console.log(response)
            this.fetchProducts()
          }
        )
        .catch(error => {
          console.log(error)
        })
    }
  },

  computed: {
    filteredProducts() {
      let filtered = this.products;
      // Filtrar por categoría
      if (this.selectedCategory !== '') {

        filtered = filtered.filter((product) => product.subCategory.category === this.selectedCategory);
        console.log(filtered)
      }

      // Filtrar por subcategoría
      if (this.selectedSubcategory !== '') {
        filtered = filtered.filter((product) => product.subCategory.nameSubCategory === this.selectedSubcategory);
      }

      // Filtrar por término de búsqueda
      if (this.searchTerm !== '') {
        const searchTermLower = this.searchTerm.toLowerCase();
        filtered = filtered.filter((product) => {
          const nameLower = product.nameProduct.toLowerCase();
          const descriptionLower = product.description.toLowerCase();
          return nameLower.includes(searchTermLower) || descriptionLower.includes(searchTermLower);
        });
      }

      return filtered;
    }
  }
};
</script>

<style>
.product-image img {
    width: 100%;
    height: 125px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
}

.file-select {
  position: relative;
  display: inline-block;
}

.file-select::before {
  background-color: #2ac100;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 12px;
  content: 'Seleccionar'; /* testo por defecto */
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.file-select input[type="file"] {
  opacity: 0;
  width: 200px;
  height: 32px;
  display: inline-block;
}

#src-file::before {
  content: 'Cambiar';
}

</style>

