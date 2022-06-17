<template>
  <!-- <div
    class="is-loading-bar has-text-centered"
    v-bind:class="{ 'is-loading': $store.state.isLoading }"
  >
    <div class="lds-dual-ring"></div>
  </div> -->
  <!-- <DobleSlider/> -->
  <div class="container mt-4 p-5 bg-primary text-white rounded">
    <i class="fa-solid fa-leaf fa-2xl p-4"></i>
    <HelloWorld msg="Bienvenido al Simulador de Acuaponía" />
    <section>
      <div>
        {{ msg }}
      </div>
    </section>
  </div>
  <div class="card mt-4">
    <div class="card-body">
      <h2 class="card-title fw-bold">Tipos de cultivo</h2>
      <div class="row">
        <div class="overflow-auto col-2 my-custom-scrollbar">
          <div
            id="mydiv"
            class="btn-group-vertical mt-4"
            role="group"
            aria-label="Basic checkbox toggle button group"
          >
            <template v-for="(cultivo, i) in datosHidroponia" :key="i">
              <input
                type="checkbox"
                class="btn-check"
                :id="i"
                autocomplete="off"
                @click="getSelected()"
                checked
              />
              <label class="btn btn-outline-primary" v-bind:for="i">{{
                cultivo.cultivo
              }}</label>
            </template>
          </div>
        </div>

        <div class="col-10">
          <label for="minT" class="form-label"
            >Temperatura mínima: 
            <span id="slider_value"> {{tmin_value}} °C</span
          ></label>
          <input :min="this.t_min" :max="this.t_max" type="range" class="form-range" id="minT" v-model="tmin_value" @change="filterTemps()"/>
          <label for="maxT" class="form-label">Temperatura máxima: 
            <span id="slider_value"> {{tmax_value}} °C</span>
          </label>
          <input type="range"  :min="this.t_min" :max="this.t_max" class="form-range" id="maxT" v-model="tmax_value" @change="filterTemps()"/>
          <LineChart :chartData="datosGraficaHidroponia" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";
import LineChart from "@/components/LineChart.vue";
// import DobleSlider from "@/components/DobleSlider.vue";

export default {
  name: "Dashboard",
  data() {
    return {
      msg: "",
      datosHidroponia: [],
      datosMunicipios: [],
      tmax_value: 40,
      t_max: 40,
      tmin_value: -20,
      t_min: -20,
      loaded: false,
      datosGraficaHidroponia: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
        ],
      },
    };
  },
  components: {
    HelloWorld,
    LineChart,
    // DobleSlider
  },
  mounted() {
    this.getSimulator();
    document.title = "Inicio | Simulador";
  },
  methods: {
    getSimulator() {
      this.datosGraficaHidroponia.labels = [];
      this.datosGraficaHidroponia.datasets = [];
      this.datosGraficaHidroponia.datasets.push({
        label: "Temperatura Máxima",
        backgroundColor: "#f87979",
        borderColor: "#f87979",
        pointRadius: 0,
        data: [],
      });
      this.datosGraficaHidroponia.datasets.push({
        label: "Temperatura Mínima",
        backgroundColor: "#4d4dff",
        borderColor: "#4d4dff",
        pointRadius: 0,
        data: [],
      });
      axios
        .get("api/v1/datos-hidroponia/")
        .then((response) => {
          for (let x in response.data) {
            this.datosGraficaHidroponia.labels.push(response.data[x].cultivo);
            this.datosGraficaHidroponia.datasets[0].data.push(
              response.data[x].t_max
            );
            this.datosGraficaHidroponia.datasets[1].data.push(
              response.data[x].t_min
            );
          }
          this.datosHidroponia = response.data;
          this.loaded = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getSelected() {
      let inputs = document
        .getElementById("mydiv")
        .getElementsByTagName("input");
      let labels = document
        .getElementById("mydiv")
        .getElementsByTagName("label");
      let newlabels = [];
      let new_tmax = [];
      let new_tmin = [];

      for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].checked == true) {
          newlabels.push(this.datosHidroponia[i].cultivo);
          new_tmax.push(this.datosHidroponia[i].t_max);
          new_tmin.push(this.datosHidroponia[i].t_min);
        }
      }
      this.datosGraficaHidroponia.labels = newlabels;
      this.datosGraficaHidroponia.datasets[0].data = new_tmax;
      this.datosGraficaHidroponia.datasets[1].data = new_tmin;
    },
    checkTemp(T) {
      return T < this.tmax_value && T > this.t_min
    },
    filterTemps() {
      let newlabels = [];
      let new_tmax = [];
      let new_tmin = [];
      for (let i = 0; i < this.datosHidroponia.length; i++) {
        if (this.datosHidroponia[i].t_max < this.tmax_value && this.datosHidroponia[i].t_min > this.tmin_value) {
          newlabels.push(this.datosHidroponia[i].cultivo);
          new_tmax.push(this.datosHidroponia[i].t_max);
          new_tmin.push(this.datosHidroponia[i].t_min);
        }
      }
      this.datosGraficaHidroponia.labels = newlabels;
      this.datosGraficaHidroponia.datasets[0].data = new_tmax;
      this.datosGraficaHidroponia.datasets[1].data = new_tmin;
    }
    // ajusteDatos() {
    //   if (this.datosHidroponia) {
    //     this.datosGraficaHidroponia.labels = [];
    //     this.datosGraficaHidroponia.datasets = [];
    //     this.datosGraficaHidroponia.datasets.push({
    //       label: "T max",
    //       backgroundColor: "#540303",
    //       data: [],
    //     });
    //     for (let x in this.datosHidroponia) {
    //       this.datosGraficaHidroponia.labels.push(this.datosHidroponia[x].cultivo);
    //       this.datosGraficaHidroponia.datasets[0].data.push(
    //         this.datosHidroponia[x].t_max
    //       );
    //     }
    //   }
    // },
  },
};
</script>

<style>
.my-custom-scrollbar {
  position: relative;
  height: 500px;
  overflow: auto;
}
.table-wrapper-scroll-y {
  display: block;
}
</style>
