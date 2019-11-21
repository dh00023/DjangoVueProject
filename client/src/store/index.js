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
  	styleshare: [],
  	brandItems: [],
  	addStyleShare:{
  		tags: [],
  		items: [],
  		image: {}
  	}
  },
  // computed와 유사
  getters: {
  },
  // mutation은 state 값을 변경하는 로직
	// 인자를 받아 vuex에 넘겨줄 수 있고, methods와 연결
  mutations: {
  	successToGetLookBook(state, payload) {
  		state.lookbook = payload;
  	},
  	successToGetStyleShare(state, payload) {
  		state.styleshare = payload;
  	},
  	succestToGetBrandItem(state, payload){
  		state.brandItems = payload.result[0].rowDatas;
  	},
  	succestToGetItem(state, payload){
  		state.items = payload;
  	},
  	addTag(state, payload) {
  		state.addStyleShare.tags.push(payload);
  	},
  	checkedItem(state,payload){
  		state.addStyleShare.items.push(payload);
  	},
  	successCreateStyle(state, payload){
  		state.styleshare.push(payload);
  		
  	}
  },
  // 비동기
  actions: {
  	getLookBook(context) {
			axios.get('/api/magazines/').then(function(res) {
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
		getBrandItems(context) {
			axios.get('/api/item/brand/').then(function(res) {
				context.commit('succestToGetBrandItem',res.data);
			}).catch(function() {
			});
		},
		getItems(context) {
			axios.get('/api/item/').then(function(res) {
				res.data.forEach((item) => { 
	        item.checked = false; 
	      });
				context.commit('succestToGetItem',res.data);
			}).catch(function() {
			});
		},
		addTag(context, payload) {
			context.commit('addTag', payload);
		},
		addStyleShare(context, payload) {
			let config = {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			};
			axios.post('/api/styleshare/create/', payload, config).then(function(res){
				window.console.log(res);
				context.commit('successCreateStyle', res.data);
			}).catch(function(err){
				window.console.log(err.request.response);
			});
		},
		checkedItem(context, payload){
			context.commit('checkedItem', payload);
		}
  },
  modules: {}
});

