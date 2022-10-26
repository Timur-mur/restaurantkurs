<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong> Эmurr </strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/menu" class="navbar-item"> Меню </router-link>
          <router-link to="/about" class="navbar-item"> О нас </router-link>
          <router-link to="/reviews" class="navbar-item"> Отзывы </router-link>
          <router-link to="/сhat" class="navbar-item"> Чат </router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light"> Вход </router-link>
              
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
<!--                <span> Корзина ({{cartTotalLength}})</span>-->
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Navbar",
  data(){
    return{
      showMobileMenu: false,
      cart:{
        items: []
      }
    }
  },
  mounted() {
  },
  computed: {
  }
}
</script>

<style scoped>

</style>