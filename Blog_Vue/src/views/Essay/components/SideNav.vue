<template>
  <div class="quickLeader">
    <!-- <router-link :to="{ path: '/login' }" id="butten_1">登录</router-link> -->
    <router-link :to="{ path: '/' }" id="butten_2">首页</router-link>
    <!-- <a id="butten_3" href="https://www.baidu.com">baidu</a> -->
  </div>
</template>

<script setup name="LeftNav"></script>

<style scoped lang="scss">
/* 左侧按钮部分 */
@media (max-width: 1025px) {
  .quickLeader {
  a {
    background-color: black;
    height: 50px;
    width: 130px;
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
    height: 50px;
    width: 250px;
  }
  /* 分别设置 top 和 animation-delay */
  #butten_2 {
    top: 300px;
    animation-delay: -1s;
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
      width: 130px;
    }
  }
}
}

@media(min-width: 1025px) {
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
    height: 50px;
    width: 250px;
  }
  /* 分别设置 top 和 animation-delay */
  #butten_2 {
    top: 300px;
    animation-delay: -1s;
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
}

</style>
