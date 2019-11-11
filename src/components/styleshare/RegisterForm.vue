<template>
	<div class="modal fade" id="addStyle" tabindex="-1" role="dialog" aria-hidden="true">
	  <div class="modal-dialog modal-dialog-centered" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
	          <span aria-hidden="true">&times;</span>
	        </button>
	      </div>
	      <div class="modal-body">
	        <form  enctype="multipart/form-data" @submit.prevent>
	          <div class="form-group">
	            <label for="recipient-name" class="col-form-label">이미지</label>
	            <input type="file" accept="image/*" id="image-file" @change="uploadImage($event)">
	          </div>
	          <div class="form-group">
	            <label for="message-text" class="col-form-label">태그</label>
	            <input type="text" class="form-control" id="tag" v-model="newTag" @keyup.enter="addTag">
	            <div id="tags">
	            	<span v-for="tag in getTags" :key="tag.id" class="tag-btn">#{{ tag }}</span>	
	            </div>
	          </div>
	          <label for="message-text" class="col-form-label">관련 상품</label>
	          <ul class="form-group" id="check-list">
	            <ItemCheckBox v-for="(item) in getItems" :key="item.itemCode" :item="item"/>
	          </ul>
	        </form>
	      </div>
	      <div class="modal-footer">
        	<button type="button" class="btn btn-dark" @click="addStyleShare">등록</button>
	      </div> 
	    </div>
	  </div>
	</div>
	<!-- 
1. 이미지 파일 선택해서 올리는 경우에 파일 경로 알아두기
2. 태그 @keyup.enter 이벤트 등록해서 엔터치면, 밑에 보여지도록!(todo 참조)
3. 등록 버튼 클릭시 axios.post
4. 장고에 keyword 모델 생성하기(styleshare랑 1:N 관계
-->
</template>
<script>	
	import ItemCheckBox from '@/components/styleshare/ItemCheckBox.vue'
	export default {
		name: 'style-register-form',
		components: {
    	ItemCheckBox
  	},
  	data() {
  		return{
  			image: '',
  			newTag: ''
  		};
  	},
  	created() {
			this.$store.dispatch('getItems');
		},
		computed: {
			getItems() {
				return this.$store.state.items;
			},
			getTags() {
				return this.$store.state.addStyleShare.tags;
			}
		},
		methods: {
			addTag() {
				if(this.newTag.trim().length == 0){
					return;
				}
				this.$store.dispatch('addTag', this.newTag);
				this.newTag = '';
			},
			addStyle(event) {
				window.console.log(event);
			},
			uploadImage(event) {
				// const URL = 'api/upload/'; 
				this.image = event.target.files[0];

				window.console.log(this.image);

		    // let data = new FormData();
		    // data.append('file', event.target.files[0]); 

		    // let config = {
		    //   header : {
		    //     'Content-Type' : 'image/*'
		    //   }
		    // }
		    // axios.put(
		    //   URL, 
		    //   data,
		    //   config
		    // ).then(
		    //   response => {
		    //     window.console.log('image upload response > ', response);
		    //   }
		    // )
			},
			addStyleShare(){
				let dataForm = new FormData();
				dataForm.append('image', this.image);
				// dataForm.append('tags', this.$store.state.addStyleShare.tags);
				// dataForm.append('items', this.$store.state.addStyleShare.items);

				this.$store.dispatch('addStyleShare', dataForm);
			}
		}
  }
</script>
<style scoped>
	#check-list{
		padding: 0;
	}
	#tags {
		margin: 1rem 0;
	}
	.tag-btn {
		color: #007bff;
		border: 2px groove #007bff;
    background-color: white;
    padding: 3px;
    margin-right: 3px;
    margin-bottom: 10px;
    display: inline-block;
    font-size: 12px;
	}
</style>

