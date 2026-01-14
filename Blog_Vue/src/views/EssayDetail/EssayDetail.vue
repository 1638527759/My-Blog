<template>
    <div class="background">
        <nav class="top-nav">
            <MainNav></MainNav>
        </nav>


        <main class="container">
            <div class="essay-content">
                <div class="title-box">
                    <h2>{{ Essay.title }}</h2>
                </div>
                <article>
                    {{ Essay.content }}
                </article>
            </div>

            <div class="message-card">

            </div>
        </main>
    </div>
</template>
<script setup name="EssayDetail">
import MainNav from '@/components/MainNav.vue'
import api from '@/api/blog'
import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';

const Essay = ref('')
const route = useRoute()

const getEssay = async () => {
    const id = route.params.id
    const res = await api.get(`/essays/${id}/`)
    Essay.value = res.data.data

}

onMounted(() => {
    getEssay()
})

</script>
<style scoped lang="scss">
* {
    padding: 0;
    margin: 0;
}

.background {
    background-color: rgb(240, 240, 240);
}

.top-nav {
    position: relative;
    z-index: 10;
    width: 100vw;
    height: 100%;
    background-color: rgb(0, 0, 0);
}

@media (min-width: 1026px) {
    .container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        width: 75vw;
        height: 100vh;
        margin: auto;
        margin-top: 30px;

        .essay-content {
            width: 70%;
            height: 100%;
            background-color: white;
            box-shadow: 4px 2px 4px #55555555;
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            justify-content: start;
            align-items: center;

            article {
                padding: 20px;
                text-align: left;
                line-height: 1.6;
            }

        }

        .message-card {
            top: 0;
            width: 25%;
            height: 70%;
            background-color: white;
            box-shadow: 4px 2px 4px #55555555;
            border-radius: 5px;
            margin: auto;
            margin-top: 0;
        }
    }
}

@media (max-width: 1025px) {
    .container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        width: 75vw;
        height: 100vh;
        margin: auto;
        margin-top: 30px;

        .essay-content {
            width: 100%;
            height: 100%;
            background-color: white;
            box-shadow: 4px 2px 4px #55555555;
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            justify-content: start;
            align-items: center;

            article {
                padding: 20px;
                text-align: left;
                line-height: 1.6;
            }
        }

        .message-card {
            display: none;
        }
    }
}
</style>