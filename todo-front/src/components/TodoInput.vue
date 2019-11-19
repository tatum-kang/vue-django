<template>
  <div class="todo-input">
    <form action="" class="input-group mb-3" @submit.prevent="onSubmit">
      <input type="text" class="form-control" v-model="input_data">
      <button type="submit" class="btn btn-success">add</button>
    </form>

  </div>
</template>

<script>

export default {
  name:"TodoInput",
  data(){
    return {
      input_data : ''
    }
  },
  methods:{
    onSubmit(){
      this.$emit('createTodo', this.input_data)
      this.input_data=''
    }
  }
}
</script>

<style>

</style>