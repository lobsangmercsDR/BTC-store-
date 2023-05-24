import { createStore } from 'vuex';

const store = createStore({
  modules: {
    cart: {
      state: {
        items: [],
      },
      mutations: {
        addToCart(state, item) {
          state.items.push(item);
        },
        removeFromCart(state, itemId) {
          state.items = state.items.filter((item) => item.id !== itemId);
        },
      },
      actions: {
        addToCart({ commit }, item) {
          commit('addToCart', item);
        },
        removeFromCart({ commit }, itemId) {
          commit('removeFromCart', itemId);
        },
      },
      getters: {
        cartItems(state) {
          return state.items;
        },
        cartTotal(state) {
          return state.items.reduce((total, item) => total + item.price * item.quantity, 0);
        },
      },
    },
  },
});

export default store;
