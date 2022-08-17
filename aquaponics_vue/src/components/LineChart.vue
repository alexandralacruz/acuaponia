<template>
  <Line
    :chart-data="chartData"
    :chart-options="chartOptions"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
  />
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Plugin,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

export default {
  name: "LineChart",
  components: {
    Line,
  },
  props: {
    chartId: {
      type: String,
      default: "line-chart",
    },
    datasetIdKey: {
      type: String,
      default: "label",
    },
    // width: {
    //   type: Number,
    //   default: 200,
    // },
    // height: {
    //   type: Number,
    //   default: 300,
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
        labels: [
        ],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
    },
    chartOptions: {
      type: Object,
      default: {
        responsive: true,
        maintainAspectRatio: false,
      }
    },
    txt: "",
  },
  data() {
    return {

    };
  },
};
</script>