<template>
  <div class="container">
    <h1 class="heading">Editor de Categorías</h1>

    <div v-if="categories.length === 0" class="message">
      No hay categorías disponibles.
    </div>

    <div v-for="category in categories" :key="category.id" class="category">
      <div class="category-header">
        <h2 class="category-name">{{ category.name }}</h2>
        <button @click="toggleSubcategories(category)" class="toggle-button">
          {{ category.showSubcategories ? '-' : '+' }}
        </button>
      </div>
      <div v-if="category.showSubcategories" class="subcategory-list">
        <div v-if="category.subcategories.length === 0" class="message">
          No hay subcategorías disponibles.
        </div>
        <ul>
          <li v-for="subcategory in category.subcategories" :key="subcategory.id" class="subcategory">
            <div class="subcategory-header">
              <span>{{ subcategory.name }}</span>
              <div class="subcategory-actions">
                <button @click="editSubcategory(category, subcategory)" class="edit-button">
                  Editar
                </button>
                <button @click="deleteSubcategory(category, subcategory)" class="delete-button">
                  Eliminar
                </button>
              </div>
            </div>
            <div class="subcategory-list">
              <div v-if="subcategory.subcategories.length === 0" class="message">
                No hay subcategorías disponibles.
              </div>
              <ul>
                <li v-for="subsubcategory in subcategory.subcategories" :key="subsubcategory.id" class="subcategory">
                  <div class="subcategory-header">
                    <span>{{ subsubcategory.name }}</span>
                    <div class="subcategory-actions">
                      <button @click="editSubcategory(subsubcategory)" class="edit-button">
                        Editar
                      </button>
                      <button @click="deleteSubcategory(subcategory, subsubcategory)" class="delete-button">
                        Eliminar
                      </button>
                    </div>
                  </div>
                </li>
              </ul>
              <div class="add-subcategory">
                <button @click="showCreateSubcategoryModal(subcategory)" class="add-button">
                  Agregar Subcategoría
                </button>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="category-actions">
        <button @click="editCategory(category)" class="edit-button">
          Editar
        </button>
        <button @click="deleteCategory(category)" class="delete-button">
          Eliminar
        </button>
        <button @click="showCreateSubcategoryModal(category)" class="add-button">
          Agregar Subcategoría
        </button>
      </div>
    </div>

    <button @click="showCreateCategoryModal" class="add-button">
      Agregar Categoría
    </button>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2 class="modal-title">Crear/Edita Categoría</h2>
        <div class="modal-form">
          <label for="categoryName" class="modal-label">Nombre:</label>
          <input type="text" id="categoryName" v-model="modalCategoryName" class="modal-input">
        </div>
        <div class="modal-actions">
          <button @click="saveCategory" class="save-button">
            Guardar
          </button>
          <button @click="cancelModal" class="cancel-button">
            Cancelar
          </button>
        </div>
      </div>
    </div>

    <div v-if="showSubcategoryModal" class="modal">
      <div class="modal-content">
        <h2 class="modal-title">Crear Subcategoría</h2>
        <div class="modal-form">
          <label for="subcategoryName" class="modal-label">Nombre:</label>
          <input type="text" id="subcategoryName" v-model="modalSubcategoryName" class="modal-input">
        </div>
        <div class="modal-actions">
          <button @click="saveSubcategory" class="save-button">
            Guardar
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
      categories: [
        {
          id: 1,
          name: 'Electrónica',
          showSubcategories: false,
          categories: null,
          subcategories: [
            {
              id: 1,
              name: 'Televisores',
              subcategories: []
            },
            {
              id: 2,
              name: 'Computadoras',
              showSubcategories: false,
              subcategories: [
                {
                  id: 1,
                  name: 'Laptops',
                  subcategories: []
                },
                {
                  id: 2,
                  name: 'Desktops',
                  subcategories: []
                }
              ]
            },
            {
              id: 3,
              name: 'Teléfonos',
              subcategories: []
            }
          ]
        },
        {
          id: 2,
          name: 'Ropa',
          showSubcategories: false,
          subcategories: [
            {
              id: 1,
              name: 'Camisetas',
              subcategories: []
            },
            {
              id: 2,
              name: 'Pantalones',
              subcategories: []
            },
            {
              id: 3,
              name: 'Zapatos',
              subcategories: []
            }
          ]
        }
      ],
      showModal: false,
      showSubcategoryModal: false,
      modalCategoryId: null,
      modalCategoryName: '',
      modalSubcategoryName: ''
    };
  },

  created(){
    this.getCategories()
  },
  methods: {
    async getCategories() {
      await axios.get("http://127.0.0.1:8000/api/categorias?prod=true", {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {console.log(response.data)})
      .catch(error => {console.log(error.response.data)})
    },


    toggleSubcategories(category) {
      category.showSubcategories = !category.showSubcategories;
    },
    editCategory(category) {
      this.modalCategoryId = category.id;
      this.modalCategoryName = category.name;
      this.showModal = true;
    },
    deleteCategory(category) {
      const index = this.categories.findIndex((c) => c.id === category.id);
      if (index !== -1) {
        this.categories.splice(index, 1);
      }
    },
    editSubcategory(category, subcategory) {
      this.modalCategoryId = category.id;
      this.modalCategoryName = category.name;
      this.modalSubcategoryName = subcategory.name;
      this.showSubcategoryModal = true;
    },
    deleteSubcategory(category, subcategory) {
      const index = category.subcategories.findIndex((s) => s.id === subcategory.id);
      if (index !== -1) {
        category.subcategories.splice(index, 1);
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
      this.modalSubcategoryName = '';
      this.showSubcategoryModal = true;
    },
    saveCategory() {
      if (this.modalCategoryName.trim() === '') {
        alert('Ingrese un nombre de categoría válido.');
        return;
      }
      if (this.modalCategoryId !== null) {
        const category = this.categories.find((c) => c.id === this.modalCategoryId);
        if (category) {
          category.name = this.modalCategoryName;
        }
      } else {
        const newCategory = {
          id: Date.now(),
          name: this.modalCategoryName,
          showSubcategories: false,
          subcategories: []
        };
        this.categories.push(newCategory);
      }
      this.cancelModal();
    },
    cancelModal() {
      this.showModal = false;
      this.modalCategoryId = null;
      this.modalCategoryName = '';
    },
    saveSubcategory() {
      if (this.modalSubcategoryName.trim() === '') {
        alert('Ingrese un nombre de subcategoría válido.');
        return;
      }
      const category = this.categories.find((c) => c.id === this.modalCategoryId);
      if (category) {
        const newSubcategory = {
          id: Date.now(),
          name: this.modalSubcategoryName,
          subcategories: []
        };
        category.subcategories.push(newSubcategory);
      }
      this.cancelSubcategoryModal();
    },
    cancelSubcategoryModal() {
      this.showSubcategoryModal = false;
      this.modalCategoryId = null;
      this.modalCategoryName = '';
      this.modalSubcategoryName = '';
    }
  }
};
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
  margin-left: 20px;
}

.subcategory {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.subcategory-header {
  display: flex;
  align-items: center;
}

.subcategory-actions {
  margin-left: 10px;
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
}

.edit-button:hover {
  background-color: #3182ce;
}

.delete-button {
  background-color: #e53e3e;
  margin-left: 10px;
}

.delete-button:hover {
  background-color: #c53030;
}

.add-button {
  background-color: #48bb78;
  margin-left: 10px;
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
