<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">Withdrawal Requests</h2>
    <table class="table min-w-full border border-gray-300">
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
          <td class="py-2 px-4 border-b">{{ transaction.wallet }}</td>
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
      ]
    };
  },
  methods: {
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
