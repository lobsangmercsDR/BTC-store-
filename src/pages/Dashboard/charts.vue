<template>
    <h1>si</h1>
    <section class="bar-container">
        <Bar :id="2" :data="this.chartData" :options="chartOptions"></Bar>
    </section>
    



</template>

<script>
import {Bar} from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    components:{
        Bar
    },

    data() {
    return{
    chartData: {
        labels: [ 'January', 'February', 'March','asd','asd','asds','asd' ],
        datasets: [ { data: [40, 20, 12],  backgroundColor:['rgba(54, 162, 235, 0.2)',] } ]
      },
      chartOptions: {
        responsive: true,
        aspectRatio:2
        
      }
    }
    }
}
</script>

<style>
.bar-container {
    max-width: 900px;
    display: center;
    align-self: center;
    margin: 10px auto;
}
.bar-container canvas {
    width: 100% !important;
    height: 100% !important;
}

@media (max-width:730px) {
    .bar-container {
        max-width: 550px;
    }
}
</style>