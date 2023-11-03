import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import '@/assets/style/style.scss'
import '@/assets/style/media.scss'
createApp(App).use(router).mount('#app')
