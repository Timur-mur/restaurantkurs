<template>
  <Navbar></Navbar>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Корзина</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
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
            <CartItem v-for="item in cart.items" v-bind:key="item.Products.id" v-bind:initialItem="item" v-on:removeFromCart="removeFromCart"/>
          </tbody>
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
export default {
  name: "Cart",
  components: {Navbar, CartItem},
  data(){
    return{
      cart:{
        items: []
      }
    }
  },
  // mounted() {
  //   // this.$store.dispatch('initStore')
  //   this.cart = this.$store.state.cart
  //   document.title = 'Корзина | Эmurr'
  // },
  methods:{
    removeFromCart(item){
      this.cart.items = this.cart.items.filter(i => i.Products.id !== item.Products.id)
    },
  },
  computed: {
    cartTotalLength(){
      return this.cart.items.reduce((acc, curVal) =>{
        return acc+=curVal.quantity
      },0)
    }
  }
}
</script>

<style scoped>

</style>