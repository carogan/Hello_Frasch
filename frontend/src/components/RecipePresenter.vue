<template>
    <div class="container">
        <button class="nutrition-manager-button" :class="{'button-hidden': showSideElement}" @click="toggleSideElement">
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
                <p style="margin-top: 100px; margin-left: 10px;">
                    Vitamin B9: {{ nutrientSums.vitaminB9 }} IU
                    <Doughnut :data="nutrientChartData('vitaminB9')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                </p>
                <p style="margin-left: 10px;">
                    Vitamin B12: {{ nutrientSums.vitaminB12 }} mg
                    <Doughnut :data="nutrientChartData('vitaminB12')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                </p>
                <!-- Add other nutrients as needed -->
                <!--b9,b12,k,iron, zink-->
            </div>
        </div>

    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import {Chart as ChartJS, ArcElement, Tooltip, Legend} from 'chart.js'
import {Doughnut} from "vue-chartjs";
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
                vitaminB9: 300,
                vitaminB12: 1000,
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
                vitaminB9: 0,
                vitaminB12: 0,
                // Add other nutrients as needed
            };

            // Calculate nutrient sums across all recipes
            this.recipes.forEach((recipe) => {
                this.nutrientSums.vitaminB9 += recipe.recipe.nutrition["vitaminB9"] || 12; // todo change
                this.nutrientSums.vitaminB12 += recipe.recipe.nutrition["vitaminB12"] || 18; // todo change
                // Add other nutrients as needed
            });
        },
        nutrientChartData(vitamin) {
            const percentage = this.calculateFulfillmentPercentage()[vitamin];
            const remainingPercentage = 100 - percentage;

            return {
                //labels: ["Fulfilled", "Remaining"],
                datasets: [
                {
                    data: [percentage, remainingPercentage],
                    backgroundColor: [percentage >= 100 ? "green" : "green", "red"],
                },
                ],
            };
        },
        calculateFulfillmentPercentage() {
            // Replace these values with your expected daily consumption
            const expectedVitaminB9 = 1000; // Example value in IU
            const expectedVitaminB12 = 1000; // Example value in mg

            const percentageVitaminB9 = (this.nutrientSums.vitaminB9 / expectedVitaminB9) * 100;
            const percentageVitaminB12 = (this.nutrientSums.vitaminB12 / expectedVitaminB12) * 100;

            // Return the overall percentage (you can customize this based on your needs)
            return {
                'vitaminB9': percentageVitaminB9,
                'vitaminB12': percentageVitaminB12,
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
    top: 25px;
    right: 10px;
    padding: 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    z-index: 3; /* Ensure the button is above other elements */

}

.button-icon {
    width: 20px; /* Adjust the width of the icon as needed */
    height: auto; /* Maintain the aspect ratio */
    margin-right: 5px; /* Add margin to separate the icon from text */
    filter: invert(100%);
}

.button-hidden {
    visibility: hidden;
}

.side-element {
    width: 200px; /* Adjust width as needed */
    height: 100%;
    background-color: #f0f0f0; /* Adjust background color as needed */
    position: fixed;
    top: 0;
    right: -500px; /* Initially hide the side element off-screen */
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
