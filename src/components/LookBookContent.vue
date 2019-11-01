<template>
	<div class="content mt-5">
		<div class="card mb-3">
			<img src="https://static.celebshop.com/skin/frontend/celebshop/mobile/images/lookbook/ce_19fw/ce_19fw_03.jpg" class="card-img-top" alt="...">
			<div class="card-body">
				<h5 class="card-title">Ce& 19 FW</h5>
				<p class="card-text">
					Ce& will emerge as the epicenter of all young creators around the globe.
				</p>
				<LookBookItem/>
			</div>

		</div>
	</div>	
</template>
<script>
	import LookBookItem from '@/components/LookBookItem.vue'
	
	export default {
		name: 'content',
  	components: {
    	LookBookItem
  	}
	}
</script>
<style scoped>
	.card {
		border-style: none !important;
	}
</style>