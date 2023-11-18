<template>
    <nav-bar></nav-bar>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from "@/components/NavBar.vue";

export default {
  name: 'App',
  components: {
      NavBar,
    HelloWorld
  }
}
</script>

<style>
</style>
