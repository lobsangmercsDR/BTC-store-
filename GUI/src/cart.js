const state = {
    cartItems: []
  };
  
  const mutations = {
    ADD_TO_CART(state, item) {
      state.cartItems.push(item);
    },
    REMOVE_FROM_CART(state, itemId) {
      state.cartItems = state.cartItems.filter(item => item.id !== itemId);
    }
  };
  
  const actions = {
    addToCart({ commit }, item) {
      commit('ADD_TO_CART', item);
    },
    removeFromCart({ commit }, itemId) {
      commit('REMOVE_FROM_CART', itemId);
    }
  };
  
  export default {
    namespaced: true, // Asegúrate de agregar esta línea para indicar que el módulo está en un espacio de nombres
    state,
    mutations,
    actions
  };
  