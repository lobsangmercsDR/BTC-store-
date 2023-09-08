<template>
  <div>
    <h2 class="text-3xl font-semibold mb-4">Inventario</h2>

    <!-- Filtros -->
    <input type="checkbox" name="own" id="own" style="width: 20px; height: 20px;"  @change="this.own = !this.own;this.makeOwnProductsRequest()">
    <label for="own" style="font-size: 20px; margin: 0 10px;">Propios</label>   
    <div class="flex items-center mb-2 filters">
      <div class="filter">
        <label for="categoryFilter " class="text-lg font-semibold">Categoría:</label>
        <select v-model="selectedCategory" id="categoryFilter" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
          <option value="">Todas las Categorías</option>
          <option v-for="category in categories" :key="category.id" :value="category.nameCategory">{{ category.nameCategory }}</option>
        </select>
      </div>
      <div class="ml-4 filter">
        <label for="subcategoryFilter" class="text-lg font-semibold">Subcategoría:</label>
        <select v-model="selectedSubcategory" id="subcategoryFilter" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
          <option value="">Todas las Subcategorías</option>
          <option v-for="subcategory in getSubcategories(selectedCategory)" :key="subcategory.id" :value="subcategory.id">{{ subcategory.nameSubCategory }}</option>
        </select>
      </div>
      <div class="ml-4 filter">
        <label for="searchInput" class="text-lg font-semibold"> Buscar:</label>
        <input v-model="searchTerm" id="searchInput" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
      </div>
    </div>
    <button class="mt-0 mb-4 bg-orange-500 hover:bg-orange-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-orange-500" @click="filteredProducts()"> Buscar</button>

    <!-- Tabla de productos -->
    <div style="min-height: 370px">
      <table class="table-auto w-full" style="margin: auto;" v-if="!isWindowSmall">
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
          <tr v-for="product in products" :key="product.id">
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
                Editar
              </button>
              <button @click="deleteProduct(product.id)" class="mx-1 bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500">
                Retirar
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <table :key="product.id" v-if="isWindowSmall" v-for="product in products" class=" tableWit responsive-table">
        <tbody>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">ID</td>
            <td class="py-2 px-4 border-b">{{ product.id }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Producto</td>
            <td class="py-2 px-4 border-b">{{ product.name }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Categoria</td>
            <td class="py-2 px-4 border-b">{{ product.subCategory.category }}</td>
          </tr>
          
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Subcategoria</td>
            <td class="py-2 px-4 border-b">{{ product.subCategory.nameSub }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Cantidad</td>
            <td class="py-2 px-4 border-b">{{ product.quantity }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Precio</td>
            <td class="py-2 px-4 border-b">{{ product.price }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Usuario</td>
            <td class="py-2 px-4 border-b">{{ product.store.nameStore }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Acciones</td>
            <td class="py-2 px-4 border-b">{{ product.store.seller.name }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Acciones</td>
            <td class="border px-4 py-2 ">
              <button @click="openEditModal(product)" class="mx-1 bg-blue-500 hover:bg-blue-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
                Editar
              </button>
              <button @click="deleteProduct(product.id)" class="mx-1 bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500">
                Retirar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <section class="nav-arrows cont">
        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(-1)"  class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M15 18l-6-6 6-6"/>
        </svg> 
        <div  class="pageCounter"> <span>{{ pageInfo.act_page }}</span></div>
        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(1)" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 18l6-6-6-6"/>
        </svg>
    </section>


    <!-- Modal de Edición de Producto -->
    <div v-if="isEditModalOpen" class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-gray-800 bg-opacity-75 ">
      <div class="bg-white rounded-lg shadow-md p-8 modalForm" style="max-width: 800px; width: 90%; max-height: 775px; overflow: auto;">
        <h2 class="text-3xl font-semibold mb-4">Editar Producto</h2>
        <form >
          <div class="grid formGrid">
            <div v-if="editedProduct.subCategory.category === 'Fisicos'">
              <label for="editProductName" class="text-lg font-semibold">Imagen:</label>
              <div class="product-image">
                <img :src="getImageURL()"  alt="Product Image">
              <input @change="handleImageUpload" id="src-file" type="file" accept="image/*" class=" file-select">
              </div>
              
            </div>
            <div>
              <label for="editProductName" class="text-lg font-semibold">Nombre del Producto:</label>
              <input v-model="editedProduct.name" id="editProductName" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
            </div>
            <div v-if="editedProduct.subCategory.category === 'Fisicos'">
              <label for="editProductQuantity" class="text-lg font-semibold">Cantidad del Producto:</label>
              <input v-model="editedProduct.quantity" id="editProductQuantity" type="number" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" min="1">
            </div>
            <div>
              <label for="editProductDescription" class="text-lg font-semibold">Descripción del Producto:</label>
              <textarea v-model="editedProduct.description" id="editProductDescription" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4"></textarea>
            </div>
            <div>
              <label for="editProductPriceUSD" class="text-lg font-semibold">Precio del Producto</label>
              <input v-model="editedProduct.price" id="editProductPriceUSD" type="number" step="0.01" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg w-20" min="0" required>
            </div>
            <div v-if="editedProduct.subCategory.category === 'Fisicos'">
              <label for="editProductBrand" class="text-lg font-semibold">Marca del Producto:</label>
              <input v-model="editedProduct.brand" id="editProductBrand" type="text" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg">
            </div>
            <div v-if="editedProduct.subCategory.category === 'Fisicos'">
              <label for="editProductVariants" class="text-lg font-semibold">Direccion</label>
              <textarea v-model="editedProduct.address_direction" id="editProductVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2"></textarea>
            </div>
            <div v-if="editedProduct.subCategory.category === 'Digitales'">
              <label for="editProductVariants" class="text-lg font-semibold">Texto de Checker</label>
              <textarea v-model="editedProduct.checkerText" id="editProductVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2"></textarea>
            </div>
            <div>
              <label for="editProductDetails" class="text-lg font-semibold">Detalles Adicionales:</label>
              <textarea v-model="editedProduct.aditional_details" id="editProductDetails" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="4"></textarea>
            </div>
            <div v-if="editedProduct.subCategory.category === 'Digitales'">
              <label for="editProductVariants" class="text-lg font-semibold">Comision de Checker</label>
              <textarea v-model="editedProduct.comisionCheck" id="editProductVariants" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" rows="2"></textarea>
              <div class="flex checkerInp">
                <label for="editProductVariants" class="text-lg font-semibold">Necesita Checker</label>
                <input type="checkbox" v-model="editedProduct.needChecker">
              </div>
              
            </div>
          </div>
          <div class="flex justify-end mt-4">
            <button @click="closeEditModal" class="bg-gray-500 hover:bg-gray-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500">
              Cancelar
            </button>
            <button @click="updateExistingProduct" class="ml-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-2 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500">
              Guardar Cambios
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
      isWindowSmall: false,
      own: false,
      products: [],
      categories: [],
      subcategories: [],
      selectedCategory: '',
      selectedSubcategory: '',
      searchTerm: '',
      isEditModalOpen: false,
      isPaginated: true,
      pageInfo: {
        act_page: 1,
        rest_pages: 0
      },
      editedProduct: {
        id: null,
        name: '',
        description: '',
        price: 0,
        image_product: null,
        image_view: null,
        brand: '',
        variants: '',
        category: '',
        subCategory: '',
        quantity: 0,
        aditional_details: '',
        username: '',
        localImage: false
      },
      selectedProduct: null
    };
  },

  created() {
    this.fetchProducts();
    this.fetchCategories();
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
  },

  methods: {
    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 870;
    },  
    async fetchProducts(id=1, query=[], own=false) {
      let url =""
      console.log("2")
      if(own) {
        url = `http://127.0.0.1:8000/api/inventory?page=${id}&paginated=t&own=t`
      } else {
        url=`http://127.0.0.1:8000/api/inventory?page=${id}&paginated=t`
      }
      try {
        const response = await axios.get(url, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        });
        console.log(response)
        this.products = response.data.items;
        this.pageInfo.act_page = response.data.act_page
        this.pageInfo.rest_pages = response.data.rest_pages
        console.log(this.products)

      } catch (error) {
        console.error('Error al obtener los productos:', error);
      }
    },

    async handleChangePage(steps) {
      if((this.pageInfo.act_page+steps != 0 && this.pageInfo.act_page+steps <= this.pageInfo.rest_pages + this.pageInfo.act_page)) {
          this.fetchProducts(this.pageInfo.act_page+steps)
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
      const updatedProduct =  this.editedProduct

      const formData= new FormData();

      if (this.editedProduct.localImage) {
        formData.append('image_product',this.editedProduct.image_product)
        const image = this.editedProduct.image_product
        axios.put(`http://127.0.0.1:8000/api/images/${image}`, formData)
        .then(response => {
          console.log(response)
        })
      }

      let requestData = {...updatedProduct}
      let deleteList= ['image_product', 'dateCreated', 'subCategory', 'seller','store']
      for(let i = 0; i <= deleteList.length-1; i++ ) {
        delete requestData[deleteList[i]]
      }
      const tipo = this.editedProduct.id.split(".")[0]
      let url = ""
      if (tipo== 1) {
        url = `http://127.0.0.1:8000/api/productos/${this.editedProduct.id.split('.')[1]}` 
      }
      else if(tipo==2) {
        url = `http://127.0.0.1:8000/api/productos/digit/${this.editedProduct.id.split('.')[1]}`
      }
      
      
      // Lógica para enviar los cambios del producto existente al servidor
      axios.put(url, requestData, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        console.log(response)
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
      this.fetchProducts();
    })
    .catch(error => {
      console.error( error.response.data);
    })
    .finally(() => {
      this.closeEditModal();
    });
},


    handleImageUpload(event) {
      const file = event.target.files[0];
      this.editedProduct.localImage = true
      this.editedProduct.image_product = file;
      console.log(file)
      const reader = new FileReader();
      reader.onload = () => {
        this.editedProduct.image_view = reader.result;
      };
      reader.readAsDataURL(file);
    },

    getImageURL() {

      if(this.editedProduct.localImage) {
          return this.editedProduct.image_view
      }
      else {
        return `http://127.0.0.1:8000/api${this.editedProduct.image_product}`
      }
    },

    getSubcategories(category) {
      if (category !== '') {
        const selectedCategory = this.categories.find((c) => c.nameCategory === category);
        return selectedCategory.subCategories;
      }
      return [];
    },

    async filteredProducts() {
      let query=["","",""]
      let filtered = this.products;
      if (this.selectedCategory !== '') {
        query[0] = this.selectedCategory
      }

      if (this.selectedSubcategory !== '') {
        query[1] = this.selectedSubcategory
      }

      if (this.searchTerm !== '') {
        query[2] = this.searchTerm.toLowerCase()
        
        // const searchTermLower = this.searchTerm.toLowerCase();
        // filtered = filtered.filter((product) => {
        //   const nameLower = product.name.toLowerCase();
        //   const descriptionLower = product.description.toLowerCase();
        //   return nameLower.includes(searchTermLower) || descriptionLower.includes(searchTermLower);
        // });
      }
      let url = 'http://127.0.0.1:8000/api/seeker?query='+this.searchTerm
      if(this.selectedCategory) {
      url=  url +"&tip="+this.selectedCategory 
      }
      if(this.selectedSubcategory) {
      url=  url +"&subC="+this.selectedSubcategory 
      }

      await axios.get(url)
      .then(response=> {
        this.products = response.data
      })
    },
    async makeOwnProductsRequest() {
       await this.fetchProducts(1,[],this.own)
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

.filters  {
  max-width: 1000px;
    margin: 20px auto;
    margin-bottom: 10px;
    flex-direction: column;
}

.filter {
  display: flex;
    flex-direction: column;
}


.tableWit {
  min-width: 400px;
  border: 3px solid;
  margin: 40px auto;
}

.formGrid {
  display: grid;
    grid-template-columns: repeat(auto-fit, minmax(205px, 1fr));
    grid-gap: 49px;
}

.modalForm {
  max-width: 955px !important;
}
@media (min-width:870px) {
  .filters {
    flex-direction: row;
    justify-content: space-between;
  }
  

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


.checkerInp {
  gap: 20px;
  margin: 5px;
}

.checkerInp label {
  margin-bottom: 0px;
}

.cont {
  justify-content: center;
  margin-top: 23px;
}
</style>

