<template>
	<div class="card" id="style-card">
		<img :src="imageUrl" class="card-img-top">
		<small class="text-muted">
			author @<cite title="Source Title">{{ author }}</cite>
		</small>
	</div>	
</template>
<script>
	export default {
		name: 'style-share-item',
		props: {
			styleshare: {
				type: Object,
				required: true
			}
		},
		data() {
			return {
				'id': this.styleshare.id,
				'author': this.styleshare.author,
				'imageUrl': this.styleshare.imageUrl,
				'items': this.styleshare.items
			}
		}
	}
</script>
<style>
#style-card {
	background: #F5F5F5;
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
</style>