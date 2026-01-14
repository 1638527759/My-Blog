<template>
  <div id="active" class="active">
    <ul class="leader">
      <li>
        <a data-toggle="tab" href="/">
          <span class="leader_title-cn">主页</span>
          <span class="leader_title-en">Home</span>
          <span class="underLine"></span>
        </a>
      </li>
      <li>
        <a href="view3/">
          <span class="leader_title-cn">随笔</span>
          <span class="leader_title-en">Essay</span>
          <span class="underLine"></span>
        </a>
      </li>
      <li>
        <a class="leader_bar" data-toggle="tab" href="javascript:;">
          <span class="leader_title-cn">杂项</span>
          <span class="leader_title-en">Sundry</span>
          <span class="underLine"></span>
        </a>
        <div class="dropdown">
          <ul class="dropdown-menu">
            <li>???</li>
            <li>!!!</li>
          </ul>
        </div>
      </li>

      <li class="Persion">
        <a data-toggle="tab" href="javascript:;">
          <span class="leader_title-cn">个人</span>
          <span class="leader_title-en">Persion</span>
          <span class="underLine"></span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script setup name="MainNav">
import { RouterLink } from 'vue-router'
</script>

<style scoped lang="scss">
#active {
  position: sticky;
  top: 0;
  z-index: 5;

  ul {
    list-style-type: none;
    overflow: hidden;
    background-color: rgba(37, 37, 37, 0.8);
    border: 2px solid rgba(37, 37, 37, 0.6);
    margin: 0;
    position: sticky;
    display: flex;
    flex-direction: row;
    justify-content: end;
    top: 0;
    padding: 0;

    animation: fadeIn 0.3s;

    li {
      position: relative; // 添加相对定位，为下划线定位提供参考
    }

    li a {
      float: right;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 5px;
      padding: 2px 15px;
      transition-duration: 0.3s;
      text-decoration: none;
      position: relative; // 为下划线定位提供参考

      .leader_title-cn {
        color: rgb(255, 255, 255);
        text-decoration: none;
        font-size: 18px;
      }

      .leader_title-en {
        color: rgb(206, 205, 205);
        text-decoration: none;
        font-size: 12px;
      }

      // 为所有链接添加下划线效果
      &::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 0;
        height: 2px;
        background-color: rgb(4, 194, 219);
        transform: translateX(-50%);
        transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      }

      &:hover::after {
        width: 80%;
      }
    }

    li a:hover:not(.active) {
      color: rgb(0, 174, 255);
      font-size: 18px;
      text-decoration: none;
    }

    li a:active {
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
  }

  @keyframes fadeIn {
    0% {
      height: 0px;
    }

    100% {
      height: 52px;
    }
  }
}
</style>
