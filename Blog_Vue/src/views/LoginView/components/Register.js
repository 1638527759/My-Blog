import { reactive } from "vue"

// 注册表单
export const registerForm = reactive({
    username: '',
    email: '',
    password: '',
    passwordAgain: ''
});

export const registerRules = {
    username: [
        { required: true, message: "请输入用户名", trigger: "blur" },
        { min: 3, max: 20, message: "用户名长度在3到20个字符", trigger: "blur" }
    ],
    email: [
        { required: true, message: "请输入邮箱", trigger: "blur" },
        { type: "email", message: "请输入正确的邮箱格式", trigger: ["blur", "change"] }
    ],
    password: [
        { required: true, message: "请输入密码", trigger: "blur" },
        { min: 6, message: "密码至少6位", trigger: "blur" }
    ],
    passwordAgain: [
        { required: true, message: "请输入密码", trigger: "blur" },
        { min: 6, message: "密码至少6位", trigger: "blur" },
        {
            //     // 自定义校验逻辑
            //     // value: 当前输入的数据
            //     // callback: 校验处理函数 校验通过调用
            validator: (rule, value, callback) => {
                if (value === registerForm.password) {
                    callback()
                } else {
                    callback(new Error("两次输入的密码不一致"))
                }
            },
            trigger: "blur"
        }
    ],

}