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
	        <img :src="`${base_url}`+imageUrl" >
	        <span>@{{ author }}</span>
	      </div>

	      <div class="modal-footer">
	      	<ul>
	      		<CommonItem v-for="(item) in items" :key="item.itemCode" :item="item"/>		
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
				'author': this.styleshare.author,
				'imageUrl': this.styleshare.imageUrl,
				'items': this.styleshare.items,
				'base_url': process.env.BASE_URL
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
</style>