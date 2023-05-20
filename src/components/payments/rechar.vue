<template>
    <div class="flex">
      <!-- Panel lateral -->
      <div class="flex flex-col w-1/4 bg-gray-200 p-4">
        <h2 class="text-2xl font-bold mb-4">Panel de usuario</h2>
        <div class="mb-2">
          <span class="font-bold">Nombre de usuario:</span>
          <span>{{ username }}</span>
        </div>
        <div class="mb-2">
          <span class="font-bold">Saldo actual:</span>
          <span>{{ balance }} BTC</span>
        </div>
        <div class="mb-2">
          <span class="font-bold">Dólares:</span>
          <span>{{ balanceInUSD }} USD</span>
        </div>
        <div class="mb-4">
          <span class="font-bold">Palabras de la cartera:</span>
          <div class="grid grid-cols-4 gap-2">
            <div v-for="word in walletWords" :key="word" class="px-2 py-1 bg-white border border-gray-300 rounded">{{ word }}</div>
          </div>
        </div>
      </div>
  
      <!-- Formulario de depósito -->
      <div class="flex flex-col items-center w-3/4 p-4">
        <h2 class="text-2xl font-bold mb-4">Depósito de Bitcoin</h2>
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
              placeholder="Ingrese la cantidad de Bitcoin"
              @input="convertBTCtoUSD"
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
              @input="convertUSDtoBTC"
            />
          </div>
          <button
            class="mt-4 px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-md transition-colors duration-300 ease-in-out"
            @click="depositBitcoin"
            :disabled="isDepositing || amountBTC === 0"
          >
            {{ isDepositing ? 'Depositar...' : 'Depositar' }}
          </button>
        </div>
  
        <!-- Código QR -->
        <div class="flex flex-col items-center mt-8">
          <h3 class="text-xl font-bold mb-4">Código QR para depósito:</h3>
          <div class="w-48 h-48">
            <img :src="qrCodeURL" alt="Código QR" v-if="qrCodeURL" class="mx-auto" />
          </div>
        </div>
  
        <!-- Valor actual del BTC -->
        <div class="mt-4">
          <span class="font-bold">Valor actual del BTC:</span>
          <span>{{ btcValue }} USD</span>
        </div>
  
    
        <!-- Historial de recargas -->
        <div class="mt-8">
          <h3 class="text-xl font-bold mb-4">Historial de recargas</h3>
          <ul>
            <li v-for="recharge in rechargeHistory" :key="recharge.id" class="mb-2">
              <span class="font-bold">{{ recharge.amount }} BTC</span>
              <span class="text-gray-500">- {{ recharge.date }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        username: "JohnDoe",
        balance: 0,
        balanceInUSD: 0,
        amountBTC: 0,
        amountUSD: 0,
        walletWords: [
          "word1", "word2", "word3", "word4", "word5", "word6",
          "word7", "word8", "word9", "word10", "word11", "word12"
        ],
        qrCodeURL: "",
        rechargeHistory: [],
        isDepositing: false,
        btcValue: 0,
        usdToBtc: 0,
        btcToUsd: 0
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
      convertBTCtoUSD() {
        this.amountUSD = (this.amountBTC * this.btcValue).toFixed(2);
      },
      convertUSDtoBTC() {
        this.amountBTC = (this.amountUSD / this.btcValue).toFixed(8);
      },
      async depositBitcoin() {
        if (this.isDepositing) return;
  
        this.isDepositing = true;
  
        // Simulamos una llamada asincrónica con un retardo de 1 segundo
        setTimeout(() => {
          console.log(`Se ha depositado ${this.amountBTC} Bitcoin.`);
          const recharge = {
            id: Date.now(),
            amount: this.amountBTC,
            date: new Date().toLocaleString()
          };
          this.rechargeHistory.unshift(recharge);
          this.balance += parseFloat(this.amountBTC);
  
          this.fetchBTCValue();
  
          this.amountBTC = 0;
          this.amountUSD = 0;
          this.isDepositing = false;
        }, 1000);
      }
    },
    mounted() {
      this.fetchBTCValue();
      // Generamos el código QR para depositar
      this.qrCodeURL = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(
        'Dirección_de_la_cartera'
      )}&size=200x200`;
    }
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
  