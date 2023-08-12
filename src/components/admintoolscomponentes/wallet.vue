<template>
  <div>
    <h2 class="text-2xl font-bold mb-4 mt-4">Withdrawal Requests</h2>
    <table class="table retireTable min-w-full border border-gray-300" v-if="!isWindowSmall">
      <thead>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">Withdrawal Order Number</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Username</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Amount (BTC)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Amount (USD)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Status</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Date</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in transactionHistory" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.withdrawalOrderNumber }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.username }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amountInUSD }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.status === 'pending', 'text-red-500': transaction.status === 'completed'}">{{ transaction.status }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.date }}</td>
          <td class="py-2 px-4 border-b" style="word-break: break-all;">{{ transaction.wallet }}</td>
          <td class="py-2 px-4 border-b">
            <button
              class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-md transition-colors duration-300 ease-in-out mr-2"
              @click="approveWithdrawal(transaction)"
              :disabled="transaction.status !== 'pending'"
            >
              Approve
            </button>
            <button
              class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
              @click="rejectWithdrawal(transaction)"
              :disabled="transaction.status !== 'pending'"
            >
              Reject
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!--Tabla responsive -->
    <table :key="transaction.id" v-if="isWindowSmall" v-for="transaction in transactionHistory" class=" tableWit responsive-table">
  <tbody>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Withdrawal Order Number</td>
      <td class="py-2 px-4 border-b">{{ transaction.withdrawalOrderNumber }}</td>
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
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Acciones</td>
      <td class="py-2 px-4 border-b">
        <button
              class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-md transition-colors duration-300 ease-in-out mr-2"
              @click="approveWithdrawal(transaction)"
              :disabled="transaction.status !== 'pending'"
            >
              Approve
            </button>
            <button
              class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
              @click="rejectWithdrawal(transaction)"
              :disabled="transaction.status !== 'pending'"
            >
              Reject
            </button>
      </td>
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
      transactionHistory: [
        {
          id: 1,
          withdrawalOrderNumber: "ABC123",
          amount: 0.5,
          amountInUSD: 25000,
          status: "pending",
          date: "2023-05-28",
          wallet: "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
          username: "john_doe"
        },
        {
          id: 2,
          withdrawalOrderNumber: "DEF456",
          amount: 1.2,
          amountInUSD: 60000,
          status: "pending",
          date: "2023-05-29",
          wallet: "3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS",
          username: "jane_smith"
        },
        {
          id: 3,
          withdrawalOrderNumber: "GHI789",
          amount: 0.8,
          amountInUSD: 40000,
          status: "pending",
          date: "2023-05-30",
          wallet: "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
          username: "alice_johnson"
        }
      ],
      isWindowSmall: false
    };
  },
  methods: {
    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 960;

    },  
    async getUserData() { 
      await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
      }})
      .then(response => {this.user = response.data})
      .catch(error => {console.log(error.response.data)})
    },

    approveWithdrawal(transaction) {
      transaction.status = "completed";
      // Realiza acciones adicionales para aprobar el retiro, como enviar fondos a la billetera de destino.
    },
    rejectWithdrawal(transaction) {
      transaction.status = "rejected";
      // Realiza acciones adicionales para rechazar el retiro.
    }
  }
};
</script>

<style>
.retireTable {
  min-width: 960px;
}

.tableWit {
  max-width: 600px;
  border: 3px solid;
  margin: 40px auto;
}

</style>
