<template>
	<div>
		<div id="styleButton" class="row justify-content-center">
			<button type="button" class="btn btn-dark" data-toggle="modal" data-target="#addStyle" @click="showModal = true">+내 스타일 공유하기+</button>	
		</div>
		
		<StyleShareForm v-if="showModal" @close="showModal = false"/>
		<div class="cards">
			<StyleSharePost v-for="(styleshare) in getStyleShare" :key="styleshare.id" :styleshare="styleshare" />
		</div>	
	</div>
	
</template>

<script>
	import StyleSharePost from '@/components/styleshare/Post.vue'
	import StyleShareForm from '@/components/styleshare/RegisterForm.vue'

	export default {
		components: {
			StyleSharePost,
			StyleShareForm
		},
		data() {
  		return {
  			'showModal': false,
  		}
  	},
		created() {
			this.$store.dispatch('getStyleShare');
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
#style-card {
	padding: 5px;
	margin: 0 0 1em;
	width: 100%;
	cursor: pointer;
	transition: all 100ms ease-in-out;
	display: inline-block;
	-webkit-column-break-inside: avoid;
}
#styleButton{
	margin: 1rem;
}
</style>