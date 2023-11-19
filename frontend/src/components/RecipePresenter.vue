<template>
    <div class="container">
        <button class="nutrition-manager-button" :class="{'button-hidden': showSideElement}" @click="toggleSideElement">
            <img src="/chef.png" alt="Nutrition Manager Icon" class="button-icon">
            Nutrition Manager
        </button>

        <div class="row" :class="{ 'shifted-row': showSideElement }">
            <div class="col-4" v-for="(recipe, index) in recipes" :key="index">
                <dismissed-recipe-card v-if="recipe.dismissed" :recipe="recipe"></dismissed-recipe-card>
                <recipe-card :recipe="recipe" v-if="!recipe.dismissed" @replace="replaceRecipe"></recipe-card>

                <recipe-card v-if="getNewRecipes()[index] && !getNewRecipes()[index].minimized"
                             :recipe="getNewRecipes()[index]"></recipe-card>
                <minimized-recipe-card v-if="getNewRecipes()[index] && getNewRecipes()[index].minimized"
                                       :recipe="getNewRecipes()[index]"></minimized-recipe-card>
            </div>
        </div>

        <div class="row" :class="{ 'shifted-row': showSideElement }">
            <div class="collapse" id="newRecipeCollapse">
                <div class="card card-body">
                    <h2>Choose your new meal...</h2>
                    <div style="margin-top: 20px;"></div>

                    <div class="row">
                        <div class="col-3" v-for="(recipe, index) in replacementRecipeChoices.slice(0, 3)" :key="index">
                            <recipe-card :recipe="recipe" @choose="chooseRecipe">
                            </recipe-card>
                        </div>
                    </div>

                    <div style="display: flex; align-items: center" v-if="replacementRecipeChoices.length === 0">
                        <div>We have nothing more to recommend to you. :(</div>
                        <button
                            class="btn btn-primary m-lg-2"
                            type="button"
                            data-bs-toggle="collapse"
                            data-bs-target="#newRecipeCollapse"
                            aria-expanded="false"
                            aria-controls="newRecipeCollapse"
                        >
                            Close
                        </button>
                    </div>


                    <!-- <button
                        class="btn btn-primary"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#newRecipeCollapse"
                        aria-expanded="false"
                        aria-controls="newRecipeCollapse"
                        @click="enlargeAndReplace"
                    >
                        Toggle Collapse
                    </button> -->
                </div>
            </div>

            <!-- Side Element -->
            <div class="side-element" :class="{ 'show-side-element': showSideElement }" ref="sideElement">
                <!-- Close Button -->
                <button class="close-button btn btn-outline-danger mt-4" @click="closeSideElement">&times;</button>
                <h3 class="mt-4">Nutrition Manager</h3>
                <h5>Percentage of RDA</h5>
                <div style="margin-top: -10px">(Recommended Dietary Allowance)</div>
                <div class="nutrient-sum" v-if="showSideElement">
                    <div style="margin-top: 30px; margin-left: 10px;">
                        <strong class="vitamin-listing">
                            Vitamin C: {{ this.calculateFulfillmentPercentage()['vitaminC'].toFixed(2) }}%
                            <Doughnut :data="nutrientChartData('vitaminC')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                        </strong>
                    </div>

                    <div style="margin-left: 10px; margin-top: 25px">
                        <strong class="vitamin-listing">
                            Vitamin A: {{ this.calculateFulfillmentPercentage()['vitaminA'].toFixed(2) }}%
                            <Doughnut :data="nutrientChartData('vitaminA')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                        </strong>
                    </div>

                    <div style="margin-left: 10px; margin-top: 25px">
                        <strong class="vitamin-listing">
                            Vitamin K: {{ this.calculateFulfillmentPercentage()['vitaminK'].toFixed(2) }}%
                            <Doughnut :data="nutrientChartData('vitaminK')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                        </strong>
                    </div>

                    <div style="margin-left: 10px; margin-top: 25px">
                        <strong class="vitamin-listing">
                            Iron: {{ this.calculateFulfillmentPercentage()['iron'].toFixed(2) }}%
                            <Doughnut :data="nutrientChartData('iron')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                        </strong>
                    </div>

                    <div style="margin-left: 10px; margin-top: 25px">
                        <strong class="vitamin-listing">
                            Calcium: {{ this.calculateFulfillmentPercentage()['calcium'].toFixed(2) }}%
                            <Doughnut :data="nutrientChartData('calcium')" :options="{responsive: false, maintainAspectRatio: false}" style="width: 100px; height: 100px;"></Doughnut>
                        </strong>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import {ArcElement, Chart as ChartJS, Legend, Tooltip} from 'chart.js'
import {Doughnut} from "vue-chartjs";
import mockedRecipes from '../../../backend/mockedRecipes_with_Nutrition.json'
import DismissedRecipeCard from "@/components/DismissedRecipeCard.vue";
import {RECIPE_HAS_BEEN_REPLACED, RECIPE_IN_REPLACEMENT, RECIPE_NOT_YET_REPLACED} from "@/const";
import MinimizedRecipeCard from "@/components/MinimizedRecipeCard.vue";

ChartJS.register(ArcElement, Tooltip, Legend);


export default {
    props: ['data', 'options'],
    components: {
        MinimizedRecipeCard,
        DismissedRecipeCard,
        RecipeCard,
        Doughnut
    },
    data() {
        return {
            recipes: mockedRecipes.map(recipe => ({...recipe, dismissed: false, replacementChoice: RECIPE_NOT_YET_REPLACED})).slice(0, 3),
            previousRecipes: mockedRecipes.map(recipe => ({...recipe, dismissed: false, replacementChoice: RECIPE_NOT_YET_REPLACED})).slice(0, 3),
            replacementRecipeChoices: mockedRecipes.map(recipe => ({...recipe, replacementChoice: RECIPE_IN_REPLACEMENT})).slice(3, 7),
            replacedRecipeIndex: null,
            newRecipes: [null, null, null],
            showSideElement: false,
            nutrientSums: {
                vitaminC: 0,
                vitaminA: 0,
                vitaminK: 0,
                iron: 0,
                calcium: 0,
                // Add other nutrients as needed
            },
        };
    },

    mounted() {
        this.calculateNutrientSums();
    },


    methods: {
        getRecipesForComputation() {
            return this.recipes.filter(r => !r.dismissed).concat(this.newRecipes.filter(r => !!r));
        },
        getNewRecipes() {
            return this.newRecipes;
        },
        replaceRecipe(replacedRecipe) {
            // ugly way to deep copy an array
            this.previousRecipes = JSON.parse(JSON.stringify(this.recipes));

            // can use index here
            this.replacedRecipeIndex = replacedRecipe.index - 1;
            this.previousRecipes[this.replacedRecipeIndex].dismissed = true;

            // after we took note of which we minimized, make all of them smaller
            this.recipes.forEach(r => r.dismissed = true);
            this.newRecipes.filter(r => !!r).forEach(r => r.minimized = true);
        },
        enlargeOthers() {
            this.recipes = this.previousRecipes;
            this.newRecipes.filter(r => !!r).forEach(r => r.minimized = false);
        },
        chooseRecipe(chosenRecipe) {
            this.enlargeOthers();
            this.newRecipes[this.replacedRecipeIndex] = chosenRecipe;
            this.newRecipes[this.replacedRecipeIndex].replacementChoice = RECIPE_HAS_BEEN_REPLACED;
            this.newRecipes[this.replacedRecipeIndex].minimized = false;
            this.calculateNutrientSums();//update nutrient sums

            // remove from other choices
            this.replacementRecipeChoices = this.replacementRecipeChoices.filter(i => i !== chosenRecipe);
        },
        closeSideElement() {
            this.showSideElement = false;
        },
        toggleSideElement() {
            this.showSideElement = !this.showSideElement;
            this.calculateNutrientSums();//update nutrient sums
        },
        calculateNutrientSums() {
            // Reset nutrient sums
            this.nutrientSums = {
                vitaminC: 0,
                vitaminA: 0,
                vitaminK: 0,
                iron: 0,
                calcium: 0,
                // Add other nutrients as needed
            };
            // Calculate nutrient sums across all recipes
            this.getRecipesForComputation().forEach((recipe) => {
                this.nutrientSums.vitaminC += recipe.recipe.nutrition["Vitamin C"].value || 1; // todo change
                this.nutrientSums.vitaminA += recipe.recipe.nutrition["Vitamin A"].value || 1; // todo change
                this.nutrientSums.vitaminK += recipe.recipe.nutrition["Vitamin K"].value || 1; // todo change
                this.nutrientSums.iron += recipe.recipe.nutrition["Iron"].value || 1; // todo change
                this.nutrientSums.calcium += recipe.recipe.nutrition["Calcium"].value || 1; // todo change
                // Add other nutrients as needed
            });
        },
        nutrientChartData(vitamin) {
            const percentage = this.calculateFulfillmentPercentage()[vitamin];
            let remainingPercentage = 100 - percentage;
            if (remainingPercentage < 0){
                remainingPercentage = 0;
            }

            return {
                //labels: ["Fulfilled", "Remaining"],
                datasets: [
                    {
                        data: [percentage, remainingPercentage],
                        backgroundColor: [percentage >= 100 ? "#4caf50" : "#4caf50", "#dc3545"],
                    },
                ],
            };
        },
        calculateFulfillmentPercentage() {
            // Replace these values with your expected daily consumption
            const expectedVitaminC = 90*3; // Example value in mg daily
            const expectedVitaminA = 900*3; // Example value in mcg
            const expectedVitaminK = 120*3; // Example value in mcg
            const expectedIron = 8*3; // Example value in mg
            const expectedCalcium = 1000*3; // Example value in mg

            const percentageVitaminC = ((this.nutrientSums.vitaminC*0.5) / expectedVitaminC) * 100;//0.5 because 2 servings
            const precentageVitaminA = ((this.nutrientSums.vitaminA*0.5) / expectedVitaminA) * 100;
            const percentageVitaminK = ((this.nutrientSums.vitaminK*0.5) / expectedVitaminK) * 100;
            const percentageIron = ((this.nutrientSums.iron*0.5) / expectedIron) * 100;
            const percentageCalcium = ((this.nutrientSums.calcium*0.5) / expectedCalcium) * 100;

            // Return the overall percentage (you can customize this based on your needs)
            return {
                'vitaminC': percentageVitaminC,
                'vitaminA': precentageVitaminA,
                'vitaminK': percentageVitaminK,
                'iron': percentageIron,
                'calcium': percentageCalcium,
                // Add other nutrients as needed
            };

        },
    },

};
</script>

<style scoped>
.vitamin-listing {
    font-size: 15pt;
}

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
    width: 350px; /* Adjust width as needed */
    height: 100%;
    background-color: #f0f0f0; /* Adjust background color as needed */
    position: fixed;
    top: 0;
    right: -350px; /* Initially hide the side element off-screen */
    transition: right 0.3s ease;
}

.show-side-element {
    right: 0; /* Move the side element into view */
}

.close-button {
    position: absolute;
    right: 10px;
    font-size: 20px;
    cursor: pointer;
    background: none;
    width: 30px;
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
