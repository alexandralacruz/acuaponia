<template>

  <div id="rangosID" class="container-fluid p-1 bg-white rounded border-bottom">
    <h2 class="fs-5 fw-bold">Límites de temperatura</h2>
    <p class="text-center text-wrap fs-7 fst-italic mb-1 p-0">Seleccione la temperatura máxima y la temperatura mínima
      para
      observar solamente los municipios y cultivos que estén dentro de este rango.</p>
    <label for="minT" class="form-label fw-bold text-primary fs-6 m-0">Temperatura mínima: <span id="slider_value"> {{
        tmin_value }}
        °C</span></label>
    <input :min="t_min" :max="t_max" type="range" class="form-range" id="minT" v-model="tmin_value"
      @change="filterTemps" />
    <label for="maxT" class="form-label fw-bold text-danger fs-6 m-0">Temperatura máxima: <span id="slider_value"> {{
        tmax_value }}
        °C</span></label>
    <input type="range" :min="t_min" :max="t_max" class="form-range" id="maxT" v-model="tmax_value"
      @change="filterTemps" />

  </div>

  <div class="row row-cols-lg-3 row-cols-md-2 g-md-3 g-lg-2">
    <div class="col col-md-6 mb-3">
      <MunicipiosSection v-if="datosMunicipios" :tmax_value="Number(tmax_value)" :tmin_value="Number(tmin_value)"
        :rawData="datosMunicipios" />
    </div>
    <div class="col col-md-6 mb-3">
      <CultivosSection v-if="datosHidroponia" :tmax_value="Number(tmax_value)" :tmin_value="Number(tmin_value)"
        :rawData="datosHidroponia" @get-crops="getCropTypes" />
    </div>
    <div class="col col-md-12 mb-3">
      <IndicadoresCultivo v-if="datosHidroponia" :tmax_value="Number(tmax_value)" :tmin_value="Number(tmin_value)"
        :rawData="datosHidroponia" @filtrar-distancias="filterD" />
    </div>
  </div>


</template>
<script>
// @ is an alias to /src
import MunicipiosSection from "@/components/MunicipiosSection.vue";
import CultivosSection from "@/components/CultivosSection.vue";
import IndicadoresCultivo from "@/components/IndicadoresSection.vue";

import axios from "axios";
// import LineChart from "@/components/LineChart.vue";
import PieChart from "@/components/PieChart.vue";
// import DobleSlider from "@/components/DobleSlider.vue";

