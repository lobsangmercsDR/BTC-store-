<template>
    <div class="order-review">
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4">Vigentes</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('active')">
            <button class="accordion-button" :class="{ 'active': activeAccordion === 'active' }">
              Vigentes
            </button>
          </h3>
          <div v-show="activeAccordion === 'active'" class="accordion-collapse">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID de Checker</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Estado del Checker</th>
                  <th class="py-2">Valor del BTC del Checker</th>
                  <th class="py-2">Equivalente en Dólares</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in activeOrders" :key="order.checkerId">
                  <td class="py-2">{{ order.checkerId }}</td>
                  <td class="py-2">{{ order.productName }}</td>
                  <td class="py-2">{{ order.productId }}</td>
                  <td class="py-2">{{ order.checkerStatus }}</td>
                  <td class="py-2">{{ order.btcValue }}</td>
                  <td class="py-2">{{ order.dollarEquivalent }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
      
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4">Pendientes de Aprobación</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('pending')">
            <button class="accordion-button" :class="{ 'active': activeAccordion === 'pending' }">
              Pendientes de Aprobación
            </button>
          </h3>
          <div v-show="activeAccordion === 'pending'" class="accordion-collapse">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID de Checker</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Estado del Checker</th>
                  <th class="py-2">Valor del BTC del Checker</th>
                  <th class="py-2">Equivalente en Dólares</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in pendingOrders" :key="order.id">
                  <td class="py-2">{{ order.checkerId }}</td>
                  <td class="py-2">{{ order.productName }}</td>
                  <td class="py-2">{{ order.productId }}</td>
                  <td class="py-2">{{ order.checkerStatus }}</td>
                  <td class="py-2">{{ order.btcValue }}</td>
                  <td class="py-2">{{ order.dollarEquivalent }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
      
      <section class="column">
      <h2 class="text-2xl font-bold mt-8 mb-4">Expiradas</h2>
      <div class="accordion">
        <div class="accordion-item">
          <h3 class="accordion-header" @click="toggleAccordion('expired')">
            <button class="accordion-button" :class="{ 'active': activeAccordion === 'expired' }">
              Expiradas
            </button>
          </h3>
          <div v-show="activeAccordion === 'expired'" class="accordion-collapse">
            <table class="table w-full">
              <thead>
                <tr>
                  <th class="py-2">ID de Checker</th>
                  <th class="py-2">Nombre del producto</th>
                  <th class="py-2">ID del producto</th>
                  <th class="py-2">Estado del Checker</th>
                  <th class="py-2">Valor del BTC del Checker</th>
                  <th class="py-2">Equivalente en Dólares</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in expiredOrders" :key="order.checkerId">
                  <td class="py-2">{{ order.checkerId }}</td>
                  <td class="py-2">{{ order.productName }}</td>
                  <td class="py-2">{{ order.productId }}</td>
                  <td class="py-2">{{ order.checkerStatus }}</td>
                  <td class="py-2">{{ order.btcValue }}</td>
                  <td class="py-2">{{ order.dollarEquivalent }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeOrders: [
          // Órdenes vigentes
          {
            checkerId: 1,
            productName: "Producto 1",
            productId: 123,
            checkerStatus: "Activo",
            btcValue: 0.5,
            dollarEquivalent: 5000
          },
          // ...
        ],
        pendingOrders: [
          // Órdenes pendientes de aprobación
          {
            id: 1,
            checkerId: 2,
            productName: "Producto 2",
            productId: 456,
            checkerStatus: "Pendiente",
            btcValue: 1.2,
            dollarEquivalent: 12000
          },
          // ...
        ],
        expiredOrders: [
          // Órdenes expiradas
          {
            checkerId: 3,
            productName: "Producto 3",
            productId: 789,
            checkerStatus: "Expirado",
            btcValue: 1.8,
            dollarEquivalent: 18000
          },
          // ...
        ],
        activeAccordion: ""
      };
    },
    methods: {
      toggleAccordion(accordionName) {
        if (this.activeAccordion === accordionName) {
          this.activeAccordion = "";
        } else {
          this.activeAccordion = accordionName;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .order-review {
    max-width: 800px;
    /* margin: 0 auto; */
    padding: 2rem;
    /* justify-content: space-around !important; */
    display: flex;
    min-width: 100%;
    gap: 46px;
  }
  
  .table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid #e2e8f0;
  }
  
  .table th,
  .table td {
    border: 1px solid #e2e8f0;
    padding: 0.75rem;
  }
  
  .accordion {
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    overflow: hidden;
  }
  
  .accordion-item {
    border-bottom: 1px solid #e2e8f0;
  }
  
  .accordion-header {
    padding: 1rem;
    background-color: #f7fafc;
    border-bottom: 1px solid #e2e8f0;
    cursor: pointer;
  }
  
  .accordion-button {
    background-color: transparent;
    border: none;
    text-align: left;
    width: 100%;
    transition: background-color 0.3s ease;
  }
  
  .accordion-button:focus {
    outline: none;
  }
  
  .accordion-button.active {
    background-color: #edf2f7;
  }
  
  .accordion-collapse {
    padding: 1rem;
    background-color: #edf2f7;
    display: none;
  }
  
  .accordion-collapse[style] {
    display: block;
  }
  
  .accordion-body {
    padding: 1rem;
  }
  </style>
  