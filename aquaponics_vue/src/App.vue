<template>
  <div class="wrapper">
    <div id="content">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.wrapper {
  display: flex;
  width: 100%;
  align-items: stretch;
}
#sidebar {
    min-width: 250px;
    max-width: 250px;
}
</style>
