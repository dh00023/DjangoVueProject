<template>
	<div id="carouselExampleInterval" class="carousel slide" data-ride="carousel">
		<div class="carousel-inner ">
			<LookBookBanner v-for="(banner,index) in getLookBook" :key="banner.id" :banner="banner" :index="index" />
		</div>
		<a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-slide="prev">
			<span class="carousel-control-prev-icon" aria-hidden="true"></span>
			<span class="sr-only">Previous</span>
		</a>
		<a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="sr-only">Next</span>
		</a>
	</div>
</template>

<script>
	import LookBookBanner from '@/components/LookBookBanner.vue'
	export default {
		name: 'lookbook-banner',

		components: {
			LookBookBanner
		},
		computed: {
			getLookBook() {
				return this.$store.state.lookbook;
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