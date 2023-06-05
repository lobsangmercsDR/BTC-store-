import { createApp } from 'vue';
import App from './App.vue';
import Swiper from 'swiper';
import 'vue-material-design-icons/styles.css';
import 'swiper/swiper-bundle.css';
import './assets/css/app.css';
import router from './router';
import productCard from './components/productCard.vue';
import store from './store';
import cart from './cart';
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const app = createApp(App);

app.use(PrimeVue);
app.use(router);
app.use(store);

app.component('productCard', productCard);

app.mount('#app');

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
