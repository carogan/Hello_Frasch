<template>
    <div class="recipe-card card">
        <div class="emoji-container">
            <div class="seasonal-emoji">{{ recipe.seasonalEmoji }}</div>
        </div>

        <img :src="recipe.image" class="card-img-top" alt="Recipe Image">
        <div class="card-body">
            <h5 class="card-title">{{ recipe.name }}</h5>
            <div style="height: 50px; overflow: hidden; margin-bottom: 10px">
                <p class="card-text">{{ recipe.headline }}</p>
            </div>
            <div class="d-flex justify-content-between align-items-center" style="height: 50px">
                <div>
          <span class="badge bg-success" :key="tag.name" v-for="tag in recipe.tags"
                style="margin: 2px">
            {{ tag.name }}
          </span>
                </div>
                <button @click="dismissCard" class="btn btn-danger">Dismiss</button>
            </div>

            <hr>
            <p class="card-text" style="font-size: 10pt"><strong>Recommendation:</strong> based on your preferences.</p>
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
        dismissCard() {
            this.$emit('dismiss', this.recipe)
        }
    }
};
</script>

<style scoped>
.recipe-card {
    position: relative;
    max-width: calc(33.33% - 20px); /* 33.33% for three cards in a row, minus margin */
    margin: 0 10px 20px 10px; /* Adjust margin as needed */
}

.card-img-top {
    position: relative;
}

.emoji-container {
    position: absolute;
    top: 0px;
    right: 0px;
    background-color: white; /* Set the background color for the frame */
    padding: 5px; /* Adjust padding as needed */
    border-radius: 10%; /* Make it circular */
    z-index: 2; /* Set a z-index value higher than the image */
}

@media (max-width: 768px) {
    .recipe-card {
        max-width: 100%; /* Full width on smaller screens */
    }
}
</style>
