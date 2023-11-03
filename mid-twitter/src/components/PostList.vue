<template>
    <div class="p-list">
        <div class="p-list__content container">
            <div class="d-flex justify-between align-items mb-20">
                <p class="text-l">Post List</p>
                <RouterLink to="/add"><button>Add post</button></RouterLink>
            </div>
            <template v-for="post in posts" :key="post.id">
                <li>
                    <router-link :to="{ name: 'postDetail', params: { id: post.id } }">
                        <p>{{ post.title }}</p>
                    </router-link>
                </li>
            </template>
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';

const posts = ref([]);

onMounted(async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        posts.value = await response.json();
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
});
</script>

<style lang="scss" scoped>
a {
  color: initial !important;
  text-decoration: none;
  &:visited, &:focus, &:active {
    color: initial !important;
  }
}
.p-list {
    &__content {
        h2 {
            margin-bottom: 30px;
        }
    }
    li {
        list-style: none;
        background: #bffee7;
        border: 1px solid #bffee7;
        border-radius: 20px;
        padding: 40px 20px;
        transition: all .3s ease;
        &:hover {
            cursor: pointer;
            border: 1px solid #07563b;
        }
        & p {
            font-weight: 500;
        }
        & + li {
            margin-top: 30px;
        }   
    }
}
</style>