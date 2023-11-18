<template>
    <div class="container">
        <div class="row">
            <recipe-card v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" @dismiss="dismissRecipe">
            </recipe-card>
        </div>
    </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard.vue";

export default {
    components: {
        RecipeCard
    },
    data() {
        return {
            recipes: [
                {
                    "id": 1,
                    "title": "Spaghetti Bolognese",
                    "description": "Classic Italian pasta dish with meat sauce.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 2,
                    "title": "Chicken Alfredo",
                    "description": "Creamy pasta with grilled chicken and Alfredo sauce.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 3,
                    "title": "Margherita Pizza",
                    "description": "Traditional pizza with tomato, mozzarella, and basil.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 4,
                    "title": "Caesar Salad",
                    "description": "Fresh salad with romaine lettuce, croutons, and Caesar dressing.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 5,
                    "title": "Chocolate Cake",
                    "description": "Decadent chocolate cake with rich chocolate frosting.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 6,
                    "title": "Grilled Salmon",
                    "description": "Healthy grilled salmon fillets with lemon and herbs.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 7,
                    "title": "Vegetable Stir-Fry",
                    "description": "Colorful stir-fried vegetables with tofu or chicken.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 8,
                    "title": "Mango Salsa Chicken",
                    "description": "Grilled chicken topped with refreshing mango salsa.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 9,
                    "title": "Caprese Sandwich",
                    "description": "Delicious sandwich with fresh tomatoes, mozzarella, and basil.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                },
                {
                    "id": 10,
                    "title": "Berry Smoothie Bowl",
                    "description": "Healthy and colorful smoothie bowl with mixed berries.",
                    "image": "https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png"
                }
            ],
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
