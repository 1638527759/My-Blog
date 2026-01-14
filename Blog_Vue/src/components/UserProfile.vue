<template>
    <div style="border: 1px solid #ccc; padding: 15px; border-radius: 8px;">
        <h3>这是子组件 (编辑区)</h3>

        <p>当前姓名：<strong>{{ name }}</strong></p>

        <label>修改姓名：</label>
        <input type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
            placeholder="请输入新名字" />
    </div>
</template>

<script setup>
// 声明 Props
defineProps({
    name: String,        // 仅用于展示的静态/动态属性
    modelValue: String   // 专门用于 v-model 双向绑定的属性
});

// 声明 Emits (通知父组件修改数据)
defineEmits(['update:modelValue']);
</script>