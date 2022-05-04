<template>
  <div>
    <i class="fa-solid fa-leaf fa-2xl p-4"></i>
    <HelloWorld msg="Bienvenido al Simulador de Acuaponía" />
    <section>
      <div>
        {{ msg  }}
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from 'axios'

export default {
  name: "HomeView",
  data() {
    return {
      msg: ""
    }
  },
  components: {
    HelloWorld,
  },
  mounted() {
    this.getSimulator()
  },
  methods: {
    getSimulator() {
      axios
        .get('api/v1/simulator/')
        .then(response => {
          this.msg = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>
