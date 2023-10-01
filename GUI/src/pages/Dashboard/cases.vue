<template > 
    <div class="bg-white caseContainer shadow-md rounded-md p-6 sm:container mx-auto mt-4">
      <h2 class="text-lg font-medium mb-4">Transacciones</h2>
      <section class="filter-cont">
        <section class="datePicker">
          <VueDatePicker :enable-time-picker="false" range v-model="date"></VueDatePicker>
        </section>
        <section class="own">
          <input type="checkbox" name="own" id="own" style="width: 20px; height: 20px;"  @change="this.own = !this.own;this.makeOwnProductsRequest()">
          <label for="own" style="font-size: 20px; margin: 0 10px;">Propios</label>   
        </section>
        <div class=" filter">
          <input v-model="searchTerm" id="searchInput" type="text" class="text-gray-600 border border-gray-300 searcher">
          <button class="btn" @click="searchData()"> 
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
              <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
          </button>
        </div>
      </section>

      
      <!--Table For desktop-->
      <table class="table-auto w-full tableCases" v-if="!isWindowSmall">
        <thead>
          <tr>
            <th class="px-4 py-2 text-center">Id</th>
            <th class="px-4 py-2 text-center">Fecha</th>
            <th class="px-4 py-2 text-center">Producto</th>
            <th class="px-4 py-2 text-center">Precio p/u</th>
            <th class="px-4 py-2 text-center">Cantidad</th>
            <th class="px-4 py-2 text-center">Total</th>
            <th class="px-4 py-2 text-center">Comprador</th>
            <th class="px-4 py-2 text-center">Vendedor</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transact in allTransacts" :key="transact.id">
            <td class="border px-4 py-2">{{ transact.id }}</td>
            <td class="border px-4 py-2">{{ transact.dateTransact }}</td>
            <td class="border px-4 py-2">{{ transact.product.name }}</td>
            <td class="border px-4 py-2">{{ transact.product.price }}</td>
            <td class="border px-4 py-2">{{ transact.quantity_asked }}</td>
            <td class="border px-4 py-2">{{ transact.total }}</td>
            <td class="border px-4 py-2">{{ transact.buyers.name }}</td>
            <td class="border px-4 py-2">{{ transact.product.store.seller.name }}</td>
          </tr>
        </tbody>
      </table>

      <!--Table for responsive-->
      <table style="border: 2px solid;margin: 39px auto;" class="table min-w-full border border-gray-300 responsive-table" v-if="isWindowSmall" v-for="transact in allTransacts" :key="transact.id">
      <tbody>
        <tr>
          <td class="py-2 px-4  border-b">Id</td>
          <td class="py-2 px-4 border-b">{{ transact.id }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Fecha</td>
          <td class="py-2 px-4 border-b">{{ transact.dateTransact }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Producto</td>
          <td class="py-2 px-4 border-b">{{ transact.product.name }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Precio</td>
          <td class="py-2 px-4 border-b">{{ transact.product.price }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Cantidad</td>
          <td class="py-2 px-4 border-b">{{ transact.quantity_asked}}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Total</td>
          <td class="py-2 px-4 border-b">{{ transact.total }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Comprador</td>
          <td class="py-2 px-4 border-b">{{ transact.buyers.name }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 border-b">Vendedores</td>
          <td class="py-2 px-4 border-b">{{ transact.product.store.seller.name }}</td>
        </tr>
      </tbody>
    </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import VueDatePicker from '@vuepic/vue-datepicker'
  import Cookies from 'js-cookie'
  import '@vuepic/vue-datepicker/dist/main.css'

  export default {

    watch: {
      date(newVal) {
        this.makeFilterwithData(newVal)
      }
    },
    components: {
      VueDatePicker
    },

    data() {
      return {
        own: false,
        date:null,
        isWindowSmall: false,
        allTransacts: [],
        dateInput:null,
        searchTerm:""
      }
    },
    created() {
      this.getTransacts()
      this.checkWindowSize()
      window.addEventListener('resize', this.checkWindowSize);
    },
    methods: {
      async makeOwnProductsRequest() {
        let url = ""
        if (this.own) {
          url= `http://127.0.0.1:8000/api/transacts/admin?own=t`
        } else {
          url = `http://127.0.0.1:8000/api/transacts/admin`
        }
        await  axios.get(url, {
        headers:{
          Authorization:`Token ${Cookies.get('token')}`
        }})
        .then(response => {
          this.allTransacts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      },

      async searchData() {
       if(this.searchTerm !="") {
        await axios.get(`http://127.0.0.1:8000/api/transacts/admin?sq=${this.searchTerm}`)
        .then(response => {
          this.allTransacts = response.data
        })
       } else {
        this.getTransacts()
       }
      },

      async makeFilterwithData(date) {
        if(date!=null) { 
          let startDate = date[0].toJSON()
          let endDate= date[1].toJSON()
          await axios.get(`http://127.0.0.1:8000/api/transacts/admin?dr_s=${startDate}&dr_e=${endDate}`)
          .then(response => {
            this.allTransacts = response.data
          })
        } else {
          this.getTransacts()
        }
      },

      async getTransacts() {
        await axios.get(`http://127.0.0.1:8000/api/transacts/admin?dr={}`)
        .then(response => {
          this.allTransacts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      },

    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 1020;
    },  
    }
  }
  </script>
  
  <style>
  @import './main.css';
  .table-auto {
    width: auto;
  }

  .filter {
    gap: 20px;
    flex-direction: row !important;
  }

  button{
    margin-top: 0px !important;
  }

  .btn {
    padding: 9px;
    border: solid 1px rgb(22, 22, 22);
    border-radius: 8px;
    transition: background-color 0.3s, border-color 0.3s;
  }

  .btn:hover {
    background-color: rgb(60, 122, 255);
    border-color:rgb(4, 4, 200) ;
    color: white;

  }

  .filter-cont {
    margin: 15px auto;
    display: flex;
    flex-direction: row;
    max-width: 1131px;
    justify-content: space-around;
  }

  .tableCases {
    margin: auto;
  }

  .caseContainer {
    margin-top: 40px;
  }

  .searcher {
    padding: 5px;
    height: 38px;
    border-radius:4px ;
  }


  </style>
  