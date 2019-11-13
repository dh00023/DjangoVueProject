<template>
	<div class="carousel-item" :class="{ active: isActive }"  data-interval="1500">
		<img :src="bnrImageUrl" class="d-block w-100" alt="...">
		<h5 class="card-title mx-auto">{{ title }}</h5>
	</div>
</template>

<script>
	export default {
		name: 'lookbook-banner-item',
		props: {
			banner: {
				type: Object,
				required: true
			},
			index: {
				type: Number,
				required: true
			}
		},
		data() {
			return {
				'id': this.banner.id,
				'title': this.banner.title,
				'bnrImageUrl': this.banner.bnrImageUrl
			}
		},
		computed: {
			isActive() {
				return this.index === 0;
			}
		}
	}
</script>
<style>
	.carousel-item > img {
		height: 230px;
	}
	.carousel-item > h5 {
		padding-left: 0.8em;
		margin-top: 0.6em;
	}
</style>