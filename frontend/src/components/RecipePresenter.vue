<template>
    <div class="container">
        <div class="row">
            <div
                class="col"
                v-for="(recipe, index) in recipes.slice(0, 3)"
                :key="index">
                <dismissed-recipe-card v-if="recipe.dismissed" :recipe="recipe"></dismissed-recipe-card>
                <recipe-card
                    :recipe="recipe"
                    v-if="!recipe.dismissed"
                    @dismiss="dismissRecipe">
                </recipe-card>
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
            recipes: mockedRecipes.map(recipe => ( {...recipe, dismissed: false}))
        };
    },
    methods: {
        dismissRecipe(dismissedRecipe) {
            dismissedRecipe.dismissed = true
            //this.recipes = this.recipes.filter(recipe => recipe !== dismissedRecipe);
        },
    },
}
</script>

<style scoped>

</style>
