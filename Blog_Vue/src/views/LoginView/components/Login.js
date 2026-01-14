import { reactive } from "vue";

// 登录表单对象
export const loginForm = reactive({
    password: "",
    username: "",
    remember: false
})

// 登录规则
export const loginRules = {
    username: [
        { required: true, message: "请输入用户名", trigger: "blur" }
    ],
    password: [
            { required: true, message: "请输入密码", trigger: "blur" }
        ]
        // remember: [{
        //     // 自定义校验逻辑
        //     // value: 当前输入的数据
        //     // callback: 校验处理函数 校验通过调用
        //     validator: (rule, value, callback) => {

    //     }
    // }]
}