<template>
  <div class="flex">
    <!-- Panel lateral -->
    <div class="flex flex-col w-1/4 bg-gray-200 p-4">
      <h2 class="text-2xl font-bold mb-4">Panel de Carteras</h2>
      <div class="mb-2">
        <span class="font-bold">Nombre de usuario:</span>
        <span>{{ username }}</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Saldo actual:</span>
        <span>{{ balance }} BTC</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Balance pendiente:</span>
        <span>{{ balanceInUSD }} USD</span>
      </div>
      <div>
        <span class="font-bold">Dirección de la cartera:</span>
        <span>{{ walletAddress }}</span>
      </div>
      <div class="flex flex-col items-center mt-8">
    <h3 class="text-xl font-bold mb-4">Código QR para depósito:</h3>
    <div class="w-48 h-48">
      <img :src="qrCodeURL" alt="Código QR" v-if="qrCodeURL" class="mx-auto" />
    </div>
  </div>
    </div>

    <!-- Formulario de retiro -->
    <div class="flex flex-col items-center w-3/4 p-4">
      <h2 class="text-2xl font-bold mb-4">Retiro de Bitcoin</h2>
      <div class="w-full max-w-xs">
        <label for="amountBTC" class="block mb-2">Cantidad (BTC):</label>
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <span class="text-gray-500">$</span>
          </div>
          <input
            type="number"
            id="amountBTC"
            v-model="amountBTC"
            class="pl-8 pr-3 py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
            placeholder="Ingrese la cantidad de Bitcoin a retirar"
            @input="convertBTCToUSD"
          />
        </div>
        <label for="amountUSD" class="block mt-4 mb-2">Cantidad (USD):</label>
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <span class="text-gray-500">$</span>
          </div>
          <input
            type="number"
            id="amountUSD"
            v-model="amountUSD"
            class="pl-8 pr-3 py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
            placeholder="Ingrese la cantidad en USD"
          />
        </div>
        <label for="walletAddress" class="block mt-4 mb-2">Dirección de la cartera de destino:</label>
        <input
          type="text"
          id="walletAddress"
          v-model="walletAddress"
          class="pl-3 pr-2 py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Ingrese la dirección de la cartera de destino"
        />
        <button
          class="mt-4 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
          @click="withdrawBitcoin"
          :disabled="isWithdrawing || amountBTC <= 0 || amountBTC > balance || amountUSD <= 0 || walletAddress === ''"
        >
          {{ isWithdrawing ? 'Retirando...' : 'Retirar' }}
        </button>
      </div>
    </div>
  </div>

  <div class="mt-8">
    <h3 class="text-xl font-bold mb-4">Historial de transacciones</h3>
    <table class="min-w-full border border-gray-300">
      <thead>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">Cantidad (BTC)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Cantidad (USD)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Tipo</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha</th>
          <th v-if="transactionHistory.length > 0" class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactionHistory" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amountInUSD }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.type === 'deposit', 'text-red-500': transaction.type === 'withdrawal'}">{{ transaction.type }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.date }}</td>
          <td v-if="transaction.type === 'deposit'" class="py-2 px-4 border-b">{{ transaction.wallet }}</td>
          <td v-if="transaction.type === 'withdrawal'" class="py-2 px-4 border-b">{{ transaction.wallet }}</td>
        </tr>
      </tbody>
    </table>
  </div>

 
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "JohnDoe",
      balance: 5, // Ejemplo: saldo inicial de 5 BTC
      balanceInUSD: 0,
      amountBTC: 0,
      amountUSD: 0,
      walletAddress: "Dirección_de_la_cartera_de_ejemplo", // Dirección de la cartera de destino
      qrCodeURL: "",
      transactionHistory: [
        {
          id: 1,
          amount: 2.5,
          amountInUSD: 15000,
          type: "deposit",
          date: "2023-05-25 10:30 AM",
          wallet: "Dirección_de_la_cartera_de_ejemplo",
        },
      ],
      isWithdrawing: false,
      btcValue: 0,
    };
  },
  methods: {
    async fetchBTCValue() {
      try {
        const response = await axios.get(
          "https://api.coinbase.com/v2/prices/spot?currency=USD"
        );
        this.btcValue = parseFloat(response.data.data.amount);
        this.balanceInUSD = this.balance * this.btcValue;
      } catch (error) {
        console.error("Error al obtener el valor del BTC:", error);
      }
    },
    async withdrawBitcoin() {
      if (
        this.isWithdrawing ||
        this.amountBTC <= 0 ||
        this.amountBTC > this.balance ||
        this.amountUSD <= 0 ||
        this.walletAddress === ""
      )
        return;

      this.isWithdrawing = true;

      // Simulamos una llamada asincrónica con un retardo de 1 segundo
      setTimeout(() => {
        console.log(`Se ha retirado ${this.amountBTC} Bitcoin a la dirección ${this.walletAddress}.`);
        const transaction = {
          id: Date.now(),
          amount: this.amountBTC,
          amountInUSD: this.amountUSD,
          type: "withdrawal",
          date: new Date().toLocaleString(),
          wallet: this.walletAddress,
        };
        this.transactionHistory.unshift(transaction);
        this.balance -= parseFloat(this.amountBTC);

        this.fetchBTCValue();

        this.amountBTC = 0;
        this.amountUSD = 0;
        this.walletAddress = "";
        this.isWithdrawing = false;
      }, 1000);
    },
    convertBTCToUSD() {
      this.amountUSD = (this.amountBTC * this.btcValue).toFixed(2);
    },
  },
  mounted() {
    this.fetchBTCValue();
    // Generamos el código QR para depositar
    this.qrCodeURL = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(
      this.walletAddress
    )}&size=200x200`;
  },
};
</script>

<style>
/* Estilos personalizados para el panel y la sección inferior */
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

button:hover {
  transform: translateY(-2px);
}
</style>
