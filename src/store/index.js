import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

Vue.use(Vuex);

// 토큰명과 header명은 장고에서 전달되는 것이다. 이 값은 장고 settings에서 변경 가능
// defaults 값을 설정해주면 자동으로 api 호출시마다 설정된다.
// 장고에서 {% csrf_token %}을 선언하면 csrf_token이 생성된다.

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default new Vuex.Store({
  state: {
  	items: [],
  	lookbook: [],
  	styleshare: []
  },
  // computed와 유사
  getters: {  	
  },
  mutations: {
  	successToGetLookBook(state, payload) {
  		state.lookbook = payload;
  	},
  	successToGetStyleShare(state, payload) {
  		state.styleshare = payload;
  	},
  	succestToGetItem(state, payload){
  		state.items = payload.result[0].rowDatas;
  	}
  },
  // 비동기
  actions: {
  	getLookBook(context) {
			axios.get('/api/lookbook/').then(function(res) {
				context.commit('successToGetLookBook',res.data);
			}).catch(function() {
			});
		},
		getStyleShare(context) {
			axios.get('/api/styleshare/').then(function(res) {
				context.commit('successToGetStyleShare',res.data);
			}).catch(function() {
			});
		},
		getItems(context) {
			axios.get('/api/brandItemList/').then(function(res) {
				context.commit('succestToGetItem',res.data);
			}).catch(function() {
			});
		},
  },
  modules: {}
});
