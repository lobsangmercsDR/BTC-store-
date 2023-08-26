<template>
  <div>
    <h2 class="text-2xl font-bold mb-4 mt-4">Solicitudes de retiro</h2>
    <div class="filter" style="margin: 22px 14px;">
        <label for="categoryFilter " class="text-lg font-semibold"  style="align-self: center;">Tipo:</label>
        <select v-model="selectedType" id="categoryFilter" class="text-gray-600 text-lg p-2 border border-gray-300 rounded-lg" @change = "this.getWitdrawsRequests()">
          <option value="pending"> Pendientes</option>
          <option value="approved"> Aprobadas</option>
          <option value="declined"> Rechazadas</option>
        </select>
      </div>
    <table class="table retireTable min-w-full border border-gray-300" v-if="!isWindowSmall">
      <thead>
        <tr>
          <th class="py-2 px-4 bg-gray-100 border-b">No. de orden</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Username</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Peticion (USD)</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Estado</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Fecha de solicitud</th>
          <th class="py-2 px-4 bg-gray-100 border-b">Wallet</th>
          <th class="py-2 px-4 bg-gray-100 border-b" v-if="this.selectedType =='pending'">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="transaction in withdrawRequests" :key="transaction.id">
          <td class="py-2 px-4 border-b">{{ transaction.no_orden }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.user.name }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
          <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.status === 'pending', 'text-red-500': transaction.status === 'completed'}">{{ transaction.status }}</td>
          <td class="py-2 px-4 border-b">{{ transaction.fecha_solicitud }}</td>
          <td class="py-2 px-4 border-b" style="word-break: break-all;">{{ transaction.walletRequested }}</td>
          <td class="py-2 px-4 border-b" v-if="transaction.status == 'Pendiente'">
            <button
              class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-md transition-colors duration-300 ease-in-out mr-2"
              @click="approveWithdrawal(transaction)"
            >
              Aprobar
            </button>
            <button
              class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
              @click="rejectWithdrawal(transaction)"
            >
              Rechazar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!--Tabla responsive -->
    <table :key="transaction.id" v-if="isWindowSmall" v-for="transaction in withdrawRequests" class=" tableWit responsive-table">
  <tbody>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">No. de orden</td>
      <td class="py-2 px-4 border-b">{{ transaction.no_orden }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Username</td>
      <td class="py-2 px-4 border-b">{{ transaction.user.name }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Cantidad (USD)</td>
      <td class="py-2 px-4 border-b">{{ transaction.amount }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Estado</td>
      <td class="py-2 px-4 border-b" :class="{'text-green-500': transaction.status === 'pending', 'text-red-500': transaction.status === 'completed'}">{{ transaction.status }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Fecha de solicitud</td>
      <td class="py-2 px-4 border-b">{{ transaction.fecha_solicitud }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b">Wallet</td>
      <td class="py-2 px-4 border-b">{{ transaction.walletRequested }}</td>
    </tr>
    <tr>
      <td class="py-2 px-4 bg-gray-100 border-b" v-if="transaction.status=='Pendiente'">Acciones</td>
      <td class="py-2 px-4 border-b">
        <button
              class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-md transition-colors duration-300 ease-in-out mr-2"
              @click="approveWithdrawal(transaction)"
            >
              Aprobar
            </button>
            <button
              class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-md transition-colors duration-300 ease-in-out"
              @click="rejectWithdrawal(transaction)"
            >
              Rechazar
            </button>
      </td>
    </tr>
  </tbody>
</table>


  </div>
</template>

<script>
  import axios from 'axios';
  import Cookies from 'js-cookie';
export default {


  created() {
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
    this.getWitdrawsRequests()
  },

  data() {
    return {
      selectedType:"pending",
      withdrawRequests: [],
      isWindowSmall: false
    };
  },
  methods: {
    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 960;

    },  
    async getWitdrawsRequests() { 
      await axios.get(`http://127.0.0.1:8000/api/admin/withdraws?t=${this.selectedType}`, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
      }})
      .then(response => {this.withdrawRequests = response.data; console.log(response.data)})
      .catch(error => {console.log(error.response.data)})
    },

    async approveWithdrawal(transaction) {
      await axios.put(`http://127.0.0.1:8000/api/admin/withdraws/${transaction.id}?approve=t`,null, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        console.log(response)
        this.getWitdrawsRequests()
      })
      .catch(error => {
        console.log(error)
      })
    },


   async rejectWithdrawal(transaction) {
      await axios.put(`http://127.0.0.1:8000/api/admin/withdraws/${transaction.id}`,null, {
        headers:{
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        console.log(response)
        this.getWitdrawsRequests()
      })
      .catch(error => {
        console.log(error)
      })
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
