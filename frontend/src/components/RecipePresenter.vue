<template>
    <div class="container">
        <button class="nutrition-manager-button" @click="toggleSideElement">
            <img src="/chef.png" alt="Nutrition Manager Icon" class="button-icon">
            Nutrition Manager
        </button>
        <div class="row" :class="{ 'shifted-row': showSideElement }">
            <!-- Recipe Cards -->
            <recipe-card
                v-for="(recipe, index) in recipes.slice(0, 3)"
                :key="index"
                :recipe="recipe"
                @dismiss="dismissRecipe"
            ></recipe-card>
        </div>

        <!-- Side Element -->
        <div class="side-element" :class="{ 'show-side-element': showSideElement }" ref="sideElement">
            <!-- Close Button -->
            <button class="close-button" @click="closeSideElement">&times;</button>
            <div class="nutrient-sum" v-if="showSideElement">
                <p style="margin-top: 170px; margin-left: 10px;">
                    Vitamin A: {{ nutrientSums.vitaminA }} IU
                    <Doughnut :data="nutrientChartData('vitaminA')" :options="{responsive: true, maintainAspectRatio: false}"></Doughnut>
                </p>
                <p style="margin-left: 10px;">
                    Vitamin B: {{ nutrientSums.vitaminB }} mg
                    <Doughnut :data="nutrientChartData('vitaminB')" :options="{responsive: true, maintainAspectRatio: false}"></Doughnut>
                </p>
                <!-- Add other nutrients as needed -->
            </div>
        </div>

    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Doughnut } from "vue-chartjs";
import mockedRecipes from '../../../backend/mockedRecipes.json'

ChartJS.register(ArcElement, Tooltip, Legend);

export default {
    props: ['data', 'options'],
    components: {
        RecipeCard,
        Doughnut
    },
    data() {
        return {
            recipes: mockedRecipes,
            showSideElement: false,
            nutrientSums: {
                vitaminA: 300,
                vitaminB: 1000,
                // Add other nutrients as needed
            },
        };
    },


    methods: {

        dismissRecipe(dismissedRecipe) {
            this.recipes = this.recipes.filter((recipe) => recipe !== dismissedRecipe);
            this.calculateNutrientSums();
            this.showSideElement = false;
        },
        closeSideElement() {
            this.showSideElement = false;
        },
        toggleSideElement() {
            this.showSideElement = !this.showSideElement;
        },
        calculateNutrientSums() {
            // Reset nutrient sums
            this.nutrientSums = {
                vitaminA: 0,
                vitaminB: 0,
                // Add other nutrients as needed
            };

            // Calculate nutrient sums across all recipes
            this.recipes.forEach((recipe) => {
                this.nutrientSums.vitaminA += recipe.recipe.nutrition["vitaminA"] || 12; // todo change
                this.nutrientSums.vitaminB += recipe.recipe.nutrition["vitaminB"] || 18; // todo change
                // Add other nutrients as needed
            });
        },
        nutrientChartData(vitamin) {
            const percentage = this.calculateFulfillmentPercentage()[vitamin];
            const remainingPercentage = 100 - percentage;

            return {
                labels: ["Fulfilled", "Remaining"],
                datasets: [
                {
                    data: [percentage, remainingPercentage],
                    backgroundColor: [percentage >= 100 ? "white" : "red", "blue"],
                },
                ],
            };
        },
        calculateFulfillmentPercentage() {
            // Replace these values with your expected daily consumption
            const expectedVitaminA = 1000; // Example value in IU
            const expectedVitaminB = 1000; // Example value in mg

            const percentageVitaminA = (this.nutrientSums.vitaminA / expectedVitaminA) * 100;
            const percentageVitaminB = (this.nutrientSums.vitaminB / expectedVitaminB) * 100;

            // Return the overall percentage (you can customize this based on your needs)
            return {
                'vitaminA': percentageVitaminA,
                'vitaminB': percentageVitaminB,
                // Add other nutrients as needed
            };

        },
    },
    watch: {
        recipes: 'calculateNutrientSums', // Recalculate sums when recipes change
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
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  z-index: 3; /* Ensure the button is above other elements */
}
.button-icon {
  width: 20px; /* Adjust the width of the icon as needed */
  height: auto; /* Maintain the aspect ratio */
  margin-right: 5px; /* Add margin to separate the icon from text */
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
