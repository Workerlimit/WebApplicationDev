<template>
    <div class="p-detail">
        <Header></Header>
        <div class="container p-detail__content">
            <div class="d-flex align-center justify-between">
                <p class="text-l mb-20">Post Detail</p>
                <RouterLink :to="`${route.params.id}/edit`"><button>Edit post</button>   </RouterLink>  
            </div>

            <p>{{ post.title }}</p>
            <p>{{ post.body }}</p>
            
            <div class="comments">
                <div class="d-flex align-center justify-between">
                    <p class="text-m">Comments</p>
                    <span class="text-xs" @click="isHide = !isHide">{{ isHide ? 'Show all' : 'Hide all' }}</span>
                </div>
                

                <ul v-if="!isHide" class="mt-10">
                    <li v-for="comment in comments" :key="comment.id">
                        <strong>{{ comment.name }}</strong>: {{ comment.body }}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

import Header from "@/components/Header.vue";

const route = useRoute();

const post = ref({});
const comments = ref([]);

const isHide = ref(true);

onMounted(async () => {
    try {
        const postId = route.params.id;
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`);
        post.value = await response.json();

        const commentsResponse = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
        comments.value = await commentsResponse.json();
    } catch (error) {
        console.error('Error fetching post details:', error);
    }
});
</script>

<style lang="scss" scoped>
.p-detail {
    & .comments {
        background: #3a589968;
        border: 20px;
        padding: 20px;
        margin-top: 16px;
        border-radius: 16px;
        & span:hover {
            cursor: pointer;
        }
    }
    &__content {
        margin: 30px 0;
    }
}
</style>
  