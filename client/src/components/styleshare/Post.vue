<template>
	<div class="card" id="style-card">
		<img :src="imageUrl" class="card-img-top" data-toggle="modal" :data-target="'#styleShareModal'+id">
		<StyleShareModal :styleshare="styleshare" />
		<small class="text-muted">
			author @<cite title="Source Title">{{ author }}</cite>
		</small>
	</div>	
</template>
<script>
	import StyleShareModal from '@/components/styleshare/Modal.vue'
	export default {
		name: 'style-share-item',
		components: {
    	StyleShareModal
  	},
		props: {
			styleshare: {
				type: Object,
				required: true
			}
		},
		data() {
			return {
				'id': this.styleshare.id,
				'author': this.styleshare.user.username,
				'imageUrl': this.styleshare.image,
				'items': this.styleshare.items
			}
		}
	}
</script>
<style>
img {
	display: block;
	width: 100%;
}
</style>