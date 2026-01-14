<template>
  <!-- <Embed src="../static/bootstrap/music/志倉千代丸 - 澄空学园校歌.mp3" width="0" height="0" AUTOSTART="TRUE" LOOP="TRUE"></Embed> -->

  <!-- 开场动画 -->
  <div class="start"></div>

  <div class="container">
    <!-- 头部 -->


    <!-- 快速导航栏 -->
    <left-nav></left-nav>

    <home-header></home-header>

    <!-- 中部 -->

    <!-- 导航栏 -->
    <!-- <main-nav></main-nav> -->
    <main-nav2></main-nav2>

    <!-- 主页内容 -->
    <main class="content">
      <!-- <write-essay style="margin: 0; background-color: rgba(255, 255, 255, 0.8)"></write-essay> -->

      <div class="left-content">
        <essay-card></essay-card>
      </div>

      <div class="right-card">
        <right-card></right-card>
      </div>

      <el-backtop :right="100" :bottom="100" />

    </main>


  </div>
</template>

<script setup name="HomeView">
import { RouterLink } from 'vue-router'
import EssayCard from './components/EssayCard.vue'
import MainNav from './components/MainNav.vue'
import MainNav2 from '@/components/MainNav2.vue'


import LeftNav from './components/LeftNav.vue'
import RightCard from './components/RightCard.vue'
import HomeHeader from './components/HomeHeader.vue'
</script>

<style lang="scss" scoped>
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  cursor: url(/prectise3/sucai/魔法棒.cur), auto;
}

a {
  text-decoration: none;
  text-align: center;
  display: block;
}

img {
  vertical-align: middle;
}

.container {
  padding: 0;
  max-width: 100vw;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  background-color: rgb(240, 240, 240);
  // height: 100%;
  // width: 100vw;

  @media (min-width: 1025px) {
    .content {
      top: 0;
      // background-color: whitesmoke;
      margin: auto;
      margin-top: 0px;
      // box-shadow: 4px 2px 4px #55555555;
      border: solid 2px #55555555;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      width: 75vw;
      min-height: 100vh;
      overflow: hidden;


      .left-content {
        width: 70%;
        height: 100%;
        margin: auto;
        display: flex;
        flex-direction: column;
      }

      .right-card {
        position: sticky;
        margin-right: 5vw;
        margin-top: 0;
        height: 550px;
        width: 25%;
        margin: auto;
        margin-top: 30px;
      }

    }
  }

  @media (max-width: 1025px) {
    .content {
      top: 0;
      background-color: whitesmoke;
      margin: auto 20px;
      margin-top: 0px;
      box-shadow: 4px 2px 4px #55555555;
      border-radius: 10px;


      .right-card {
        display: none;
      }

      .left-content {
        margin: auto;
        margin-right: 40px;
        display: flex;
        flex-direction: column;
      }
    }
  }
}



#background {
  object-fit: cover;
  z-index: 0;
  height: 100vh;
}

body {
  background-color: rgb(224, 224, 224);
}

/* ---------------------------------------------------------------------- */

@keyframes welcome {
  0% {
    right: 50px;
  }

  100% {
    right: 1800px;
  }
}

.start {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(to right, rgb(255, 255, 255), 90%, rgba(255, 255, 255, 0));
  animation-name: welcome;
  animation-timing-function: ease;
  animation-duration: 2s;
  animation-delay: 0.7s;
  animation-direction: normal;
  animation-fill-mode: both;
  animation-name: welcome;
  z-index: 15;
  position: absolute;
}

/* ------------------------------------------------------------------------- */
</style>
