import { createStore } from 'vuex'


export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    username:'',
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    token: (state) => state.token,
    username: (state) => state.username,
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem("token")){
        state.token = localStorage.getItem("token")
        state.isAuthenticated = true
        state.username = localStorage.getItem("username")
      } else {
        state.token = ""
        state.isAuthenticated = false
        state.username = ""
      }
    },
    setToken(state, token){
      state.token = token
      localStorage.setItem("token", token)
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ""
      localStorage.removeItem("token")
      state.isAuthenticated = false
      state.username = ""
    }
  },
  actions: {
  },
  modules: {
  }
})
