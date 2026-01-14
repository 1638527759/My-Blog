<template>
  <!-- 头部 -->
  <div class="header">
    <!-- 云 -->
    <!-- <top-wave></top-wave> -->

    <template v-if="data.token">
      <div class="welcome" v-if="data.token">
        <h1 class="words" style="font-size: 70px;">Welcome<br></br>{{ data.user.username }}</h1>
      </div>
    </template>

    <div class="welcome" v-else>
      <h1 class="words">Welcome<br></br>游客</h1>
    </div>

    <!-- 
    <div class="welcome">
      <h1 class="words">Welcome</h1>
    </div> -->

    <down-button></down-button>
    <!-- 背景 -->


    <!-- 背景 - Swiper 轮播 -->
    <swiper :modules="modules" :slides-per-view="1" :space-between="0" :autoplay="{
      delay: 2000,
      disableOnInteraction: false,
    }" :effect="'fade'" :fade-effect="{ crossFade: true }" :loop="true" :speed="1000" class="swiper-container">
      <swiper-slide>
        <img :src="aloneImg" alt="alone" />
      </swiper-slide>
      <swiper-slide>
        <img :src="snowImg" alt="snow" />
      </swiper-slide>
      <swiper-slide>
        <img :src="railwayImg" alt="railway" />
      </swiper-slide>
      <swiper-slide>
        <img :src="girlImg" alt="girl" />
      </swiper-slide>
    </swiper>


  </div>
</template>
<script setup>
import { ElCarousel, ElCarouselItem } from 'element-plus'
import DownButton from './DownButton.vue'
import aloneImg from '@/assets/img/alone.jpg'
import snowImg from '@/assets/img/snow.jpg'
import railwayImg from '@/assets/img/railway.png'
import girlImg from '@/assets/img/girl2.png'
import TopWave from './TopWave.vue'

import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectFade } from 'swiper/modules'

// 引入 Swiper 样式
import 'swiper/css'
import 'swiper/css/effect-fade'

import { ref } from 'vue'
import { useUserStore } from '@/stores/userStore'

const modules = [Autoplay, EffectFade]
const userStore = useUserStore()
const data = userStore.userInfo.data
// const token = userStore.userInfo.data.token
// const userInfo = userStore.userInfo.data.user


// console.log(data.user.username)




</script>
<style scoped lang="scss">
// Swiper 容器样式
.swiper-container {
  height: 100vh;
  width: 100%;
  position: relative;
}

// Swiper 滑块样式
:deep(.swiper-slide) {
  height: 100vh;
  width: 100%;

  img {
    height: 100%;
    width: 100%;
    object-fit: cover;
    display: block;
  }
}


@keyframes welcome {
  0% {
    right: 50px;
  }

  100% {
    right: 1800px;
  }
}

.welcome {
  height: 200px;
  width: 600px;
  margin: auto;
  position: absolute;
  top: -40%;
  right: 0;
  bottom: 0;
  left: 0;
  border-radius: 10px;
  background-color: #2221214f;
  box-shadow: 4px 2px 4px #55555555;
  z-index: 5;

  text-align: center;
  color: rgb(252, 249, 249);
  user-select: none;

  .words {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 80px;
    font-family: Arial, Helvetica, sans-serif;
    text-shadow: 0 0 10px rgba(255, 0, 85, 0.6);
    animation: float 3s ease-in-out infinite,
      glow 2.5s ease-in-out infinite;
  }

  //  
  /* 上下漂浮动画 */
  @keyframes float {
    0% {
      transform: translateY(0);
    }

    50% {
      transform: translateY(-10px);
      /* 可调 */
    }

    100% {
      transform: translateY(0);
    }
  }

  /* 霓虹颜色光影动画 */
  @keyframes glow {
    0% {
      text-shadow: 0 0 15px rgb(255, 0, 85);
      color: rgb(255, 0, 85);
    }

    50% {
      text-shadow: 0 0 15px rgb(0, 174, 255);
      color: rgb(0, 174, 255);
    }

    100% {
      text-shadow: 0 0 15px rgb(255, 0, 85);
      color: rgb(255, 0, 85);
    }
  }
}

@keyframes message {
  0% {
    height: 200px;
    width: 0px;
  }

  30% {
    height: 200px;
    width: 0px;
  }

  40% {
    height: 200px;
    width: 20px;
  }

  50% {
    height: 200px;
    width: 20px;
  }

  70% {
    height: 200px;
    width: 20px;
    font-size: 0px;
    border-radius: 5px;
  }

  73% {
    font-size: 0px;
  }

  100% {
    height: 200px;
    width: 600px;
    border-radius: 10px;
    font-size: 80px;
  }
}
</style>