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
              <h2 class="is-size-4">{{ feeds.author.get_username }}</h2>
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
export default {
  name: "Reviews",
  components: {Navbar},
  data(){
    return{
      feedbacks: null,
      feedtext: '',

    }
  },
  mounted() {
    this.GetFeedbacks()
  },
  methods:{
    GetFeedbacks(){
      axios
          .get('http://localhost:8000/api/v2/feedbacks')
          .then(response =>{
            this.feedbacks = response.data
            document.title = 'Отзывы | Эmurr'
            console.log(response.data)
          })
    },
    CreateFeedbacks(){
      axios
          .post('http://localhost:8000/api/v2/feeds-create', {})
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