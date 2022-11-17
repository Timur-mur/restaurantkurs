<template>
  <navbar></navbar>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Ресторан Эmurr
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2  has-text-centered"> Новые блюда </h2>
      </div>
      <div class="column is-3" v-for="product in Products" v-bind:key="product.id">
        <div class="box">
          <h2 class="is-size-4">{{ product.name }}</h2>
          <h3 class="is-size-5 has-text-grey">{{ product.description}}</h3>
           <p class="is-size-5 has-text-grey">{{ product.price }}</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
export default {
  name: "Main",
  components: {Navbar},
  data(){
    return{
      Products: [],
    }
  },
  mounted() {
    axios
        .get("http://localhost:8000/api/v1/product-list/")
        .then(response=>{
          this.Products = response.data
          document.title = 'Эmurr'
        })
  },
}
</script>

<style scoped>

</style>