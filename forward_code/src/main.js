import Vue from 'vue'
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
import App from './App.vue'
import router from './router/index'
import store from '@/store/index'

Vue.use(Mint)

Vue.config.productionTip = false
// 订阅mutaton
store.subscribe((mutation, state) => {
  // console.log({mutation, state})
  window.localStorage.setItem('cyqLikes', JSON.stringify(state.likes))
  window.localStorage.setItem('cyqCollection', JSON.stringify(state.collection))
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
