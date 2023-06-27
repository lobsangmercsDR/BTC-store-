<template>
    <div class="category-cards">
      <div
        v-for="category in categories"
        :key="category.id"
        class="category-card"
      >
        <h2 @click="toggleSubcategories(category)" class="category-name">
          {{ category.nameCategory }}
          <span :class="{'arrow-down': category.showSubcategories, 'arrow-right': !category.showSubcategories}"></span>
        </h2>
        <div v-if="category.showSubcategories" class="subcategory-cards">
          <div
            v-for="subcategory in category.subCategories"
            :key="subcategory.id"
            class="subcategory-card"
          >
            <h3 class="subcategory-name">{{ subcategory.nameSubCategory }}</h3>
            <div class="price-range">
              Precio mínimo de producto: {{ subcategory.minPriceBTC }} 
              <br>
              Precio máximo de producto: {{ subcategory.maxPriceBTC }} 
            </div>
            <button v-if="!subcategory.purchased" @click="openPurchaseModal(subcategory)" class="buy-button">
              Comprar
            </button>
            <button v-else class="purchased-button">
              Comprado
            </button>
          </div>
        </div>
      </div>
  
      <div v-if="showPurchaseModal" class="modal">
        <div class="modal-content">
          <h2 class="modal-title">Confirmar compra</h2>
          <div class="modal-info">
            <p><strong>Subcategoría:</strong> {{ selectedSubcategory.nameSubCategory }}</p>
            <p><strong>Precio:</strong> {{ selectedSubcategory.minPriceBTC }} BTC</p>
            <p><strong>Usuario:</strong> {{ username }}</p>
            <p><strong>Saldo disponible:</strong> {{ balance }}</p>
          </div>
          <div class="modal-actions">
            <button @click="processPurchase(selectedSubcategory.id)" class="buy-button">
              Comprar
            </button>
            <button @click="closePurchaseModal" class="cancel-button">
              Cancelar
            </button>
          </div>
        </div>
      </div>
  
      <div v-if="showProcessingModal" class="modal">
        <div class="modal-content">
          <h2 class="modal-title">Procesando transacción...</h2>
          <div class="loader"></div>
        </div>
      </div>
  
      <div v-if="showSuccessModal" class="modal">
        <div class="modal-content">
          <h2 class="modal-title">¡Transacción exitosa!</h2>
          <p>La subcategoría ha sido comprada con éxito.</p>
          <button @click="closeSuccessModal" class="buy-button">
            Cerrar
          </button>
        </div>
      </div>
  
      <div v-if="showFailedModal" class="modal">
        <div class="modal-content">
          <h2 class="modal-title">¡Transacción fallida!</h2>
          <p>No tienes suficientes fondos para realizar la compra.</p>
          <button @click="closeFailedModal" class="cancel-button">
            Cerrar
          </button>
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
        showModal: false,
        selectedSubcategory: null,
        username: 'John Doe', // Ejemplo de nombre de usuario (puedes reemplazarlo con los datos reales)
        balance: 0, // Ejemplo de saldo disponible (puedes reemplazarlo con los datos reales)
        showPurchaseModal: false,
        showProcessingModal: false,
        showSuccessModal: false,
        showFailedModal: false,
      };
    },
  
    created() {
      this.getCategories();
      this.getUserInfo();
    },
  
    methods: {
      async getCategories() {
        await axios
          .get('http://127.0.0.1:8000/api/categorias', {
            headers: {
              Authorization: `Token ${Cookies.get('token')}`,
            },
          })
          .then((response) => {
            this.categories = response.data.map((category) => ({
              ...category,
              subCategories: category.subCategories.map((subcategory) => ({
                ...subcategory,
              })),
            }));
          })
          .catch((error) => {
            console.log(error);
          });
      },

      async getUserInfo() {
        await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`,
        {
          headers:{
            Authorization:`Token ${Cookies.get('token')}`
          }
        })
        .then(response => {
          console.log(response.data)
          this.username = response.data.name
          this.balance = response.data.userBalance
        })
        .catch(error => {
          console.log(error.response.data)
        })
      },

      async processTransact(subCaId) {
        await axios.post(`http://127.0.0.1:8000/api/transactscategories`,{subcategory_id:subCaId},
        {
          headers: {
            Authorization:`Token ${Cookies.get('token')}`
          }
        })
        .then(response => {
            this.getCategories()
        })
        .catch(error=> {
          console.log(error.response.data)
        })
      },


      openPurchaseModal(subcategory) {
        this.selectedSubcategory = subcategory;
        this.showPurchaseModal = true;
      },
      processPurchase(subCaId) {
        this.showPurchaseModal = false;
        this.showProcessingModal = true;
  
        // Simulación de procesamiento de la transacción
        setTimeout(() => {
          console.log(parseInt(this.selectedSubcategory.minPriceBTC))
          if (this.balance >= parseInt(this.selectedSubcategory.minPriceBTC)) {
            // Transacción exitosa
            this.selectedSubcategory.purchased = true;
            this.showProcessingModal = false;
            this.showSuccessModal = true;
            this.processTransact(subCaId)
          } else {
            // Transacción fallida por falta de fondos
            this.showProcessingModal = false;
            this.showFailedModal = true;
          }
        }, 2000);
      },
      closePurchaseModal() {
        this.showPurchaseModal = false;
      },
      closeSuccessModal() {
        this.showSuccessModal = false;
      },
      closeFailedModal() {
        this.showFailedModal = false;
      },
      toggleSubcategories(category) {
        category.showSubcategories = !category.showSubcategories;
      },
    },
  };
  </script>
  
  <style scoped>
  .category-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
  }
  
  .category-card {
    background-color: #f2f2f2;
    padding: 20px;
    border-radius: 8px;
    cursor: pointer;
  }
  
  .category-name {
    margin: 0;
    font-size: 18px;
    display: flex;
    align-items: center;
  }
  
  .arrow-down,
  .arrow-right {
    width: 12px;
    height: 12px;
    margin-left: 5px;
    transition: transform 0.3s ease-in-out;
  }
  
  .arrow-down::before,
  .arrow-right::before {
    content: '';
    display: block;
    width: 100%;
    height: 100%;
    border: solid #000;
    border-width: 0 2px 2px 0;
    transform-origin: center;
    transition: transform 0.3s ease-in-out;
  }
  
  .arrow-down {
    transform: rotate(90deg);
  }
  
  .arrow-down::before {
    transform: translate(-2px, -2px) rotate(45deg);
  }
  
  .arrow-right {
    transform: rotate(0);
  }
  
  .arrow-right::before {
    transform: translate(1px, 1px) rotate(-45deg);
  }
  
  .subcategory-cards {
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 10px;
    margin-top: 10px;
  }
  
  .subcategory-card {
    background-color: #fff;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .subcategory-name {
    margin: 0;
    font-size: 16px;
  }
  
  .price-range {
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .buy-button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 6px 12px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .purchased-button {
    background-color: #28a745;
    color: #fff;
    border: none;
    padding: 6px 12px;
    border-radius: 4px;
    cursor: default;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    max-width: 400px;
  }
  
  .modal-title {
    margin-top: 0;
    margin-bottom: 20px;
  }
  
  .modal-info {
    margin-bottom: 20px;
  }
  
  .modal-actions {
    display: flex;
    justify-content: space-between;
  }
  
  .cancel-button {
    background-color: #ccc;
    color: #fff;
    border: none;
    padding: 6px 12px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .loader {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #007bff;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 1s linear infinite;
    margin: 0 auto;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  </style>
  