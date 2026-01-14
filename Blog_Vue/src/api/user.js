// 用户相关API
import request from '@/api/blog'
import { ElMessage } from 'element-plus'

export const loginAPI = ({ username, password }) => {
    return request({
        url: '/blog/login/',
        method: 'POST',
        data: {
            username,
            password
        }
    })
}

export const registerAPI = ({ username, password, passwordAgain, email }) => {
    return request({
        url: '/blog/register/',
        method: 'POST',
        data: {
            username,
            password,
            passwordAgain,
            email
        }
    })
}