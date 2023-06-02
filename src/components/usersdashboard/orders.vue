<template>
  <div class="bg-white rounded shadow">
    <div class="px-4 py-3 border-b">
      <h2 class="text-lg font-semibold">Mis órdenes</h2>
    </div>
    <div class="p-4">
      <div v-if="physicalOrders.length === 0 && digitalOrders.length === 0" class="text-gray-600">
        No hay órdenes disponibles.
      </div>

      <div v-if="physicalOrders.length > 0">
        <h3 @click="toggleOrderSection('physical')" class="text-lg font-semibold my-2 cursor-pointer">
          Órdenes de productos físicos
          <span v-if="isOrderSectionOpen('physical')" class="text-sm ml-2">[-]</span>
          <span v-else class="text-sm ml-2">[+]</span>
        </h3>
        <table class="table-auto w-full" v-show="isOrderSectionOpen('physical')">
          <thead>
            <tr>
              <th class="px-4 py-2">Orden</th>
              <th class="px-4 py-2">Fecha</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Total</th>
              <th class="px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in physicalOrders" :key="order.id" class="border-b">
              <td class="px-4 py-2">{{ order.id }}</td>
              <td class="px-4 py-2">{{ order.date }}</td>
              <td class="px-4 py-2">{{ order.status }}</td>
              <td class="px-4 py-2">${{ calculateTotalPrice(order.products) }}</td>
              <td class="px-4 py-2">
                <button @click="toggleOrderDetails(order)">Detalles</button>
                <button @click="reportProblem(order)">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-if="order && order.showDetails">
          <ul>
            <li v-for="product in order.products" :key="product.id">{{ product.name }} - {{ product.price }}</li>
          </ul>
        </div>
      </div>

      <div v-if="digitalOrders.length > 0">
        <h3 @click="toggleOrderSection('digital')" class="text-lg font-semibold my-2 cursor-pointer">
          Órdenes de productos digitales
          <span v-if="isOrderSectionOpen('digital')" class="text-sm ml-2">[-]</span>
          <span v-else class="text-sm ml-2">[+]</span>
        </h3>
        <table class="table-auto w-full" v-show="isOrderSectionOpen('digital')">
          <thead>
            <tr>
              <th class="px-4 py-2">Orden</th>
              <th class="px-4 py-2">Fecha</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Total</th>
              <th class="px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in digitalOrders" :key="order.id" class="border-b">
              <td class="px-4 py-2">{{ order.id }}</td>
              <td class="px-4 py-2">{{ order.date }}</td>
              <td class="px-4 py-2">Completado</td>
              <td class="px-4 py-2">${{ calculateTotalPrice(order.products) }}</td>
              <td class="px-4 py-2">
                <button @click="toggleOrderDetails(order)">Detalles</button>
                <button @click="reportProblem(order)">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div v-if="order && order.showDetails">
          <ul>
            <li v-for="product in order.products" :key="product.id">{{ product.name }} - {{ product.price }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      physicalOrders: [
        {
          id: 1,
          date: "2023-05-31",
          status: "Entregado",
          products: [
            { id: 1, name: "Producto 1", price: "$10.00" },
            { id: 2, name: "Producto 2", price: "$15.00" },
          ],
          showDetails: false,
        },
        // ... otras órdenes físicas ...
      ],
      digitalOrders: [
        {
          id: 2,
          date: "2023-05-30",
          status: "Completado",
          products: [
            { id: 3, name: "Producto 3", price: "$20.00" },
            { id: 4, name: "Producto 4", price: "$25.00" },
          ],
          showDetails: false,
        },
        // ... otras órdenes digitales ...
      ],
      openOrderSections: [],
      order: null,
    };
  },
  methods: {
    toggleOrderDetails(order) {
      this.order = order;
      this.order.showDetails = !this.order.showDetails;
    },
    toggleOrderSection(section) {
      if (this.isOrderSectionOpen(section)) {
        this.openOrderSections = this.openOrderSections.filter((s) => s !== section);
      } else {
        this.openOrderSections.push(section);
      }
    },
    isOrderSectionOpen(section) {
      return this.openOrderSections.includes(section);
    },
    calculateTotalPrice(products) {
      return products.reduce((total, product) => total + parseFloat(product.price.replace("$", "")), 0).toFixed(2);
    },
    reportProblem(order) {
      alert(`Reportando problema para la orden ${order.id}`);
    },
  },
};
</script>

<style scoped>
.table-auto {
  width: auto;
}

h3 {
  cursor: pointer;
}

ul {
  list-style-type: disc;
  margin-left: 20px;
}

/* Estilos adicionales para la tabla */
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  text-align: left;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}

button {
  background-color: #3182ce;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
}

button svg {
  width: 16px;
  height: 16px;
  margin-right: 4px;
}
</style>
