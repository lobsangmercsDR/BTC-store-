import { createRouter, createWebHistory } from "vue-router";
 
import dashboard from '../pages/master/dashboard'

import home from '../pages/Dashboard/home'
import profile from '../pages/Dashboard/profile'
import products_fis from '../pages/Dashboard/products_fis.vue'
import cases from '../pages/Dashboard/cases.vue'
import inventario from '../pages/Dashboard/inventario.vue'
import CriptoView from '../pages/Dashboard/CriptoView.vue'
import users from '../pages/Dashboard/users.vue'
import login from '../pages/Login/login.vue'
import signup from '../pages/Login/signup.vue'
import resetpass from '../pages/Login/resetpass.vue'
import homePageEcommerce from '../pages/Store/homePageEcommerce.vue'
import { isAuthenticated, getAuthToken } from "../../utils/auth.js"; 
import Cookies from "js-cookie";
import logout from '../pages/Login/logout.vue'


  const routes = [
    {
      name: 'Dashboard',
      path: '/',
      component: dashboard,
      meta : {requiresAuth: true},
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
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout
    },
    {
      path: '/signup',
      name: 'signup',
      component: signup
    },
    {
      path: '/resetpass',
      name: 'resetpass',
      component: resetpass
    },
    {
      path: '/homePageEcommerce',
      name: 'homePageEcommerce',
      component: homePageEcommerce
    }

   
   
  ];


function Router() {
    const router = new createRouter({
        history: createWebHistory(),
        routes,
    });
    return router;
}

const router = Router();

router.beforeEach((to, from, next) => {
  if(to.matched.some(route => route.meta.requiresAuth)) {

    console.log("asda");
    console.log(Cookies.get('token'))
    console.log(getAuthToken())
    console.log(isAuthenticated())
    if(isAuthenticated()) {
      next();
    } else {
      next('/login')
    } 
  }else {
    next();
  }
});
  
export default router;