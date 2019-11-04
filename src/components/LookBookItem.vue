<template>
	<div class="card-footer row">
		<img :src="imageUrl" class="card-img-top col-5">
		<div class="col-7">
			<p>{{name}}</p>
			<p>{{price}}원</p>
		</div>
	</div>
</template>

<script>
	export default {
		props: {
  		item: {
				type: Object,
				required: true
			}
  	},
  	data() {
  		return {
  			'id': this.item.id,
	  		'name': this.item.name,
	  		'imageUrl': this.item.imageUrl,
	  		'price': this.item.price
  		}
  	}
	}
</script>