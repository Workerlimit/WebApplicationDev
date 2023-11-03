<template>
  <Header></Header>
  <div class="home">
    <div>
      <PostList />
    </div>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import PostList from '@/components/PostList.vue';
</script>

<style lang="scss" scoped>
a {
  color: initial !important;
  text-decoration: none;
  &:visited, &:focus, &:active {
    color: initial !important;
  }
}

.home {
  padding: 48px 0;
  background: #ffffff;
}
</style>
