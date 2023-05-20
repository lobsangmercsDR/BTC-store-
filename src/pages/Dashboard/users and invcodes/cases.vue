<template>
    <div class="bg-white shadow-md rounded-md p-6">
      <h2 class="text-lg font-medium mb-4">Órdenes de venta pendientes</h2>
      <table class="table-auto w-full">
        <thead>
          <tr>
            <th class="px-4 py-2 text-left">Cliente</th>
            <th class="px-4 py-2 text-left">Producto</th>
            <th class="px-4 py-2 text-left">Cantidad</th>
            <th class="px-4 py-2 text-left">Precio</th>
            <th class="px-4 py-2 text-left">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orders" :key="order.id">
            <td class="border px-4 py-2">{{ order.customer }}</td>
            <td class="border px-4 py-2">{{ order.product }}</td>
            <td class="border px-4 py-2">{{ order.quantity }}</td>
            <td class="border px-4 py-2">$ {{ order.price }}</td>
            <td class="border px-4 py-2">
              <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
                @click="approveOrder(order)">
                Aprobar
              </button>
              <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
                @click="rejectOrder(order)">
                Rechazar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        orders: [],
      }
    },
    mounted() {
      this.getOrders();
    },
    methods: {
      async getOrders() {
        try {
          const response = await axios.get('/api/orders');
          this.orders = response.data.filter(order => order.status === 'pendiente');
        } catch (error) {
          console.log(error);
        }
      },
      async approveOrder(order) {
        try {
          await axios.put(`/api/orders/${order.id}`, { status: 'aprobada' });
          this.orders = this.orders.filter(o => o.id !== order.id);
        } catch (error) {
          console.log(error);
        }
      },
      async rejectOrder(order) {
        try {
          await axios.put(`/api/orders/${order.id}`, { status: 'rechazada' });
          this.orders = this.orders.filter(o => o.id !== order.id);
        } catch (error) {
          console.log(error);
        }
      },
    },
  }
  </script>
  
  <style>
  .table-auto {
    width: auto;
  }
  </style>
  