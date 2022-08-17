<template>
  <div class="card mt-2 mx-0 shadow p-1 rounded">
    <div class="card-body">
      <h2 class="card-title fw-bold fs-5 mb-4">Temperaturas por Municipios del Tolima</h2>
      <div class="div-flex flex-column">
      <div class="row row-cols-2">
        <div class="col-md-auto gx-0">
          <div class="scroll-container">
            <div class="form-check mx-auto">
              <input id="todosMunicipios" class="form-check-input" type="checkbox" value="" checked
                @change="validar('ChecksMunicipios')">
              <label class="form-check-label" for="flexCheckDefault">
                Todos
              </label>
            </div>

            <div class="my-custom-scrollbar">
              <div id="ChecksMunicipios" class="btn-group-vertical mt-1" role="group"
                aria-label="Basic checkbox toggle button group">
                <template v-for="(mun,i) in rawData" :key="i">
                  <template v-if="mun.show || mun.show == undefined">
                    <input type="checkbox" class="btn-check" :id="'Municipio_' + i" autocomplete="off"
                      @click="getSelectedTowns" checked />
                    <label class="btn btn-outline-primary btn-sm px-0" :for="'Municipio_' + i">{{mun.municipio}}</label>

                  </template>
                </template>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md align-self-start p-0">
          <div class="d-flex flex-column">
            <div style="height:50px">
              <div class="d-flex flex-row justify-content-center">
                <i class="fa-solid fa-mountain-city fa-2xl p-3"></i>{{}}Municipios
              </div>
            </div>
            <div class="canvas-container">
              <LineChart v-if="datosGraficaMunicipios" :chartData="datosGraficaMunicipios" :chartOptions="options" />
            </div>
          </div>
        </div>
      </div>
      <div class="container my-3 rounded border border-3 border-secondary" style="--bs-border-opacity:.5">
        <h4 class="fw-bold fst-italic text-decoration-underline">Instrucciones</h4>
        <div class="text-start fs-6" style="overflow-y:auto;max-height: 25rem;">
          <p>Este es un simulador que le permite consultar cultivos hidropónicos viables en diferentes municipios del Tolima para la construcción de un sistema de acuaponía en su hogar o empredimiento.
            En el panel superior, usted puede <strong>arrastrar los deslizadores</strong> para seleccionar los <strong>límites de temperatura</strong> de su interés.
          </p>
          <p>El simulador se divide en <strong>3 secciones principales</strong>:</p>
          <ul>
            <li>Temperaturas por municipios del Tolima</li>
            <li>Temperaturas por tipos de Cultivo</li>
            <li>Datos de indicadores de cultivo</li>
          </ul>
          <p>En las secciones de <strong>Temperaturas</strong>, usted puede observar un gráfico con los valores de temperaturas máximas y mínimas de cada municipio/cultivo. Para cada municipio también observará temperaturas promedio y para cada cultivo, la temperatura óptima de crecimiento.
          Para <strong>activar o desactivar un municipio o cultivo</strong> específico, <strong>oprima el botón</strong> dentro del listado disponible.
           Además, podrá filtrar los tipos de cultivos dependiendo el <strong>tipo de planta</strong> (frutas, verduras, aromáticas y medicinales) oprimiendo los <strong>botones</strong>.</p>
           <p>Finalmente, en la sección de <strong>Indicadores</strong> usted puede filtrar los cultivos que seleccionó a partir de factores de crecimiento y 
           cosecha de su interés. Los factores disponibles son:</p>
           <ul>
            <li>Distancia entre cultivos</li>
            <li>Tiempo de primera cosecha</li>
            <li>Número de cosechas anual</li>
            <li>Distancia por cosecha anual</li>
           </ul>
           Para filtrar, <strong>utilice los deslizadores</strong> para seleccionar los límites superiores e inferiores de cada indicador. La gráficas con la información de tipos de cultivos se actualizarán automáticamente.
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>

import LineChart from "@/components/LineChart.vue";
import { nextTick } from 'vue'

export default {
  name: "MunicipiosSection",
  data() {
    return {
      municipios: 0,
      datosMunicipios: [],
      datosGraficaMunicipios: {
        type: Object,
      },
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
    }
  },
  components: {
    LineChart,
  },
  props: {
    rawData: {
      type: Object,
      default: undefined,
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
  mounted() {
    this.getData();
  },
  updated() {
    this.getData();
  },
   methods: {
    getData() {
       this.datosGraficaMunicipios.labels = [];
       this.datosGraficaMunicipios.datasets = [];
       this.datosGraficaMunicipios.datasets.push({
         label: "Temperatura Máxima",
         backgroundColor: "#FF3030",
         borderColor: "#FF3030",
         pointRadius: 3,
         data: [],
       });
       this.datosGraficaMunicipios.datasets.push({
         label: "Temperatura Promedio",
         backgroundColor: "#4EDD41",
         borderColor: "#4EDD41",
         pointRadius: 3,
         data: [],
       });
       this.datosGraficaMunicipios.datasets.push({
         label: "Temperatura Mínima",
         backgroundColor: "#1F56D6",
         borderColor: "#1F56D6",
         pointRadius: 3,
         data: [],
       });
      for (let x of this.rawData) {
        if (x.show || x.show == undefined) {  
          this.datosGraficaMunicipios.labels.push(x.municipio);
          this.datosGraficaMunicipios.datasets[0].data.push(x.t_max);
          this.datosGraficaMunicipios.datasets[2].data.push(x.t_min);
          this.datosGraficaMunicipios.datasets[1].data.push(x.t_avg);
        }
          }
          this.datosMunicipios = this.rawData;
          // this.municipios = this.rawData.length;
    },
    getSelectedTowns() {
      // this.filterTemps()
      let inputs = document
        .getElementById("ChecksMunicipios")
        .getElementsByTagName("input");
      let labels = document
        .getElementById("ChecksMunicipios")
        .getElementsByTagName("label");
      let newlabels = [];
      let new_tmax = [];
      let new_tavg = [];
      let new_tmin = [];

      for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].checked == true) {
          newlabels.push(this.datosMunicipios[i].municipio);
          new_tmax.push(this.datosMunicipios[i].t_max);
          new_tavg.push(this.datosMunicipios[i].t_avg);
          new_tmin.push(this.datosMunicipios[i].t_min);
        }
      }
      this.datosGraficaMunicipios.labels = newlabels;
      this.datosGraficaMunicipios.datasets[0].data = new_tmax;
      this.datosGraficaMunicipios.datasets[1].data = new_tavg;
      this.datosGraficaMunicipios.datasets[2].data = new_tmin;
    },
    validar(group) {
      if (document.getElementById('todosMunicipios').checked) {
        this.seleccionarTodos(group)
      } else if (!document.getElementById('todosMunicipios').checked) {
        this.desseleccionarTodos(group)
      }
      // this.municipios = this.datosGraficaMunicipios.labels.length;
      // console.log(this.datosGraficaMunicipios);
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
      this.getSelectedTowns()
    },
  },
  computed: {
    // municipiosCount() {
    //   return this.datosGraficaMunicipios.datasets[0].data.length
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
/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: var(--blue3); 
}
/* .grid-graficas {
  position: relative;
  width: 100%;
  height: 80%;
  padding: 5px;
  display: grid;
  grid-template-columns: auto auto;
  gap: 2px;
  justify-content: center;
  background-color: var(--white);
} */

/* .grid-container > div {
  position: relative;
  height: 100%;
} */
.card {
  background-color: rgba(237, 125, 49, 0.6);
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

</style>