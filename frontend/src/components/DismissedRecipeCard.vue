<template>
    <div class="recipe-card card">
        <div class="card-frame">
            <div class="row g-0">
                <div class="col-md-4">
                    <div class="image-container">
                        <img :src="recipe.recipe.image" class="img-fluid rounded-start img-fill" alt="Image">
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h6 class="card-title text-muted">{{ recipe.recipe.name }}</h6>
                        <p class="card-text text-muted">{{ recipe.recipe.headline }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        recipe: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.img-fill {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.5;
}

.image-container {
    height: 165px;
    overflow: hidden;
}

.recipe-card {
    position: relative;
    margin: 0 10px 20px 10px; /* Adjust margin as needed */
    height: 165px;
}


.card-img-top {
    position: relative;
}


@media (max-width: 768px) {
    .recipe-card {
        max-width: 100%; /* Full width on smaller screens */
    }
}
</style>
