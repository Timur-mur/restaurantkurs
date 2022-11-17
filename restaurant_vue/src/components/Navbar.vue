<template>
<!--  <div id="wrapper">-->
<!--    <nav class="navbar is-dark">-->
<!--      <div class="navbar-brand">-->
<!--        <router-link to="/" class="navbar-item"><strong> Эmurr </strong></router-link>-->

<!--        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">-->
<!--          <span aria-hidden="true"></span>-->
<!--          <span aria-hidden="true"></span>-->
<!--          <span aria-hidden="true"></span>-->
<!--        </a>-->
<!--      </div>-->
<!--      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">-->
<!--        <div class="navbar-end">-->
<!--          <router-link to="/menu" class="navbar-item"> Меню </router-link>-->
<!--          <router-link to="/about" class="navbar-item"> О нас </router-link>-->
<!--          <router-link to="/reviews" class="navbar-item"> Отзывы </router-link>-->
<!--          <router-link to="/orders" class="navbar-item" v-if="username==='root'"> Заказы </router-link>-->
<!--          <router-link to="/client" class="navbar-item" v-else> Заказы </router-link>-->

<!--&lt;!&ndash;          <router-link to="/chat" class="navbar-item"> Чат </router-link>&ndash;&gt;-->
<!--          <div class="navbar-item">-->
<!--            <div class="buttons">-->
<!--              <router-link to="/log-in" class="button is-light" v-if="!isAuthenticated"> Вход </router-link>-->
<!--              <button  class="button is-light" v-if="isAuthenticated" @click="LogOut()"> Выход </button>-->
<!--              <router-link to="/cart" class="button is-success">-->
<!--                <span class="icon"><i class="fas fa-shopping-cart"></i></span>-->
<!--&lt;!&ndash;                <span> Корзина ({{cartTotalLength}})</span>&ndash;&gt;-->
<!--              </router-link>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </nav>-->
<!--  </div>-->
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";

export default {
  name: "Navbar",
  data(){
    return{
      showMobileMenu: false,
    }
  },
  mounted() {
    this.$store.commit('initializeStore')
  },
  methods:{
    LogOut(){
      this.$store.commit('removeToken')
      this.$router.push('/log-in')
    }
  },
  computed:{
    ...mapGetters({
          isAuthenticated: "isAuthenticated",
          username: "username"
    }),
  }
}
</script>

<style scoped>

</style>