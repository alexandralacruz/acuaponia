<template>
  <Doughnut
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    ref="pie"
  />
</template>

<script>
// import { defineComponent, h, PropType } from 'vue'

import { Doughnut } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  Plugin,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: "DoughnutChart",
  components: {
    Doughnut,
  },
  props: {
    chartId: {
      type: String,
      default: "doughnut-chart",
    },
    // width: {
    //   type: Number,
    //   default: 400,
    // },
    // height: {
    //   type: Number,
    //   default: 400,
    // },
    cssClasses: {
      default: "",
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    chartData: {
      type: Object,
      default: {
        labels: ["VueJs", "EmberJs", "ReactJs", "AngularJs"],
        datasets: [
          {
            backgroundColor: ["#41B883", "#E46651", "#00D8FF", "#DD1B16"],
            data: [40, 20, 80, 10],
          },
        ],
      },
    },
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        hoverOffset: 5,
        maintainAspectRatio: false,
        cutout: "30%",
        plugins: {
          legend: {
            position: 'top',
          }
        },
        onClick: (point, event) => {
        },
      },
    };
  },
};
</script>