<template>
    <div class="recipe-card card">
        <div class="card-frame">
            <div class="emoji-container">
                <img :src="recipe.recipe.seasonalEmoji" alt="Seasonal Emoji">
            </div>

            <img :src="recipe.recipe.image" class="card-img-top" alt="Recipe Image">
            <div class="card-body">
                <h5 class="card-title" style="height: 70px; overflow: hidden">{{ recipe.recipe.name }}</h5>
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
                        v-if="!recipe.replacementChoice"
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
                        v-if="recipe.replacementChoice"
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
                <p class="card-text" v-if="recipe.recipe.seasonalEmoji === '/christmas.png'" style="font-size: 10pt">
                    <strong>Recommendation:</strong> seasonal ingredients.
                </p>
                <p class="card-text" v-if="recipe.recipe.seasonalEmoji === '/healthy.png'" style="font-size: 10pt">
                    <strong>Recommendation:</strong> based on your micronutrient levels.
                </p>
            </div>
        </div>
    </div>
</template>
<!-- Kochzeit, Tags, Text: Based on which? -->
<!-- Seasonal Recommendations / e.g. Apfel/Schneeflocke -->

<script>
export default {
    props: {
        recipe: {
            type: Object,
            required: true
        }
    },
    methods: {
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
}
.emoji-container img {
    position: absolute;
    top: -6px; /* dont change */
    right: 7px; /* dont change */
    max-width: 500%; /* Ensure the animated emoji fits within the container */
    max-height: 500%; /* Ensure the animated emoji fits within the container */
    border-radius: 10%;
    background-color: #85e459;
    object-fit: contain;
}

@media (max-width: 768px) {
    .recipe-card {
        max-width: 100%; /* Full width on smaller screens */
    }
}
</style>
