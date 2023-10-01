<template>
    <div class="bg-gray-100 min-h-screen py-8">
      <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg p-6">
        <h2 class="text-2xl font-medium mb-4">Inventario</h2>
        <table class="w-full table-auto">
          <thead>
            <tr>
              <th class="px-4 py-2">Nombre</th>
              <th class="px-4 py-2">Descripción</th>
              <th class="px-4 py-2">Cantidad</th>
              <th class="px-4 py-2">Precio</th>
              <th class="px-4 py-2">Imagen</th>
              <th class="px-4 py-2">Marca</th>
              <th class="px-4 py-2">Vendedor</th>
              <th class="px-4 py-2">Rating</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(producto, index) in productos" :key="index">
              <td class="border px-4 py-2">{{ producto.nombre }}</td>
              <td class="border px-4 py-2">{{ producto.descripcion }}</td>
              <td class="border px-4 py-2">{{ producto.cantidad }}</td>
              <td class="border px-4 py-2">{{ producto.precio }}</td>
              <td class="border px-4 py-2">
                <img :src="producto.imagenes[0]" class="h-16 w-16 object-cover" alt="">
              </td>
              <td class="border px-4 py-2">{{ producto.marca }}</td>
              <td class="border px-4 py-2">{{ producto.vendedor }}</td>
              <td class="border px-4 py-2">{{ producto.rating }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        productos: []
      };
    }
  };
  </script>
  