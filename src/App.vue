<template>
  <div id="app">
    <header id="header">
      <nav class="navbar justify-content-center">
        <router-link to="/" class="text-dark h3 pt-3">CelepShop</router-link>
      </nav>
      <div id="tab">
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

<style>
#header a{
  color: black;
  background-color: white;
}
.router-link-active {
  font-weight: bold;
}
</style>
