<template>
  <div>
    <div v-for="dialog in dialogs">
      <h2>{{dialog.user.username}}</h2>
      <p>{{dialog.text}}</p>
      <span>{{dialog.date}}</span>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "dialog",
    props: {
      id: ""
    },
    data() {
      return {
        dialogs: '',
      }
    },
    created() {
      $.ajaxSetup(
        {
          headers: {'Authorization': "Token " + sessionStorage.getItem("auth_token")}
        }
      );
      this.loadDialog();
    },
    methods: {
      loadDialog() {
        $.ajax({
          url: "http://127.0.0.1:8090/api/v1/chat/message/",
          type: 'GET',
          data: {
            "room": this.id
          },
          success: (response) => {
            this.dialogs = response.data.data;
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
