<template>
  <div class="down2"></div>
  <a class="down" href="#active">
    <span style="top: 25%" class="glyphicon glyphicon-menu-down" aria-hidden="true">▽</span>
  </a>
</template>

<script setup name="DownButton"></script>

<style scoped lang="scss">
.down {
  height: 80px;
  width: 80px;
  position: absolute;
  top: 40%;
  margin: auto;
  right: 0;
  left: 0;
  bottom: 0;
  border: solid 3px rgba(255, 255, 255, 0.171);
  border-radius: 50%;
  text-align: center;
  font-size: 40px;
  color: whitesmoke;
  text-decoration: none;
  z-index: 5;
  animation-name: drop;
  animation-duration: 1.2s;
  animation-iteration-count: infinite;
}

.down:hover {
  color: rgb(213, 233, 252);
  border: rgb(213, 233, 252);
}

@keyframes drop {
  0% {
    border: solid 3px white;
  }
  100% {
    height: 110px;
    width: 110px;
    border: rgba(255, 255, 255, 0.11);
  }
}

.down2 {
  height: 90px;
  width: 90px;
  position: absolute;
  top: 40%;
  margin: auto;
  right: 0;
  left: 0;
  bottom: 0;
  border: solid 3px rgba(255, 255, 255, 0.76);
  border-radius: 50%;
  text-align: center;
  z-index: 4;
  animation-name: drop2;
  animation-duration: 1.2s;
  animation-delay: 0.2s;
  animation-iteration-count: infinite;
}

@keyframes drop2 {
  0% {
    width: 70px;
    height: 70px;
  }
  100% {
    width: 140px;
    height: 140px;
    border: rgba(255, 255, 255, 0.178);
  }
}
</style>
