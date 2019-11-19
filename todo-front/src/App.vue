<template>
  <div id="app">
    <div id="nav">
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <!-- prevent로 사용하는 이유는 리다이렉트를 방지하기 위해 -->
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login" >Login</router-link>
      </div>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>


<script>
import router from '@/router'

export default {
  name:'App',
  data(){
    return {
      isLoggedIn: this.$session.has('jwt')
    }
  },
  methods:{
    logout(){
      this.$session.destroy()
      router.push('/login')
    },
  },

  // data에 변화가 일어나느 시점에 실행하는 함수 
  updated(){
    this.isLoggedIn = this.$session.has('jwt')
  }
}
</script>


<style>boot
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active{
  color: #42b983;
}
</style>
