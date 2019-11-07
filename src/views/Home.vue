<template>
  <div id="home">
  	<h4 class="mt-4">LookBook</h4>
  	<LookBookBanners />
    <div id="item-list" class="mt-4">
    	<h4>Item List</h4>
    	<div class="item-list" >
		    <Item v-for="(item) in getItemList" :key="item.itemCode" :item="item"></Item>
	    </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import LookBookBanners from '@/components/LookBookBanners.vue'
import Item from '@/components/Item.vue'

export default {
  name: 'home',
  components: {
    LookBookBanners,
    Item
  },
  computed: {
  	getItemList() {
  		return this.$store.state.items;
		}
	},
  created() {
      this.$store.dispatch('getItems');
    },
}
</script>

<style scoped>
	h4 {
		padding-left: 20px;
	}
	.item-list {
		column-count: 2;
		column-gap: 1em; 
		margin: 0 0.8em;
	}
</style>