export default {
  name: "Dashboard",
  data() {
    return {
      msg: "",
      tmax_value: 40,
      t_max: 40,
      tmin_value: -20,
      t_min: -20,
      loaded: this.$store.state.isLoaded,
      datosHidroponia: undefined,
      // datosGraficaHidroponia: {
      //   labels: [],
      //   datasets: [
      //     {
      //       label: "Data One",
      //       backgroundColor: "#f87979",
      //       data: [],
      //     },
      //   ],
      // },
      // datosGraficaDistancias: {
      //   labels: [],
      //   datasets: [
      //     {
      //       label: "Data One",
      //       backgroundColor: "#f87979",
      //       data: [],
      //     },
      //   ],
      // },
      datosMunicipios: undefined,
      // datosGraficaMunicipios: {
      //   labels: [],
      //   datasets: [
      //     {
      //       label: "Data One",
      //       backgroundColor: "#f87979",
      //       data: [],
      //     },
      //   ],
      // },
    };
  },
  components: {
    MunicipiosSection,
    CultivosSection,
    IndicadoresCultivo,
    PieChart,
},
  created() {
    document.title = "Inicio | Simulador";
    this.getSimulator();
  },
  methods: {
    async getSimulator() {
      //       this.datosGraficaHidroponia.labels = [];
      //       this.datosGraficaHidroponia.datasets = [];
      //       this.datosGraficaHidroponia.datasets.push({
      //         label: "Temperatura Máxima",
      //         backgroundColor: "#f87979",
      //         borderColor: "#f87979",
      //         pointRadius: 3,
      //         data: [],
      //       });
      //       this.datosGraficaHidroponia.datasets.push({
      //         label: "Temperatura Óptima",
      //         backgroundColor: "#41B883",
      //         borderColor: "#41B883",
      //         pointRadius: 3,
      //         data: [],
      //       });
      //       this.datosGraficaHidroponia.datasets.push({
      //         label: "Temperatura Mínima",
      //         backgroundColor: "#4d4dff",
      //         borderColor: "#4d4dff",
      //         pointRadius: 3,
      //         data: [],
      //       });
      // 
      // 
      //       this.datosGraficaDistancias.labels = [];
      //       this.datosGraficaDistancias.datasets = [];
      //       this.datosGraficaDistancias.datasets.push({
      //         label: "Cosecha anual",
      //         backgroundColor: "#f87979",
      //         borderColor: "#f87979",
      //         pointRadius: 3,
      //         data: [],
      //       });
      // this.datosGraficaDistancias.datasets.push({
      //   label: "Distancia entre plantas",
      //   backgroundColor: "#41B883",
      //   borderColor: "#41B883",
      //   pointRadius: 3,
      //   data: [],
      // });

      this.$store.commit('setIsLoading', true)
      console.log('getting data')
      await axios
        .get("api/v1/datos-hidroponia/")
        .then((response) => {
          this.datosHidroponia = response.data;
          this.cultivos = response.data.length;
          this.loaded = true;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false)

      this.$store.commit('setIsLoading', true)
      await axios
        .get("api/v1/datos-municipios/")
        .then((response) => {
          this.datosMunicipios = response.data;
          this.municipios = response.data.length;
          this.loaded = true;
        })
        .catch((error) => {
          console.log(error);
        });
      console.log('data ready')
      this.$store.commit('setIsLoading', false)
    },

    filterTemps() {
      // Calcula nuevos municipios basado en las nuevas temperaturas máxima y mínima.
      let newlabels_m = [];
      let new_tmax_m = [];
      let new_tavg_m = [];
      let new_tmin_m = [];

      for (let mun of this.datosMunicipios) {
        if (
          mun.t_max < this.tmax_value &&
          mun.t_min > this.tmin_value
        ) {
          // newlabels_m.push(this.datosMunicipios[i].municipio);
          // new_tmax_m.push(this.datosMunicipios[i].t_max);
          // new_tavg_m.push(this.datosMunicipios[i].t_avg);
          // new_tmin_m.push(this.datosMunicipios[i].t_min);
          mun.show = true;
        } else {
          mun.show = false;
        }
      }
      // this.datosGraficaMunicipios.labels = newlabels_m;
      // this.municipios = newlabels_m.length
      // this.datosGraficaMunicipios.datasets[0].data = new_tmax_m;
      // this.datosGraficaMunicipios.datasets[1].data = new_tavg_m;
      // this.datosGraficaMunicipios.datasets[2].data = new_tmin_m;


      // Calcula nuevos cultivos basado en las nuevas temperaturas máxima y mínima.
      let newlabels_h = [];
      let new_tmax_h = [];
      let new_topt_h = [];
      let new_tmin_h = [];
      // let new_types = new Array(this.datosTiposCultivo.labels.length).fill(0);

      for (let cul of this.datosHidroponia) {
        if (
          // this.datosHidroponia[i].t_max < Math.max.apply(Math, new_tmax_m) &&
          // this.datosHidroponia[i].t_min > Math.max.apply(Math, new_tmin_m)
          cul.t_max < this.tmax_value &&
          cul.t_min > this.tmin_value
        ) {
          // newlabels_h.push(this.datosHidroponia[i].cultivo);
          // new_tmax_h.push(this.datosHidroponia[i].t_max);
          // new_topt_h.push(this.datosHidroponia[i].t_opt);
          // new_tmin_h.push(this.datosHidroponia[i].t_min);
          // new_types[this.datosTiposCultivo.labels.indexOf(this.datosHidroponia[i].tipo)]++
          cul.show = true;
        } else {
          cul.show = false;
        }
      }
      // this.datosTiposCultivo.datasets[0].data = new_types;
      // this.datosGraficaHidroponia.labels = newlabels_h;
      // this.datosGraficaHidroponia.datasets[0].data = new_tmax_h;
      // this.datosGraficaHidroponia.datasets[1].data = new_topt_h;
      // this.datosGraficaHidroponia.datasets[2].data = new_tmin_h;
    },
    filterD() {
      let min = document.getElementById('minD').value
      let max = document.getElementById('maxD').value
      for (let cul of this.datosHidroponia) {
        if (cul.distancia < max && cul.distancia > min) {
          cul.show = true
        } else {
          cul.show = false
        }
      }
    },
    filterHarvest() {
      let min = document.getElementById('minH').value
      let max = document.getElementById('maxH').value
      for (let cul of this.datosHidroponia) {
        if (cul.distancia < max && cul.distancia > min) {
          cul.show = true
        } else {
          cul.show = false
        }
      }
    },
    getCropTypes() {
      this.filterTemps();
      let inputs = document
        .getElementById("ChecksTipos")
        .getElementsByTagName("input");
      for (const tipo of inputs) {
        if (!tipo.checked) {
          console.log(tipo.id,tipo.checked);
          this.datosHidroponia.map(cultivo => {
            if (cultivo.tipo == tipo.id) {
              cultivo.show = false;
            }
          });
        }
      }
    }
  },
  // ajusteDatos() {
  //   if (this.datosHidroponia) {
  //     this.datosGraficaHidroponia.labels = [];
  //     this.datosGraficaHidroponia.datasets = [];
      // this.datosGraficaHidroponia.datasets.push({
  //       label: "T max",
  //       backgroundColor: "#540303",
  //       data: [],
  //     });
  //     for (let x in this.datosHidroponia) {
        // this.datosGraficaHidroponia.labels.push(this.datosHidroponia[x].cultivo);
        // this.datosGraficaHidroponia.datasets[0].data.push(
  //         this.datosHidroponia[x].t_max
  //       );
  //     }
  //   }
  // },
}
</script>

<style>
.card {
  height: 990px;
}

#rangosID {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--blue2);
}
.canvas-container {
  position: relative;
  margin: auto;
  /* height: 80%; */
  width: 80%;
}

</style>