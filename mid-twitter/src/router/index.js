import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: function () {
      return import('../views/AboutView.vue')
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: function () {
      return import('../views/ProfileView.vue')
    }
  },
  {
    path: '/post/:id',
    name: 'postDetail',
    component: function () {
      return import('../views/PostDetail.vue')
    }
  },
  {
    path: '/add',
    name: 'addPost',
    component: function () {
      return import('../views/NewPost.vue')
    }
  },
  {
    path: '/post/:id/edit',
    name: 'editPost',
    component: function () {
      return import('../views/EditPost.vue')
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
