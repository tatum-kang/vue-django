<template>
  <div class="home">
    <h1>Todo</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
// import jwtDecode from 'jwt-decode'  // jwt를 해석해서 보여주는 라이브러리 
import { mapGetters } from 'vuex'  // import vuex from 'vuex', vuex.mapGetters와 같은 문법 


export default {
  name:'Home',
  components:{
    TodoList,
    TodoInput
  },
  data(){
    return {
      todos: []
    }
  },
  computed:{
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  methods:{
    // 로그인 체크 로그인 유무 확인 없을시 로그인 페이지로 보낸다.
    checkLoggedIn() {
      // 1. 세션을 시작해서 
      // this.$session.start()
      if (!this.isLoggedIn) {
        // jwt가 없다면 로그인페이지로 보내겠다. 
        router.push('/login')
      }
    },
    // 우리가 만든 django API 서버로 TODOS를 달라는 요청을 보낸뒤 TODOS DATA에 할당하는 함수 
    getTodo(){
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const user_id = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // const options = {
      //   headers : {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      axios.get(`${SERVER_IP}/api/v1/users/${this.userId}/`, this.options)
        .then(response => {
          this.todos = response.data.todo_set
        })
        .catch(error => {
          console.log(error)
        })
    },
    createTodo(title){
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const user_id = jwtDecode(token).user_id
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      // const options = {
      //   headers:{
      //     Authorization: 'JWT ' + token
      //   }
      // }
      const data = {
          title,
          user: this.userId
        }
      
      axios.post(`${SERVER_IP}/api/v1/todos/`, data, this.options)
        .then(response => {
          this.todos.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
      
    }
  },
  // vue가 화면에 그려지면 실행하는 함수
  mounted(){
    if(this.isLoggedIn){
      this.checkLoggedIn()
      this.getTodo()
    }
  },
  watch:{
    isLoggedIn(){
      this.checkLoggedIn()
      this.getTodo()
    }
  }
}
</script>

<style>

</style>