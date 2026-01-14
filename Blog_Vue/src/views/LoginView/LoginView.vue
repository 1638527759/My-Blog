<template>
  <!-- <canvas></canvas> -->
   <div>
    <img :src="background" alt="/" class="background">
     <!-- <img src="" alt=""> -->
      <!-- <div class="background"></div> -->
   </div>

  <!-- 登陆界面 -->
  <div class="window" v-show="isLogin">
    
    <el-form class="form" ref="loginFormRef" :rules="loginRules" :model="loginForm" label-width="0" @submit.prevent="handleLogin">
      <h2 class="title1">登录</h2>
      <div class="form-wrap">
        <el-form-item prop="username">
          <!-- <div class="input-wrap"> -->
            <el-input type="text" placeholder="用户名" class="input" v-model="loginForm.username" />
          <!-- </div> -->
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="密码" class="input" v-model="loginForm.password"/>
        </el-form-item>
        <el-form-item prop="remember" class="checkbox-item">
          <!-- <div class="input-wrap checkbox-wrap"> -->
            <el-checkbox class="checkbox" v-model="loginForm.remember">记住密码</el-checkbox>
          <!-- </div> -->
        </el-form-item>
      </div>   
      <el-form-item>
        <el-button class="button" type="primary" :disabled="isLoading" @click="handleLogin">登录</el-button>
      </el-form-item>
    </el-form>
    <div class="up" @click="isLogin = false">
      <span></span>
      <div class="switchBtn">注册</div>
    </div>

  </div>

  <!-- 注册界面 -->
  <div class="window" v-show="!isLogin">
    
    <el-form class="form" ref="registerFormRef" :model="registerForm" :rules="registerRules" @submit.prevent="handleRegister">
      <h2 class="title2">注册</h2>
      <div class="form-wrap">
        <el-form-item prop="username">
          <el-input type="text" placeholder="请输入用户名" class="input" v-model="registerForm.username"/>
        </el-form-item>
        <el-form-item prop="email">
          <el-input type="text" placeholder="请输入邮箱" class="input" v-model="registerForm.email" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="text" placeholder="请输入密码 "class="input" v-model="registerForm.password" />
        </el-form-item>
        <el-form-item prop="passwordAgain">
          <el-input type="text" placeholder="请再次输入密码 "class="input" v-model="registerForm.passwordAgain" />
        </el-form-item>
      </div>
      <el-form-item>
        <el-button class="button" type="primary" :disabled="isLoading" @click="handleRegister">注册</el-button>
      </el-form-item>
    </el-form>
    <div class="up" @click="isLogin = true">
      <div class="switchBtn">登陆</div>
    </div>
  </div>

  <router-link :to="{ path: '/' }">
    <div id="back">
      <p>返回</p>
    </div>
  </router-link>

</template>

<script setup>
import { ref, reactive } from 'vue';
import { ElMessage } from 'element-plus';
import background from '@/components/img/窗.png'
import {loginForm, loginRules} from "./components/Login"
import {registerForm, registerRules} from "./components/Register"
import { useUserStore } from '@/stores/userStore'
// import { loginAPI, registerAPI } from "@/api/user"
import router from '@/router';


// 控制显示登录还是注册
const isLogin = ref(true)
const isLoading = ref(false)
// 实例化Store对象
const userStore = useUserStore()

// 表单引用
const loginFormRef = ref(null);
const handleLogin = () => {
    const {username, password} = loginForm
    // 调用实例方法
    loginFormRef.value.validate(async (valid) => {   
      if(valid) {
        userStore.getUserInfo({username, password})
        ElMessage({type: "success", message: "登陆成功"})
        // 跳转首页
        // router.replace({ path: '/' })
      }
    })
}

const registerFormRef = ref(null);
const handleRegister = () => {
  const {username, password, passwordAgain, email} = registerForm
  registerFormRef.value.validate(async (valid) => {
    // valid: 所以表单都通过校验 才为true
    //  以valid作为判断条件 通过检验才执行登录逻辑
     if(valid) {
      const res = await registerAPI({username, password, passwordAgain, email})
      console.log(res)
      ElMessage({type: 'success', message: "注册成功"})
     }
  })
}

</script>

<style lang="scss" scoped>
// 基础重置
* {
  padding: 0px;
  margin: auto;
  border: 0px;
}

a {
  text-decoration: none;
  display: block;
}

// 背景
.background{
/* canvas { */
  position: fixed;
  height: 100%;
  width: 100%;
  z-index: -10;
  background-size: cover;
  background-repeat: no-repeat;
  background-image: url(background);
  /* background-image: url(../components/img/窗.png); */
}

//   :deep(.el-input) {
//   width: 100% !important;  /* 让它遵循内容宽度或外部容器宽度 */
// }

