<template>
    <div>
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        type="button"
        @click="openModal"
      >
        Pagar con Bitcoin
      </button>
  
      <!-- Ventana emergente (Modal) -->
      <div
        class="fixed inset-0 flex items-center justify-center z-50"
        v-show="showModal"
        @click.self="closeModal"
      >
        <div class="bg-white rounded shadow-lg p-8 max-w-md">
          <h2 class="text-2xl font-bold mb-4">Pago de Producto</h2>
  
          <div class="mb-4">
            <p class="text-gray-500">Nombre de Usuario del Comprador: {{ buyerUsername }}</p>
            <p class="text-gray-500">Saldo disponible: {{ availableBalance }} BTC</p>
          </div>
  
          <h3 class="text-lg font-bold mb-2">Detalles de la compra</h3>
          <div class="bg-gray-100 p-4 rounded mb-4">
            <table class="w-full">
              <thead>
                <tr>
                  <th class="px-4 py-2">Producto</th>
                  <th class="px-4 py-2">Precio</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in products" :key="product.id">
                  <td class="border px-4 py-2">{{ product.name }}</td>
                  <td class="border px-4 py-2">{{ product.price }} BTC</td>
                </tr>
              </tbody>
            </table>
          </div>
  
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
            type="button"
            @click="submitPayment"
          >
            Pagar con Bitcoin
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  import SingleDigitalProduct from '../SingleDigitalProduct.vue';
  export default {
    data() {
      return {
        buyerUsername: 'Nombre de Usuario del Comprador',
        availableBalance: 5.0,
        products: [
          { id: 1, name: 'Producto 1', price: 0.01 },
          { id: 2, name: 'Producto 2', price: 0.02 },
          { id: 3, name: 'Producto 3', price: 0.03 },
        ],
        showModal: false,
      };
    },
    methods: {
      openModal() {
        this.showModal = true;
      },
      closeModal() {
        this.showModal = false;
      },
      submitPayment() {
        // Aquí puedes implementar la lógica para procesar el pago con Bitcoin
        // ...
        alert('Pago realizado con éxito');
        this.closeModal();
      },
    },
  };
  </script>
  