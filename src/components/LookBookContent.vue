<template>
	<div class="content mt-5">
		<div class="card mb-3">
			<img :src="mainImageUrl" class="card-img-top" alt="...">
			<div class="card-body">
				<h5 class="card-title">{{ title }}</h5>
				<p class="card-text">
					{{ text }}
				</p>
				<LookBookItem v-for="(item) in items" :key="item.itemCode" :item="item" />
			</div>

		</div>
	</div>	
</template>
<script>
	import LookBookItem from '@/components/LookBookItem.vue'
	
	export default {
		name: 'lookbook-content',
  	components: {
    	LookBookItem
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
	  		'mainImageUrl': this.lookbook.mainImageUrl,
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
</style>