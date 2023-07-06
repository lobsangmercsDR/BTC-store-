<template>
  <div class="flex">
    <!-- Side panel -->
    <div class="flex flex-col w-1/4 bg-gray-200 p-4" style="width: 295px;">
      <h2 class="text-2xl font-bold mb-4">Wallet Panel</h2>
      <div class="mb-2">
        <span class="font-bold">Username: </span>
        <span>{{ user.name }}</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Balance Actual: </span>
        <span class="text-green-500"> {{ user.userBalance }} USD</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Balance Pendiente:</span>
        <span class="text-yellow-500"> {{ user.userBalance }} USD</span>
      </div>
      <div>
        <p class="font-bold">Wallet Address: </p>
        <p style="word-wrap: break-word;">{{ user.wallet_address}}</p>
      </div>
      <div class="flex flex-col items-center mt-8">
        <h3 class="text-xl font-bold mb-4">QR Code para depositos:</h3>
        <div class="w-48 h-48">
          <img :src="qrCodeURL" alt="QR Code" v-if="qrCodeURL" class="mx-auto" />
        </div>
      </div>
    </div>
    <!-- Withdrawal form -->
    <div class="flex flex-col items-center w-3/4 p-4">
      <h2 class="text-2xl font-bold mb-4">Enviar Solicitud de Retiro</h2>
      <div class="w-full max-w-xs">
        <label for="amountUSD" class="block mt-4 mb-2">Cantidad en dolares:</label>
        <input
          type="number"
          id="amountUSD"
          v-model="amountUSD"
          class="py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Enter the amount in USD"
          @input="convertUSDtoBTC"
        />

         <label for="destinationWalletAddress" class="block mt-4 mb-2">Wallet a Depositar</label>
         <input
          type="text"
          id="destinationWalletAddress"
          v-model="destinationWalletAddress"
          class="py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Enter the destination wallet address"
        />
        <button
          class="mt-4 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
          @click="requestWithdrawal"
        >
          Solicitar Retiro
        </button>
        <p v-if="withdrawalOrderNumber" class="mt-2">
          Withdrawal order number: {{ withdrawalOrderNumber }}
        </p>
      </div>
    </div>
  </div>

  <div class="mt-8">
    <h3 class="text-xl font-bold mb-4">Historial de retiros</h3>
    <table class="table min-w-full border border-gray-300">
      <thead>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">No. de orden</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Monto</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Estado</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de Solicitud</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de Respuesta</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactionHistory" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.withdrawalOrderNumber }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amountInUSD }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-black-500': transaction.status === 'Pendiente', 'text-red-500': transaction.status === 'Rechazada', 'text-green-500':transaction.status=== 'Aprobada'}">{{ transaction.status }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.date }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.date }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.wallet }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      user: {
        name: '',
        userBalance: 0,
        wallet_address: ''
      },
      transactionHistory: []
    };
  },
  created() {
    this.getUserData()
  },
  methods: {
    async getUserData() { 
      await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
      }})
      .then(response => {this.user = response.data; console.log(response.data)})
      .catch(error => {console.log(error.response.data)})
    },
    async requestWithdrawal() {
      this.isWithdrawing = true;

      try {
        console.log('lelgo')
        // await new Promise((resolve) => setTimeout(resolve, 2000));

        const withdrawalOrderNumber = generateWithdrawalOrderNumber(); // Generate a withdrawal order number
        this.withdrawalOrderNumber = withdrawalOrderNumber;

        this.transactionHistory.push({
          id: Date.now(),
          withdrawalOrderNumber: withdrawalOrderNumber,
          amount: this.amountBTC,
          amountInUSD: this.amountUSD,
          status: "Rechazada",
          date: new Date().toLocaleDateString(),
          wallet: this.destinationWalletAddress,
        });

        // Reset form fields
        this.amountBTC = 0;
        this.amountUSD = 0;
        this.destinationWalletAddress = "";
      } catch (error) {
        console.error("Error requesting Bitcoin withdrawal:", error);
      }

      this.isWithdrawing = false;
    },
    convertBTCToUSD() {
      this.amountUSD = this.amountBTC * this.btcValue;
    },
    convertUSDtoBTC() {
      this.amountBTC = this.amountUSD / this.btcValue;
    },
  },
  async mounted() {
    this.qrCodeURL = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${this.walletAddress}`;
  },
};

// Generate a random withdrawal order number
function generateWithdrawalOrderNumber() {
  return Math.floor(Math.random() * 1000000) + 1;
}
</script>

<style scoped>
.table {
  border-collapse: collapse;
}
</style>
