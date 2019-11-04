<template>
	<div class="cards" id="style_share">
		<StyleShareItem v-for="(styleshare) in getStyleShare" :key="styleshare.id" :styleshare="styleshare" />
	</div>
</template>

<script>
	import StyleShareItem from '@/components/StyleShareItem.vue'
	
	export default {
		components: {
			StyleShareItem
		},
		computed: {
			getStyleShare() {
				return this.$store.state.styleshare;
			}
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