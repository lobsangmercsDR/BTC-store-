<template>
  <div class="max-w-4xl mx-auto grid flex-col items-center">
    <!-- Campo de descripción y generación de código -->
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Descripción:</label>
      <input v-model="descripcion" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Ingrese una descripción" required>
    </div>
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Código generado:</label>
      <input type="text" :value="codigo" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" readonly>
    </div>
    <button @click="generarCodigo" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">Generar</button>
    
    <!-- Tabla con códigos y descripciones generados previamente -->
    <div class="mt-8">
      <h2 class="text-lg font-bold mb-2">Códigos generados</h2>
      <table class="min-w-full bg-white border border-gray-300">
        <thead>
          <tr>
            <th class="px-4 py-2 border-b">Descripción</th>
            <th class="px-4 py-2 border-b">Código</th>
            <th class="px-4 py-2 border-b">Fecha de Generación</th>
            <th class="px-4 py-2 border-b">Usuarios Registrados</th>
            <th class="px-4 py-2 border-b">Creado por</th>
            <th class="px-4 py-2 border-b"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in codigosGenerados" :key="index">
            <td class="px-4 py-2 border-b">{{ item.descripcion }}</td>
            <td class="px-4 py-2 border-b">{{ item.codigo }}</td>
            <td class="px-4 py-2 border-b">{{ item.fechaGeneracion }}</td>
            <td class="px-4 py-2 border-b">{{ item.usuariosRegistrados }}</td>
            <td class="px-4 py-2 border-b">{{ item.creadoPor }}</td>
            <td class="px-4 py-2 border-b">
              <button @click="eliminarCodigo(index)" class="text-red-600 font-semibold hover:text-red-800">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.flex {
  display: flex;
}

.items-center {
  align-items: center;
}
</style>

<script>
export default {
  data() {
    return {
      descripcion: '',
      codigo: '',
      codigosGenerados: [],
      creadoPor: 'Nombre del creador', // Agrega el nombre del creador predeterminado aquí
    };
  },
  methods: {
    generarCodigo() {
      const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      let codigoGenerado = '';
      for (let i = 0; i < 16; i++) {
        codigoGenerado += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
      }
      this.codigo = codigoGenerado;
      
      // Agregar el código, la descripción, la fecha de generación, la cantidad de usuarios registrados y el nombre del creador a la lista de códigos generados
      this.codigosGenerados.push({
        descripcion: this.descripcion,
        codigo: this.codigo,
        fechaGeneracion: new Date().toLocaleString(), // Obtener la fecha actual
        usuariosRegistrados: 0, // Inicialmente, no hay usuarios registrados
        creadoPor: this.creadoPor,
      });
      
      // Limpiar el campo de descripción y reiniciar el campo de código
      this.descripcion = '';
      this.codigo = '';
    },
    eliminarCodigo(index) {
      this.codigosGenerados.splice(index, 1);
    },
  },
};
</script>
