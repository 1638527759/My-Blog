<template>
  <div class="quickLeader">
    <router-link :to="{ path: '/login' }" id="butten_1">登录</router-link>
    <router-link :to="{ path: '/test' }" id="butten_2">测试用页面</router-link>
    <a id="butten_3" href="https://www.baidu.com">baidu</a>
  </div>
</template>

<script setup name="LeftNav">
import { ref, onMounted, watch, watchEffect, onUnmounted } from 'vue'

const scollX = ref(0)
const scollY = ref(0)

const updateScrollPosision = () => {
  scollX.value = window.scrollX
  scollY.value = window.scrollY
  // console.log('滚动中:', scollX.value, scollY.value)
}

const disappear = () => {
  if (scollY.value >= 700) {
    document.getElementById('butten_1').style.width = '120px'
    document.getElementById('butten_2').style.width = '120px'
    document.getElementById('butten_3').style.width = '120px'
  } else {
    document.getElementById('butten_1').style.width = '180px'
    document.getElementById('butten_2').style.width = '180px'
    document.getElementById('butten_3').style.width = '180px'
  }
}

onMounted(() => {
  window.addEventListener('scroll', updateScrollPosision)
  window.addEventListener('scroll', disappear)
  disappear()
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateScrollPosision)
  window.removeEventListener('scroll', disappear)
})

// watchEffect(() => {
//   console.log(scollX, scollY)
// })
</script>

<style scoped lang="scss">
/* 左侧按钮部分 */
.quickLeader {
  a {
    background-color: black;
    height: 50px;
    width: 180px;
    position: fixed;
    left: -38px;
    transform: rotate(-30deg);
    box-shadow: 5px 5px 3px rgba(34, 34, 34, 0.7);
    animation-name: live;
    animation-duration: 4s;
    animation-direction: normal;
    animation-timing-function: ease;
    transition: 0.7s;
    transition-timing-function: ease;
    z-index: 10;
    text-align: right;
    font-family: fantasy;
    font-style: italic;
    font-size: 20px;
    padding: 10px 10px;
    color: rgba(245, 243, 243, 0.486);
    text-decoration: none;
  }
  /* hover 统一 */
  a:hover {
    height: 50px !important;
    width: 250px !important;
  }
  /* 分别设置 top 和 animation-delay */
  #butten_1 {
    top: 200px;
    animation-delay: -1.5s;
  }
  #butten_2 {
    top: 300px;
    animation-delay: -1s;
  }
  #butten_3 {
    top: 400px;
    animation-delay: -0.5s;
  }
  /* 动画 */
  @keyframes live {
    0% {
      width: 0px;
    }
    60% {
      width: 0px;
    }
    80% {
      width: 230px;
    }
    100% {
      width: 180px;
    }
  }
}
</style>
