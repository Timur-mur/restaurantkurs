<template>
  <Navbar></Navbar>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Корзина</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="products.length!==0">
          <thead>
            <tr>
              <th>Блюдо</th>
              <th>Цена</th>
              <th>Количество</th>
              <th>Общая стоимость</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <CartItem v-for="product in products" v-bind:key="product.id" :product="product"/>
          </tbody>
          <thead>
            <tr>
              <th>Общая стоимость: {{cart_total}}</th>
              <th>
                Номер столика:
                <div class="control" style="display: inline-block">
                  <input  type="number" class="input" v-model="table">
                </div>
              </th>
              <th>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="PostOrder"> Заказать </button>
                  </div>
                </div>
              </th>
            </tr>
          </thead>
        </table>
        <p v-else> Ваша корзина пуста </p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import CartItem from "@/components/CartItem";
import axios  from "axios";
import {toast} from "bulma-toast";
export default {
  name: "Cart",
  components: {Navbar, CartItem},
  data(){
    return {
      table: '',
      userinfo: '',
      ordersArray: [],
    }
  },
  mounted() {
    this.$store.commit("updateCartFromLocalStorage")
    document.title = 'Корзина | Эmurr'
    this.GetUserId()
  },
  methods:{
    GetUserId(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
          .get('http://127.0.0.1:8000/auth/users/me')
          .then(response =>{
            this.userinfo = response.data
          })
    },
    PostOrder(){
      let len = Object.keys(this.products).length;
            for (let i = 0; i < len; i++)
              this.ordersArray.push({
                username_id: this.userinfo.id,
                table: this.table,
                product_name: this.products[i].name,
                quantity: this.products[i].quantity
              });
      console.log(this.ordersArray)
      axios
          .post("http://localhost:8000/api/v1/orders", this.ordersArray)
          .then(response => {
              toast({
                  message: 'Уже начали готовить! Спасибо, что вы с нами',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
      this.ordersArray.length = 0
    },
  },
  computed: {
    products(){
      return this.$store.getters.cartItems
    },
    cart_total(){
      return this.$store.getters.cartTotal
    }
  }
}
</script>

<style scoped>

</style>