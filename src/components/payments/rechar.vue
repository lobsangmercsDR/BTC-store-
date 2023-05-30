<template>
  <div class="flex">
    <!-- Side panel -->
    <div class="flex flex-col w-1/4 bg-gray-200 p-4">
      <h2 class="text-2xl font-bold mb-4">Wallet Panel</h2>
      <div class="mb-2">
        <span class="font-bold">Username:</span>
        <span>{{ username }}</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Current Balance:</span>
        <span class="text-green-500">{{ balance }} BTC | {{ balanceInUSD }} USD</span>
      </div>
      <div class="mb-2">
        <span class="font-bold">Pending Balance:</span>
        <span class="text-yellow-500">{{ pendingBalance }} BTC | {{ pendingBalanceInUSD }} USD</span>
      </div>
      <div>
        <span class="font-bold">Wallet Address:</span>
        <span>{{ walletAddress }}</span>
      </div>
      <div class="flex flex-col items-center mt-8">
        <h3 class="text-xl font-bold mb-4">QR Code for deposit:</h3>
        <div class="w-48 h-48">
          <img :src="qrCodeURL" alt="QR Code" v-if="qrCodeURL" class="mx-auto" />
        </div>
      </div>
    </div>
    <!-- Withdrawal form -->
    <div class="flex flex-col items-center w-3/4 p-4">
      <h2 class="text-2xl font-bold mb-4">Bitcoin Withdrawal</h2>
      <div class="w-full max-w-xs">
        <label for="amountBTC" class="block mb-2">Amount (BTC):</label>
        <input
          type="number"
          id="amountBTC"
          v-model="amountBTC"
          class="py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Enter the amount of Bitcoin to withdraw"
          @input="convertBTCToUSD"
        />
        <label for="amountUSD" class="block mt-4 mb-2">Amount (USD):</label>
        <input
          type="number"
          id="amountUSD"
          v-model="amountUSD"
          class="py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Enter the amount in USD"
          @input="convertUSDtoBTC"
        />
        <label for="destinationWalletAddress" class="block mt-4 mb-2">Destination Wallet Address:</label>
        <input
          type="text"
          id="destinationWalletAddress"
          v-model="destinationWalletAddress"
          class="py-2 border border-gray-300 rounded-md w-full focus:outline-none focus:border-blue-500"
          placeholder="Enter the destination wallet address"
        />
        <button
          class="mt-4 px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
          @click="withdrawBitcoin"
          :disabled="isWithdrawing || amountBTC <= 0 || amountBTC > balance || amountUSD <= 0 || destinationWalletAddress === '' || destinationWalletAddress === walletAddress"
        >
          {{ isWithdrawing ? 'Withdrawing...' : 'Withdraw' }}
        </button>
      </div>
    </div>
  </div>

  <div class="mt-8">
    <h3 class="text-xl font-bold mb-4">Transaction History</h3>
    <table class="table min-w-full border border-gray-300">
      <thead>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">Amount (BTC)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Amount (USD)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Type</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Date</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactionHistory" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amountInUSD }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.type === 'deposit', 'text-red-500': transaction.type === 'withdrawal'}">{{ transaction.type }}</td>
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
      username: "", // Empty string as default value for username
      balance: 5, // Example: initial balance of 5 BTC
      balanceInUSD: 0,
      pendingBalance: 0, 
      pendingBalanceInUSD: 0,
      amountBTC: 0,
      amountUSD: 0,
      walletAddress: "Example_wallet_address", // Own wallet address
      destinationWalletAddress: "", // Destination wallet address
      qrCodeURL: "",
      transactionHistory: [],
      isWithdrawing: false,
      btcValue: 0,
    };
  },
  methods: {
    async fetchBTCValue() {
      try {
        const response = await axios.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json");
        this.btcValue = parseFloat(response.data.bpi.USD.rate.replace(',', ''));
        this.balanceInUSD = this.balance * this.btcValue;
        this.pendingBalanceInUSD = this.pendingBalance * this.btcValue;
      } catch (error) {
        console.error("Error fetching BTC value:", error);
      }
    },
    async withdrawBitcoin() {
      if (
        this.isWithdrawing ||
        this.amountBTC <= 0 ||
        this.amountBTC > this.balance ||
        this.amountUSD <= 0 ||
        this.destinationWalletAddress === "" ||
        this.destinationWalletAddress === this.walletAddress
      ) {
        return;
      }

      this.isWithdrawing = true;

      try {
        // Placeholder for the actual withdrawal process, replace it with the actual process.
        await new Promise((resolve) => setTimeout(resolve, 2000));

        this.transactionHistory.push({
          id: Date.now(),
          amount: this.amountBTC,
          amountInUSD: this.amountUSD,
          type: "withdrawal",
          date: new Date().toLocaleDateString(),
          wallet: this.destinationWalletAddress,
        });

        this.balance -= this.amountBTC;
        this.pendingBalance += this.amountBTC;
        this.balanceInUSD = this.balance * this.btcValue;
        this.pendingBalanceInUSD = this.pendingBalance * this.btcValue;
        this.amountBTC = 0;
        this.amountUSD = 0;
        this.destinationWalletAddress = "";
      } catch (error) {
        console.error("Error withdrawing Bitcoin:", error);
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
    this.username = Cookies.get('username') || '';
    await this.fetchBTCValue();
    this.qrCodeURL = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${this.walletAddress}`;
  },
};
</script>

<style scoped>
.table {
  border-collapse: collapse;
}
</style>
