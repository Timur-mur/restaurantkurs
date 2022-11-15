<template>
  <Navbar></Navbar>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Корзина</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="products!==null">
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
export default {
  name: "Cart",
  components: {Navbar, CartItem},
  mounted() {
    document.title = 'Корзина | Эmurr'
  },
  methods:{

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