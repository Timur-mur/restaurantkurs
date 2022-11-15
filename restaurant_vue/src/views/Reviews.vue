<template xmlns="http://www.w3.org/1999/html">
  <navbar></navbar>
  <div class="feedbacks">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Все о нас от вас)
        </p>
      </div>
    </section>
    <div class="form-control-feedback">
      <div v-for="feeds in feedbacks">
        <div class="has-feedback">
              <h2 class="is-size-4">{{ feeds.author.username }}</h2>
              <h3 class="is-size-5 has-text-grey">{{ feeds.text}}</h3>
              <p class="is-size-5 has-text-grey">Дата публикации: {{ feeds.create_date }}</p>
            </div>
      </div>
    </div>
    <div class="column" v-if="isAuthenticated">
      <form @submit.prevent="CreateFeedbacks">
        <input class="textarea" placeholder="Отзыв сюды" v-model="feedtext">
        <button class="button is-dark">  Отправить </button>
      </form>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {mapGetters} from "vuex";
import {toast} from "bulma-toast";
export default {
  name: "Reviews",
  components: {Navbar},
  data(){
    return{
      userinfo: '',
      feedbacks: null,
      feedtext: '',
    }
  },
  mounted() {
    axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
    this.GetFeedbacks()
    this.GetUserId()
  },
  methods:{
    GetFeedbacks(){
      axios
          .get('http://localhost:8000/api/v2/feedbacks')
          .then(response =>{
            this.feedbacks = response.data
            document.title = 'Отзывы | Эmurr'
          })
    },
    GetUserId(){
      axios
          .get('http://127.0.0.1:8000/auth/users/me')
          .then(response =>{
            this.userinfo = response.data
          })
    },
    CreateFeedbacks(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      const formData = {
        author: this.userinfo.id,
        text: this.feedtext
      }
      console.log(formData)
      axios
          .post('http://localhost:8000/api/v2/feeds-create', formData)
          .then(response => {
                  toast({
                      message: 'Спасибо за ваш отзыв!',
                      type: 'is-success',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
              })
    }
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "isAuthenticated",
      username: "username",
    }),
  },
}
</script>

<style scoped>

</style>