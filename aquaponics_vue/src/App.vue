<template>

  <HeaderSection @print-pdf="printPDF"/>

  <!-- <div v-if="loaded" class="spinner-border text-primary" role="status">
    <span class="visually-hidden">Loading...</span>
  </div> -->


  <div v-if="loaded" class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': loaded }">
    <div class="lds-dual-ring"></div><span class="visually-hidden">Loading...</span>
  </div>

  <div v-else class="section" ref="content" id="content">
    <router-view />
  </div>

</template>


<script>
import HeaderSection from "@/components/HeaderSection.vue";
import axios from 'axios'
import { jsPDF } from "jspdf";
import html2canvas from "html2canvas";

export default {
  data() {
    return {
      loaded : this.$store.state.isLoading,
    }
  },
  components: {
    HeaderSection,
  },
  methods: {
    printPDF() {
      var content = document.getElementById('content')
      var doc = new jsPDF('p', 'pt','letter');
      var margin = 5;
      var scale = (doc.internal.pageSize.width - margin*2)/document.body.scrollWidth;
      doc.html(content, {
        x: margin,
        y: margin,
        html2canvas: {
          scale: scale,
        },
        callback: function(doc) {
          doc.output('dataurlnewwindow',{filename:'Simulador.pdf'})
        }
      });
      // window.html2canvas = html2canvas
      // let doc = new jsPDF();
      // let html = this.$refs.content.innerHTML
      // doc.html(html, {
      //   callback: function (doc) {
      //     doc.save('Simulador.pdf');
      //   },
      //   x: 15,
      //   y: 15,
      //   width: 1150,
      // });
      //       let pdf_content = document.getElementById("content");
      //       var options = {
      //       margin:       1,
      //       filename:     'Simulador.pdf',
      //       image:        { type: 'jpeg', quality: 0.98 },
      //       html2canvas:  { scale: 10 },
      //       jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      //       };
      // 
      //       html2pdf(pdf_content, options);
      // print();
    }
  }
}
</script>
<style lang="scss">

@page { size: legal landscape; }

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 14px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #031254;
}

:root {
  --blue: #5798f8;
  --blue2: #dee8f8;
  --blue3: #3682f4;
  --white: #fff;
  --white2: rgba(241, 241, 241, 0.844);
  --grey: #f5f5f5;
  --black1: #222;
  --black2: #999;
}
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: var(--blue) transparent var(--blue) transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>