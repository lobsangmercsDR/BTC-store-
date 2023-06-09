<template>
    <div class="parent">
        <div class="div1 grid-limitada">
            <!-- Table 1 -->
            <h1>Últimos productos digitales agregados</h1>
            <div class="component-container component-container-color1">
                <table class="table text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="" style="
                        background: #c65a03;
                        color: #fff;
                    ">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Comprada</th>
                            <th class="p-2">Fecha de Compra</th>
                            <th class="p-2">Precio</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(product, index) in displayedProductsTable1" :key="index"
                            class="bg-gray-200 text-gray-700">
                            <td class="p-2">{{ product.name }}</td>
                            <td class="p-2">{{ product.quantitySold }}</td>
                            <td class="p-2">{{ product.dateSold }}</td>
                            <td class="p-2">{{ product.price }}</td>
                        </tr>
                    </tbody>
                </table>
                <section class="nav-arrows">
            <md-icon class="arrow-icon" @click="previousSlide">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </md-icon>
                <md-icon>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
            </md-icon>
        </section>
            </div>
        </div>
        <div class="div2 grid-limitada" style="width:840px;">
            <!-- Table 2 -->
            <h1>Methods</h1>
            <div class="component-container component-container-color2">
                
                <div v-for="(product,index) in displayedProductsTable1_5" :key="index" class="method-item"> 
                    <img :src="'https://picsum.photos/150/150?random=' + index" alt="Product Image" class="product-table-img">
                    <!-- <div class="description">
                    <span>{{ product.name }}</span>
                    <p>{{ product.price }}</p>
                    <p> {{ product.quantityAvailable }}</p>
                    <p> {{ product.datePublished }}</p>   
                    <p>{{ product.user }}</p>
                    </div> -->
                </div>
                <!-- <table class="table text-gray-400 border-separate space-y-4 text-sm">
                     <thead class="bg-gray-800 text-gray-500">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Disponibles</th>
                            <th class="p-2">Fecha de Publicación</th>
                            <th class="p-2">Precio</th>
                        </tr>
                    </thead> 
                    <tbody>
                        <tr v-for="(product, index) in displayedProductsTable1_5" :key="index"
                            class="bg-gray-200 text-gray-700">
                            <td class="p-2">{{ product.name }}</td>
                            <td class="p-2">{{ product.quantityAvailable }}</td>
                            <td class="p-2">{{ product.datePublished }}</td>
                            <td class="p-2">{{ product.price }}</td>

                        </tr>
                    </tbody>
                </table> -->
                <section class="nav-arrows">
            <md-icon class="arrow-icon" @click="previousSlide">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </md-icon>
                <md-icon>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
            </md-icon>
        </section>
            </div>
        </div>





        <div class="div2">
            <!-- Table 2 -->
            <h1>Últimos productos digitales Vendidos</h1>
            <div class="component-container component-container-color2">
                <table class="table text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="" style="
                        background: rgb(122 0 160);
                        color: #fff;
                    ">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Disponibles</th>
                            <th class="p-2">Fecha de Publicación</th>
                            <th class="p-2">Precio</th>

                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(product, index) in displayedProductsTable2" :key="index"
                            class="bg-gray-200 text-gray-700">
                            <td class="p-2">{{ product.name }}</td>
                            <td class="p-2">{{ product.quantityAvailable }}</td>
                            <td class="p-2">{{ product.datePublished }}</td>
                            <td class="p-2">{{ product.price }}</td>
                        </tr>
                    </tbody>
                </table>
                <section class="nav-arrows">
            <md-icon class="arrow-icon" @click="previousSlide">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </md-icon>
                <md-icon>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
            </md-icon>
        </section>
            </div>
        </div>


    </div>
    <div class="div4">
            <section id="header_icons">
                <h1 style="flex-grow: 1;">Ultimos Productos Fisicos vendidos</h1>
                <md-icon class="arrow-icon" @click="previousSlide">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                </md-icon>
                <md-icon>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
                </md-icon>
            </section>
            <div class="slider-container hidden md:block" id="slideshow" >
                    <div v-for="(product, index) in productsSlider" :key="index" class="slider-item">
                        <div class="product-info">
                            <div class="product-image">
                                <img :src="'https://picsum.photos/150/150?random=' + index" alt="Product Image">
                            </div>
                            <h4 class="product-name">{{ product.name }}</h4>
                            <p class="product-price">$ {{ product.price }}</p>
                            <p>Comprado por:</p>
                            <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
                        </div>
                    </div>
            </div>
    </div>







