<template>
  <div class="container-fluid">
    <header class="d-flex flex-wrap justify-content-center py-2">
      <a href="/" class="d-flex align-items-center mb-2 mb-md-0 me-md-auto text-white text-decoration-none">
        <i class="fa-solid fa-leaf fa-2xl p-2"></i>
        <span class="fs-4 fw-bold">Simulador de Acuaponía</span>
      </a>

      <ul class="nav nav-pills">
        <li class="nav-item"><button class="btn text-white bg-primary" @click="$emit('print-pdf')"><i class="fa-solid fa-file-pdf fa-lg"></i> Guardar</button></li>
        <li class="nav-item"><a href="/" class="nav-link active text-white" aria-current="page">Principal</a></li>
        <li class="nav-item"><a href="#" class="nav-link text-white">About</a></li>
      </ul>
    </header>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
    
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.container-fluid {
  background-color: var(--blue);
}
</style>
