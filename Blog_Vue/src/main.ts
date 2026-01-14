// import './assets/main.css'
// import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
// app.use(createPinia())
app.use(router)
app.use(ElementPlus)
// pinia.use(piniaPluginPersistedstate)
pinia.use(piniaPluginPersistedstate)

app.mount('#app')



