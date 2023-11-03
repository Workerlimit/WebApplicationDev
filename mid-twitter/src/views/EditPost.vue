<template>
    <div class="edit-page">
        <div class="container">
            <div class="edit-page__content">
                <h2>Edit Post</h2>
                <form @submit.prevent="editPost">
                    <label for="title">Title:</label>
                    <input type="text" id="title" v-model="editedPost.title" required>

                    <label for="body">Body:</label>
                    <textarea id="body" v-model="editedPost.body" required></textarea>

                    <button type="submit">Save Changes</button>
                </form>

                <div v-if="isSuccess" class="success-popup">
                    Post updated successfully!
                </div>

                <div v-if="isError" class="error-popup">
                    Error updating post. Please try again.
                </div>
            </div>
        </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const editedPost = ref({
  title: '',
  body: '',
});

const originalPost = ref({
  title: '',
  body: '',
});

const isSuccess = ref(false);
const isError = ref(false);
const router = useRouter();

onMounted(async () => {
  try {
    const postId = router.params.id;

    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`);
    const postDetails = await response.json();

    originalPost.value.title = postDetails.title;
    originalPost.value.body = postDetails.body;

    editedPost.value.title = postDetails.title;
    editedPost.value.body = postDetails.body;
  } catch (error) {
    console.error('Error fetching post details for editing:', error);
  }
});

const editPost = async () => {
  try {
    const postId = router.params.id;

    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(editedPost.value),
    });

    if (response.ok) {
      isSuccess.value = true;
      isError.value = false;

      router.push({ name: 'postDetail', params: { id: postId } });
    } else {
      isSuccess.value = false;
      isError.value = true;
    }
  } catch (error) {
    console.error('Error updating post:', error);
    isSuccess.value = false;
    isError.value = true;
  }
};
</script>
  
<style lang="scss" scoped>
.edit-page {
    &__content {
        padding: 60px 0;
    }
    form {
        width: 500px;
        gap: 10px;
    }
}
</style>
  