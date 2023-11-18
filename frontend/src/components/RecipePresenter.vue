<template>
    <div class="container">
        <div class="row">
            <div class="col" v-for="(recipe, index) in recipes" :key="index">
                <dismissed-recipe-card v-if="recipe.dismissed" :recipe="recipe"></dismissed-recipe-card>
                <recipe-card :recipe="recipe" v-if="!recipe.dismissed" @replace="replaceRecipe">
                </recipe-card>
            </div>
        </div>

        <div class="row">
            <div class="collapse" id="newRecipeCollapse">
                <div class="card card-body">
                    <h2>Choose your new recipe</h2>

                    <div class="row">
                        <div class="col" v-for="(recipe, index) in replacementRecipeChoices" :key="index">
                            <recipe-card :recipe="recipe" @choose="chooseRecipe">
                            </recipe-card>
                        </div>
                    </div>

                    <button
                        class="btn btn-primary"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#newRecipeCollapse"
                        aria-expanded="false"
                        aria-controls="newRecipeCollapse"
                        @click="enlargeAndReplace"
                    >
                        Toggle Collapse
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import mockedRecipes from '../../../backend/mockedRecipes.json'
import DismissedRecipeCard from "@/components/DismissedRecipeCard.vue";

export default {
    components: {
        DismissedRecipeCard,
        RecipeCard
    },
    data() {
        return {
            recipes: mockedRecipes.map(recipe => ({...recipe, dismissed: false, replacementChoice: false})).slice(0, 3),
            previousRecipes: mockedRecipes.map(recipe => ({...recipe, dismissed: false, replacementChoice: false})).slice(0, 3),
            replacementRecipeChoices: mockedRecipes.map(recipe => ({...recipe, replacementChoice: true})).slice(3, 6),
            replacedRecipeIndex: null
        };
    },
    methods: {
        replaceRecipe(replacedRecipe) {
            // ugly way to deep copy an array
            this.previousRecipes = JSON.parse(JSON.stringify(this.recipes));

            // can use index here
            this.replacedRecipeIndex = replacedRecipe.index - 1;
            this.previousRecipes[this.replacedRecipeIndex].dismissed = true;

            // after we took note of which we minimized, make all of them smaller
            this.recipes.forEach(r => r.dismissed = true);
        },
        enlargeAndReplace() {
            this.recipes = this.previousRecipes;
        },
        chooseRecipe(chosenRecipe) {
            alert("You chose: " + chosenRecipe)
        }
    },
}
</script>

<style scoped>
/* Your styles go here */
</style>
