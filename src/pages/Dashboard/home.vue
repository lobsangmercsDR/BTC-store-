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
        <section class="input">
          <label for="key" style="align-self: center;">Key de cartera</label>
          <input type="text" id="key" name="key" v-model="SKey"  :disabled="this.disldInp">
        <button class="btn" @click="updateSecKey()" :disabled="this.disldInp">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-save" viewBox="0 0 16 16">
            <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1H2z"/>
          </svg>
        </button>
        </section>

        <section class="alw-checkboc">
          <input type="checkbox" name="" id="always" @change="makeAllRequest()">
          <label for="always">Siempre</label>
        </section>
        
        <section class="datefilter">
            <VueDatePicker v-model="selectedRange" :enable-time-picker="false" range max-range="7" @change="filtDate()"></VueDatePicker>
          </section>
      </div>
      <charts :dataobj="chartData"></charts>
      {{  }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'
import charts from './charts.vue'
import VueDatePicker from '@vuepic/vue-datepicker'

export default {
  components: {
    charts,
    VueDatePicker
  },

  watch: {
    selectedRange(newVal) {
    this.$nextTick(() => {
     this.filtDate(newVal)
    })
  }
  },
  data() {
    return {
      SKey:"", 
      disldInp: false,
      genData:{
        total_shares: 0,
        allData: false,
      },
      chartData: {
        labels:[]
      },
      selectedRange:[],
      chartAPIData:{}
    }
  },

  created() {
    this.fetchApiKey(),
    this.selectDefaultDate(),
    this.getAllData(),
    this.filtDate(),
    this.getChartData()
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
        this.SKey = response.data.sec_key.secret_key
      }) 
      .catch(error => {
        console.log(error.response.data)
      })
    },

    async getAllData(allData=false) {
      let url = ""
      if(allData ==false) {
        url = 'http://127.0.0.1:8000/api/admin/general/data'
      } else {
        url = `http://127.0.0.1:8000/api/admin/general/data?all=t`
      }
      await axios.get(url)
      .then(response => {
        this.genData = response.data
      })
      .catch(error => {
        console.log(error.response.data)
      })
    },

    makeAllRequest() {
      this.allData = !this.allData
      this.getAllData(this.allData)
    },  

    async filtDate(date) {
      if(date) {
        const currDate = new Date(date[0])
        let weekDays = ['Sabado','Domingo', 'Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
        let selectedWeekDays = []

        while(currDate <= date[1]) {
          currDate.setDate(currDate.getDate()+1)
          selectedWeekDays.push(weekDays[currDate.getDay()])
        }
        await this.getChartData()
        let datasets = this.chartAPIData
        this.chartData =  {labels:selectedWeekDays, datasets: datasets}
      } else {
        this.chartData = {labels:[]}
      }
    },

    selectDefaultDate() {
      const now = new Date()
      const actDate =  new Date(now.getFullYear(),now.getMonth(), now.getDate())
      let lateDate = new Date()
      lateDate.setDate(actDate.getDate() -6)
      lateDate = new Date(lateDate.getFullYear(), lateDate.getMonth(), lateDate.getDate())
      this.selectedRange = [lateDate, actDate]
    },

    async getChartData() {
      await axios.get(`http://127.0.0.1:8000/api/admin/general/graphics?stDate=${this.selectedRange[0].toJSON()}&edDate=${this.selectedRange[1].toJSON()}`)
      .then(response => {
        this.chartAPIData = response.data.result
      })
      .catch(error => {
        console.log(error.response.data)
      })
    }


  }
}
</script>

<style>
@import './main.css';

.alw-checkboc {
  display: flex;
}

.alw-checkboc input {
  width: 20px;
  margin: 0px 13px;
}

#always:focus {
 border: none;
 outline: none;
 box-shadow: none;
}
#always:active {
 border: none;
}

.alw-checkboc label {
  font-size: 17px;
  align-self: center;
}



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
  gap: 20px;
  margin: 40px 70px;
  justify-content: space-around;
}


.input input {
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

@media (max-width: 855px) {
  .input-filters {
    flex-direction: column;
  }

  #always {
    margin: 0px 13px 0px 0px;
  }

  .datefilter {
    max-width: 245px;
  }
}
</style>