<template>
  <Navbar></Navbar>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title"> Регистрация </h1>
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
          <div class="field">
            <label>Подтвердите пароль</label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark"> Зарегистрироваться </button>
            </div>
          </div>
          <hr>
            Уже зарегистрированы? <router-link to="/log-in"> Войти </router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import Navbar from "@/components/Navbar";
export default {
  name: "SignUp",
  components: {Navbar},
  data(){
    return{
      username: '',
      password: '',
      password2: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Регистрация | Эmurr'
  },
  methods:{
    submitForm(){
      this.errors = []
      if (this.username ==='')
        this.errors.push('Введите имя пользователя')
      if (this.password ==='')
        this.errors.push('Введите пароль')
      if (this.password !== this.password2)
        this.errors.push('Пароли не совпадают')
      if (!this.errors.length)
      {
        const formData = {
          username: this.usernam,
          password: this.password
        }
        axios
            .post('api/v1/users/', formData)
            .then(response=>{
              toast({
                message: 'Регистрация прошла успешно! Войдите в аккаунт',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })
              this.$router.push('log-in')
            })
            .catch(error =>{
              if(error.response){
                for(const property in error.response.data){
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                console.log(JSON.stringify(error.response.data))
              }
              else if (error.message){
                this.errors.push("Что-то пошло не так. Попробуйте еще раз")
                console.log(JSON.stringify(error))
              }
            })

      }
    }
  },
}
</script>

<style scoped>

</style>