import { createRouter, createWebHistory } from "vue-router";
 
import dashboard from '../pages/master/dashboard'
import orders from '../components/usersdashboard/orders.vue';
import sell_orders from '../components/usersdashboard/sell_orders';
import home from '../pages/Dashboard/home'
import profile from '../pages/Dashboard/profile'
import rechar from '../components/payments/rechar.vue';
import user_checker from '../components/usersdashboard/user_checker.vue'
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
import logout from '../pages/Login/logout.vue'
import product_dig from '../pages/Dashboard/Products and categories/product_dig.vue'
import categories_manage from '../pages/Dashboard/Products and categories/categories_manage.vue'
import inventory_general from '../pages/Dashboard/Products and categories/inventory_general.vue'
import user_control from '../pages/Dashboard/users_control/user_control.vue'
import invitation_code_manager from '../pages/Dashboard/users_control/invitation_code_manager.vue'
import Wallet from '../pages/Dashboard/wallet_cripto/Wallet.vue'
import deposit_coins from '../pages/Dashboard/wallet_cripto/deposit_coins.vue'
import users_profile_component from '@/components/usersdashboard/users_profile_component.vue';
import profile_modification from '../components/usersdashboard/profile_modification.vue';
import buy_categories from '../components/usersdashboard/buy_categories'
import user_shop from '../components/usersdashboard/user_shop.vue'

  const routes = [

    {
      name:'test',
      path:'/test',
      component:profile,
      children: [
        {
          name:'profilemodif',
          path:'pm',
          component:deposit_coins
        }
      ]
    },
    {
      
      name: 'Dashboard',
      path: '/',
      component: dashboard,
      redirect: {name: 'home'},
      meta : {requiresAuth: true},
      children: [
         {
          name: 'home',
          path: '/home',
          component:home,
          meta : {requiresAuth: true},
        },
       
        {
          name: 'products_fis',
          path: '/products_fis',
          component:products_fis
        },
        {
          path: '/product_dig',
          name: 'product_dig',
          component: product_dig
        },
        {
          path: '/categories_manage',
          name: 'categories_manage',
          component: categories_manage
        },
        {
          path: '/inventory_general',
          name: 'inventory_general',
          component: inventory_general
        },
        {
          name: 'user_control',
          path: 'user_control',
          component:user_control
        },
        {
          name: 'invitation_code_manager',
          path: '/invitation_code_manager',
          component:invitation_code_manager
        },
        {
          name: 'Wallet',
          path: '/Wallet',
          component:Wallet
        },
        {
          path: '/user_checker',
          name:'user_checker',
          component : user_checker
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
          name: 'deposit_coins',
          path: '/deposit_coins',
          component:deposit_coins
        },
        
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
      component: logout,
      meta: {requiresAuth: true}
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
    },
    {
      name: 'profile',
      path: '/profile',
      component:profile,
      redirect:{name:'profModif'},
      children: [
        { 
          name:'profModif', 
          path: 'modificate', 
          component: profile_modification
        },
        {
          name: 'walletUser',
          path:'rechar',
          component:rechar
        },
        {
          name:'bOrders',
          path:'buying_orders',
          component: orders
        },
        {
          name:'sOrders',
          path:'sell_orders',
          component: sell_orders
        },
        {
          name:'BuyCategories',
          path:'categories_store',
          component: buy_categories
        },
        {
          name:'checkerPanel',
          path:'Pchecker',
          component: user_checker
        },
        {
          name:'add_product_f',
          path:'add_product_f',
          component: products_fis
        },
        {
          name:'tienda',
          path:'store',
          component: user_shop
        },
        {
          name:'add_product_d',
          path:'add_product_d',
          component: product_dig
        }
      ]
    },

   
   
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

    if(isAuthenticated()) {
      next();
    } else {
      next('/homePageEcommerce')
    } 
  }else {
    next();
  }
});
  
export default router;