<template>
    <div class="parent" ref="variable_container">
        <div class="div2">
            <!-- Table 2 -->
            <h1>Últimos productos digitales Vendidos</h1>
            <div class="component-container component-container-color2">
                <table class="table text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="" style="
                        background: rgb(122 0 160);
                        color: #fff;">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Tienda</th>
                            <th class="p-2">Fecha de Publicación</th>
                            <th class="p-2">Precio</th>

                        </tr>
                    </thead>
                    <tbody>
                        <tr v-if="transactsMaked.data" v-for="(product, index) in transactsMaked.data" :key="index"
                            class="bg-gray-200 digit-selled-item text-gray-700" @click="openModal(product.productDigit.id, 'digits')">
                            <td class="p-2">{{ product.productDigit.name }}</td> 
                            <td class="p-2">{{ product.productDigit.store.nameStore }}</td>
                            <td class="p-2 wid">{{ product.dateTransact }}</td>
                            <td class="p-2">{{ product.productDigit.price }}</td>
                        </tr>
                    </tbody>
                </table>
                <!-- Flechas  -->
                <section class="nav-arrowHV">
                    <span class="arrow-icon" @click="changePageSP" :style="{color:previousArrowColorSP}" name="previous-arrow">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                        </svg>
                    </span>
                    <span class="arrow-icon" @click="changePageSP" :style="{color:nextArrowColorSP}" name="next-arrow">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                        </svg>
                    </span>
                </section>
            </div>
        </div>
        <div class="div2 grid-limitada" style="width:840px;">
            <!-- Table 2 -->
            <h1>Methods</h1>
            <div  class="component-container component-container-color2">
                
                <div v-for="(product,index) in methodCreated" :key="index" class="method-item"> 
                    <img :src="'http://127.0.0.1:8000/api'+ product.image" alt="Product Image" class="product-table-img">
                    <section class="method-content">
                        <div class="title3 title">{{ product.name}}</div>
                        <div class="description">
                            <div class="FRow">
                                <div style="margin-top: -8px;">{{ product.dateCreated }}</div>
                                <div class="quantity_buy"><b>No. de compras:</b> {{ product.transacts_count }}</div>
                                <div class="price"><b>Precio:</b> {{ product.price }}</div>
                                <div class="tienda"><b>Tienda:</b> {{ product.store.nameStore }}</div>
                            </div>
                        </div>
                        <div class="quantity"><span>{{ product.description }}</span></div>
                        <div class="details"><button @click="openModal(product.id, 'method')" class="product-button">Comprar</button></div>
                    </section>
                        </div>
                <section class="nav-arrowHV">
            <span class="arrow-icon" @click="changePageSMP" name="previous-arrow">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </span>
                <span class="arrow_icon" @click="changePageSMP" name="next-arrow">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
            </span>
        </section>
            </div>
        </div>
        <div class="div1 grid-limitada" ref="container">
            <!-- Table 1 -->
            <h1>Últimos productos digitales agregados </h1>
            <div class="component-container component-container-color1">
                <table class="table  text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="" style="
                        background: rgb(122 0 160);
                        color: #fff;">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Agregada</th>
                            <th class="p-2">Fecha de Compra</th>
                            <th class="p-2">Precio</th>
                            <th class="p-2">Tienda</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(product, index) in productsAdded" :key="index"
                            class="bg-gray-200 digit-selled-item text-gray-700" @click="openModal(product.id, 'digits')">
                            <td class="w-1/4 p-2">{{ product.name }}</td>
                            <td class="p-2" style="width: 20px;">{{ product.orgQuantity }}</td>
                            <td class="p-2">{{ product.dateCreated }}</td>
                            <td class="p-2">{{ product.price }}</td>
                            <td class="w-1/4 p-2">{{ product.store.nameStore }}</td>
                        </tr>
                    </tbody>
                </table>
                <section class="nav-arrowHV">
            <span class="arrow-icon" :style="{color:previousArrowColor}" name="previous-arrow" @click="changePageAP">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </span>
                <span class="arrow-icon" @click="changePageAP" :style="{color: nextArrowColor}" name="next-arrow">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
            </span>
        </section>
            </div>
        </div>





        


    </div>
    <div class="PF-slideshow">
            <section id="header_icons">
                <h1 style="flex-grow: 1;">Ultimos Productos Fisicos vendidos</h1>
                <span class="arrow-icon" @click="changePageSlP" :style="{color: previousArrowColorSlP}" name="previous-arrow">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </span>
                <span  @click="changePageSlP" name="next-arrow" :style="{color: nextArrowColorSlP}">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
                </span>
            </section>
            <div class="slider-container hidden md:block" id="slideshow" >
                    <div v-for="(product, index) in displayedProductsTableSlider()" :key="index" class="slider-item">
                        <div class="product-info">
                            <div class="product-image">
                                <img :src="'http://127.0.0.1:8000/api'+product.image" alt="Product Image">
                            </div>
                            <h4 class="product-name">{{ product.name }}</h4>
                            <p class="product-price">$ {{ product.price }}</p>
                            <p>Tienda: <b> {{ product.store.nameStore }} </b></p>
                            <button class="product-button-slide" @click="openModal(product.id, 'fisic')">Go to Product</button>
                        </div>
                    </div>
            </div>
    </div>
    <div>
        <SingleProduct :modalInfo="modalData"></SingleProduct>
        <SingleDigitalProduct :modalInfo="modalData"> </SingleDigitalProduct>
    </div>
