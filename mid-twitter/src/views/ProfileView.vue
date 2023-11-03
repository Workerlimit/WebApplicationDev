<template>
    <div class="profile">
        <div class="container">
            <div class="profile__content d-flex column">
                <h2 class="mb-20">User Profile</h2>
                <p><strong>Name:</strong> {{ user.name }}</p>
                <p><strong>Email:</strong> {{ user.email }}</p>
                
                <div class="comments">
                    <h3 class="mb-20">Your comments</h3>
                    <ul>
                        <li v-for="comment in userComments" :key="comment.id">
                            <strong>{{ comment.name }}</strong>: {{ comment.body }}
                        </li>
                    </ul>
                </div>    
            </div> 
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';

const user = ref({});
const userComments = ref({});

onMounted(async () => {
    try {
        const userId = 1;

        const userResponse = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
        user.value = await userResponse.json();

        const commentsResponse = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${userId}`);
        userComments.value = await commentsResponse.json();
    } catch (error) {
        console.error('Error fetching user details or comments:', error);
    }
});
</script>

<style lang="scss" scoped>
.profile {
    &__content {
        padding: 30px 0;
    }
}

.comments {
    background: #3a589968;
    border: 20px;
    padding: 20px;
    margin-top: 16px;
    border-radius: 16px;
    & span:hover {
        cursor: pointer;
    }
}
</style>