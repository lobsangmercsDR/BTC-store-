<template>
  <div class="bg-gray-100">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-4 px-6">
        <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>
      </div>
    </header>
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="infoContainer">
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Ventas totales</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">${{ genData.total_shares }} </p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Clientes nuevos</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">{{genData.usersAdded}}</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Productos vendidos</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">{{genData.total_num_shares}}</p>
        </div>
      </div>
      <div class="input-filters">
        <label for="key" style="align-self: center;">Key de cartera</label>
        <div class="input">
          <input type="text" id="key" name="key" v-model="SKey"  :disabled="this.disldInp">
        <button class="btn" @click="updateSecKey()" :disabled="this.disldInp">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-save" viewBox="0 0 16 16">
  <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1H2z"/>
</svg>
          </button>
        </div>
      </div>
      <charts></charts>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'
import charts from './charts.vue'

export default {
  components: {
    charts
  },

  data() {
    return {
      SKey:"", 
      disldInp: false,
      genData:{
        total_shares: 0
      },
    }
  },

  created() {
    this.fetchApiKey(),
    this.getAllData()
  },
  methods: {
    async updateSecKey() {
      this.disldInp = true
      await axios.put(`http://127.0.0.1:8000/api/admin/general`,{secret_key:this.SKey})
      .then(response => {
        console.log(response.data)
        this.disldInp = false
      })
      .catch(error=> {
        console.log(error.response.data)
      })
    },

    async fetchApiKey() {
      await axios.get(`http://127.0.0.1:8000/api/admin/general`)
      .then(response => {
        console.log(response)
        this.SKey = response.data.sec_key.secret_key
        console.log(this.SKey)
      }) 
      .catch(error => {
        console.log(error.response.data)
      })
    },

    async getAllData() {
      await axios.get('http://127.0.0.1:8000/api/admin/general/data')
      .then(response => {
        this.genData = response.data
        console.log(this.genData)
      })
      .catch(error => {
        console.log(error.response.data)
      })
    }
  }
}
</script>

<style>
.infoContainer {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(285px, 1fr));
  grid-gap: 20px;
}

:disabled {
  cursor: not-allowed;
    background-color: #fff;
    color: black;
}
.box {
  min-width: 250px;
}

.input-filters {
  display: flex;
  gap: 2px;
  margin: 40px 70px;
}

.input-filters input {
  margin: 0px 13px;
    display: flex;
    padding: 2px 10px;
    border-radius: 6px;
}

.btn {
  padding: 4px 8px;
}

.input {
  display: flex;
}

@media (max-width: 502px) {
  .input-filters {
    flex-direction: column;
  }
}
</style>