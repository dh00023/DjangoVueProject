<template>
	<div class="container" id="lookbook">
		<LookBookBanner/>
		<LookBookContent/>
	</div>
</template>
<script>
	import LookBookBanner from '@/components/LookBookBanner.vue'
	import LookBookContent from '@/components/LookBookContent.vue'
	
	export default {
		name: 'lookbook',
  	components: {
    	LookBookBanner,
    	LookBookContent
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