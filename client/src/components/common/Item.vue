<template>
	<li class="card-footer row" @click="clickToItem">
		<img :src="imageUrl" class="card-img-top col-5">
		<div class="col-7">
			<p>{{itemName}}</p>
			<p>{{price}}원</p>
		</div>
	</li>
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
  			'itemCode': this.item.item_code,
	  		'itemName': this.item.item_name,
	  		'imageUrl': this.item.image_url,
	  		'price': this.item.price
  		}
  	},
  	methods: {
			clickToItem() {
				window.location.href = "https://display.cjmall.com/m/item/"+this.itemCode;
			}
		}
	}
</script>