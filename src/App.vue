<template>
  <div id="app">
    <header id="header">
      <nav class="navbar justify-content-center">
        <router-link to="/" class="text-dark h3 pt-3">CelepShop</router-link>
      </nav>
      <div id="tab" v-if="showTabView">
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <router-link to="/lookbook" class="nav-link">Lookbook</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/styleShare" class="nav-link">Style Share</router-link>
          </li>
        </ul>
      </div>
    </header>
    <router-view/>
  </div>
</template>
<script>
  export default {
    computed: {
      showTabView() {
        window.console.log(document.location.pathname.indexOf('add'))
        return (document.location.pathname.indexOf('add') < 0) ? true : false;
      }
    }
  }
</script>
<style>
#header a{
  color: black;
  background-color: white;
}
.router-link-active {
  font-weight: bold;
}
</style>
