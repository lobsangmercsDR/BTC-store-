<template>
  <div class="max-w-fit mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
    <h1 class="text-3xl font-bold text-center bg-blue-500 text-white py-4">Administrador de Usuarios</h1>

    <!-- Buscador -->
    <div class="flex justify-end mt-4 px-4">
      <input v-model="searchQuery" type="text" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Buscar por usuario">
    </div>

    <!-- Lista de usuarios -->
    <table class="min-w-full">
      <thead>
        <tr>
          <th class="px-4 py-2 text-left">ID</th>
          <th class="px-4 py-2 text-left">Nombre</th>
          <th class="px-4 py-2 text-left">Correo Electrónico</th>
          <th class="px-4 py-2 text-left">Rol</th>
          <th class="px-4 py-2 text-left">Fecha de Registro</th>
          <th class="px-4 py-2 text-left">Cartera Bitcoin</th>
          <th class="px-4 py-2 text-left">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in paginatedUsers" :key="user.id">
          <td class="border px-4 py-2">{{ user.id }}</td>
          <td class="border px-4 py-2">{{ user.name }}</td>
          <td class="border px-4 py-2">{{ user.email }}</td>
          <td class="border px-4 py-2">{{ user.role }}</td>
          <td class="border px-4 py-2">{{ user.registrationDate }}</td>
          <td class="border px-4 py-2">{{ user.bitcoinWallet }}</td>
          <td class="border px-4 py-2">
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
              @click="editUser(user)"
            >
              Editar
            </button>
            <button
              class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
              @click="deleteUser(user.id)"
            >
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Paginación -->
    <div class="flex justify-center mt-4">
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        @click="previousPage"
        :disabled="currentPage === 1"
      >
        Anterior
      </button>
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-2"
        @click="nextPage"
        :disabled="currentPage === totalPages"
      >
        Siguiente
      </button>
    </div>

    <!-- Formulario para editar un usuario -->
    <form class="mt-4 px-4 pb-4" v-if="editUserData">
      <h2 class="text-xl font-bold mb-2">Editar Usuario</h2>
      <div class="mb-2">
        <label class="block text-gray-700">Nombre:</label>
        <input v-model="editUserData.name" type="text" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Correo Electrónico:</label>
        <input v-model="editUserData.email" type="email" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Rol:</label>
        <select v-model="editUserData.role" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
          <option>Administrador</option>
          <option>Usuario</option>
          <option>Baneado</option>
        </select>
      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Fecha de Registro:</label>
        <input v-model="editUserData.registrationDate" type="date" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Cartera Bitcoin:</label>
        <input v-model="editUserData.bitcoinWallet" type="text" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
      </div>
      <div class="text-right">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          @click.prevent="updateUser"
        >
          Actualizar
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [
        { id: 1, name: "John Doe", email: "johndoe@example.com", role: "Usuario", registrationDate: "2023-05-01", bitcoinWallet: "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa" },
        { id: 2, name: "Jane Smith", email: "janesmith@example.com", role: "Administrador", registrationDate: "2023-05-02", bitcoinWallet: "3KmQjFFCrJHb1hPjH8m2N5jn5HLH8dFPfH" },
        { id: 3, name: "Mike Johnson", email: "mikejohnson@example.com", role: "Baneado", registrationDate: "2023-05-03", bitcoinWallet: "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq" },
        { id: 4, name: "Sarah Williams", email: "sarahwilliams@example.com", role: "Usuario", registrationDate: "2023-05-04", bitcoinWallet: "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF" },
        { id: 5, name: "David Brown", email: "davidbrown@example.com", role: "Administrador", registrationDate: "2023-05-05", bitcoinWallet: "bc1qes3g7yp7pkvt8v44hq0aamr23jkuec3q69kl5u" },
        { id: 6, name: "Emily Davis", email: "emilydavis@example.com", role: "Usuario", registrationDate: "2023-05-06", bitcoinWallet: "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC" },
        { id: 7, name: "Michael Wilson", email: "michaelwilson@example.com", role: "Usuario", registrationDate: "2023-05-07", bitcoinWallet: "1AC4gh14wwZPULVPCdxUkgqbtPvC92PQPN" },
        { id: 8, name: "Jessica Taylor", email: "jessicataylor@example.com", role: "Administrador", registrationDate: "2023-05-08", bitcoinWallet: "3AnNxabYGoTxYiTEZwFEnerUoeFXK2Zoks" },
        { id: 9, name: "William Anderson", email: "williamanderson@example.com", role: "Baneado", registrationDate: "2023-05-09", bitcoinWallet: "1J6PYkjCj7mQv3avVaU5N7JtsyakGtjyKx" },
        { id: 10, name: "Olivia Martinez", email: "oliviamartinez@example.com", role: "Usuario", registrationDate: "2023-05-10", bitcoinWallet: "bc1q8c6fshw2dlwun7ekn9qwf37cu2rn755upcp6el" },
      ],
      searchQuery: '',
      itemsPerPage: 3,
      currentPage: 1,
      editUserData: null,
    };
  },
  computed: {
    filteredUsers() {
      if (!this.searchQuery) {
        return this.users;
      }

      const query = this.searchQuery.toLowerCase();

      return this.users.filter(user =>
        user.name.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query) ||
        user.role.toLowerCase().includes(query) ||
        user.bitcoinWallet.toLowerCase().includes(query)
      );
    },
    totalPages() {
      return Math.ceil(this.filteredUsers.length / this.itemsPerPage);
    },
    paginatedUsers() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;

      return this.filteredUsers.slice(startIndex, endIndex);
    },
  },
  methods: {
    editUser(user) {
      this.editUserData = { ...user };
    },
    updateUser() {
      const userIndex = this.users.findIndex(user => user.id === this.editUserData.id);

      if (userIndex !== -1) {
        // Show a confirmation dialog
        if (confirm("¿Estás seguro de que deseas actualizar los datos del usuario?")) {
          this.users[userIndex] = { ...this.editUserData };
          this.editUserData = null;
          console.log("Usuario actualizado correctamente");
        } else {
          console.log("Actualización de usuario cancelada");
        }
      } else {
        console.error("Error: No se encontró el usuario en la lista");
      }
    },
    deleteUser(userId) {
      const userIndex = this.users.findIndex(user => user.id === userId);

      if (userIndex !== -1) {
        this.users.splice(userIndex, 1);
        console.log("Usuario eliminado correctamente");
      } else {
        console.error("Error: No se encontró el usuario en la lista");
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
};
</script>

<style>
/* Estilos adicionales si los necesitas */

body {
  background-color: #f3f4f6;
}

input:focus {
  outline: none;
  border-color: #4c51bf;
  box-shadow: 0 0 0 2px rgba(76, 81, 191, 0.5);
}

button[disabled] {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
