<template>
  <div class="card mt-2 mx-0 shadow p-2 rounded">
    <div class="card-body">
      <h2 class="card-title fw-bold fs-5">Indicadores Cultivo</h2>
      <div class="row row-cols-1">
        <div class="col-md align-self-start px-0">
          <div class="d-flex flex-row justify-content-between">
            <p style="color:#2E98F5" class="fw-bold text-nowrap">Distancia entre cultivos (cm)</p>
            <p style="color:#FEA82F" class="fw-bold fs-6">Distancia/cosechas anuales</p>
          </div>
          <div class="d-flex flex-row">
            <div class="d-flex flex-column col-2">
              <div class="d-flex flex-row flex-grow-1">
                <div class="d-flex flex-column mx-1">
                  <label for="minD" class="form-label fw-bold text-primary fs-6 m-0">Min</label>
                  <span class="fw-bold text-primary fs-6 m-0">{{ dmin_value }}</span>
                  <input id="minD" type="range" class="form-range" v-bind:min="mind" v-bind:max="maxd"
                    v-model="dmin_value" @change="filtrarDistancias">
                </div>
                <div class="d-flex flex-column mx-1">
                  <label for="maxD" class="form-label fw-bold text-danger fs-6 m-0">Max</label>
                  <span class="fw-bold text-danger fs-6 m-0">{{ dmax_value }}</span>
                  <input id="maxD" type="range" class="form-range" v-bind:min="mind" v-bind:max="maxd"
                    v-model="dmax_value" @change="filtrarDistancias">
                </div>
              </div>
            </div>
            <div class="canvas-container">
              <LineChart v-if="datosGraficaIndicadores1" :chartData="datosGraficaIndicadores1"
                :chartOptions="options" />
            </div>
            <div class="d-flex flex-column col-1">
              <div class="d-flex flex-row flex-grow-1">
                <div class="d-flex flex-column mx-1">
                  <label for="minH" class="form-label fw-bold text-primary fs-6 m-0">Min</label>
                  <span class="fw-bold text-primary fs-6 m-0">{{ hmin_value }}</span>
                  <input id="minH" type="range" class="form-range" v-bind:min="minh" v-bind:max="maxh"
                    v-model="hmin_value">
                </div>
                <div class="d-flex flex-column mx-1">
                  <label for="maxCos" class="form-label fw-bold text-danger fs-6 m-0">Max</label>
                  <span class="fw-bold text-danger fs-6 m-0">{{ hmax_value }}</span>
                  <input id="maxCos" type="range" class="form-range" v-bind:min="minh" v-bind:max="maxh"
                    v-model="hmax_value">
                </div>
              </div>
            </div>
          </div>
          <div class="d-flex flex-row justify-content-between mt-5">
            <p style="color:#2E98F5" class="fw-bold text-nowrap">Distancia entre cultivos (cm)</p>
            <p style="color:#FEA82F" class="fw-bold fs-6">Distancia/cosechas anuales</p>
          </div>
          <div class="d-flex flex-row">
            <div class="d-flex flex-column col-1">
              <div class="d-flex flex-row flex-grow-1 justify-content-between">
                <div class="d-flex flex-sm-column mx-1">
                  <label for="minD" class="form-label fw-bold text-primary fs-6 m-0">Min</label>
                  <span class="fw-bold text-primary fs-6 m-0">{{ dmin_value }}</span>
                  <input id="minD" type="range" class="form-range" v-bind:min="mind" v-bind:max="maxd"
                    v-model="dmin_value" @change="filtrarDistancias">
                </div>
                <div class="d-flex flex-column mx-1">
                  <label for="maxD" class="form-label fw-bold text-danger fs-6 m-0">Max</label>
                  <span class="fw-bold text-danger fs-6 m-0">{{ dmax_value }}</span>
                  <input id="maxD" type="range" class="form-range" v-bind:min="mind" v-bind:max="maxd"
                    v-model="dmax_value" @change="filtrarDistancias">
                </div>
              </div>
            </div>
            <div class="canvas-container">
              <LineChart v-if="datosGraficaIndicadores2" :chartData="datosGraficaIndicadores2"
                :chartOptions="options" />
            </div>
            <div class="d-flex flex-column col-1">
              <div class="d-flex flex-row flex-grow-1">
                <div class="d-flex flex-column mx-1">
                  <label for="minH" class="form-label fw-bold text-primary fs-6 m-0">Min</label>
                  <span class="fw-bold text-primary fs-6 m-0">{{ hmin_value }}</span>
                  <input id="minH" type="range" class="form-range" v-bind:min="minh" v-bind:max="maxh"
                    v-model="hmin_value">
                </div>
                <div class="d-flex flex-column mx-1">
                  <label for="maxCos" class="form-label fw-bold text-danger fs-6 m-0">Max</label>
                  <span class="fw-bold text-danger fs-6 m-0">{{ hmax_value }}</span>
                  <input id="maxCos" type="range" class="form-range" v-bind:min="minh" v-bind:max="maxh"
                    v-model="hmax_value">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

import LineChart from "@/components/LineChart.vue";
import PieChart from "@/components/PieChart.vue";

