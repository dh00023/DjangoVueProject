<template>
	<div class="card">
		<img :src="setImageUrl" class="card-img-top" alt="..." @click="clickToItem">
		<p class="card-text"><small>{{ itemName | truncate()}}</small></p>
		<p>{{ price }}원</p>
	</div>
</template>
<script>
	export default {
		name: 'brand-item-list',
		props: {
			item: {
				type: Object,
				required: true
			} 
		},
		data() {
			return {
				'itemCode': this.item.itemCd,
				'itemName': this.item.itemNm,
				'imageUrl': this.item.pmgItemImgUrl,
				'price': this.item.pmgCustomerPrice
			}
		},
		computed: {
			setImageUrl() {
				return '//thumb.cjmall.net/unsafe/fit-in/280x280/itemimage.cjmall.net/'.concat(this.imageUrl);
			}
		},
		methods: {
			clickToItem() {
				window.location.href = "https://display.cjmall.com/m/item/"+this.itemCode;
			}
		}
	}
</script>

<style scoped>
	.card{
		border-radius: 0;
		border-style: none;
		padding: 5px;
		margin: 0 0 1em;
		width: 100%;
		cursor: pointer;
		display: inline-block;
		-webkit-column-break-inside: avoid;
	}
	img {
		display: block;
		width: 100%;
	}
	p {
		margin: 0;
		height: 48px;
		overflow: hidden;
	}
</style>

