<template>
  <!-- <Embed src="../static/bootstrap/music/志倉千代丸 - 澄空学园校歌.mp3" width="0" height="0" AUTOSTART="TRUE" LOOP="TRUE"></Embed> -->

  <!-- 开场动画 -->
  <div class="start"></div>

  <!-- 头部 -->
  <div class="header">
    <!-- 云 -->
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

    <!-- 背景 -->
    <!-- <div id="lunbo" class="carousel slide" data-ride="carousel" data-interval="4000"> -->
    <div
      id="lunbo"
      class="carousel slide carousel-fade"
      data-bs-ride="carousel"
      data-bs-interval="2000"
    >
      <div id="welcome">
        <h1 id="words">Welcome</h1>
        <!-- <h1 id="words">{% if request.user %} {{ request.user }} {% endif %}</h1> -->
        <!-- <script>
          var welcome = document.getElementById('welcome')
          var words = document.getElementById('words')
          welcome.onmousemove = function rad() {
            words.style.textShadow = '-4px -1px rgb(255, 0, 85)'
          }
          welcome.onmouseleave = function blue() {
            words.style.textShadow = '4px 1px rgb(0, 174, 255)'
          }
        </script> -->
      </div>

      <div class="down2"></div>
      <a class="down" href="#active">
        <span style="top: 25%" class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>
      </a>

      <!-- 轮播图片 -->
      <div id="backgruond" class="carousel-inner" data-bs-interval="1000">
        <div class="carousel-item active">
          <img src="../components/img/alone.jpg" />
        </div>
        <div class="carousel-item">
          <img src="../components/img/snow.jpg" />
        </div>
        <div class="carousel-item">
          <img src="../components/img/railway.png" />
        </div>
        <div class="carousel-item">
          <img src="../components/img/girl2.png" />
        </div>
      </div>
    </div>

    <!-- 快速导航栏 -->
    <div class="quickLeader">
      <a id="butten_1" href="/view2/">登陆</a>
      <!-- <a id="butten_1" href="../templates/view2.html">登陆</a> -->
      <a id="butten_2" href="../templates/index.html">测试用页面</a>
      <a id="butten_3" href="https://www.baidu.com">baidu</a>
    </div>
  </div>

  <!-- 中部 -->

  <!-- 导航栏 -->
  <div id="active" class="active">
    <ul class="leader">
      <li>
        <a data-toggle="tab" href="javascript:;">
          <!-- {% if request.user %}
          {{ request.user }}
          {% endif %} -->
        </a>
      </li>
      <li><a href="view3/">随笔</a></li>
      <li>
        <a class="something" data-toggle="tab" href="javascript:;">杂项</a>
        <div class="dropdown">
          <ul class="dropdown-menu">
            <li>???</li>
            <li>!!!</li>
          </ul>
        </div>
      </li>
      <li><a data-toggle="tab" href="/">主页</a></li>
    </ul>
  </div>
  <!-- live 2D  -->
  <div style="z-index: 10">
    <!-- <script src="https://cdn.jsdelivr.net/gh/stevenjoezhang/live2d-widget@latest/autoload.js"></script> -->
  </div>

  <div style="width: 70%; margin: auto" class="jumbotron">
    <div style="width: 80%; margin: auto">
      <img
        width="100%"
        src="../static/bootstrap/img/temp.jpg"
        border="0"
        usemap="#planetmap"
        alt="Planets"
      />
    </div>

    <map name="planetmap" id="planetmap">
      <area
        shape="rect"
        coords="0,0,110,260"
        href="../static/bootstrap/img/illust_82630792_20220315_230806.jpg"
        target="_blank"
        alt="Sun"
      />
    </map>
  </div>

  <div class="card">
    <div class="bg-info text-white">
      <div class="card-header">
        <h4 class="card-title">John Doe</h4>
      </div>
    </div>
    <div class="card-body">
      <p class="card-text">
        Some example text some example text. John Doe is an architect and engineer
      </p>
      <a href="#" class="btn btn-primary">See Profile</a>
    </div>
    <br />
  </div>

  <div class="card">
    <div class="bg-info text-white">
      <div class="card-header">
        <h4 class="card-title">John Doe</h4>
      </div>
    </div>
    <div class="card-body">
      <p class="card-text">
        Some example text some example text. John Doe is an architect and engineer
      </p>
      <a href="#" class="btn btn-primary">See Profile</a>
    </div>
    <br />
  </div>

  <div class="card">
    <div class="bg-info text-white">
      <div class="card-header">
        <h4 class="card-title">John Doe</h4>
      </div>
    </div>
    <div class="card-body">
      <p class="card-text">
        Some example text some example text. John Doe is an architect and engineer
      </p>
      <a href="#" class="btn btn-primary">See Profile</a>
    </div>
    <br />
  </div>
