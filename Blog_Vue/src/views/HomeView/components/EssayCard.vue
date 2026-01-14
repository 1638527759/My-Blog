<template>

  <div v-for="essay in essays" :key="essay.id">
    <RouterLink :to="`/detail/${essay.id}`" class="cardBox">
      <div class="bg-info">
        <div class="card-header text-white">
          <h4 class="card-title">{{ essay.title }}</h4>
        </div>
      </div>

      <div class="card-body">
        <div v-if="isLoading">
          <p>"加载中..."</p>
        </div>
        <div v-else-if="error">
          <p>{{ error }}</p>
        </div>
        <div v-else>
          <div class="card-text" v-html="essay.content"></div>
        </div>
        <!-- <a href="#" class="btn btn-primary">See Profile</a> -->
      </div>
    </RouterLink>
  </div>

  <br />
</template>

<script setup name="CardBox">
import api from '@/api/blog'
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const essays = ref([])
const error = ref(null)
const isLoading = ref(true)

const getEssay = async () => {
  try {
    const res = await api.get('/essays/')
    essays.value = res.data.data
  }
  catch (error) {
    alert("加载失败:" + error)
    essays.value = "加载失败，请稍后再试"
  }
  finally {
    isLoading.value = false
  }

}

onMounted(() => {
  getEssay()
})


</script>

<style scoped lang="scss">
a {
  text-decoration: none;
}

.cardBox {
  position: relative;
  top: 30px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 400px;
  width: 50vw;
  text-align: center;
  border-radius: 10px;
  box-shadow: 5px 5px 5px gray;
  background-color: white;

  @media (max-width: 1025px) {
    width: 80vw;
  }

  .card-header {
    height: 70px;
    background-color: rgb(43, 43, 43);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    .card-title {
      font-size: 30px;
    }
  }

  .card-body {
    display: flex;
    flex-direction: row;
    align-items: start;

    .card-text {
      color: black !important;

      // 使用深度选择器影响v-html渲染的内容
      :deep(p) {
        color: black !important;
      }

      :deep(*) {
        color: black !important;
      }
    }
  }
}
</style>
