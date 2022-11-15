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
<!--                <div class="control">-->
<!--                  <input class="input" type="number" min="1" v-model="product.quantity">-->
<!--                </div>-->
                <div class="control">
                  <a class="button is-dark" @click="addToCart(product)"> В корзину </a>
                </div>
              </div>
            </div>
          </div>
    </div>
    <div v-if="username==='root'">
      <div class="columns">
        <div class="column">
          <button class="button is-light" v-on:click="isOpen = 1"> Добавить блюдо </button>
        </div>
        <div class="column">
          <button class="button is-light" v-on:click="isOpen = 2"> Добавить категорию </button>
        </div>
        <div class="column">
          <button class="button is-light" v-on:click="isOpen = 4"> Удалить категорию </button>
        </div>
        <div class="column">
          <button class="button is-light" v-on:click="isOpen = 3" v-if="products!==null"> Удалить блюдо </button>
        </div>
        <div class="column">
          <button class="button is-light" v-on:click="isOpen = 5" v-if="products!==null"> Отредактировать блюдо </button>
        </div>
      </div>
        <div v-if="isOpen === 1">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Добавление позиции в меню </h1>
              <form @submit.prevent="CreateProduct">
                <div class="field">
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="prod.category" >
                          <option v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <label>Название блюда</label>
                  <div class="control">
                    <input type="text" class="input" v-model="prod.name">
                  </div>
                </div>
                <div class="field">
                  <label>Описание</label>
                  <div class="control">
                    <input type="text" class="input" v-model="prod.description">
                  </div>
                </div>
                <div class="field">
                  <label>Стоимость</label>
                  <div class="control">
                    <input type="number" class="input" v-model="prod.price">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark"> Добавить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>

        <div v-if="isOpen === 2">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Добавление категории </h1>
              <form @submit.prevent="CreateCategory">
                <div class="field">
                  <label>Название категории</label>
                  <div class="control">
                    <input type="text" class="input" v-model="cat.name">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark"> Добавить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 3">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Удаление позиции </h1>
              <form>
                <div class="field">
                  <label>Позиция</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="prod in products" v-bind:value="prod.id" >{{ prod.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="DeleteProduct(idparam)"> Удалить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 4">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Удаление категории </h1>
              <form>
                <div class="field">
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="DeleteCategory(idparam)"> Удалить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 5">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Редактирование позиции </h1>
              <form>
                <div class="field">
                  <label>Выберите продукт</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="prod in products" v-bind:value="prod.id" >{{ prod.name }}</option>
                      </select>
                    </div>
                  </div>
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="prod.category" >
                          <option v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <label>Название блюда</label>
                  <div class="control">
                    <input type="text" class="input" v-model="prod.name">
                  </div>
                </div>
                <div class="field">
                  <label>Описание</label>
                  <div class="control">
                    <input type="text" class="input" v-model="prod.description">
                  </div>
                </div>
                <div class="field">
                  <label>Стоимость</label>
                  <div class="control">
                    <input type="number" class="input" v-model="prod.price">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="UpdateProduct(idparam)"> Отредактировать </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import { toast } from "bulma-toast";
import {mapGetters} from "vuex";
export default {
  name: "Menu",
  components: {Navbar},
  data(){
    return{
      category: null,
      products: null,
      quantity: 1,
      isOpen: 0,
      prod: {
        category: '',
        name: '',
        description: '',
        price: '',
      },
      cat: {
        id: '',
        name: ''
      },
      idparam: '',
    }
  },
   mounted() {
    this.$store.commit("updateCartFromLocalStorage")
    axios
          .get('http://localhost:8000/api/v1/category-list/')
          .then(response=>{
            this.category = response.data
            console.log(response.data)
            document.title ='Меню | Эmurr'
          })
  },
  methods: {
     getProduct(cat_id){
      axios
          .get('http://localhost:8000/api/v1/product-list/' + cat_id)
          .then(response=>{
            this.products = response.data
          })
    },
    CreateProduct(){
       axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
       const formData = {
         category: this.prod.category,
         name: this.prod.name,
         description: this.prod.description,
         price: this.prod.price,
      }
       axios
           .post('http://localhost:8000/api/v1/product-create/', formData)
           .then(response => {
              toast({
                  message: 'Блюдо было добавлено',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    CreateCategory(){
       axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
       const formData = {
         name: this.cat.name,
      }
       axios
           .post('http://localhost:8000/api/v1/category-create/', formData)
           .then(response => {
              toast({
                  message: 'Категория была создана',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    UpdateProduct(prod_id){
        axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
        const formData = {
          category: this.prod.category,
          name: this.prod.name,
          description: this.prod.description,
          price: this.prod.price
        }
        axios
            .post('http://localhost:8000/api/v1/product-update/'+ prod_id, formData)
            .then(responce => {
              toast({
                  message: 'Позиция была обновлена',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
            })
    },
    DeleteCategory(cat_id){
       axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")

       axios
           .delete('http://localhost:8000/api/v1/category-delete/' + cat_id )
           .then(response => {
              toast({
                  message: 'Категория была удалена',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    DeleteProduct(prod_id){
       axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")

       axios
           .delete('http://localhost:8000/api/v1/product-delete/' + prod_id )
           .then(response => {
              toast({
                  message: 'Позиция была удалена',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    addToCart(prod) {
      this.$store.commit('addToCart', prod)

      toast({
        message: 'Позиция была добавлена в корзину',
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
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