<template>
    <div class="parent">
        <div class="div1">
            <!-- Table 1 -->
            <h1>Últimos productos digitales agregados</h1>
            <div class="component-container component-container-color1">
                <table class="table text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="bg-gray-800 text-gray-500">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Comprada</th>
                            <th class="p-2">Fecha de Compra</th>
                            <th class="p-2">Precio</th>
                            <th class="p-2">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(product, index) in productsTable1" :key="index" class="bg-gray-200 text-gray-700">
                            <td class="p-2">{{ product.name }}</td>
                            <td class="p-2">{{ product.quantitySold }}</td>
                            <td class="p-2">{{ product.dateSold }}</td>
                            <td class="p-2">{{ product.price }}</td>
                            <td class="p-2">
                                
                            </td>
                        </tr>
                    </tbody>
                    <button class="table-button" @click="openModal1()">Ver Más</button>
                </table>
            </div>
        </div>
        <div class="div2">
            <!-- Table 2 -->
            <h1>Últimos productos digitales Vendidos</h1>
            <div class="component-container component-container-color2">
                <table class="table text-gray-400 border-separate space-y-4 text-sm">
                    <thead class="bg-gray-800 text-gray-500">
                        <tr>
                            <th class="p-2">Producto</th>
                            <th class="p-2">Cantidad Disponibles</th>
                            <th class="p-2">Fecha de Publicación</th>
                            <th class="p-2">Precio</th>
                            <th class="p-2">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(product, index) in productsTable2" :key="index" class="bg-gray-200 text-gray-700">
                            <td class="p-2">{{ product.name }}</td>
                            <td class="p-2">{{ product.quantityAvailable }}</td>
                            <td class="p-2">{{ product.datePublished }}</td>
                            <td class="p-2">{{ product.price }}</td>
                            <td class="p-2">
                                <button class="table-button" @click="openModal2(product)">Ver Más</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>









        <div class="div3">
            <h1>Ultimos productos Fisicos agregados</h1>

            <!-- Slider -->
            <div class="slider-container">
                <agile :options="sliderOptions" @afterChange="handleAfterChange" ref="agile">
                    <div v-for="(product, index) in productsSlider" :key="index" class="slider-item">
                        <div class="product-info">
                            <div class="product-image">
                                <img :src="product.image" alt="Product Image">
                            </div>
                            <h4 class="product-name">{{ product.name }}</h4>
                            <p class="product-price">$ {{ product.price }}</p>
                            <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
                        </div>
                    </div>
                </agile>
            </div>
        </div>
        <div class="div4">
            <h1>Productos Fisicos mas vendidos</h1>

            <div class="slider-container">
                <agile :options="sliderOptions1" @afterChange="handleAfterChange" ref="agile">
                    <div v-for="(product, index) in productsSlider" :key="index" class="slider-item">
                        <div class="product-info">
                            <div class="product-image">
                                <img :src="product.image" alt="Product Image">
                            </div>
                            <h4 class="product-name">{{ product.name }}</h4>
                            <p class="product-price">$ {{ product.price }}</p>
                            <button class="product-button" @click="goToProduct(product.id)">Go to Product</button>
                        </div>
                    </div>
                </agile>
            </div>
        </div>
        <div class="div5">
            <div class="component-container component-container-color1">
                <div class="news-section">
                    <h2 class="news-section-title">Noticias y Actualizaciones</h2>
                    <div class="news-item">
                        <h3 class="news-title">Título de la Noticia 1</h3>
                        <p class="news-description">Descripción de la Noticia 1</p>
                    </div>
                    <div class="news-item">
                        <h3 class="news-title">Título de la Noticia 2</h3>
                        <p class="news-description">Descripción de la Noticia 2</p>
                    </div>
                    <div class="news-item">
                        <h3 class="news-title">Título de la Noticia 3</h3>
                        <p class="news-description">Descripción de la Noticia 3</p>
                    </div>
                    <div class="news-item">
                        <h3 class="news-title">Título de la Noticia 4</h3>
                        <p class="news-description">Descripción de la Noticia 4</p>
                    </div>
                    <div class="news-item">
                        <h3 class="news-title">Título de la Noticia 5</h3>
                        <p class="news-description">Descripción de la Noticia 5</p>
                    </div>
                </div>

            </div>
        </div>




        <div class="div6">
        </div>
    </div>

     <!-- Modal 1 -->
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
          <tr class="bg-gray-200 text-gray-700">
            <td class="p-2">{{ selectedProduct.name }}</td>
            <td class="p-2">{{ selectedProduct.quantitySold }}</td>
            <td class="p-2">{{ selectedProduct.dateSold }}</td>
            <td class="p-2">{{ selectedProduct.price }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Modal 2 -->
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
          <tr class="bg-gray-200 text-gray-700">
            <td class="p-2">{{ selectedProduct.name }}</td>
            <td class="p-2">{{ selectedProduct.quantityAvailable }}</td>
            <td class="p-2">{{ selectedProduct.datePublished }}</td>
            <td class="p-2">{{ selectedProduct.price }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

   
   
</template>
  
<script>
import { VueAgile } from 'vue-agile'

export default {
    components: {
        'agile': VueAgile,
    },
    data() {
        return {
            showModal1: false,
            showProductTable: false,
            
            showModal2: false,
            selectedProduct: null,


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
                slidesToScroll: -1,
                autoplay: true,
                autoplaySpeed: 3000,
                dots: true,
                initialSlide: 0,
            },
            productsTable1: [
                // Aquí van los datos de la tabla 1
                { name: "Producto 1", quantitySold: 10, dateSold: "2023-05-20", price: 100 },
                { name: "Producto 2", quantitySold: 5, dateSold: "2023-05-18", price: 50 },
                // Agrega más productos según tus necesidades
            ],
            productsTable2: [
                // Aquí van los datos de la tabla 2
                { name: "Producto A", quantityAvailable: 20, datePublished: "2023-05-15", price: 200 },
                { name: "Producto B", quantityAvailable: 8, datePublished: "2023-05-12", price: 80 },
                // Agrega más productos según tus necesidades
            ],
            productsSlider: [
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 1, name: 'Product Slider 1', price: '250', image: 'product1.jpg' },
                { id: 2, name: 'Product Slider 2', price: '180', image: 'product2.jpg' },
                { id: 3, name: 'Product Slider 3', price: '120', image: 'product3.jpg' },
                { id: 4, name: 'Product Slider 4', price: '300', image: 'product4.jpg' },
                { id: 5, name: 'Product Slider 5', price: '220', image: 'product5.jpg' },
                { id: 6, name: 'Product Slider 6', price: '150', image: 'product6.jpg' },
            ],
        }
    },
    methods: {
        goToProduct(productId) {
            this.$router.push({ name: 'Product', params: { id: productId } })
        },
        handleAfterChange(currentSlide) {
            if (currentSlide === this.productsSlider.length - 1) {
                this.$refs.agile.goTo(0)
            }
        },
        openModal1(product) {
            this.showModal1 = true;
            // Obtén los productos de la tabla correspondiente
            this.productsTable1 = this.getProductsForTable1(product);
        },
        closeModal1() {
            this.showModal1 = false;
            // Limpia los datos de la tabla en el modal al cerrarlo
            this.productsTable1 = [];
        },
        getProductsForTable1(product) {
            // Lógica para obtener los productos de la tabla correspondiente
            // Puedes realizar alguna filtración o consulta según tus necesidades
            // En este ejemplo, simplemente retornamos todos los productos
            return this.products;
        },

    }
}
</script>
  
<style>
.parent {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(5, 1fr);
    grid-column-gap: 30px;
    grid-row-gap: 0px;
    align-items: start;
}

.div1 {
    grid-area: 1 / 1 / 2 /1;
}

.div2 {
    grid-area: 2 / 1 / 3 / 2;
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
}

.div5 {
    grid-area: 1 / 5 / 4 / 6;
}


.component-container {
    padding: 10px;
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
}

.slider-items-wrapper {
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    margin: -10px;
}

.slider-item {
    height: 220px;
    width: 180px;
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
}

.slider-item:hover {
    transform: scale(1.02);
}

.product-info {
    text-align: center;
}

.product-image img {
    width: 100%;
    max-height: 120px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
}

.product-name {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
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
    transition: background-color 0.3s ease;
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
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.news-item {
    margin-bottom: 1rem;
}

.news-title {
    color: #555;
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.news-description {
    color: #777;
    font-size: 1rem;
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
</style>
  