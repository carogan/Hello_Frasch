<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img src="/Hello_Fresh_Lockup.png" alt="Hello Fresh Branding Image">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="#">
                <strong style="color: darkgreen;">📦 Select Box</strong>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <strong style="color: darkgreen;">📝 Register</strong>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <strong style="color: darkgreen;">🚚 Delivery</strong>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" tabindex="-1">
                <strong style="color: darkgreen;">💰 Payment Plan</strong>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" tabindex="-1">
                <strong style="color: darkgreen">🍲 Select Recipe</strong>
              </a>
            </li>
          </ul>
          <div class="d-flex align-items-center" style="visibility: hidden">
            <div class="mr-6">
              <i class="bi bi-cart3" style="font-size: 24px;"></i>
            </div>
            <div class="ml-6" style="margin-left: 20px !important;">
              <p class="mb-0">Pause or cancel</p>
              <p class="mb-0">subscription</p>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template>

  <script>
  export default {
    name: 'NavBar',
  };
  </script>

  <style scoped>
  /* Add any custom styles if needed */

  /* Additional styling for increased space between links */
  .navbar-nav {
    margin: 0 auto; /* Center the navbar links */
  }

  .nav-link {
    margin-right: 20px; /* Adjust the space between links */
  }

  /* Style for the shopping cart icon */
  .fas {
    font-size: 24px; /* Adjust the size of the icon */
  }
  </style>
