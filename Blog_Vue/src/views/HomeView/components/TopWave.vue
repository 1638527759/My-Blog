<template>
  <div class="waveWrapper waveAnimation">
    <div class="waveWrapperInner bgTop">
      <div class="wave waveTop"></div>
    </div>
    <div class="waveWrapperInner bgMiddle">
      <div class="wave waveMiddle"></div>
    </div>
    <div class="waveWrapperInner bgBottom">
      <div class="wave waveBottom"></div>
    </div>
  </div>
</template>

<script setup name="TopWave"></script>

<style scoped lang="scss">
@keyframes move_wave {
  0% {
    transform: translateX(0) translateZ(0) scaleY(1);
  }
  50% {
    transform: translateX(-25%) translateZ(0) scaleY(0.55);
  }
  100% {
    transform: translateX(-50%) translateZ(0) scaleY(1);
  }
}

.waveWrapper {
  overflow: hidden;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  margin: auto;
  z-index: 5;
  background-size: 50%;
}

.bgTop {
  z-index: 15;
  opacity: 0.5;
}

.bgMiddle {
  z-index: 10;
  opacity: 0.75;
}

.bgBottom {
  z-index: 5;
}

.wave {
  position: absolute;
  left: 0;
  width: 200%;
  height: 50%;
  background-repeat: repeat no-repeat;
  background-position: 0 top;
  transform-origin: center top;
}

.waveTop {
  background-image: url('../img/wave2.png');
  background-size: 15% 100px;
}

.waveAnimation .waveTop {
  animation: move-wave 3s;
  -webkit-animation: move-wave 3s;
  -webkit-animation-delay: 1s;
  animation-delay: 1s;
}

.waveMiddle {
  background-image: url('../img/wave2.png');
  background-size: 15% 120px;
}

.waveAnimation .waveMiddle {
  animation: move_wave 10s linear infinite;
}

.waveBottom {
  background-image: url('../img/wave2.png');
  background-size: 20% 100px;
}

.waveAnimation .waveBottom {
  animation: move_wave 15s linear infinite;
}
</style>
