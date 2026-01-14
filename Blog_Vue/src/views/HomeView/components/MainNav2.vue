<template>
    <div class="container">
        <el-menu :default-active="activeIndex" class="navMenu" mode="horizontal" @select="hanleSelect">
            <el-menu-item index="1" class="item">
                <Router-link to="/">
                    <span class="leader_title-cn">主页</span>
                    <span class="leader_title-en">Home</span>
                    <span class="underLine"></span>
                </Router-link>
            </el-menu-item>

            <el-menu-item index="2" class="item">
                <Router-link to="/essay">
                    <span class="leader_title-cn">随笔</span>
                    <span class="leader_title-en">Essay</span>
                    <span class="underLine"></span>
                </Router-link>
            </el-menu-item>

            <el-menu-item index="3" class="item">
                <a>
                    <span class="leader_title-cn">杂项</span>
                    <span class="leader_title-en">Sundry</span>
                    <span class="underLine"></span>
                </a>
            </el-menu-item>

            <el-sub-menu index="4" class="item">
                <template #title>
                    <a>
                        <span class="leader_title-cn">个人</span>
                        <span class="leader_title-en">Persion</span>
                        <span class="underLine"></span>
                    </a>
                </template>
                <el-menu-item id="sub_item" index="4-1">个人空间</el-menu-item>
                <el-menu-item id="sub_item" @click="handleLogout" index="4-2">退出登录</el-menu-item>
            </el-sub-menu>

        </el-menu>

    </div>

</template>

<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue';
import { useUserStore } from '@/stores/userStore'
import { ElMessageBox, ElMessage } from 'element-plus'

const activeIndex = ref('1')

const hanleSelect = (key, keyPath) => {
    console.log(key, keyPath)
}

const userStore = useUserStore()
const handleLogout = () => {
    ElMessageBox.confirm(
        "确认退出登录？",

    )
        .then(() => {
            userStore.clearUserInfo()
            ElMessage({
                type: 'success',
                message: "退出成功"
            })
        })
}

</script>

<style scoped lang="scss">
.container {
    position: sticky;
    top: 0;
    z-index: 5;

    :deep(.el-menu) {
        list-style-type: none;
        overflow: visible;
        background-color: rgb(37, 37, 37);
        border: 2px solid rgb(37, 37, 37);
        margin: 0;
        height: 55px;
        position: sticky;
        display: flex;
        flex-direction: row;
        justify-content: end;
        top: 0;

        .el-sub-menu.is-active .el-sub-menu__title {
            border-bottom: none;
        }

        .el-sub-menu__title,
        .item {
            height: 100%;
            position: relative; // 添加相对定位，为下划线定位提供参考
            align-items: center;
            border-bottom: none;
            line-height: normal; // 重置行高，允许内部双行文字自然堆叠
            padding: 0;

            #sub_item {
                background-color: rebeccapurple;
            }

            a {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border-bottom: none;
                padding-top: 5px;
                height: 100%;
                background-color: rgb(37, 37, 37);
                padding: 0 15px; //Padding 加在这里，撑开点击区域
                transition-duration: 0.3s;
                text-decoration: none;
                position: relative; // 为下划线定位提供参考

                .leader_title-cn {
                    color: rgb(255, 255, 255);
                    text-decoration: none;
                    font-size: 18px;
                    line-height: 1.5; //控制行高，确保文本不会堆叠
                }

                .leader_title-en {
                    color: rgb(206, 205, 205);
                    text-decoration: none;
                    font-size: 12px;
                    line-height: 1.5;
                }

                // 为所有链接添加下划线效果
                &::after {
                    content: '';
                    position: absolute;
                    bottom: 0;
                    left: 50%;
                    width: 0;
                    height: 2px;
                    background-color: rgb(4, 194, 219);
                    transform: translateX(-50%);
                    transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                }

                &:active,
                &:hover {
                    background-color: rgb(37, 37, 37);

                    &::after {
                        width: 80%; // 现在的宽是相对于整个菜单格子的 80%，效果更佳
                    }
                }

            }

            // 隐藏 Element 自带的小箭头（可选，为了美观）
            .el-sub-menu__icon-arrow {
                display: none;
            }

        }

        // 鼠标覆盖后
        .item:hover:not(.active) {
            background-color: rgb(37, 37, 37);
            // background-color: red;
            color: rgb(0, 174, 255);
            font-size: 18px;
            text-decoration: none;

            .leader_title-cn {
                color: rgb(255, 255, 255);
            }

            .leader_title-en {
                color: rgb(206, 205, 205);
            }

        }

        // 鼠标点击后
        .item:active,
        .item:focus,
        .item:active {
            background-color: rgb(37, 37, 37);
            // background-color: red;
            color: rgb(0, 174, 255);
            font-size: 18px;
            text-decoration: none;
        }

    }
}
</style>
