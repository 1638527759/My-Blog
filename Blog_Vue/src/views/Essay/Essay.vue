<template>
  <div class="background">
    <!-- 上方导航栏 -->
    <div class="blankArea">
      <main-nav class="topNav"></main-nav>
    </div>

    <!-- 侧边导航栏 -->
    <side-nav></side-nav>

    <div class="container">
      <div class="left">
        <div class="editor-box">
          <input type="text" class="title" v-model="essay.title">
          <quill-editor class="editor" content-type="html" v-model:content="essay.content"></quill-editor>
        </div>
      </div>
      <ul class="right">
        <li @click="submitEssay" :class="{ disabled: isSubmitting }">
          <p>{{ isSubmitting ? '提交中...' : '提交' }}</p>
        </li>
        <li>
          <p>话题</p>
        </li>
        <li>
          <p>模块</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup name="Essay">
import { ref, reactive } from 'vue'
import { QuillEditor } from '@vueup/vue-quill'
import { ElMessage } from 'element-plus'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import SideNav from './components/SideNav.vue'
import MainNav from '@/components/MainNav.vue'
import axios from 'axios'
import api from '@/api/blog.js'
import request from '@/https/blog'

// 文章数据
const essay = reactive({
  title: '',
  content: ''
})

// 提交状态
const isSubmitting = ref(false)

// 消息提示
const message = reactive({
  show: false,
  text: '',
  type: 'success' // 'success' | 'error' | 'warning'
})

// 显示消息
const showMessage = (text, type = 'success') => {
  message.text = text
  message.type = type
  message.show = true
  setTimeout(() => {
    message.show = false
  }, 3000)
}


// 提交文章函数（使用 axios）
const submitEssay = async () => {
  // 验证标题
  if (!essay.title.trim()) {
    showMessage('请输入文章标题', 'warning')
    return
  }

  // 验证内容
  if (!essay.content || essay.content.trim() === '<p><br></p>') {
    showMessage('请输入文章内容', 'warning')
    return
  }

  // 防止重复提交
  if (isSubmitting.value) {
    return
  }

  try {
    isSubmitting.value = true

    // 使用 axios 发送请求
    const response = await api.post('/essays/', {
      title: essay.title,
      content: essay.content
    })

    // axios 自动解析 JSON，直接访问 data
    const result = response.data

    if (result.code === 200) {
      showMessage('文章发布成功！', 'success')
      ElMessage({ type: "success", message: "发布成功" })

      // 清空表单
      essay.title = ''
      essay.content = ''

      // 可选：跳转到文章详情页或列表页
      // setTimeout(() => {
      //   router.push(`/essay/${result.data.id}`)
      // }, 1500)
    } else {
      showMessage(result.message || '发布失败，请重试', 'error')
    }
  } catch (error) {
    console.error('提交失败:', error)

    // axios 错误处理更详细
    if (axios.isAxiosError(error)) {
      if (error.response) {
        // 服务器返回了错误状态码
        const errorMsg = error.response.data?.message || '服务器错误'
        showMessage(errorMsg, 'error')
      } else if (error.request) {
        // 请求已发出但没有收到响应
        showMessage('网络错误，请检查连接后重试', 'error')
      } else {
        // 其他错误
        showMessage('请求失败，请重试', 'error')
      }
    } else {
      showMessage('未知错误，请重试', 'error')
    }
  } finally {
    isSubmitting.value = false
  }
}


</script>

<style scoped lang="scss">
* {
  margin: 0;
  padding: 0;
}

.background {
  position: relative;
  min-height: 100vh;
  // max-width: 100vw;
  min-width: 100vw;
  // background-color: rgb(12, 18, 63);
  background-image: url(../../components/img/girl.png);
  background-position: center center;
  /* 背景图不平铺 */
  background-repeat: no-repeat;
  /* 当内容高度大于图片高度时，背景图像的位置相对于viewport固定 */
  background-attachment: fixed;
  /* 让背景图基于容器大小伸缩 */
  background-size: cover;
  /* 设置背景颜色，背景图加载过程中会显示背景色 */
  background-color: #464646;
}

.blankArea {
  position: absolute;
  z-index: 10;
  width: 100vw;
  height: 25px;
  animation-name: appear;

  .topNav {
    display: none;
  }
}

