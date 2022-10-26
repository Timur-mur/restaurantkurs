<template>
<navbar></navbar>
  <div class="menu">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Познакомьтесь с нашим меню
        </p>
        <div class="columns">
           <div class="column"  v-for="sl in category">
              <button class="button is-light" @click="getProduct(sl.id)"> {{ sl.name }} </button>
           </div>
        </div>

      </div>
    </section>
    <div class="columns is-multiline">
          <div class="column is-3" v-for="product in products" >
            <div class="box">
              <h2 class="is-size-4">{{ product.name }}</h2>
              <h3 class="is-size-5 has-text-grey">{{ product.description}}</h3>
               <p class="is-size-5 has-text-grey">Стоимость: {{ product.price }} рублей</p>
              <div class="field has-addons mt-6">
                <div class="control">
                  <input class="input" type="number" min="1" v-model="product.quantity">
                </div>
                <div class="control">
                  <a class="button is-dark" @click="addToCart"> В корзину </a>
                </div>
              </div>
            </div>
          </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "Menu",
  components: {Navbar},
  data(){
    return{
      category: null,
      products: null,
      quantity: 1,
    }
  },
   mounted() {
    axios
          .get('http://localhost:8000/api/v1/category-list/')
          .then(response=>{
            this.category = response.data
            console.log(response.data)
            document.title = this.category.name + ' | Эmurr'
          })
  },
  methods: {
     getProduct(cat_id){
      axios
          .get('http://localhost:8000/api/v1/product-list/' + cat_id)
          .then(response=>{
            this.products = response.data
            document.title = this.category.name + ' | Эmurr'
          })
    },
    // addToCart() {
    //   if (isNaN(this.quantity) || this.quantity < 1)
    //   {
    //     this.quantity = 1
    //   }
    //   const item = {
    //     products: this.products,
    //     quantity: this.quantity,
    //   }
    //   console.log(this.products)
    //   this.$store.commit('addToCart', item)
    //
    //   toast({
    //     message: 'Позиция была добавлена в корзину',
    //     type: 'is-success',
    //     dismissible: true,
    //     pauseOnHover: true,
    //     duration: 2000,
    //     position: "bottom-right",
    //   })
    // }
  }
}
</script>

<style scoped>

</style>