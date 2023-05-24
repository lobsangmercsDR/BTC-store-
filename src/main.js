import { createApp } from 'vue';
import App from './App.vue';
import Swiper from 'swiper';

// Importa los estilos de Swiper
import 'swiper/swiper-bundle.css';

// Importa el archivo de estilos de tu aplicación
import './assets/css/app.css';

// Importa el enrutador si lo estás utilizando
import router from './router';

// Importa el componente ProductCard.vue
import productCard from './components/productCard.vue';

// Importa el Vuex store
import store from './store';
import cart from './cart'; 


// Crea la aplicación
const app = createApp(App);

// Registra el enrutador si lo estás utilizando
if (router) {
  app.use(router);
}

// Aplica el store a tu aplicación Vue
app.use(store);


// Registra el componente ProductCard
app.component('productCard', productCard);

// Monta la aplicación en el elemento con el id 'app'
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
