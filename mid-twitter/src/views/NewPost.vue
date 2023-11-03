<template>
    <div class="new-post">
        <div class="container">
            <div class="new-post__content">
                <p class="text-l mb-20">Add new post</p>
                <form @submit.prevent="addPost" class="d-flex column">
                    <label for="title">Title:</label>
                    <input type="text" placeholder="Title" id="title" v-model="data.title" required>

                    <label for="body">Message:</label>
                    <textarea id="body" placeholder="Message" v-model="data.body" required></textarea>

                    <button type="submit">Add Post</button>
                </form>

                <div v-if="isSuccess" class="success-popup">
                    Post added successfully!
                </div>

                <div v-if="isError" class="error-popup">
                    Error adding post. Please try again.
                </div>
            </div>
        </div>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const data = ref({
    title: '',
    body: '',
});

const isSuccess = ref(false);
const isError = ref(false);

const addPost = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data.value),
        });

        if (response.ok) {
            // isSuccess.value = true;
            // isError.value = false;
            
            data.value.title = '';
            data.value.body = '';
            router.push({ name: 'home' });
        } else {
            isSuccess.value = false;
            isError.value = true;
        }
    } catch (error) {
        isSuccess.value = false;
        isError.value = true;
    }
};
</script>
  
<style lang="scss" scoped>
.new-post {
    &__content {
        padding: 60px 0;
    }
    form {
        width: 500px;
        gap: 10px;
    }
}
</style>
  