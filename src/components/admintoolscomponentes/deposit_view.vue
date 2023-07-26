<template>
    <div style="padding: 20px;">
      <h2 class="text-2xl font-bold mb-4 mt-7">Depositos</h2>
  
      <div class="flex items-center mb-4">
        <label for="search" class="mr-2">Buscar:</label>
        <input type="text" id="search" v-model="searchQuery" placeholder="Enter search query" class="py-2 px-4 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-300 focus:border-blue-300">
      </div>
  
      <table class="min-w-full bg-white shadow-md rounded-lg overflow-hidden " v-if="!isWindowSmall">
        <thead>
          <tr class="bg-gray-200 text-gray-700 uppercase text-sm leading-normal">
            <th class="py-3 px-4 border-b border-gray-300">Deposit Order Number</th>
            <th class="py-3 px-4 border-b border-gray-300">Username</th>
            <th class="py-3 px-4 border-b border-gray-300">Amount (BTC)</th>
            <th class="py-3 px-4 border-b border-gray-300">Amount (USD)</th>
            <th class="py-3 px-4 border-b border-gray-300">Status</th>
            <th class="py-3 px-4 border-b border-gray-300">Date</th>
            <th class="py-3 px-4 border-b border-gray-300">Wallet</th>
            <th class="py-3 px-4 border-b border-gray-300">Blockchain Address</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in filteredTransactions" :key="transaction.id" class="text-gray-700">
            <td class="py-3 px-4 border-b border-gray-300">{{ transaction.depositOrderNumber }}</td>
            <td class="py-3 px-4 border-b border-gray-300">{{ transaction.username }}</td>
            <td class="py-3 px-4 border-b border-gray-300">{{ transaction.amount }}</td>
            <td class="py-3 px-4 border-b border-gray-300">{{ transaction.amountInUSD }}</td>
            <td class="py-3 px-4 border-b border-gray-300" :class="{'text-green-500': transaction.status === 'pending', 'text-red-500': transaction.status === 'completed'}">{{ transaction.status }}</td>
            <td class="py-3 px-4 border-b border-gray-300">{{ transaction.date }}</td>
            <td class="py-3 px-4 border-b border-gray-300" style="word-break: break-all;">{{ transaction.wallet }}</td>
            <td class="py-3 px-4 border-b border-gray-300">
              <a :href="getBlockchainLink(transaction.wallet)" target="_blank" class="text-blue-500 underline">View on Blockchain</a>
            </td>
          </tr>
        </tbody>
      </table>

    <table style="border: 3px solid;margin: 39px auto;" class="table min-w-full border border-gray-300 responsive-table" v-if="isWindowSmall" v-for="transaction in filteredTransactions" :key="transaction.id">
      <tbody>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Deposit Order Number</td>
          <td class="py-2 px-4 border-b">{{ transaction.depositOrderNumber }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Username</td>
          <td class="py-2 px-4 border-b">{{ transaction.username }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Amount (BTC)</td>
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Amount (USD)</td>
          <td class="py-2 px-4 border-b">{{ transaction.amountInUSD }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Status</td>
          <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.status === 'pending', 'text-red-500': transaction.status === 'completed'}">{{ transaction.status }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Date</td>
          <td class="py-2 px-4 border-b">{{ transaction.date }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Wallet</td>
          <td class="py-2 px-4 border-b">{{ transaction.wallet }}</td>
        </tr>
      </tbody>
    </table>

    </div>
  </template>
  
  <script>
  export default {
    created() {
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
  },
    data() {
      return {
        isWindowSmall: false,
        transactionHistory: [
          {
            id: 1,
            depositOrderNumber: "ABC123",
            amount: 0.5,
            amountInUSD: 25000,
            status: "completed",
            date: "2023-05-28",
            wallet: "2MsuJGLHTy4BkbdKaxRXtGS3EsdT4ze9geJ",
            username: "john_doe"
          },
          {
            id: 2,
            depositOrderNumber: "DEF456",
            amount: 1.2,
            amountInUSD: 60000,
            status: "completed",
            date: "2023-05-29",
            wallet: "3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS",
            username: "jane_smith"
          },
          {
            id: 3,
            depositOrderNumber: "GHI789",
            amount: 0.8,
            amountInUSD: 40000,
            status: "completed",
            date: "2023-05-30",
            wallet: "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
            username: "alice_johnson"
          }
        ],
        searchQuery: '',
        currentPage: 1,
        itemsPerPage: 10
      };
    },
    computed: {
      filteredTransactions() {
        return this.transactionHistory.filter(transaction => {
          return transaction.depositOrderNumber.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                 transaction.username.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                 transaction.wallet.toLowerCase().includes(this.searchQuery.toLowerCase());
        });
      },
      totalPages() {
        return Math.ceil(this.filteredTransactions.length / this.itemsPerPage);
      }
    },
    methods: {
      checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 960;
    },  
      getBlockchainLink(walletAddress) {
        return `https://chain.so/address/BTCTEST/${walletAddress}`;
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      },
      previousPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      }
    }
  };
  </script>
  
  <style scoped>

  button {
    margin-top: 0;
  }
  .displayButtons {
    display: grid; 
    grid-auto-columns: 1fr; 
    grid-template-columns: 1fr 1fr; 
    grid-template-rows: 0.3fr 0.7fr; 
    gap: 0px 0px; 
    grid-template-areas: 
      "number number"
      "previous next"; 
    max-width: 200px;
    display: center;
    margin: 15px auto;
    gap: 10px;
  }

  .previous {
    grid-area: previous;
  }
  .next {
    grid-area: next ;

  }
  .number {
    grid-area: number;

  }

  table {
    width: 100%;
  }
  
  th {
    text-align: left;
  }
  
  tr:nth-child(even) {
    background-color: #f8fafc;
  }
  
  tr:hover {
    background-color: #edf2f7;
  }
  
  td {
    padding: 12px;
  }
  
  .text-2xl {
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .shadow-md {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
  
  .rounded-lg {
    border-radius: 0.5rem;
  }
  
  .overflow-hidden {
    overflow: hidden;
  }
  
  .bg-gray-200 {
    background-color: #edf2f7;
  }
  
  .border-gray-300 {
    border-color: #e2e8f0;
  }
  
  .py-3 {
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
  }
  
  .px-4 {
    padding-left: 1rem;
    padding-right: 1rem;
  }
  
  .border-b {
    border-bottom-width: 1px;
  }
  
  .text-gray-700 {
    color: #4a5568;
  }
  
  .text-sm {
    font-size: 0.875rem;
  }
  
  .uppercase {
    text-transform: uppercase;
  }
  
  .leading-normal {
    line-height: 1.5;
  }
  
  .text-green-500 {
    color: #48bb78;
  }
  
  .text-red-500 {
    color: #f56565;
  }
  
  .text-blue-500 {
    color: #3b82f6;
  }
  
  .underline {
    text-decoration: underline;
  }
  
  input[type="text"] {
    width: 300px;
  }
  </style>
  