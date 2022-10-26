import { createRouter, createWebHistory } from 'vue-router'
import main from "@/views/Main";
import Menu from "@/views/Menu";
import Reviews from "@/views/Reviews";
import Cart from "@/views/Cart";
import SignUp from "@/views/SignUp";
import LogIn from "@/views/LogIn";

const routes = [
  {path:'/', component: main, name: "ЭMurr"},
  {path: '/menu', component: Menu, name: "ЭMurr меню"},
  {path: '/reviews', component: Reviews, name: "Эmurr отзывы"},
  {path: '/cart', component: Cart, name: "Эmurr Корзина"},
  {path: '/sign-up', component: SignUp, name: "Эmurr Регистрация"},
  {path: '/log-in', component: LogIn, name: "Эmurr Вход"}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