</template>


<script>
import axios from 'axios';
import SingleProduct from '@/components/SingleProduct.vue'
import SingleDigitalProduct from './SingleDigitalProduct.vue';
import Cookies from 'js-cookie'


export default {
    components: {
        SingleProduct,
        SingleDigitalProduct
    },
    data() {
        return {
            modalData: null,
            pagesFisic: 5,
            heightContainer: 0,
            showModal1: false,
            showModal2: false,
            currentSlide:0,
            productsAdded: [],
            transactsMaked: [],
            productsSlider: [],
            methodCreated: [],
            pageInfoMP: {
                actualPage: 1, 
                available_page: 0
            },
            pageInfo: {
                actualPage: 1,
                available_page:0
            },
            pageInfoSP: {
                actualPage: 1, 
                available_page: 0
            },
            pageInfoSlP: {
                actualPage: 1, 
                available_page: 0
            },

            sliderOptions: {
                infinite: true,
                slidesToShow: 4,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed: 3000,
                dots: true,
                initialSlide: 0,
            },
            sliderOptions1: {
                infinite: true,
                slidesToShow: 4,
                slidesToScroll: 4,
                autoplay: false,
                autoplaySpeed: 3000,
                dots: true,
                initialSlide: 0,
                responsive: [{
                    breakpoint:809,
                    settings: {
                        infinite: true,
                        slidesToShow: 5,
                        slidesToScroll: 4,

                    }
            }]      
            },

            productsTable2: [],
        }
    },
    created() {
        this.getLast24HProducts();
        // setInterval(() => {
        //     this.getLast24HProducts(this.pageInfo.actualPage) 
        // }, 2000);
        this.getLast24HTransacts();
        this.displayedProductsTable2();
        this.displayedProductsTable1_5();
        this.getLast24HFisicProducts();
        this.getLast24HMethods();
    },
    mounted() {
        this.adaptTableHeight();
    },
    computed: {
        previousArrowColor() {
            const page = this.pageInfo.actualPage;
            if (page === 1) {
                return '#c2c2c2'; 
            } else {
                return ''; 
            }
        },
        previousArrowColorSP() {
            const page = this.pageInfoSP.actualPage;
            if (page === 1) {
                return '#c2c2c2'; 
            } else {
                return ''; 
            }
        },
        previousArrowColorSlP() {
            const page = this.pageInfoSlP.actualPage;
            if (page === 1) {
                return '#b2b2b2'; 
            } else {
                return ''; 
            }
        },
        nextArrowColor() {
            const pageNext = this.pageInfo.available_page
            if (pageNext == 0) {
                return '#c2c2c2'
            } else {
                return ''
            }
        },

        //responsive design

        nextArrowColorSP() {
            const pageNext = this.pageInfoSP.available_page
            if (pageNext == 0) {
                return '#c2c2c2'
            } else {
                return ''
            }
        },
        nextArrowColorSlP() {
            const pageNext = this.pageInfoSlP.available_page
            if (pageNext == 0) {
                return '#b2b2b2'
            } else {
                return ''
            }
        }
    },

    mounted() {
        this.handleResize()
    },




    methods: {
    handleResize() {
        const sizeScr = window.innerWidth;
        this.pagesFisic = (sizeScr < 768) ? 1 : 5 
    },

        async adaptTableHeight() {
           this.heightContainer = this.$refs.variable_container.offsetHeight
        },


        openModal(id, type) {
            if(type == "digits") {
                console.log(id);
                this.modalData = {showDigitModal: true,typeProd: type, objID: id }
            } else {
                console.log(id);
                this.modalData = {showFisicModal: true,typeProd: type, objID: id }
            }
            
        },


        async getLast24HProducts(page=1) {
            await axios.get(`http://127.0.0.1:8000/api/productos/digit?page=${page}`)
            .then(response => {
                this.productsAdded = response.data.data
                this.pageInfo.available_page = response.data.available_pages;
                this.pageInfo.actualPage = response.data.page;
            })
            .catch(error => {
                console.log(error.response.data)
            })
        },

        async getLast24HFisicProducts(page=1) {
            await axios.get(`http://127.0.0.1:8000/api/productos?page=${page}&p_size=${this.pagesFisic}`)
            .then(response => {
                this.pageInfoSlP.actualPage = response.data.actual_page
                this.pageInfoSlP.available_page = response.data.available_pages
                this.productsSlider  = response.data.data
            })
            .catch(error=> {
                console.log(error.response.data);
            })
        },

        async getLast24HMethods(page=1) {
            await axios.get(`http://127.0.0.1:8000/api/productos/methods?page=${page}`)
            .then(response => {
                this.methodCreated = response.data.data
                this.pageInfoMP.actualPage = response.data.actual_page
                this.pageInfoMP.available_page = response.data.available_pages
            })
            .catch(error => {
                console.log(error)
            })
        },

        async getLast24HTransacts(page=1) { 
            await axios.get(`http://127.0.0.1:8000/api/transacts?digitals=true&page=${page}`)
            .then(response => {
                this.transactsMaked = response.data 
                this.pageInfoSP.available_page = response.data.available_pages;
                this.pageInfoSP.actualPage = response.data.actual_page;
            })
            .catch(error => {
                console.log(error)
            })
        },

        async changePageAP(event) {
            const direction_arrow = event.currentTarget.getAttribute('name')
            if (direction_arrow == "previous-arrow") {
                let page = this.pageInfo.actualPage
                if(page > 1) {
                    this.getLast24HProducts(page-1)
                }
            } else {
                let page = this.pageInfo.actualPage + 1
                let validator = true
                if (validator == true) {
                    this.getLast24HProducts(page)
                }
            }
        },

        async changePageMP(event) {
            const direction_arrow = event.currentTarget.getAttribute('name')
            if (direction_arrow == "previous-arrow") {
                let page = this.pageInfo.actualPage
                if(page > 1) {
                    this.getLast24HProducts(page-1)
                }
            } else {
                let page = this.pageInfo.actualPage + 1
                let validator = true
                if (validator == true) {
                    this.getLast24HProducts(page)
                }
            }
        },

        async changePageSP(event) {
            const direction_arrow = event.currentTarget.getAttribute('name')
            console.log(direction_arrow);
            if (direction_arrow == "previous-arrow") {
                let page = this.pageInfoSP.actualPage
                if(page > 1) {
                    this.getLast24HTransacts(page-1)
                }
            } else {

                if(this.pageInfoSP.available_page != 0) {

                
                let page = this.pageInfoSP.actualPage + 1

                let validator = true
                if (validator == true) {
                    this.getLast24HTransacts(page)
                }
            }
            }

        },

        async changePageSMP(event) {
            const direction_arrow = event.currentTarget.getAttribute('name')
            console.log(direction_arrow);
            console.log(this.pageInfoMP)
            if (direction_arrow == "previous-arrow") {
                let page = this.pageInfoMP.actualPage
                console.log(page);
                if(page > 1) {
                    this.getLast24HMethods(page-1)
                }
            } else {

                if(this.pageInfoMP.available_page != 0) {

                
                let page = this.pageInfoMP.actualPage + 1

                let validator = true
                if (validator == true) {
                    this.getLast24HMethods(page)
                }
            }
            }

        },

        async changePageSlP(event) {
            const direction_arrow = event.currentTarget.getAttribute('name')
            let page = this.pageInfoSlP.actualPage
            if (direction_arrow == "previous-arrow") {
                
                if(page > 1) {
                    this.getLast24HFisicProducts(page-1)
                }
            } else {

                if(this.pageInfoSlP.available_page != 0) {

                let page = this.pageInfoSlP.actualPage + 1

                let validator = true
                if (validator == true) {
                    this.getLast24HFisicProducts(page)
                }
            }
            }
        },
        displayedProductsTable2() {

            return this.productsTable2.slice(0, 12);
        },

        displayedProductsTableSlider() {
            return this.productsSlider.slice(0, 5);
        },

        displayedProductsTable1_5() {
            return this.productsTable2.slice(0, 5);
        },

        handleAfterChange(currentSlide) {
            console.log(currentSlide)
            if (currentSlide === this.productsSlider.length - 5) {
                this.$refs.agile.goTo(0)
            }
        },
        openModal1() {
            this.showModal1 = true;
        },
        openModal2() {
            this.showModal2 = true;
        },
        closeModal1() {
            this.showModal1 = false;
        },
        closeModal2() {
            this.showModal2 = false;
        },
        goToPage(page) {
            if (page >= 1 && page <= this.totalPages) {
                this.currentPage = page;
            }
        },

    }
}
</script>
  
