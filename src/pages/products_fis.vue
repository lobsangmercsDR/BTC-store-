<template>
  <div class="bg-gray-100 min-h-screen py-8">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-medium mb-4">Agregar Producto</h2>
      <form class="grid grid-cols-2 gap-6">
        <div>
          <label class="block mb-2 font-medium">Nombre:</label>
          <input type="text" v-model="nombre" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Descripción:</label>
          <textarea v-model="descripcion" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500"></textarea>
        </div>
        <div>
          <label class="block mb-2 font-medium">Cantidad:</label>
          <input type="number" v-model.number="cantidad" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Precio:</label>
          <input type="number" v-model.number="precio" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Imágenes:</label>
          <input type="file" ref="imagenes" multiple class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Marca:</label>
          <input type="text" v-model="marca" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Vendedor:</label>
          <input type="text" v-model="vendedor" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div>
          <label class="block mb-2 font-medium">Rating:</label>
          <input type="number" v-model.number="rating" class="block w-full border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-500">
        </div>
        <div class="col-span-2">
          <button type="submit" @click.prevent="agregarProducto" class="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md mt-4">Agregar</button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      nombre: '',
      descripcion: '',
      cantidad: 0,
      precio: 0,
      imagenes: [],
      marca: '',
      vendedor: '',
      rating: 0
    };
  },
  methods: {
    agregarProducto() {
      // Aquí podrías enviar los datos del producto al servidor
      console.log(this.nombre, this.descripcion, this.cantidad, this.precio, this.imagenes, this.marca, this.vendedor, this.rating);
      // Luego podrías resetear los campos del formulario
      this.nombre = '';
      this.descripcion = '';
      this.cantidad = 0;
      this.precio = 0;
      this.imagenes = [];
      this.marca = '';
      this.vendedor = '';
      this.rating = 0;
      this.$refs.imagenes.value = '';
    }
  }
};
</script>