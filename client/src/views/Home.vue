<template>
  <div id="home">
    <h4 class="mt-4">LookBook</h4>
    <LookBookBanners />
    <div id="item-list" class="mt-4">
      <h4>Item List</h4>
      <div class="item-list" >
        <BrandItem v-for="(item) in getItemList" :key="item.dqId" :item="item"></BrandItem>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import LookBookBanners from '@/components/lookbook/BannerList.vue'
import BrandItem from '@/components/BrandItem.vue'

export default {
  name: 'home',
  components: {
    LookBookBanners,
    BrandItem
  },
  computed: {
    getItemList() {
      return this.$store.state.brandItems;
    }
  },
  created() {
    this.$store.dispatch('getBrandItems');
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