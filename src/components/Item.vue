<template>
	<div class="card">
		<img :src="imageUrl" class="card-img-top" alt="...">
		<p><small>{{ name }}</small></p>
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
				'id': this.item.id,
				'name': this.item.name,
				'imageUrl': this.item.imageUrl,
				'price': this.item.price
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
	}
</style>