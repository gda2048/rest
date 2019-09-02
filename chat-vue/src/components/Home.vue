<template>
  <div>
    <h1>Чат на vue.js</h1>
    <button v-if='!auth' @click="goLogin">Вход</button>
    <button v-if='auth' @click="goLogout">Выход</button>
    <Room v-if="auth"></Room>
  </div>
</template>

<script>
  import Room from '@/components/Room'

  export default {
    name: "Home",
    components: {
      Room
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true;
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      goLogout(){
        sessionStorage.removeItem("auth_token");
        window.location = '/';
      }
    }
  }
</script>

<style scoped>

</style>
