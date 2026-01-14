import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView/HomeView.vue'
import LoginView from '@/views/LoginView/LoginView.vue'
import Test from '@/views/Test.vue'
import Essay from '@/views/Essay/Essay.vue'
import EssayDetail from '@/views/EssayDetail/EssayDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/test',
      name: 'test',
      component: Test,
    },
    {
      path: '/essay',
      name: 'essay',
      component: Essay,
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: EssayDetail,
      props: true,
    }
  ],
})

export default router