</template>

<style>
/* 清除元素默认样式 */

* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  /* cursor: url(/prectise3/sucai/魔法棒.cur), auto; */
}

a {
  text-decoration: none;
  text-align: center;
  display: block;
}

img {
  vertical-align: middle;
}

.carousel-item {
  img {
    height: 100vh;
    width: 100vw;
    object-fit: cover;
    z-index: 0;
  }
}

#background {
  object-fit: cover;
  z-index: 0;
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
    height: 50px;
    width: 250px;
  }
  /* 分别设置 top 和 animation-delay */
  #butten_1 {
    top: 200px;
    animation-delay: 0s;
  }
  #butten_2 {
    top: 300px;
    animation-delay: 0.5s;
  }
  #butten_3 {
    top: 400px;
    animation-delay: 1s;
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
/* ------------------------------------------------------------------------- */

#welcome {
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
  /* animation-name: message;
        animation-delay: 0s;
        animation-duration: 6s; */
  text-align: center;
  color: rgb(252, 249, 249);
  user-select: none;
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

#words {
  text-shadow: none;
  position: relative;
  top: 20%;
  font-size: 80px;
  /* animation-name: words;
        animation-duration: 1s;
        animation-delay: 0s; */
  font-family: Arial, Helvetica, sans-serif;
}

#words:hover {
  animation-name: color;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  /* animation-fill-mode: forwards; */
}
/* @keyframes words {
        0% {
            font-size: 0%;
        }
        70% {
            font-size: 0%;
        }
        80% {
            font-size: 10px;
        }
        100% {
            font-size: 80px;
        }
    }
     */

@keyframes color {
  0% {
    text-shadow: -0px -5px rgb(255, 0, 85);
    top: 20%;
  }
  12.5% {
    top: 15%;
  }
  25% {
    text-shadow: -5px 0px rgb(0, 174, 255);
    top: 20%;
  }
  37.5% {
    top: 15%;
  }
  50% {
    text-shadow: 0px 5px rgb(255, 0, 85);
    top: 20%;
  }
  67.5% {
    top: 15%;
  }
  75% {
    text-shadow: 5px 0px rgb(0, 174, 255);
    top: 20%;
  }
  87.5% {
    top: 15%;
  }
  100% {
    text-shadow: -0px -3px rgb(255, 0, 85);
    top: 20%;
  }
}
/* ------------------------------------------------------------------------- */

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
/* ------------------------------------------------------------------------- */

#active {
  position: sticky;
  top: 0;
}

ul {
  list-style-type: none;
  overflow: hidden;
  background-color: rgb(37, 37, 37);
  border-top: 2px solid rgb(4, 194, 219);
  border-bottom: 2px solid rgb(4, 194, 219);
  position: sticky;
  top: 0;
}

li {
  float: right;
  /* border-right: 2px solid rgb(162, 221, 218); */
  /* border-top: 1px solid rgb(4, 194, 219); */
  /* border-left: 1px solid rgb(4, 194, 219); */
}
/* li:hover {
     border-top: 1px solid rgb(4, 194, 219);
     border-left: 1px solid rgb(4, 194, 219);
 } */

li a {
  display: block;
  color: rgb(255, 255, 255);
  padding: 14px 16px;
  text-decoration: none;
  transition-duration: 0.3s;
  font-size: 18px;
  /* border-radius: 10px; */
}

li a:hover:not(.active) {
  background-color: rgba(139, 243, 243, 0.979);
  color: rgb(0, 174, 255);
  font-size: 18px;
  text-decoration: none;
  /* border-radius: 10px; */
}

li a:active {
  background-color: rgba(139, 243, 243, 0.979);
  color: rgb(0, 174, 255);
  font-size: 18px;
  text-decoration: none;
}

.dropdown {
  display: none;
  position: relative;
  width: 50px;
  height: 60px;
}
/* ------------------------------------------------------------------------- */

.content {
  width: 600px;
  height: 400px;
  background-color: whitesmoke;
  margin: auto;
  box-shadow: 4px 2px 4px #55555555;
  border-radius: 10px;
}

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

.card {
  display: block;
  height: 50%;
  width: 60%;
  text-align: center;
  margin: auto;
  border: 10px;
}
</style>
