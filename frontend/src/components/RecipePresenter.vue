<template>
    <div class="container">
        <div class="row">
            <div class="col" v-for="(recipe, index) in recipes.slice(0, 3)" :key="index">
                <dismissed-recipe-card v-if="recipe.dismissed" :recipe="recipe"></dismissed-recipe-card>
                <recipe-card :recipe="recipe" v-if="!recipe.dismissed" @replace="replaceRecipe">
                </recipe-card>
            </div>
        </div>

        <!--
        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#newRecipeCollapse" aria-expanded="false" aria-controls="newRecipeCollapse">
            Toggle Collapse
        </button>
         -->

        <div class="row">
            <div class="collapse" id="newRecipeCollapse">
                <div class="card card-body">
                    Collapsible content goes here.
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
            recipes: mockedRecipes.map(recipe => ({...recipe, dismissed: false}))
        };
    },
    methods: {
        replaceRecipe(replacedRecipce) {
            replacedRecipce.dismissed = true;
        },
    },
}
</script>

<style scoped>
/* Your styles go here */
</style>
