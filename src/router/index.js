import { createRouter, createWebHistory } from "vue-router";
 
import dashboard from '../pages/master/dashboard'

import home from '../pages/home'
import profile from '../pages/profile'
import products_fis from '../pages/products_fis.vue'
import cases from '../pages/cases.vue'
import inventario from '../pages/inventario.vue'
import CriptoView from '../pages/CriptoView.vue'
import users from '../pages/users.vue'
import header from '../pages/header.vue'


  const routes = [
    {
      name: 'Dashboard',
      path: '/',
      component: dashboard,
      children: [
         {
          name: 'home',
          path: '/home',
          component:home
        },
        {
          name: 'profile',
          path: '/profile',
          component:profile
        },
        {
          name: 'products_fis',
          path: '/products_fis',
          component:products_fis
        },
        {
          name: 'cases',
          path: '/cases',
          component:cases
        },
        {
          name: 'inventario',
          path: '/inventario',
          component:inventario
        },
        {
          name: 'CriptoView',
          path: '/CriptoView',
          component:CriptoView
        },
        {
          name: 'users',
          path: '/users',
          component:users
        }
        
      ]
      
    },
    {
      name: 'header',
      path: '/header',
      component: header
    }
       
  ];
const router = Router();
export default router;
function Router() {
    const router = new createRouter({
        history: createWebHistory(),
        routes,
    });
    return router;
}
  