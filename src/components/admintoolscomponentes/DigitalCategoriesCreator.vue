<template>
  <div class="container">
    <h1 class="heading">Editor de Categorías</h1>

    <div v-if="categories.length === 0" class="message">
      No hay categorías disponibles.
    </div>

    <div v-for="category in categories" :key="category.id" class="category">
      <div class="category-header">
        <h2 class="category-name">{{ category.nameCategory }}</h2>
        <button @click="toggleSubcategories(category)" class="toggle-button">
          {{ category.showSubcategories ? '-' : '+' }}
        </button>
      </div>
      <div v-if="category.showSubcategories" class="subcategory-list">
        <div v-if="category.subCategories.length === 0" class="message">
          No hay subcategorías disponibles.
        </div>
        <table class="subcategory-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Precio Mínimo</th>
              <th>Precio Máximo</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="subcategory in category.subCategories" :key="subcategory.id" class="subcategory">
              <td>{{ subcategory.nameSubCategory }}</td>
              <td>{{ subcategory.minPriceBTC }}</td>
              <td>{{ subcategory.maxPriceBTC }}</td>
              <td>
                <button @click="editSubcategory(category, subcategory)" class="edit-button">
                  Editar
                </button>
              </td>
              <td>
                <button @click="deleteSubcategory(category, subcategory)" class="delete-button">
                  Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="category-actions">
        <button @click="showCreateSubcategoryModal(category)" class="add-button">
          Agregar Subcategoría
        </button>
      </div>
    </div>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2 class="modal-title">{{ modalCategoryId ? 'Editar Categoría' : 'Agregar Categoría' }}</h2>
        <div class="modal-form">
          <label for="categoryName" class="modal-label">Nombre:</label>
          <input type="text" id="categoryName" v-model="modalCategoryName" class="modal-input">
        </div>
        <div class="modal-actions">
          <button @click="saveCategory" class="save-button">
            {{ modalCategoryId ? 'Guardar' : 'Agregar' }}
          </button>
          <button @click="cancelModal" class="cancel-button">
            Cancelar
          </button>
        </div>
      </div>
    </div>

    <div v-if="showSubcategoryModal" class="modal">
      <div class="modal-content">
        <h2 class="modal-title">{{ modalSubcategoryId ? 'Editar Subcategoría' : 'Agregar Subcategoría' }}</h2>
        <div class="modal-form">
          <label for="subcategoryName" class="modal-label">Nombre:</label>
          <input type="text" id="subcategoryName" step="0.01" min="0" v-model="modalSubcategoryName" class="modal-input">
          <label for="subcategoryMinPrice" class="modal-label">Precio Mínimo:</label>
          <input type="number" step="0.01" min="0" id="subcategoryMinPrice" v-model="modalSubcategoryMinPrice" class="modal-input">
          <label for="subcategoryMaxPrice" class="modal-label">Precio Máximo:</label>
          <input type="number" id="subcategoryMaxPrice" v-model="modalSubcategoryMaxPrice" class="modal-input">
        </div>
        <div class="modal-actions">
          <button @click="saveSubcategory " class="save-button">
            {{ modalSubcategoryId ? 'Guardar' : 'Agregar' }}
          </button>
          <button @click="cancelSubcategoryModal" class="cancel-button">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      categories: [],
      category: null,
      showModal: false,
      showSubcategoryModal: false,
      modalCategoryId: -1,
      modalCategoryName: '',
      modalSubcategoryId: null,
      modalSubcategoryName: '',
      modalSubcategoryMinPrice: null,
      modalSubcategoryMaxPrice: null,
    };
  },

  created() {
    this.getCategories()
  },
  methods: {
    async getCategories() {
      await axios.get("http://127.0.0.1:8000/api/categorias", {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
        .then(response => { 
          console.log(response.data)
          let values = response.data
          values.forEach(element => {
            element.showSubcategories = false
          });
          console.log(values)
          this.categories = response.data 
        })
        .catch(error => { console.log(error) })
    },
    async updateCategoriesinAPI() {
      await axios.put(`http://127.0.0.1:8000/api/categorias/${this.modalCategoryId}`, { nameCategory: this.modalCategoryName }, {
            headers: {
              Authorization: `Token ${Cookies.get('token')}`
            }
          })
            .then(response => { this.getCategories() })
            .catch(error => { console.log(error.response) })
    },

    async CreateCategoriesInAPI() {
      await axios.post("http://127.0.0.1:8000/api/categorias", {nameCategory: this.modalCategoryName},{
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
    },


    toggleSubcategories(category) {
      category.showSubcategories = !category.showSubcategories;
    },
     editCategory(category) {
      this.modalCategoryId = category.id;
      this.modalCategoryName = category.nameCategory;
      this.showModal = true;
    },
    async deleteCategory(category) {
      const index = this.categories.findIndex((c) => c.id === category.id);

      if(confirm("¿Seguro desea eliminar esta categoria?")) {
        await axios.delete(`http://127.0.0.1:8000/api/categorias/${category.id}`, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        })
          .then(response => { console.log(response.data) })
          .catch(error => { console.log(error.response.data); throw new Error(error.response.data) })


        if (index !== -1) {
          this.categories.splice(index, 1);
        }
    }
  },
    editSubcategory(category, subcategory) {
      this.modalCategoryId = category.id;
      this.modalCategoryName = category.nameCategory;
      this.modalSubcategoryId = subcategory.id;
      this.modalSubcategoryName = subcategory.nameSubCategory;
      this.modalSubcategoryMinPrice = subcategory.minPriceBTC;
      this.modalSubcategoryMaxPrice = subcategory.maxPriceBTC;
      this.showSubcategoryModal = true;

      console.log(category, subcategory)
    },
    async deleteSubcategory(category, subcategory) {
      const index = category.subCategories.findIndex((s) => s.id === subcategory.id);
      console.log(index)
      await axios.delete(`http://127.0.0.1:8000/api/categorias/${category.id}/${subcategory.id}`, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {console.log(response.data)})
      .catch(error => {console.log(error.response.data)})
      if (index !== -1) {
        category.subCategories.splice(index, 1);
      }
    },
    showCreateCategoryModal() {
      this.modalCategoryId = null;
      this.modalCategoryName = '';
      this.showModal = true;
    },
    showCreateSubcategoryModal(category) {
      this.modalCategoryId = category.id;
      this.modalCategoryName = category.name;
      this.modalSubcategoryId = null;
      this.modalSubcategoryName = '';
      this.modalSubcategoryMinPrice = null;
      this.modalSubcategoryMaxPrice = null;
      this.showSubcategoryModal = true;
    },
    async saveCategory() {
      if (this.modalCategoryName.trim() === '') {
        alert('Ingrese un nombre de categoría válido.');
      }
      console.log(this.modalCategoryId)
      console.log(this.modalCategoryId)
      if (this.modalCategoryId != null) {
        console.log("ss")
        if (confirm("¿Esta seguro que desea cambiar el nombre de esta categoria?")) {
          this.updateCategoriesinAPI()
          this.cancelModal();
        }
      } else{
        const newCategory = {
            nameCategory: this.modalCategoryName,
          }
          console.log(newCategory)
          await axios.post("http://127.0.0.1:8000/api/categorias", newCategory, {
            headers: {
              Authorization: `Token ${Cookies.get('token')}`
            }
          })
            .then(response => { console.log(response.data); this.getCategories()})
            .catch(error => { console.log(error.response.data) })
        }
      },
      cancelModal() {
      this.showModal = false;
      this.modalCategoryId = null;
      this.modalCategoryName = '';
    },
   
    cancelSubcategoryModal() {
      this.showSubcategoryModal = false;
      this.modalCategoryId = null;
      this.modalCategoryName = '';
      this.modalSubcategoryId = null;
      this.modalSubcategoryName = '';
      this.modalSubcategoryMinPrice = null;
      this.modalSubcategoryMaxPrice = null;
    },

     async saveSubcategory() {
      if (
        this.modalSubcategoryName.trim() === '' ||
        this.modalSubcategoryMinPrice === null ||
        this.modalSubcategoryMaxPrice === null
      ) {
        alert('Ingrese todos los campos requeridos.');
        return;
      }
      const category = this.categories.find((c) => c.id === this.modalCategoryId);

      if (category) {
        if (this.modalSubcategoryId !== null) {
          let subcategory = category.subCategories.find((s) => s.id === this.modalSubcategoryId);
          console.log(subcategory)
          let subcategoryObj = {
            nameSubCategory:this.modalSubcategoryName,
            minPriceBTC: this.modalSubcategoryMinPrice,
            maxPriceBTC: this.modalSubcategoryMaxPrice
          }
          console.log(subcategoryObj)
          await axios.put(`http://127.0.0.1:8000/api/categorias/${category.id}/${subcategory.id}`,subcategoryObj,{
            headers: {
              Authorization: `Token ${Cookies.get('token')}`
            }
          })
          .then(response=> {
             let finalSubC = category.subCategories.findIndex((elem) => elem.id == response.data.id)
              category.subCategories[finalSubC] = response.data
            })
          .catch(error=> {error})
        } 
        else {
          const subcategory = {
            nameSubCategory: this.modalSubcategoryName,
            minPriceBTC: this.modalSubcategoryMinPrice,
            maxPriceBTC: this.modalSubcategoryMaxPrice,
          }
          console.log(subcategory)
          await axios.post(`http://127.0.0.1:8000/api/categorias/${category.id}`, subcategory, {
            headers: {
              Authorization: `Token ${Cookies.get('token')}`
            }
          })
          .then(response => {
            this.getCategories();
            categoryObj = this.categories.find((sub) => sub.id === response.data.id);
            this.toggleSubcategories(categoryObj)
            console.log(response.data)
          })
          .catch(error => console.log(error))
        }
        this.cancelSubcategoryModal();
      }
    },
  },


  }

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f7fafc;
  padding: 20px;
}

.heading {
  font-size: 24px;
  font-weight: bold;
  color: #2d3748;
  margin-bottom: 20px;
}

.message {
  font-size: 16px;
  color: #718096;
  margin-bottom: 10px;
}

.category {
  width: 100%;
  border-radius: 4px;
  background-color: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
}

.category-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.category-name {
  font-size: 18px;
  font-weight: bold;
  color: #2d3748;
}

.toggle-button {
  font-size: 18px;
  color: #4299e1;
  background: none;
  border: none;
  cursor: pointer;
}

.subcategory-list {
  margin-top: 10px;
}

.subcategory-table {
  width: 100%;
  border-collapse: collapse;
}

.subcategory-table th,
.subcategory-table td {
  padding: 8px;
}

.subcategory-actions {
  display: flex;
  align-items: center;
}

.edit-button,
.delete-button,
.add-button,
.save-button,
.cancel-button {
  font-size: 14px;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  cursor: pointer;
}

.edit-button {
  background-color: #4299e1;
  margin-right: 5px;
}

.edit-button:hover {
  background-color: #3182ce;
}

.delete-button {
  background-color: #e53e3e;
}

.delete-button:hover {
  background-color: #c53030;
}

.add-button {
  background-color: #48bb78;
}

.add-button:hover {
  background-color: #38a169;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  width: 400px;
  background-color: #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 4px;
}

.modal-title {
  font-size: 18px;
  font-weight: bold;
  color: #2d3748;
  margin-bottom: 10px;
}

.modal-form {
  margin-bottom: 10px;
}

.modal-label {
  font-size: 14px;
  font-weight: bold;
  color: #2d3748;
}

.modal-input {
  width: 100%;
  font-size: 14px;
  padding: 8px;
  border: 1px solid #a0aec0;
  border-radius: 4px;
}

.modal-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.save-button,
.cancel-button {
  font-size: 14px;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  cursor: pointer;
}

.save-button {
  background-color: #48bb78;
  margin-left: 10px;
}

.save-button:hover {
  background-color: #38a169;
}

.cancel-button {
  background-color: #718096;
  margin-left: 10px;
}

.cancel-button:hover {
  background-color: #4a5568;
}
</style>
