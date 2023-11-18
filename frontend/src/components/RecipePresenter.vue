<template>
    <div class="container">
        <div class="row">
            <recipe-card
                v-for="(recipe, index) in recipes.slice(0, 3)"
                :key="index"
                :recipe="recipe"
                @dismiss="dismissRecipe">
            </recipe-card>
        </div>
    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";
import mockedRecipes from '../../../backend/mockedRecipes.json'


export default {
    components: {
        RecipeCard
    },
    data() {
        return {
            recipes: mockedRecipes
        };
    },
    methods: {
        dismissRecipe(dismissedRecipe) {
            this.recipes = this.recipes.filter(recipe => recipe !== dismissedRecipe);
        },
    },
}
</script>

<style scoped>

</style>
