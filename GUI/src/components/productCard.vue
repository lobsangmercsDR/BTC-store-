<template>
  <div class="swiper-container">
    <div class="swiper-wrapper">
      <div v-for="(product, index) in products" :key="index" class="swiper-slide">
        <div class="product-card">
          <div class="product-image">
            <img :src="product.image" alt="Product Image" />
          </div>
          <div class="product-details">
            <h3 class="product-name">{{ product.name }}</h3>
            <p class="product-description">{{ product.description }}</p>
            <p class="product-price">{{ product.price }}</p>
          </div>
          <div class="product-actions">
            <button class="add-to-cart-button">Agregar al carrito</button>
          </div>
        </div>
      </div>
    </div>
    <div class="swiper-pagination"></div>
  </div>
</template>

<script>
import Swiper from 'swiper';

export default {
  name: 'ProductCard',
  data() {
    return {
      products: [
        {
          name: 'Producto 1',
          description: 'Descripción del Producto 1',
          price: '$10',
          image: 'https://via.placeholder.com/200x200?text=Producto+1',
        },
        {
          name: 'Producto 2',
          description: 'Descripción del Producto 2',
          price: '$20',
          image: 'https://via.placeholder.com/200x200?text=Producto+2',
        },
        {
          name: 'Producto 3',
          description: 'Descripción del Producto 3',
          price: '$30',
          image: 'https://via.placeholder.com/200x200?text=Producto+3',
        },
        {
          name: 'Producto 4',
          description: 'Descripción del Producto 4',
          price: '$40',
          image: 'https://via.placeholder.com/200x200?text=Producto+4',
        },
        {
          name: 'Producto 5',
          description: 'Descripción del Producto 5',
          price: '$50',
          image: 'https://via.placeholder.com/200x200?text=Producto+5',
        },
        {
          name: 'Producto 6',
          description: 'Descripción del Producto 6',
          price: '$60',
          image: 'https://via.placeholder.com/200x200?text=Producto+6',
        },
        {
          name: 'Producto 7',
          description: 'Descripción del Producto 7',
          price: '$70',
          image: 'https://via.placeholder.com/200x200?text=Producto+7',
        },
        {
          name: 'Producto 8',
          description: 'Descripción del Producto 8',
          price: '$80',
          image: 'https://via.placeholder.com/200x200?text=Producto+8',
        },
        {
          name: 'Producto 9',
          description: 'Descripción del Producto 9',
          price: '$90',
          image: 'https://via.placeholder.com/200x200?text=Producto+9',
        },
        {
          name: 'Producto 10',
          description: 'Descripción del Producto 10',
          price: '$100',
          image: 'https://via.placeholder.com/200x200?text=Producto+10',
        },
      ],
      swiper: null,
    };
  },
  mounted() {
    this.initSwiper();
    //this.fetchProducts(); // Descomenta esta línea para obtener los productos desde la API
  },
  methods: {
    initSwiper() {
      this.swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: {
          delay: 3000,
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
        breakpoints: {
          640: {
            slidesPerView: 2,
          },
          768: {
            slidesPerView: 3,
          },
          1024: {
            slidesPerView: 6,
          },
        },
      });

      setTimeout(() => {
        if (this.swiper && this.swiper.autoplay) {
          this.swiper.autoplay.start?.();
        }
      }, 100);
    },
    /*
    fetchProducts() {
      fetch('URL_DE_TU_API')
        .then(response => response.json())
        .then(data => {
          this.products = data;
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    */
  },
  beforeDestroy() {
    if (this.swiper) {
      this.swiper.destroy();
      this.swiper = null;
    }
  },
};
</script>

<style scoped>
.swiper-container {
  width: 100%;
  overflow: hidden;
}

.product-card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.product-image img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 4px;
}

.product-name {
  font-size: 1.2rem;
  margin: 0.5rem 0;
  color: #f66305;
  transition: color 0.3s;
}

.product-card:hover .product-name {
  color: #ab16be;
}

.product-description {
  margin-bottom: 1rem;
  color: #555;
  transition: color 0.3s;
}

.product-card:hover .product-description {
  color: #333;
}

.product-price {
  font-weight: bold;
  margin-bottom: 1rem;
  color: #ab16be;
  transition: color 0.3s;
}

.product-card:hover .product-price {
  color: #f66305;
}

.add-to-cart-button {
  background-color: #ab16be;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-to-cart-button:hover {
  background-color: #f66305;
}

.swiper-pagination {
  margin-top: 1rem;
  text-align: center;
}

.swiper-pagination-bullet {
  background-color: #ab16be;
  opacity: 0.5;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  transition: background-color 0.3s;
}

.swiper-pagination-bullet-active {
  background-color: #f66305;
  opacity: 1;
  width: 12px;
  height: 12px;
}

@media (max-width: 640px) {
  .product-card {
    padding: 0.5rem;
  }

  .product-name {
    font-size: 1rem;
    margin-bottom: 0.5rem;
  }

  .product-description {
    margin-bottom: 0.5rem;
  }
}
</style>
