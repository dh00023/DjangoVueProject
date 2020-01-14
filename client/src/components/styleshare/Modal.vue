<template>
	<div class="modal fade" :id="'styleShareModal'+id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	  <div class="modal-dialog modal-dialog-centered" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
	          <span aria-hidden="true">&times;</span>
	        </button>
	      </div>
	      <div class="modal-body">
	        <img :src="imageUrl" >
	        <div id="tags">
	        	<span v-for="tag in tags" :key="tag.name" class="tag-btn">#{{ tag.name }}</span>	
	        </div>
	        <span>@{{ author }}</span>
	      </div>
	      <div class="modal-footer">
	      	<ul>
	      		<CommonItem v-for="(item) in items" :key="item.item_code" :item="item"/>		
	      	</ul>
	      </div> 
	    </div>
	  </div>
	</div>
</template>
<script>
	import CommonItem from '@/components/common/Item.vue'
	
	export default {
		name: 'item',
		components: {
			CommonItem
		},
		props: {
			styleshare: {
				type: Object,
				required: true
			}
		},
		data() {
			return {
				'id': this.styleshare.id,
				'author': this.styleshare.user.username,
				'imageUrl': this.styleshare.image,
				'items': this.styleshare.items,
				'tags': this.styleshare.tags
			}
		}
	}
</script>
<style scoped>
	img {
		border: none;
		margin-left: auto;
		margin-right: auto;
	}
	.card-footer {
		border: none;
		background: none;
	}
	ul{
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