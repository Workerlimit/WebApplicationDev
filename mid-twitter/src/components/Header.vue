<template>
    <header>
        <div class="container">
            <nav class="d-flex">
                <router-link to="/"><p>Custom <br/>Twitter</p></router-link>
                <router-link to="/profile">Profile</router-link>
            </nav>
        </div>
    </header>
</template>

<script setup></script>

<style lang="scss" scoped>
header{
    width: 100%;
    padding: 30px 0;
    background: #dffff1;
    border-radius: 0 0 20px 20px;
    nav {
        gap: 40px;
    }
    a {
        font-weight: bold;
        color: #2c3e50;
        text-decoration: none;
        p {
        font-size: 12px;
        }

        &.router-link-exact-active {
        color: #42b983;
        }
    }
}
</style>