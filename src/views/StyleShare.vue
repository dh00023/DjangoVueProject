<template>
	<div class="cards" id="style_share">
			<!-- <img src="//thumb2.cjmall.net/unsafe/360x0/itemImage.cjmall.net/goods_images/56/387/56176387L.jpg" class="card-img-top"> -->
			<!-- <img src="http://static.celebshop.com/skin/frontend/celebshop/mobile/images/lookbook/ce_19fw/ce_19fw_01.jpg" class="card-img-top"> -->
			<!-- <img src="//thumb2.cjmall.net/unsafe/360x0/itemImage.cjmall.net/goods_images/56/387/56176387L.jpg" class="card-img-top"> -->
		<StyleShareItem/>
	</div>
</template>

<script>
	import StyleShareItem from '@/components/StyleShareItem.vue'
	
	export default {
		components: {
			StyleShareItem
		}
	
	}
</script>
<style>
.cards {
	column-count: 2;
	column-gap: 1em; 
	margin: 0 0.8em;
}
</style>