<style>


@media (max-width: 768px) {
    .parent {
        flex-direction: column;
        align-items: center !important;
    }


    .method-item .method-content {
        display: block;
    }
    .method-content .description {
        display: none;
    }
    .method-item {
        flex-direction: column;
        max-width: 500px;
    }
    .component-container-color1 {
        height: auto !important;
    }

    .title {
        margin-top: 15px !important;
        text-align: center  !important;
    }

    .component-container-color2 {
        max-width: 500px;
        margin: auto;
        height: auto !important;
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
  
}

@media (min-width: 1025px) {
  /* Estilos para pantallas de escritorio */
}

.parent {
    margin-top: 85px;
    padding: 0;
    display: flex;
    justify-content: space-between;
    gap: 40px;
    align-items: flex-start;
    
}

.PF-slideshow{
    max-width: 1330px;
    margin: auto;
    margin-top: 30px;
    margin-bottom: 30px;
}

.nav-arrows:hover {
    cursor: pointer;
}

#header_icons {
    display: flex;
}

.method-content {
    display: grid; 
    grid-auto-columns: 1fr; 
    grid-template-columns: 1.5fr 1fr 1fr; 
    grid-template-rows: 0.3fr 0.09fr; 
    gap: 0px 0px; 
    grid-template-areas: 
    "title title title"
    "description qunatity details";
}


