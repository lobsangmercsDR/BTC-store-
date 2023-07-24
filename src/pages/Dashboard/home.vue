<template>
  <div class="bg-gray-100">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-4 px-6">
        <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>
      </div>
    </header>
    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="infoContainer">
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Ventas totales</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">$3,275.89 BTC</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Clientes nuevos</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">12</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md box">
          <h2 class="text-lg font-medium text-gray-900">Productos vendidos</h2>
          <p class="mt-1 text-3xl font-semibold text-gray-700">89</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.infoContainer {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(285px, 1fr));
  grid-gap: 20px;
}

.box {
  min-width: 250px;
}

</style>