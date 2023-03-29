<template>
    <div class="flex flex-col">
      <h1 class="text-xl font-bold mb-4">Administrador de Usuarios</h1>
      <div class="flex flex-col w-full overflow-x-auto">
        <table class="table-auto w-full">
          <thead>
            <tr>
              <th class="px-4 py-2">Nombre de usuario</th>
              <th class="px-4 py-2">Dirección de cartera</th>
              <th class="px-4 py-2">Código de invitación</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="usuario in usuarios" :key="usuario.id">
              <td class="border px-4 py-2">{{ usuario.username }}</td>
              <td class="border px-4 py-2">{{ usuario.direccion }}</td>
              <td class="border px-4 py-2">{{ usuario.codigo }}</td>
              <td class="border px-4 py-2">{{ usuario.estado }}</td>
              <td class="border px-4 py-2">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                  Editar
                </button>
                <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">
                  Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminUsuarios',
    data() {
      return {
        usuarios: [
          {
            id: 1,
            username: 'juanperez',
            direccion: '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
            codigo: 'ABC123',
            estado: 'Activo',
          },
          {
            id: 2,
            username: 'mariaortega',
            direccion: '3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC',
            codigo: 'DEF456',
            estado: 'Inactivo',
          },
          {
            id: 3,
            username: 'pedrosanchez',
            direccion: '3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC',
            codigo: 'GHI789',
            estado: 'Activo',
          },
        ],
      };
    },
  };
  </script>
  