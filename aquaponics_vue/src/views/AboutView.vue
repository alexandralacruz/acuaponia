<template>

<!-- Example Code -->
    <div class="container text-center">
      <!-- Stack the columns on mobile by making one full-width and the other half-width -->
      <div class="row">
        <div class="col-md-8">.col-md-8</div>
        <div class="col-6 col-md-4">.col-6 .col-md-4</div>
      </div>
    
      <!-- Columns start at 50% wide on mobile and bump up to 33.3% wide on desktop -->
      <div class="row">
        <div class="col-6 col-md-2">.col-6 .col-md-4</div>
        <div class="col-6 col-md-2">.col-6 .col-md-4</div>
        <div class="col-6 col-md-2">.col-6 .col-md-4</div>
      </div>
    
      <!-- Columns are always 50% wide, on mobile and desktop -->
      <div class="row">
        <div class="col-6">.col-6</div>
        <div class="col-6">.col-6</div>
      </div>
    </div>
    <!-- End Example Code -->
<!-- <div class="container">
  <input  type="range" orient="vertical"/>
  <div class="row my-5">
    <div class="col">
      <h4>Tipos de Display Flex</h4>
      <hr>

      <div class="bg-primary text-white p-3 d-flex">
        <p class="mb-0">Display Flex <strong>.d-flex</strong></p>
      </div>
      <br>
      <div class="bg-primary text-white p-3 d-inline-flex">
        <p class="mb-0">Display Flex <strong>.d-inline-flex</strong></p>
      </div>
    </div>
  </div>
  
  <div class="row my-5">
    <div class="col">
      <h4>Direction</h4>
      <hr>

      <p>.flex-row</p>
      <div class="contenedor d-flex flex-row">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.flex-row-reverse</p>
      <div class="contenedor d-flex flex-row-reverse">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.flex-column</p>
      <div class="contenedor d-flex flex-column">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.flex-column-reverse</p>
      <div class="contenedor d-flex flex-column-reverse">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
    </div>
  </div>

  <div class="row my-5">
    <div class="col">
      <h4>Justify content</h4>
      <hr>

      <p>.justify-content-start</p>
      <div class="contenedor d-flex justify-content-start">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>

      <p>.justify-content-center</p>
      <div class="contenedor d-flex justify-content-center">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>

      <p>.justify-content-end</p>
      <div class="contenedor d-flex justify-content-end">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>

      <p>.justify-content-between</p>
      <div class="contenedor d-flex justify-content-between">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
        <div>Caja 4</div>
      </div>
      <p>.justify-content-around</p>
      <div class="contenedor d-flex justify-content-around">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
        <div>Caja 4</div>
      </div>
      <p>.justify-content-evenly</p>
      <div class="contenedor d-flex justify-content-evenly">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
        <div>Caja 4</div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="row my-5">
      <div class="col">
        <h4>Fill</h4>
        <hr>

        <div class="contenedor d-flex align-items-center">
          <div>Lorem ipsum, dolor sit amet.</div>
          <div class="flex-fill">.flex-fill</div>
          <div class="flex-fill">.flex-fill</div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="row my-5">
    <div class="col">
      <h4>Align items</h4>
      <hr>

      <p>.align-items-start</p>
      <div class="contenedor d-flex align-items-start">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.align-items-center</p>
      <div class="contenedor d-flex align-items-center">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.align-items-start</p>
      <div class="contenedor d-flex align-items-end">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.align-items-baseline</p>
      <div class="contenedor d-flex align-items-baseline">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
      <p>.align-items-stretch</p>
      <div class="contenedor d-flex align-items-stretch">
        <div>Caja 1</div>
        <div>Caja 2</div>
        <div>Caja 3</div>
      </div>
    </div>
  </div>
</div> -->

</template>

<style>

.contenedor {
  margin-bottom: 20px;
  background: #0d6efd;
  color: #fff;
  height: 100px;
}

.contenedor > div {
  background: rgba(255,255,255,0.2);
  padding: 15px;
  border: 1px solid #0d6efd;
}
input[type=range][orient=vertical]
{
    writing-mode: bt-lr; /* IE */
    -webkit-appearance: slider-vertical; /* Chromium */
    width: 8px;
    height: 175px;
    padding: 0 5px;
}
</style>