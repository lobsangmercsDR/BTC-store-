<template>
  <div class="container mx-auto p-4">
    <div class="mb-4 flex flex-col md:flex-row md:items-center">
      <input
        type="text"
        v-model="searchTerm"
        placeholder="Buscar productos"
        class="p-2 border border-gray-300 rounded-md mb-2 md:mb-0 md:mr-2 w-full md:w-auto"
      />
      <select v-model="selectedCategory" @change="updateSubcategories" class="p-2 border border-gray-300 rounded-md mb-2 md:mb-0 md:mr-2 w-full md:w-auto">
        <option value="">Todas las categorías</option>
        <option v-for="category in categories" :value="category">{{ category.nameCategory }}</option>
      </select>
      <select v-model="selectedSubcategory" class="p-2 border border-gray-300 rounded-md mb-2 md:mb-0 md:mr-2 w-full md:w-auto">
        <option value="">Todas las subcategorías</option>
        <option v-for="subcategory in filteredSubcategories" :value="subcategory">{{ subcategories.selectedCategory }}</option>
      </select>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full bg-white shadow-md rounded-md">
        <thead>
          <tr>
            <th class="py-2 px-4 bg-gray-100">ID</th>
            <th class="py-2 px-4 bg-gray-100">Nombre</th>
            <th class="py-2 px-4 bg-gray-100">Categoría</th>
            <th class="py-2 px-4 bg-gray-100">Subcategoría</th>
            <th class="py-2 px-4 bg-gray-100">Precio</th>
            <th class="py-2 px-4 bg-gray-100">Cantidad</th>
            <th class="py-2 px-4 bg-gray-100">Creado por</th>
            <th class="py-2 px-4 bg-gray-100">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in filteredProducts" :key="product.id">
            <td class="py-2 px-4">{{ product.id }}</td>
            <td class="py-2 px-4">{{ product.name }}</td>
            <td class="py-2 px-4">{{ product.category }}</td>
            <td class="py-2 px-4">{{ product.subcategory }}</td>
            <td class="py-2 px-4">{{ product.price }}</td>
            <td class="py-2 px-4">{{ product.quantity }}</td>
            <td class="py-2 px-4">{{ product.createdBy }}</td>
            <td class="py-2 px-4">
              <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Editar</button>
              <button class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      searchTerm: '',
      selectedCategory: '',
      selectedSubcategory: '',
      categories: [],
      subcategories: {},
      products: [],
    };
  },
  created() {
    this.getCategories();
    this.getProducts();
  },
  methods: {
    async getCategories() {
      try {
        const token = Cookies.get('token'); // Obtener la cookie de autenticación
        const response = await axios.get('http://127.0.0.1:8000/api/categorias', {
          headers: {
            Authorization: `Token ${token}`, // Incluir la cookie en el encabezado Authorization
          },
        });
        this.categories = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getProducts() {
      try {
        const token = Cookies.get('token'); // Obtener la cookie de autenticación
        const response = await axios.get('http://127.0.0.1:8000/api/productos', {
          headers: {
            Authorization: `Token ${token}`, // Incluir la cookie en el encabezado Authorization
          },
        });
        this.products = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    updateSubcategories() {
      this.selectedSubcategory = '';
    },
  },
  computed: {
    filteredProducts() {
      return this.products.filter((product) => {
        const categoryMatch = this.selectedCategory ? product.category === this.selectedCategory : true;
        const subcategoryMatch = this.selectedSubcategory ? product.subcategory === this.selectedSubcategory : true;
        const searchTermMatch = product.name.toLowerCase().includes(this.searchTerm.toLowerCase());

        return categoryMatch && subcategoryMatch && searchTermMatch;
      });
    },
    filteredSubcategories() {
      return this.subcategories[this.selectedCategory] || [];
    },
  },
};
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  text-align: left;
  padding: 0.5rem;
}

th {
  background-color: #f7fafc;
}

tr:nth-child(even) {
  background-color: #f3f4f6;
}

input,
select {
  font-size: 14px;
}

input[type="text"] {
  min-width: 200px;
}

@media (min-width: 768px) {
  input[type="text"] {
    min-width: auto;
  }
}

button {
  cursor: pointer;
}

.bg-blue-500 {
  background-color: #3f83f8;
}

.bg-blue-500:hover {
  background-color: #1d4ed8;
}

.bg-red-500 {
  background-color: #ef4444;
}

.bg-red-500:hover {
  background-color: #dc2626;
}

.text-white {
  color: #fff;
}

.font-bold {
  font-weight: bold;
}

.rounded {
  border-radius: 0.375rem;
}
</style>
