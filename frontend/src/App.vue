<template>
    <nav-bar></nav-bar>
    <recipe-presenter></recipe-presenter>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import RecipePresenter from "@/components/RecipePresenter.vue";

export default {
  name: 'App',
  components: {
      RecipePresenter,
      NavBar,
  }
}
</script>

<style>
</style>
