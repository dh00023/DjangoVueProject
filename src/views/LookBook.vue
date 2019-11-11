<template>
	<div id="lookbook">
		<LookBookBanners />
		<LookBookContent v-for="(lookbook) in getLookBook" :key="lookbook.id" :lookbook="lookbook"/>
	</div>
</template>
<script>
	import LookBookBanners from '@/components/lookbook/BannerList.vue'
	import LookBookContent from '@/components/lookbook/Content.vue'
	
	export default {
		name: 'lookbook',
  	components: {
    	LookBookBanners,
    	LookBookContent
  	},
  	computed: {
			getLookBook() {
				return this.$store.state.lookbook;
			}
		}
	}
</script>
<style scoped>
	#lookbook {
		margin: 1.3rem 0;
	}

	.card {
		border-style: none !important;
	}
</style>