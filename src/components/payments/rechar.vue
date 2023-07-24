<template>
  <div class="wallet-cont">
    <!-- Side panel -->
    <div class="bg-gray-200 card-cont" style="width: 295px;">
      <div class="content">


      <h2 class="text-2xl font-bold mb-4 ">Wallet Panel</h2>
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
          v-model="amount"
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
      </div>
    </div>
  </div>

  <div class="mt-8">
    <h3 class="text-xl font-bold mb-4">Historial de retiros</h3>
    <table class="table min-w-full border border-gray-300  responsive-table">
      <thead v-show="!isWindowSmall">
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">No. de orden</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Monto</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Estado</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de Solicitud</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de Respuesta</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
        </tr>
      </thead>
      <tbody v-if="!isWindowSmall">
        <tr v-for="transaction in transactionHistory" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.no_orden }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-black-500': transaction.status === 'Pendiente', 'text-red-500': transaction.status === 'Rechazada', 'text-green-500':transaction.status=== 'Aprobada'}">{{ transaction.status }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.fecha_solicitud }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.fecha_review }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.walletRequested }}</td>
        </tr>
      </tbody>
    </table>

    <table :key="transaction.id" v-if="isWindowSmall" v-for="transaction in transactionHistory"  class="table min-w-full border border-gray-300  responsive-table">
      <tbody>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">No. de orden</td>
          <td class="py-2 px-4 border-b">{{ transaction.no_orden }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Monto</td>
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Estado</td>
          <td class="py-2 px-4 border-b" :class="{'text-black-500': transaction.status === 'Pendiente', 'text-red-500': transaction.status === 'Rechazada', 'text-green-500':transaction.status=== 'Aprobada'}">{{ transaction.status }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Fecha de Solicitud</td>
          <td class="py-2 px-4 border-b">{{ transaction.fecha_solicitud }}</td>
        </tr>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de Respuesta</th>
          <td class="py-2 px-4 border-b">{{ transaction.fecha_review }}</td>
        </tr>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
          <td class="py-2 px-4 border-b">{{ transaction.walletRequested }}</td>
        </tr>
      </tbody>
    </table>


    <section  class="nav-arrows" v-show="2==2">
      <svg xmlns="http://www.w3.org/2000/svg" :style="{color:previousArrowColor}" @click="handleChangePage('fisics',-1)" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M15 18l-6-6 6-6"/>
      </svg> 
      <div  class="pageCounter"> <span> {{ 422 }}</span></div>

      <svg xmlns="http://www.w3.org/2000/svg" :style="{color:nextArrowColor}" @click="handleChangePage('fisics',1)" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 18l6-6-6-6"/>
      </svg>
    </section>
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
      isWindowSmall: false,
      amount:0,
      destinationWalletAddress:'',
      transactionHistory: []
    };
  },

  created() {
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
    this.getUserData()
    this.getTransactHistory()
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

    async getTransactHistory() {
      await axios.get(`http://127.0.0.1:8000/api/withdraws`, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        this.transactionHistory = response.data
        console.log(response.data, this.transactionHistory)
      })
      .catch(error =>  {
        console.log(error)
      })
    },

    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 768;
    },
    async requestWithdrawal() {
      this.isWithdrawing = true;
        // await new Promise((resolve) => setTimeout(resolve, 2000));

        const withdrawalOrderNumber = generateWithdrawalOrderNumber(); // Generate a withdrawal order number
        this.withdrawalOrderNumber = withdrawalOrderNumber;
        await axios.post(`http://127.0.0.1:8000/api/withdraws`,{
        no_orden: withdrawalOrderNumber,
        amount: this.amount,
        walletRequested: this.destinationWalletAddress
      },
      {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        console.log(response.data)
        this.getTransactHistory()
      })
      .catch(error => {
        console.log(error.response.data)
      } )
        


        // this.transactionHistory.push({
        //   id: Date.now(),
        //   withdrawalOrderNumber: withdrawalOrderNumber,
        //   amount: this.amountBTC,
        //   amountInUSD: this.amountUSD,
        //   status: "Pendiente",
        //   date: new Date().toLocaleDateString(),
        //   wallet: this.destinationWalletAddress,
        // });
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
@media (max-width: 700px) {
  .wallet-cont  {
    flex-direction: column;
    align-items: center;
  }
}


.wallet-cont {
  display: flex;
  margin-top: 40px;
}


@media (max-width:768px) {
  .responsive-table {
    display: table;
    margin-top: 20px;
    border:2px solid;
  }

}

.table {
  border-collapse: collapse;
}

.nav-arrows {
  display: flex;
    justify-content: center;
    margin-top: 20px;
}
</style>
