<template>
  <div class="home">
  	<h4>LookBook</h4>
    <LookBookBanner />
  </div>
</template>

<script>
// @ is an alias to /src
import LookBookBanner from '@/components/LookBookBanner.vue'

export default {
  name: 'home',
  components: {
    LookBookBanner
  }
}
</script>

<style scoped>
	h4 {
		padding-left: 20px;
	}
</style>