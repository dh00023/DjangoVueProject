<template>
	<div class="content mt-5">
		<div class="card mb-3">
			<img :src="mainImageUrl" class="card-img-top" alt="...">
			<div class="card-body">
				<h5 class="card-title">{{ title }}</h5>
				<p class="card-text">
					{{ text }}
				</p>
				<CommonItem v-for="(item) in items" :key="item.item_code" :item="item" />
			</div>

		</div>
	</div>	
</template>
<script>
	import CommonItem from '@/components/common/Item.vue'
	
	export default {
		name: 'lookbook-content',
  	components: {
    	CommonItem
  	},
  	props: {
  		lookbook: {
				type: Object,
				required: true
			}
  	},
  	data() {
  		return {
  			'id': this.lookbook.id,
	  		'title': this.lookbook.title,
	  		'mainImageUrl': this.lookbook.main_image_url,
	  		'text': this.lookbook.text,
	  		'items': this.lookbook.items
  		}
  	}
	}
</script>
<style scoped>
	.card {
		border-style: none !important;
	}
	img{
		padding: 1rem;
	}
</style>