/* Estilos para dispositivos móviles */

.nav-arrowHV {
    display: flex;
    justify-content: center;
    margin-top: auto;
}

.description {
display: flex;
margin: 0px 0px 0px 25px;
text-align: left;
grid-area: description;
}

.description .title3 {
   justify-content: flex-start;

}

.quantity {
    word-wrap: break-word;
    width: 190px;
    margin: 10px;
    grid-area: qunatity
}

.details {
    flex-grow: 1;
    grid-area: details;
}




.FRow {
justify-content: flex-start;
}

.title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 0 !important;
    grid-area: title;
    text-align: left;
    margin: 0px 25px;
}
/* Estilos para tabletas */
@media (min-width: 769px) and (max-width: 1024px) {
  .parent {
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(6, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px;
  }
  @media (max-width: 767px) {
  .hide-on-mobile {
    display: none;
  }
}



  .div1 {
    grid-area: 1 / 1 / 3 / 2;
  }

  .div2 {
    grid-area: 1 / 2 / 3 / 4;
  }

  .div3,
  .PF-slideshow {
    grid-area: auto;
  }

  .div5 {
    grid-area: 3 / 1 / 7 / 4;
  }
}


.component-container {
    padding: 5px;
    border-radius: 8px;
    text-align: center;
    display: flex;
    flex-direction: column;

}

.quant-num {
    font-size: 40px;
    font-weight: bold;
    padding: 0;
    margin: -10px
}

.wid {
    width: 150px;
}

.component-container-color1 {
    background-color: #ab16be;
    color: white;
    height: 100%;
    min-height: 970px; 
    min-width: 500px;
}

.component-container-color2 {
    background-color: #ab16be;
    color: white;
    min-height: 1022px;
    max-height: 1022px;
    overflow:auto; 
    min-width: 500px;
}

.slider-container {
    height: 100%;
    overflow: hidden;
    margin: auto;
    max-width: 1365px;
    display: flex;
}

#slideshow {
    display: flex;
}