<!-- 
  
    <div v-if="showModal1" class="modal">
        <div class="modal-content">
            <span class="close-button" @click="closeModal1">&times;</span>
            <h2>Detalles del producto</h2>
            <table class="table text-gray-400 border-separate space-y-4 text-sm">
                <thead class="bg-gray-800 text-gray-500">
                    <tr>
                        <th class="p-2">Producto</th>
                        <th class="p-2">Cantidad Comprada</th>
                        <th class="p-2">Fecha de Compra</th>
                        <th class="p-2">Precio</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(product, index) in productsTable1" :key="index" class="bg-gray-200 text-gray-700">
                        <td class="p-2">{{ product.name }}</td>
                        <td class="p-2">{{ product.quantitySold }}</td>
                        <td class="p-2">{{ product.dateSold }}</td>
                        <td class="p-2">{{ product.price }}</td>
                    </tr>
                </tbody>
            </table>
            <button class="modal-close" @click="closeModal1">Cerrar</button>
        </div>
    </div>


    <div v-if="showModal2" class="modal">
        <div class="modal-content">
            <span class="close-button" @click="closeModal2">&times;</span>
            <h2>Detalles del producto</h2>
            <table class="table text-gray-400 border-separate space-y-4 text-sm">
                <thead class="bg-gray-800 text-gray-500">
                    <tr>
                        <th class="p-2">Producto</th>
                        <th class="p-2">Cantidad Disponibles</th>
                        <th class="p-2">Fecha de Publicación</th>
                        <th class="p-2">Precio</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(product, index) in productsTable2" :key="index" class="bg-gray-200 text-gray-700">
                        <td class="p-2">{{ product.name }}</td>
                        <td class="p-2">{{ product.quantityAvailable }}</td>
                        <td class="p-2">{{ product.datePublished }}</td>
                        <td class="p-2">{{ product.price }}</td>
                    </tr>
                </tbody>
            </table>
            <button class="modal-close" @click="closeModal2">Cerrar</button>
        </div>
    </div> -->
</template>
  
<script>


export default {
    data() {
        return {
            showModal1: false,
            showModal2: false,
            currentSlide:0,

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
            productsTable1: [
                // Aquí van los datos de la tabla 1
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 2", quantitySold: 5, dateSold: "2023-05-18", price: 50 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                // Agrega más productos según tus necesidades
            ],
            productsTable2: [
                // Aquí van los datos de la tabla 2
                { name: "Producto A", quantityAvailable: 20, datePublished: "2023-05-15", price: 200, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin"},
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin"},
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80 , user:"Admin"},
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80, user:"Admin" },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80 , user:"Admin"},
                
                // Agrega más productos según tus necesidades
            ],
            productsSlider: [
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                // { id: 2, name: 'Product Slider 2', price: '180', image: 'product2.jpg' },
                // { id: 3, name: 'Product Slider 3', price: '120', image: 'product3.jpg' },
                // { id: 4, name: 'Product Slider 4', price: '300', image: 'product4.jpg' },
                // { id: 5, name: 'Product Slider 5', price: '220', image: 'product5.jpg' },
                // { id: 6, name: 'Product Slider 6', price: '150', image: 'product6.jpg' },
            ],
        }
    },
    computed: {
        displayedProductsTable1() {
            return this.productsTable1.slice(0, 12);
        },
        displayedProductsTable2() {
            return this.productsTable2.slice(0, 12);
        },
        displayedProductsTable1_5() {
            return this.productsTable2.slice(0, 5);
        },

        totalPages() {
            return Math.ceil(this.productsTable2.length / this.productsPerPage);
        },
    },
    methods: {
        goToProduct(productId) {
            this.$router.push({ name: 'Product', params: { id: productId } })
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
.parent {
    margin-top: 85px;
    padding: 0;
    display: flex;
    justify-content: space-between;
    gap: 40px;
    /* display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(0, 1fr);
    grid-auto-rows: minmax(1, 1fr);
    grid-column-gap: 30px;
    grid-row-gap: 0px; */
    align-items: start;
    
}

#header_icons {
    display: flex;
}

.div3 {
    grid-area: 1 / 2 / 3 / 5;
    align-self: start;
    overflow: hidden;
}

.div4 {
    grid-area: 2 / 2 / 3 / 5;
    align-self: start;
    overflow: hidden;
    max-width: 1365px;
    margin: auto;
    margin-top: 45px;
}

.div5 {
    grid-area: 1 / 5 / 4 / 6;
}

/* Estilos para dispositivos móviles */
@media (max-width: 768px) {
  .parent {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-column-gap: 10px;
    grid-row-gap: 20px;
  }

  .div1 {
    grid-area: 1 / 1 / 3 / 3;
  }

  .div2 {
    grid-area: 3 / 1 / 5 / 3;
  }

  .div3,
  .div4 {
    grid-area: auto;
  }

  .div5 {
    grid-area: 5 / 1 / 9 / 3;
  }
}

.nav-arrows {
    display: flex;
    justify-content: center;
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
  .div4 {
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
}

.component-container-color1 {
    background-color: #f66305;
    color: white;
    height: 100%;
}

.component-container-color2 {
    background-color: #ab16be;
    color: white;
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


.method-item {
    height: 110px;
    color: black;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f8f8f8;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 20px;
    margin: 20px 15px;
    transition: transform 0.3s ease;
    overflow: hidden;
    box-sizing: border-box;
    flex-shrink: 0;
    justify-content: space-between;
}

.product-table-img {
    border-radius: 15px;
    width: 160px;
    height: 100px;
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
    background-color: #fff;
    color: #333;
    border: none;
    padding: 8px 16px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
}

.product-button:hover {
    background-color: #eee;
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
  