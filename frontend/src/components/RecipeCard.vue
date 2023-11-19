<template>
    <div class="recipe-card card">
        <div class="card-frame">
            <div class="emoji-container">
                <img :src="recipe.recipe.seasonalEmoji" alt="Seasonal Emoji">
            </div>

            <img :src="recipe.recipe.image" class="card-img-top" alt="Recipe Image">
            <div class="card-body">
                <h5 class="card-title" style="height: 73px; overflow: hidden">{{ recipe.recipe.name }}</h5>
                <div style="height: 45px; overflow: hidden; margin-bottom: 10px">
                    <p class="card-text">{{ recipe.recipe.headline }}</p>
                </div>
                <div class="d-flex justify-content-between align-items-center" style="height: 50px">
                    <div>
            <span class="badge bg-success" :key="tag.name" v-for="tag in recipe.recipe.tags"
                    style="margin: 2px">
                {{ tag.name }}
            </span>
                    </div>
                    <button
                        v-if="recipe.replacementChoice === RECIPE_NOT_YET_REPLACED()"
                        @click="replaceCard"
                        class="btn btn-danger"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#newRecipeCollapse"
                        aria-expanded="false"
                        aria-controls="newRecipeCollapse">
                        Replace
                    </button>
                    <button
                        v-else-if="recipe.replacementChoice === RECIPE_IN_REPLACEMENT()"
                        @click="chooseCard"
                        class="btn btn-success"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#newRecipeCollapse"
                        aria-expanded="false"
                        aria-controls="newRecipeCollapse">
                        Replace
                    </button>
                </div>
                <hr>
                <p class="card-text" v-if="recipe.recipe.seasonalEmoji === '/user.png'" style="font-size: 10pt">
                    <strong>Recommendation:</strong> based on your preferences.
                </p>
                <p class="card-text" v-else-if="recipe.recipe.seasonalEmoji === '/christmas.png'" style="font-size: 10pt">
                    <strong>Recommendation:</strong> contains seasonal ingredients.
                </p>
                <p class="card-text" v-else-if="recipe.recipe.seasonalEmoji === '/healthy.png'" style="font-size: 10pt">
                    <strong>Recommendation:</strong> based on your micronutrient levels.
                </p>
                <p class="card-text" v-else style="font-size: 10pt">
                    <strong>Recommendation:</strong> just because we felt like it.
                </p>
            </div>
        </div>
    </div>
</template>
<!-- Kochzeit, Tags, Text: Based on which? -->
<!-- Seasonal Recommendations / e.g. Apfel/Schneeflocke -->

<script>
import {RECIPE_IN_REPLACEMENT, RECIPE_NOT_YET_REPLACED} from "@/const";

export default {
    props: {
        recipe: {
            type: Object,
            required: true
        }
    },
    methods: {
        RECIPE_IN_REPLACEMENT() {
            return RECIPE_IN_REPLACEMENT
        },
        RECIPE_NOT_YET_REPLACED() {
            return RECIPE_NOT_YET_REPLACED
        },
        replaceCard() {
            this.$emit('replace', this.recipe)
        },
        chooseCard() {
            this.$emit('choose', this.recipe)
        }
    }
};
</script>

<style scoped>
.recipe-card {
    position: relative;
    margin: 0 10px 20px 10px; /* Adjust margin as needed */
}



.card-img-top {
    position: relative;
}

.emoji-container {
    position: absolute;
    top: 5px; /* Adjust the top position as needed */
    right: 5px; /* Adjust the right position as needed */
    padding: 5px; /* Adjust padding as needed */
    z-index: 2; /* Set a z-index value higher than the image */
    width: 50px; /* Set a fixed width for the emoji container */
    height: 50px; /* Set a fixed height for the emoji container */
    border-radius: 10%;
    /*background-color: #85e459;*/
    background-color: #4caf50;
    object-fit: contain;
}

.emoji-container img {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 80%; /* Set a maximum width for the image */
    max-height: 80%; /* Set a maximum height for the image */
    filter: invert(100%);

}

@media (max-width: 768px) {
    .recipe-card {
        max-width: 100%; /* Full width on smaller screens */
    }
}
</style>
