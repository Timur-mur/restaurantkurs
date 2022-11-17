<template>
<navbar></navbar>
  <div class="page-orders">
    <div class="columns is-multiline">
      <div class="column is-12">
        <button class="button is-light" @click="CliOrders"> Мои заказы</button>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="orders.length!==0">
          <thead>
            <tr>
              <th>Блюдо</th>
              <th>Количество</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="ord in orders">
              <td>{{ ord.product_name }}</td>
              <td>{{ ord.quantity }}  </td>
              <td><button class="delete" @click="DeleteOrder(ord.id)"></button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {toast} from "bulma-toast";
export default {
  name: "Client",
  components: {Navbar},
  data(){
    return{
      orders: [],
      user: '',
    }
  },
  mounted() {
    this.GetUserIdCli()
  },
  methods:{
    GetUserIdCli(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
            .get('http://127.0.0.1:8000/auth/users/me')
            .then(response =>{
              this.user = response.data.id
            })
    },
    CliOrders(){
     axios
          .get('http://localhost:8000/api/v1/orderscli/'+ this.user)
          .then(response=>{
            this.orders = response.data
          })
   },
    DeleteOrder(id){
      axios
          .delete('http://localhost:8000/api/v1/orders-delete/' + id)
          .then(response => {
                  toast({
                      message: 'Заказ удален',
                      type: 'is-success',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
              })
    }
  }
}
</script>

<style scoped>

</style>