export default {
  name: "IndicadoresCultivo",
  components: {
    LineChart,
    PieChart,
  },
  data() {
    return {
      mind: 0,
      maxd: 100,
      dmin_value: 0,
      dmax_value: 0,
      minh: 0,
      maxh: 0,
      hmin_value: 0,
      hmax_value: 0,
      datosIndicadores: [],
      datosGraficaIndicadores1: {
        type: Object,
      },
      datosGraficaIndicadores2: {
        labels: [],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        // scaleShowValues: true,
        stacked: false,
        plugins: {
          legend: {
            display: 'false',
          }
        },
        scales: {
          xAxes: {
            display: false,
            grid: {
              display: false,
            }
          },
          y: {
            type: 'linear',
            display: true,
            position: 'right',
          },
          y1: {
            type: 'linear',
          },
        },
      },
      cultivos: 0
    }
  },
  props: {
    rawData: {
      type: Object,
      default: "hola",
    },
    tmin_value: {
      type: Number,
      default: -20,
    },
    tmax_value: {
      type: Number,
      default: 40,
    }
  },
  emits: ['filtrar-distancias'],
  beforeCreate() {
    // this.dmin_value = 
  },
  created() {
    this.getData();
  },
  mounted() {
    this.mind = this.limit_lo_d();
    this.dmin_value = this.limit_lo_d();
    this.maxd = this.limit_hi_d();
    this.dmax_value = this.limit_hi_d();
    this.minh = this.limit_lo_h();
    this.hmin_value = this.limit_lo_h();
    this.maxh = this.limit_hi_h();
    this.hmax_value = this.limit_hi_h();
  },
  updated() {
    this.getData();
    // this.dmin_value = this.limit_lo_d();
    // this.dmax_value = this.limit_hi_d();
    // this.cosmin_value = this.limit_lo_cos();
    // this.cosmax_value = this.limit_hi_cos();
    // this.dmin_value = this.limit_lo_d();
  },
  methods: {
    getData() {
      this.datosGraficaIndicadores1.labels = [];
      this.datosGraficaIndicadores1.datasets = [];
      this.datosGraficaIndicadores1.datasets.push({
        label: "Primera cosecha (mes)",
        backgroundColor: "#2E98F5",
        borderColor: "#2E98F5",
        pointRadius: 3,
        yAxisID: "y",
        data: [],
      });
      this.datosGraficaIndicadores1.datasets.push({
        label: "N cosechas/año",
        backgroundColor: "#FEA82F",
        borderColor: "#FEA82F",
        pointRadius: 3,
        yAxisID: 'y1',
        data: [],
      });

      let tmp = "";
      for (let x of this.rawData) {
        if (x.show || x.show == undefined) {
          this.datosGraficaIndicadores1.labels.push(x.cultivo);
          this.datosGraficaIndicadores1.datasets[0].data.push(x.primera_cosecha);
          this.datosGraficaIndicadores1.datasets[1].data.push(x.n_cosechas);
        }
      }
      this.datosIndicadores = this.rawData;

      this.datosGraficaIndicadores2.labels = [];
      this.datosGraficaIndicadores2.datasets = [];
      this.datosGraficaIndicadores2.datasets.push({
        label: "Cosechas/año",
        backgroundColor: "#D80000",
        borderColor: "#D80000",
        pointRadius: 3,
        yAxisID: "y",
        data: [],
      });
      this.datosGraficaIndicadores2.datasets.push({
        label: "Distancia/N cosechas*año",
        backgroundColor: "#10BB00",
        borderColor: "#10BB00",
        pointRadius: 3,
        yAxisID: 'y1',
        data: [],
      });

      for (let x of this.rawData) {
        if (x.show || x.show == undefined) {
          this.datosGraficaIndicadores2.labels.push(x.cultivo);
          this.datosGraficaIndicadores2.datasets[0].data.push(x.n_cosechas);
          this.datosGraficaIndicadores2.datasets[1].data.push(x.distanciaXcosechaAnual);
        }
      }
    },
    filtrarDistancias() {
      // let min = document.getElementById('minD').value
      // let max = document.getElementById('maxD').value
      // console.log(min);
      // console.log(max);
      this.$emit('filtrar-distancias');
    },
    filtrarCosechas() {
      this.$emit('filtrar-cosechas');
    },
    seleccionarTodos(group) {
      let inputs = document
        .getElementById(group)
        .getElementsByTagName("input");
      for (let i = 0; i < inputs.length; i++) {
        const element = inputs[i];
        element.checked = true
      }
      // this.filterTemps()
      this.getSelectedTowns()
      this.getSelectedCrops()
    },
    desseleccionarTodos(group) {
      let inputs = document
        .getElementById(group)
        .getElementsByTagName("input");
      for (let i = 0; i < inputs.length; i++) {
        const element = inputs[i];
        element.checked = false
      }
      // this.filterTemps()
      this.getSelectedCrops()
      this.getSelectedTowns()
    },
    limit_lo_d() {
      return Math.min(...this.datosGraficaIndicadores1.datasets[0].data)
    },
    limit_hi_d() {
      return Math.max(...this.datosGraficaIndicadores1.datasets[0].data)
    },
    limit_lo_h() {
      return Math.min(...this.datosGraficaIndicadores1.datasets[1].data)
    },
    limit_hi_h() {
      return Math.max(...this.datosGraficaIndicadores1.datasets[1].data)
    },
  },
  watch: {

  },
  computed: {
    //   limit_lo_d() {
    //     return Math.min(...this.datosGraficaIndicadores1.datasets[0].data)
    // },
    //   limit_hi_d() {
    //     return Math.max(...this.datosGraficaIndicadores1.datasets[0].data)
    // },
    //   limit_lo_cos() {
    //     return Math.min(...this.datosGraficaIndicadores1.datasets[1].data)
    // },
    //   limit_hi_cos() {
    //     return Math.max(...this.datosGraficaIndicadores1.datasets[1].data)
    // },

  }
}
</script>

<style scoped>
.card {
  background-color: rgba(131, 255, 126, 0.6);
}

.canvas-container {
  width: 70%;
}

.form-range {
  /* writing-mode: bt-lr; IE */
  -webkit-appearance: slider-vertical;
  /*Chromium*/
  width: 1.5rem;
  height: 80%;
  padding: 0 5px;
}
</style>