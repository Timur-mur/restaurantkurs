<template>
<Navbar></Navbar>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title"> Вход </h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Имя пользователя</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>
          <div class="field">
            <label>Пароль</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark"> Войти </button>
            </div>
          </div>
          <hr>
            Не зарегистрированы? <router-link to="/sign-up"> Зарегистрироваться </router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {toast} from "bulma-toast";
export default {
  name: "LogIn",
  components: {Navbar},
  data(){
    return{
      username: '',
      password: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Вход | Эmurr'
  },
  methods: {
     submitForm(){
      axios.defaults.headers.common['Authorization'] = ""

      const formData = {
        username: this.username,
        password: this.password
      }
       axios
          .post("http://localhost:8000/auth/token/login/", formData)
          .then(response=>{
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common["Authorization"] = "Token" + token
            localStorage.setItem("username", this.username)
            localStorage.setItem("token", token)
            this.$router.push("/cart")
          })
          .catch(error=>{
            toast({
                message: 'Что-то пошло не так. Попробуйте снова.',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
          })
    }
  }
}
</script>

<style scoped>

</style>