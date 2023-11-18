<template>
    <div class="recipe-card card">
        <img :src="recipe.image" class="card-img-top" alt="Recipe Image">
        <div class="card-body">
            <h5 class="card-title">{{ recipe.title }}</h5>
            <p class="card-text">{{ recipe.description }}</p>
            <button @click="dismissRecipe" class="btn btn-danger">Dismiss</button>
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
