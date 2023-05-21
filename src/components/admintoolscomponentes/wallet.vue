<template>
    <div>
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center space-x-4">
          <h2 class="text-2xl font-bold">Carteras de BTC</h2>
          <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Agregar Cartera</button>
        </div>
        <input type="text" class="border border-gray-300 px-4 py-2 rounded" v-model="searchQuery" placeholder="Buscar cartera...">
      </div>
      <table class="min-w-full bg-white border border-gray-200">
        <thead>
          <tr>
            <th class="py-2 px-4 border-b">Usuario</th>
            <th class="py-2 px-4 border-b">Cartera</th>
            <th class="py-2 px-4 border-b">Dirección</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="wallet in filteredWallets" :key="wallet.id">
            <td class="py-2 px-4 border-b">{{ wallet.user }}</td>
            <td class="py-2 px-4 border-b">{{ wallet.name }}</td>
            <td class="py-2 px-4 border-b">{{ wallet.address }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        wallets: [
          { id: 1, user: 'Usuario 1', name: 'Cartera 1', address: 'Dirección de la cartera 1' },
          { id: 2, user: 'Usuario 2', name: 'Cartera 2', address: 'Dirección de la cartera 2' },
          { id: 3, user: 'Usuario 3', name: 'Cartera 3', address: 'Dirección de la cartera 3' },
        ],
        searchQuery: '',
      };
    },
    computed: {
      filteredWallets() {
        if (this.searchQuery === '') {
          return this.wallets;
        } else {
          const query = this.searchQuery.toLowerCase();
          return this.wallets.filter(wallet =>
            wallet.user.toLowerCase().includes(query) ||
            wallet.name.toLowerCase().includes(query) ||
            wallet.address.toLowerCase().includes(query)
          );
        }
      },
    },
  };
  </script>
  
  <style>
  table {
    border-collapse: collapse;
  }
  
  th,
  td {
    padding: 10px;
    text-align: left;
  }
  
  th {
    background-color: #F3F4F6;
    font-weight: bold;
  }
  
  tr:nth-child(even) {
    background-color: #F9FAFB;
  }
  
  input[type="text"] {
    width: 300px;
  }
  </style>
  