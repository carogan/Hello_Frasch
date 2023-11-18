<template>
    <div class="recipe-card card">
        <img :src="recipe.image" class="card-img-top" alt="Recipe Image">
        <div class="card-body">
            <h5 class="card-title">{{ recipe.name }}</h5>
            <p class="card-text">{{ recipe.headline }}</p>
            <div class="d-flex justify-content-between">
                <div>
                    <span class="badge bg-primary" :key="tag.name" v-for="tag in recipe.tags">
                        {{ tag.name }}
                    </span>
                </div>
                <button @click="dismissCard" class="btn btn-danger">Dismiss</button>
            </div>

            <hr>
            <p class="card-text"><strong>Recommendation:</strong> Based on your preferences.</p>
        </div>
    </div>
</template>
<!-- Kochzeit, Tags, Text: Based on which? -->

<script>
export default {
    props: {
        recipe: {
            type: Object,
            required: true
        }
    },
    methods: {
        dismissRecipe() {
            this.$emit('dismiss', this.recipe)
        }
    }
};
</script>

<style scoped>
.recipe-card {
    max-width: 18rem;
    margin-bottom: 20px;
}
</style>