.blankArea:hover {
  .topNav {
    display: block;
  }
}

@media (min-width: 1026px) {
  .container {
    margin: auto;
    position: relative;
    height: auto;
    width: 90vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-family:
      -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans',
      'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Source Han Sans SC',
      'WenQuanYi Micro Hei', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    .left::before {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      filter: blur(5px);
      z-index: -1;
    }

    .left {
      position: relative;
      width: 50vw;
      height: 600px;
      background-color: rgba(141, 141, 141, 0.5);
      backdrop-filter: blur(6px);
      margin: 40px;
      margin-right: 0;

      .title {
        padding: 2px;
        border: solid 1px rgb(216, 216, 216);
        border-bottom: none;
        outline: none;
        background-color: #46464600;
        height: 45px;
        width: 100%;
        color: white;
      }

      .title:focus {
        box-shadow: inset 0px -2px 3px 0px aqua;
      }

      .editor-box {
        margin: auto;
        position: relative;
        width: 100%;
        height: 85.5%;
        color: white;
      }
    }

    .right {
      margin-top: 0;
      position: relative;
      display: flex;
      flex-direction: column;
      list-style: none;
      align-items: center;
      justify-content: center;
      top: 40px;
      left: 30px;
      width: 300px;
      height: 400px;
      border: solid 1px rgb(216, 216, 216);
      background-color: rgba(141, 141, 141, 0.5);
      backdrop-filter: blur(6px);

      li {
        margin: 40px;
        background-image: linear-gradient(rgb(238, 238, 238), 90%, rgb(112, 112, 112));
        height: 50px;
        width: 250px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;

        p {
          margin: 0;
          font-size: 16px;
          font-weight: 600;
          letter-spacing: 0.3px;
          color: rgb(94, 94, 94);
        }
      }

      li:hover {
        background-image: linear-gradient(rgb(238, 238, 238), 95%, rgb(112, 112, 112));

        p {
          color: rgb(55, 55, 55);
        }
      }
    }

    .right::before {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      filter: blur(5px);
      z-index: -1;
    }
  }
}

@media (max-width: 1025px) {
  .container {
    margin: auto;
    position: relative;
    height: auto;
    width: 90vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family:
      -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans',
      'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Source Han Sans SC',
      'WenQuanYi Micro Hei', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    .left::before {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      filter: blur(5px);
      z-index: -1;
    }

    .left {
      position: relative;
      width: 80vw;
      height: 600px;
      background-color: rgba(141, 141, 141, 0.5);
      backdrop-filter: blur(6px);
      // margin: 40px;
      margin: 40px 0 20px 0;

      .title {
        padding: 2px;
        border: solid 1px rgb(216, 216, 216);
        border-bottom: none;
        outline: none;
        background-color: #46464600;
        height: 45px;
        width: 100%;
        color: white;
      }

      .title:focus {
        box-shadow: inset 0px -2px 3px 0px aqua;
      }

      .editor-box {
        margin: auto;
        position: relative;
        width: 100%;
        height: 85.5%;
        color: white;
      }

    }

    .right {
      // margin-top: 0;
      // margin: 10px auto;
      margin: 10px 0 40px 0;
      position: relative;
      display: flex;
      flex-direction: column;
      list-style: none;
      align-items: center;
      justify-content: center;
      width: 80vw;
      height: 250px;
      border: solid 1px rgb(216, 216, 216);
      background-color: rgba(141, 141, 141, 0.5);
      backdrop-filter: blur(6px);

      li {
        margin: 15px;
        background-image: linear-gradient(rgb(238, 238, 238), 90%, rgb(112, 112, 112));
        height: 50px;
        width: 250px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;

        p {
          margin: 0;
          font-size: 16px;
          font-weight: 600;
          letter-spacing: 0.3px;
          color: rgb(94, 94, 94);
        }
      }

      li:hover {
        background-image: linear-gradient(rgb(238, 238, 238), 95%, rgb(112, 112, 112));

        p {
          color: rgb(55, 55, 55);
        }
      }
    }

    .right::before {
      content: '';
      position: absolute;
      width: 100%;
      height: 100%;
      left: 0;
      filter: blur(5px);
      z-index: -1;
    }
  }
}
</style>
