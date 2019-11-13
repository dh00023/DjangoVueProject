import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from './router';

Vue.config.productionTip = false;

Vue.filter('truncate', function (text, stop, clamp) {
    return text.slice(0, stop) + (stop < text.length ? clamp || '...' : '')
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount("#app");
