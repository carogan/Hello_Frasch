<template>
    <div class="container">
        <button class="nutrition-manager-button" @click="toggleSideElement">
            Nutrition Manager
        </button>
        <div class="row" :class="{ 'shifted-row': showSideElement }">
            <!-- Recipe Cards -->
            <recipe-card
                v-for="recipe in recipes"
                :key="recipe.index"
                :recipe="recipe"
                @dismiss="dismissRecipe"
            ></recipe-card>
        </div>

        <!-- Side Element -->
        <div class="side-element" :class="{ 'show-side-element': showSideElement }" ref="sideElement">
            <!-- Close Button -->
            <button class="close-button" @click="closeSideElement">&times;</button>
            <!-- Add your content here -->
        </div>
        <div class="arrow-button" v-if="showSideElement" @click="closeSideElement">
            &larr;
        </div>
    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import mockedRecipes from "../assets/mockedRecipes.json";

export default {
    components: {
        RecipeCard,
    },
    data() {
        return {
            recipes: mockedRecipes,
            showSideElement: false,
        };
    },
    methods: {
        dismissRecipe(dismissedRecipe) {
            this.recipes = this.recipes.filter((recipe) => recipe !== dismissedRecipe);
            this.showSideElement = false;
        },
        closeSideElement() {
            this.showSideElement = false;
        },
        toggleSideElement() {
            this.showSideElement = !this.showSideElement;
        },
    },
};
</script>

<style scoped>
.nutrition-manager-button {
  position: fixed;
  top: 100px;
  right: 10px;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  z-index: 3; /* Ensure the button is above other elements */
}
.side-element {
    width: 200px; /* Adjust width as needed */
    height: 100%;
    background-color: #f0f0f0; /* Adjust background color as needed */
    position: fixed;
    top: 0;
    right: -200px; /* Initially hide the side element off-screen */
    transition: right 0.3s ease;
}

.show-side-element {
    right: 0; /* Move the side element into view */
}

.arrow-button {
  position: fixed;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  font-size: 24px;
  cursor: pointer;
  background-color: #4caf50;
  color: white;
  padding: 10px;
  border-radius: 5px;
  z-index: 3; /* Ensure the button is above other elements */
}

.close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    cursor: pointer;
    background: none;
    border: none;
    outline: none;
    padding: 0;
}

.container {
    position: relative;
}

.row {
    transition: margin-right 0.3s ease; /* Add a transition effect for moving cards */
}

.shifted-row {
    margin-right: 200px; /* Adjust margin to make space for the side element */
}
</style>
