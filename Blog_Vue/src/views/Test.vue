<template>
  <div style="max-width: 400px; margin: 20px auto;">
    <h1>这是父组件</h1>
    <p>父组件中的数据：<mark>{{ myName }}</mark></p>
    <hr>

    <UserProfile :name="myName" v-model="myName" />

    <button @click="myName = '神秘人'" style="margin-top: 10px;">
      通过父组件按钮重置
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import UserProfile from '@/components/UserProfile.vue';

// 定义响应式变量
const myName = ref('张三');
</script>