<template>
	<div class="card">
		<img :src="setImageUrl" class="card-img-top" alt="...">
		<p class="card-text"><small>{{ itemName | truncate()}}</small></p>
		<p>{{ price }}원</p>
	</div>
</template>
<script>
	export default {
		name: 'item-list',
		props: {
			item: {
				type: Object,
				required: true
			} 
		},
		data() {
			return {
				'itemCode': this.item.itemCode,
				'itemName': this.item.itemNm,
				'imageUrl': this.item.pmgItemImgUrl,
				'price': this.item.pmgCustomerPrice
			}
		},
		computed: {
			setImageUrl() {
				return '//thumb.cjmall.net/unsafe/fit-in/280x280/itemimage.cjmall.net/'.concat(this.imageUrl);
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
		transition: all 100ms ease-in-out;
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

