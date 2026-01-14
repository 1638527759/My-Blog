<template>
  <!-- 内容 -->
  <div>
    <RouterView />
  </div>

  <HomeView></HomeView>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
// import HomeView from './views/HomeView/HomeView.vue'
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
</style>
