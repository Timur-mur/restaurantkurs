<template>
<navbar></navbar>
  <div class="page-orders">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Заказы</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="orders.length!==0">
          <thead>
            <tr>
              <th>Клиент</th>
              <th>Номер столика</th>
              <th>Блюдо</th>
              <th>Количество</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="ord in orders">
              <td> <h1> {{ ord.username_id.username }} </h1> </td>
              <td>{{ ord.table }} </td>
              <td>{{ ord.product_name }}</td>
              <td>{{ ord.quantity }}  </td>
              <td><button class="delete" @click="DeleteOrder(ord.id)"></button></td>
            </tr>
          </tbody>
        </table>
        <p v-else> Пока заказов нет </p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {toast} from "bulma-toast";
export default {
  name: "AdminOrders",
  components: {Navbar},
  data(){
    return {
      orders: [],
    }
  },
  mounted() {
    this.GetOrders()
  },
  methods:{
    GetOrders(){
      axios
          .get('http://localhost:8000/api/v1/orders')
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
  },
}
</script>

<style scoped>

</style>