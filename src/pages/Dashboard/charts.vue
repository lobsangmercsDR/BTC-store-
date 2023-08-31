<template>
    <section class="bar-container">
        <Bar :id="bar" :data="chartData" :options="this.chartOptions" ref="bar"></Bar>
    </section>

</template>

<script>
import {Bar} from 'vue-chartjs'
import VueCharts from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend,BarElement, CategoryScale, LinearScale } from 'chart.js'
import { mdiTagHidden } from '@mdi/js'

ChartJS.register(Title, Tooltip, BarElement, Legend,CategoryScale, LinearScale)

export default {
    
    props:{
        dataobj:Object
    },  


    watch: {
        dataobj(nv) {
            console.log(nv)
            this.$nextTick(() => {
                console.log(nv)
                this.chartData =
                {
                    labels: nv.labels,
                    datasets: [
                        {
                            label: 'Ventas totales',
                            backgroundColor: '#3498db',
                            data: nv.datasets.total_shares
                        },
                        {
                            label: 'Productos vendidos',
                            backgroundColor: '#2ecc71',
                            data: nv.datasets.total_cnt_shares
                        },
                        {
                            label: 'Usuarios registrados',
                            backgroundColor: '#e74c3c',
                            data: nv.datasets.total_users
                        }
                    ]
                } 
                
            })


        }
    },

    computed: {

        chartData() {
            console.log(this.chartData)
            return this.chartData
        }
    },

    data() {
        return {
            chartData: {
                labels: [],
                datasets: [
                {
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    data: [40, 20, 12]
                }]
            },
            
            chartOptions: {
                responsive: true,
                aspectRatio:2,
                legend: {
                    display: false
                }
            }
        }
    },

    computed: {
        chartData() {
            return this.chartData
        },
    },


    methods: {
    removeComponent() {
            this.chartData.labels  = []

      const targetElement = document.getElementById('bar');
      
      // Verificar si el elemento objetivo existe
      if (targetElement) {
        // Eliminar el elemento objetivo
        targetElement.parentNode.removeChild(targetElement);
      }
    }

    },

    components:{
        Bar
    },
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