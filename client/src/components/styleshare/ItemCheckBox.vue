<template>
			<li>
				<input type="checkbox" v-model="checked" @change="checkedItem">
				<div class="card-footer row">
					<img :src="imageUrl" class="col-5">
					<div class="col-7">
						<p>{{itemName}}</p>
						<p>{{price}}원</p>
					</div>
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
  			'itemCode': this.item.itemCode,
	  		'itemName': this.item.itemName,
	  		'imageUrl': this.item.imageUrl,
	  		'price': this.item.price,
	  		'checked': this.item.checked
  		}
  	},
  	methods: {
  		checkedItem(){
  			this.$store.dispatch('checkedItem', this.itemCode);
  		}
  	}
	}
</script>
<style scoped>
	.card-footer{
		border: none;
		background-color: white;
	}
	li {
		display: inline-block;
	}
</style>