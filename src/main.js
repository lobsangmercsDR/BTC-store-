import { createApp } from 'vue';
import App from './App.vue';
import Swiper from 'swiper';


// Importa los estilos de Swiper
import 'swiper/swiper-bundle.css';

// importa el archivo de estilos de tu aplicación
import './assets/css/app.css';


// importa el enrutador si lo estás utilizando
import router from './router';

// importa el componente ProductCard.vue
import productCard from './components/productCard.vue';

// crea la aplicación
const app = createApp(App);

// registra el enrutador si lo estás utilizando
if (router) {
  app.use(router);
}

// registra el componente ProductCard
app.component('productCard', productCard);

// monta la aplicación en el elemento con el id 'app'
app.mount('#app');

// Inicializa el carrusel de productos después de que la aplicación se haya montado
app.directive('swiper', {
  mounted(el) {
    new Swiper(el, {
      slidesPerView: 4,
      spaceBetween: 20,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });
  },
});
