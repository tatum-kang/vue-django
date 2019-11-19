<template>
  <div class="home">
    <h2>여기 홈임</h2>

  </div>
</template>

<script>
import router from '@/router'
export default {
  name:'Home',
  methods:{
    // 로그인 체크 로그인 유무 확인 없을시 로그인 페이지로 보낸다.
    checkLoggedIn() {
      // 1. 세션을 시작해서 
      this.$session.start()
      if (!this.$session.has('jwt')) {
        // jwt가 없다면 로그인페이지로 보내겠다. 
        router.push('/login')
      }
    }
  },
  // vue가 화면에 그려지면 실행하는 함수
  mounted(){
    this.checkLoggedIn()
  }

}
</script>

<style>

</style>