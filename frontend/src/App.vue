<template>
  <div id="app">
    <nav-bar></nav-bar>

    <!-- Add space between navbar and recipe presenter -->
    <div style="margin-top: 20px;"></div>

    <recipe-presenter></recipe-presenter>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import RecipePresenter from "@/components/RecipePresenter.vue";

export default {
  name: 'App',
  components: {
    RecipePresenter,
    NavBar,
  },
};
</script>

<style>
/* Add any global styles if needed */
</style>