// 窗口
.window {
  display: flex;
  flex-direction: row;
  z-index: 1;
  margin: auto;
  position: relative;
  top: 200px;
  width: min(500px, 90vw);
  height: 350px;
  user-select: none;
  background-color: #222222e3;
  border-radius: 15px;
  border-right: solid 2px black;
  border-left: solid 2px black;
  box-shadow: 4px 2px 4px #55555555;
  color: white;
  // transform: none;
  // animation-name: none;
  // animation-duration: 1s;
  // animation-fill-mode: forwards;

  .form {
    margin: 0 auto;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .form-wrap {
      width: 60%;
      
      .input {
        background-color: rgba(219, 219, 219, 0.26);
        border: none;
        outline: none;
        height: 40px;
        // width: 300px;
        width: 100%;
        border-radius: 8px;
        color: rgba(73, 186, 252, 0.966);
        font-size: 18px;
      }

      .checkbox {
        left: 0;
        // margin: auto;
      }
    }

      :deep(.el-form-item) {
        width: 100%;
      }

  :deep(.el-form-item__content) {
    justify-content: flex-start !important;
  }

    .title1 {
      text-align: center;
      font-size: 50px;
      color: rgba(221, 220, 220, 0.678);
      padding: 0%;
      margin: 0%;
    }

    .title2 {
      text-align: center;
      font-size: 30px;
      color: rgba(221, 220, 220, 0.678);
      padding: 0%;
      margin: 0%;
    }


    .checkbox-item :deep(.el-form-item__content) {
      margin-left: 0 !important;
      padding-left: 0 !important;
      display: flex;
      align-items: center;
    }

    .checkbox-item :deep(.el-checkbox) {
      margin-left: 0 !important;
    }

    .checkbox-wrap {
      width: fit-content;
      display: flex;
      align-items: center;
    }


    .input-wrap {
      width: fit-content;   /* 内容宽度自适应 */
    }
    
    // .input {
    //   background-color: rgba(219, 219, 219, 0.26);
    //   border: none;
    //   outline: none;
    //   height: 40px;
    //   // width: 300px;
    //   width: 50%;
    //   border-radius: 8px;
    //   // text-align: left;
    //   color: rgba(73, 186, 252, 0.966);
    //   font-size: 18px;
    // }

    :deep(.el-input__wrapper) {
      background-color: rgba(219, 219, 219, 0.26) !important;
      box-shadow: none !important;
      border-radius: 8px;
      padding: 1px 11px;
      height: 40px;
      width: 100%;

        :deep(.el-input__inner) {
          color: rgba(73, 186, 252, 0.966) !important;
          background-color: transparent !important;
          font-size: 18px;
          text-align: left;
        }

        :deep(.el-input__inner::placeholder) {
          color: rgba(255, 255, 255, 0.4);
        }
    }

    :deep(.el-input__wrapper.is-focus) {
        box-shadow: 0px 0px 20px rgb(113, 213, 252) inset !important;
        background-color: rgba(219, 219, 219, 0.26) !important;
    }
      // Element Plus 输入框样式穿透

    .input:focus {
      box-shadow: 0px 0px 20px rgb(113, 213, 252) inset;
    }



    .button {
      margin: auto;
      text-align: center;
      padding: 8px 20px;
      border: none;
      color: rgba(0, 204, 255, 0.884);
      background-color: rgba(255, 255, 255, 0);
      border-bottom: solid 2px gray;
      height: 40px;
      font-size: 16px;
      text-decoration: none;
      text-transform: uppercase;
      overflow: hidden;
      transition: 0.5s;
      transition-duration: 0.2s;
      transition-timing-function: ease;
    }

    .button:hover {
      padding: 8px 20px;
      background-color: rgba(0, 204, 255, 0.884);
      box-shadow: 0px 0px 40px rgb(59, 212, 250);
      color: white;
    }

    .button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      background-color: gray;
    }

  }

    
  .up {
    // display: flex;
    // flex-direction: column;
    // width: 0;


    .switchBtn {
      display: block;
      background-color: rgb(0, 0, 0);
      position: absolute;
      color: rgba(0, 204, 255, 0.884);
      font-family: fantasy;
      top: 110%;
      left: 96.1%;
      transform: translateY(-50%);
      text-align: center;
      padding: 8px 0px;
      height: 50px;
      width: 40px;
      border-radius: 5px;
      text-decoration: none;
      text-transform: uppercase;
      box-shadow: 0px 0px 5px rgba(0, 204, 255, 0.884);
    }

    .switchBtn::before {
      content: '';
      position: absolute;
      bottom: 100%;
      left: 50%;
      transform: translateX(-50%);
      width: 2px;
      height: 150px;
      background-color: rgb(0, 0, 0);
      pointer-events: none;  // 让伪元素不响应鼠标事件
    }

    .switchBtn:hover {
      animation-name: pull_it;
      animation-duration: 1s;
      animation-iteration-count: infinite;
    }

    @keyframes pull_it {
      0%, 100% {
        transform: translateY(-50%);  // 原位置
      }
      25%, 75% {
        transform: translateY(-30%);  // 向下移动
      }
      50% {
        transform: translateY(-50%);  // 回到原位
      }
    }

    .switchBtn:hover {
      animation-name: pull_it;
      animation-duration: 1s;
      animation-iteration-count: infinite;
    }

  }
}



@keyframes rotate_back {
  0% {
    transform: rotateX(0deg);
  }
  100% {
    transform: rotateX(-180deg);
  }
}

@keyframes rotate_face {
  0% {
    transform: rotateX(180deg);
  }
  100% {
    transform: rotateX(0deg);
  }
}



/* --------------------------------------------------------------------------- */

#back {
  background-color: black;
  height: 50px;
  width: 100px;
  position: absolute;
  top: 300px;
  left: -38px;
  transform: rotate(-30deg);
  box-shadow: 5px 5px gray;
  animation-name: live;
  animation-delay: 0s;
  animation-duration: 1.5s;
  animation-direction: normal;
  animation-timing-function: ease;
  transition: 0.7s;
  z-index: 2;
}

#back:hover {
  background-color: black;
  height: 50px;
  width: 200px;
}

@keyframes live {
  0% {
    width: 0px;
  }
  50% {
    width: 230px;
  }
  100% {
    width: 100px;
  }
}

p {
  position: relative;
  padding: 10px 10px;
  text-align: right;
  font-family: fantasy;
  font-style: italic;
  font-size: 20px;
  color: rgba(245, 243, 243, 0.486);
}



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


</style>
 



