<template>
  <div class="card mt-2 mx-0 shadow p-1 rounded">
    <div class="card-body">
      <h2 class="card-title fw-bold fs-5 mb-4">Temperaturas por tipos de cultivo</h2>
      <div class="row row-cols-2">
        <div class="col-md-auto col-auto gx-0">
          <div class="scroll-container">
            <div class="form-check mx-auto pe-auto">
              <input id="todosCultivos" class="form-check-input " type="checkbox" value="" checked
                @click="validar('ChecksCultivos')">
              <label class="form-check-label" for="flexCheckDefault">
                Todos
              </label>
            </div>

            <div class="my-custom-scrollbar">
              <div id="ChecksCultivos" class="btn-group-vertical mt-1" role="group"
                aria-label="Basic checkbox toggle button group">
                <template v-for="cultivo of rawData" :key="cultivo">
                  <template v-if="cultivo.show || cultivo.show == undefined">
                    <input type="checkbox" class="btn-check" :id="cultivo.cultivo" autocomplete="off"
                      @click="getSelectedCrops" checked />
                    <label class="btn btn-outline-primary btn px-1 pe-auto"
                      :for="cultivo.cultivo">{{cultivo.cultivo}}</label>
                  </template>
                </template>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md align-self-start">
          <div class="d-flex flex-column">
            <div style="height:50px">
              <div class="d-flex flex-row justify-content-center">
                <i class="fa-solid fa-seedling fa-2xl p-3"></i>{{ cultivos }} Cultivos
              </div>
            </div>
            <div class="canvas-container">
              <LineChart v-if="datosGraficaHidroponia" :chartData="datosGraficaHidroponia" :chartOptions="options" />
            </div>
          </div>
        </div>
      </div>
      <div class="row row-cols-md-1 mt-3" style="height:100px;">
        <div class="col my-4">
          <div class="container-tipo">
            <div id="ChecksTipos" class="btn-group mt-1" role="group"
              aria-label="Basic checkbox toggle button group">
              <template v-for="t of tipos" :key="t">
              <input type="checkbox" class="btn-check" autocomplete="off" checked :id="t" @click="$emit('get-crops')"/>
              <label :for="t" class="btn btn-outline-success btn-lg">{{t}}</label>
              </template>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="canvas-container">
            <PieChart :chartData="datosTiposCultivo" />
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
  name: "CultivosSection",
  components: {
    LineChart,
    PieChart,
  },
  data() {
    return {
      datosHidroponia: [],
      datosGraficaHidroponia: {
        type: Object,
      },
      datosTiposCultivo: {
        labels: [],
        datasets: [],
        hoverOffset: 4,
      },
      tipos: [],
      options: {
        responsive: true,
        maintainAspectRatio: true,
        // scaleShowValues: true,
        scales: {
          xAxes: {
            display: false,
            ticks: {
              autoSkip: false,
              maxRotation: 90,
              minRotation: 90
            },
            grid: {
              display: false,
            }
          },
          y: {
            grid: {
              // display: false,
            }
          }
        },
        plugins: {
          legend: {
            display: false,
          }
        }
      },
      cultivos: 0,
    }
  },
  props: {
    rawData: {
      type: Object,
      default: "hola",
    },
    tmin_value: {
      type: Number,
      default:-20,
    },
    tmax_value: {
      type: Number,
      default: 40,
    }
  },

  beforeMount() {
    this.organizeData();
  },
  mounted() {
    this.datosHidroponia = this.rawData;
    this.tipos = this.datosTiposCultivo.labels;
  },
  updated() {
    this.organizeData();
    console.log('update');
    console.log(this.datosGraficaHidroponia.labels.length);
  },
  methods: {
    organizeData() {
      this.datosGraficaHidroponia.labels = [];
      this.datosGraficaHidroponia.datasets = [];
      this.datosGraficaHidroponia.datasets.push({
        label: "Temperatura Máxima",
        backgroundColor: "#FF3030",
        borderColor: "#FF3030",
        pointRadius: 3,
        data: [],
      });
      this.datosGraficaHidroponia.datasets.push({
        label: "Temperatura Óptima",
        backgroundColor: "#4EDD41",
        borderColor: "#4EDD41",
        pointRadius: 3,
        data: [],
      });
      this.datosGraficaHidroponia.datasets.push({
        label: "Temperatura Mínima",
        backgroundColor: "#1F56D6",
        borderColor: "#1F56D6",
        pointRadius: 3,
        data: [],
      });

      this.datosTiposCultivo.labels = [];
      this.datosTiposCultivo.datasets = [];
      this.datosTiposCultivo.datasets.push({
        backgroundColor: ["#6b5b95", "#feb236", "#d64161"],
        data: [],
      });

      let tmp = "";
      for (let x of this.rawData) {
        if (x.show || x.show == undefined) {
          this.datosGraficaHidroponia.labels.push(x.cultivo);
          this.datosGraficaHidroponia.datasets[0].data.push(x.t_max);
          this.datosGraficaHidroponia.datasets[2].data.push(x.t_min);
          this.datosGraficaHidroponia.datasets[1].data.push(x.t_opt);
          if (!(x.tipo === tmp)) {
            // console.log(tmp);
            tmp = x.tipo;
            this.datosTiposCultivo.labels.push(tmp);
          }
          if (!this.datosTiposCultivo.datasets[0].data[this.datosTiposCultivo.labels.indexOf(tmp)]) {
            this.datosTiposCultivo.datasets[0].data[this.datosTiposCultivo.labels.indexOf(tmp)] = 1
          } else {
            this.datosTiposCultivo.datasets[0].data[this.datosTiposCultivo.labels.indexOf(tmp)]++;
          }
        }
      }
      this.datosHidroponia = this.rawData;
      this.cultivos = this.rawData.length;
    },
    getSelectedCrops() {
//       let inputs = document
//         .getElementById("ChecksCultivos")
//         .getElementsByTagName("input");
//       let labels = document
//         .getElementById("ChecksCultivos")
//         .getElementsByTagName("label");
//       
//       let newlabels = [];
//       let new_tmax = [];
//       let new_topt = [];
//       let new_tmin = [];
//       let new_types = new Array(this.datosTiposCultivo.labels.length).fill(0);
// 
//       for (let i in inputs) {
//         console.log(i);
//         if (inputs[i].checked) {
//           newlabels.push(this.datosHidroponia[i].cultivo);
//           new_tmax.push(this.datosHidroponia[i].t_max);
//           new_topt.push(this.datosHidroponia[i].t_opt);
//           new_tmin.push(this.datosHidroponia[i].t_min);
//           new_types[this.datosTiposCultivo.labels.indexOf(this.datosHidroponia[i].tipo)]++
//         }
//       }
//       this.datosTiposCultivo.datasets[0].data = new_types;
// 
//       this.datosGraficaHidroponia.labels = newlabels;
//       this.datosGraficaHidroponia.datasets[0].data = new_tmax;
//       this.datosGraficaHidroponia.datasets[1].data = new_topt;
//       this.datosGraficaHidroponia.datasets[2].data = new_tmin;
      // this.cultivos = this.datosGraficaHidroponia.labels.length
      // this.filterTemps()
    },
    validar(group) {
      if (document.getElementById('todosCultivos').checked) {
        this.seleccionarTodos(group)
      } else if (!document.getElementById('todosCultivos').checked) {
        this.desseleccionarTodos(group)
      }
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
      this.getSelectedCrops()
    },
    desseleccionarTodos(group) {
      let inputs = document
        .getElementById(group)
        .getElementsByTagName("input");
      for (let i = 0; i <  inputs.length; i++) {
        const element = inputs[i];
        element.checked = false
      }
      // this.filterTemps()
      this.getSelectedCrops()
    },
  },
  computed: {
    activeTypes() {
      return this.datosTiposCultivo.labels
    },
    activeCrops() {
      return this.datosGraficaHidroponia
    },
  },
  watch: {
    // rawData(nw,od) {
    //   
    // }
  }
}
</script>

<style scoped>

::-webkit-scrollbar {
  width: 8px;               /* width of the entire scrollbar */
}

::-webkit-scrollbar-thumb {
  background-color: var(--blue);    /* color of the scroll thumb */
  border-radius: 15px;       /* roundness of the scroll thumb */
}
.card {
  background-color: rgba(141, 201, 245, 0.6);
}
.form-check {
  text-align: initial;
  align-content: center;
}
.scroll-container {
  max-height: 350px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.btn {
  /* border-radius: 16px; */
  --bs-btn-font-size: .7rem;
}
.my-custom-scrollbar {
  overflow-y: auto;
  overflow-x: hidden;
}

.canvas-container {
  width: 100%;
}

div#tiposPie.canvas-container {
  width: 50%;
  height: 20%;
}
</style>