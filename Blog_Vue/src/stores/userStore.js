import { defineStore } from 'pinia'
// import { request } from '@/https/blog'
import { loginAPI } from '@/api/user'
import { ref } from 'vue'

export const useUserStore = defineStore("user", () => {
    // 定义管理用户数据的store
    const userInfo = ref({ data: {} })
    const getUserInfo = async({ username, password }) => {
        const res = await loginAPI({ username, password })
        userInfo.value = res.data
        console.log(userInfo.value.data.token)
    }

    // 清除数据初始化
    const clearUserInfo = () => {
        userInfo.value = { data: {} }
    }
    return {
        userInfo,
        getUserInfo,
        clearUserInfo
    }
}, {
    persist: true,
})