.slider-items-wrapper {
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    margin: -10px;
    overflow: auto;
}


.slider-item {
    height: 320px;
    width: 254px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
    transition: transform 0.3s ease;
    overflow: hidden;
    box-sizing: border-box;
    flex-shrink: 0;
}

/* .digit-selled-item:hover {
    transform: scale(1.002);
} */


.method-item {

    color: black;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 20px;
    margin: 19px;
    transition: transform 0.3s ease;
    overflow: hidden;
    box-sizing: border-box;
    flex-shrink: 0;
    justify-content: flex-start;
    /* transform: sca; */
}

.method-item:hover {
    transform: scale(1.02);
    background-color: rgb(255, 255, 255);
}


.product-table-img {
    border-radius: 15px;
    width: 160px;
    height: 125px;
}

.digit-selled-item:hover {
    transform: scale(1);
    background-color: rgb(255, 253, 253);
    transition: background-color 0.12s ease-in-out;
    cursor: pointer;
}

.slider-item:hover {
    transform: scale(1.02);
}

.product-info {
    text-align: center;
    position: relative;
}

.product-image img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
}

.product-name {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
    margin-bottom: 5px;
}
.div6 {
  display: none;
}

.product-price {
    font-size: 14px;
    margin-bottom: 10px;
}

.product-button {
    background-color: #570b60;
    color: #fff;
    border: none;
    padding: 8px 16px;
    font-weight: bold;
    font-size: 16px;
    border-radius: 20px;
    cursor: pointer;
}

.product-button-slide {
    background-color: #fff;
    color: #333;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
}

.product-button:hover {
    transform: scale(1.05);
    background-color: #9a15ac;
}

.table {
    border-spacing: 0 10px;
    width: 100%;
    height: 100%;
}

.table tr {
    border-radius: 4px;
}

.bg-gray-200 {
    background-color: rgba(255, 255, 255, 0.8);
}

.news-section {
    padding: 1rem;
    background-color: #f5f5f5;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.news-section-title {
    color: #ab16be;
    font-size: 24px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
}

.news-item {
    margin-bottom: 20px;
}

.news-title {
    color: #333;
    font-size: 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}

.news-description {
    color: #777;
    font-size: 16px;
    margin-bottom: 0;
}








.modal {
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 90%;
    max-height: 80%;
    overflow-y: auto;
}

.modal-close {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 24px;
    color: #888;
    cursor: pointer;
}

.pagination {
    margin-top: 10px;
}

.pagination-button {
    background-color: #fff;
    color: #333;
    border: none;
    padding: 5px 10px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-right: 5px;
}

.pagination-button.active {
    background-color: #ccc;
}



</style>
  