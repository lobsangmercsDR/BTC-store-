<template>
  <div class="max-w-fit mx-auto  bg-white shadow-lg rounded-lg overflow-hidden containersDash">
    <h1 class="text-3xl font-bold text-center bg-blue-500 text-white py-4">Administrador de Usuarios</h1>

    <!-- Buscador -->
    <div class="flex justify-end mt-4 px-4">
      <input v-model="searchQuery" type="text" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Buscar por usuario">
    </div>

    <!-- Lista de usuarios -->
    <table class="min-w-full" v-show="!isWindowSmall">
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
         {{  }}
        <tr v-for="(user, index) in usersTable" :key="user.id">
          <td class="border px-4 py-2">{{ user.id }}</td>
          <td class="border px-4 py-2">{{ user.name }}</td>
          <td class="border px-4 py-2">{{ user.email }}</td>
          <td class="border px-4 py-2">{{ user.group }}</td>
          <td class="border px-4 py-2">{{ user.createdAt }}</td>
          <td class="border px-4 py-2">{{ user.wallet_address }}</td>
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

    <!--Lista de tablas responsive-->
    <table 
    style="
    border: 3px solid;
    margin: 39px auto;
    " 
    
    class="
    table 
    min-w-full 
    border 
    border-gray-300 
    responsive-table"
    
    v-if="isWindowSmall" 
    v-for="(user, index) in usersTable" :key="user.id">

      <tbody>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">ID</td>
          <td class="py-2 px-4 border-b">{{ user.id }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Username</td>
          <td class="py-2 px-4 border-b">{{ user.name }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Amount (BTC)</td>
          <td class="py-2 px-4 border-b">{{ user.email }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Amount (USD)</td>
          <td class="py-2 px-4 border-b">{{ user.group }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Date</td>
          <td class="py-2 px-4 border-b">{{ user.createdAt }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Wallet</td>
          <td class="py-2 px-4 border-b">{{ user.wallet_address }}</td>
        </tr>
        <tr>
          <td class="py-2 px-4 bg-gray-100 border-b">Actions</td>
          <td class="py-2 px-4 border-b">
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
    <div class="flex justify-center mt-4" v-if="edi">
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
        <div v-if="error && error.hasOwnProperty('email')" class="text-red-500 errorText"> 
            <small>{{ error.email[0] }}</small>
        </div>
        <input v-model="editUserData.email" type="email" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" :class="{'errorInput': error && error.hasOwnProperty('email')}"> 
      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Rol:</label>
        <select v-show="editUserData.group != 'SuperUser'" v-model="editUserData.group" @change="updateGroupUser" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
          <option value="administrator">Administrador</option>
          <option value="sellers">Vendedor</option>
          <option value="buyers">Comprador</option>
          <option value="checkers">Checker</option>
          <option value=false >Baneado</option>
        </select>
        <input v-show="editUserData.group == 'SuperUser'" v-bind:value="editUserData.group" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" readonly>
          
        

      </div>
      <div class="mb-2">
        <label class="block text-gray-700">Cartera Bitcoin:</label>
        <input v-model="editUserData.wallet_address" type="text" class="w-full border px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" readonly>
      </div>
      <div class="text-right">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          @click.prevent="updateUserInTable"
        >
          Actualizar
        </button>
        <button
          class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          @click.prevent="this.editUserData = false; this.formatData()"
        >
          Cancelar
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {


  data() {
    return {
      isWindowSmall: true,
      users: [],
      usersTable:[],
      error: null,
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

  created() {
    this.formatData();
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
    console.log(this.usersTable)
  },

  methods: {
    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 1045;
    },  
     async formatData() {  
      await this.getUsers()

      let modifiedResponse = JSON.parse(JSON.stringify(this.users));

        for (let i = 0; i < modifiedResponse.length; i++) {
          switch (modifiedResponse[i].group) {
            case "administrator":
            modifiedResponse[i].group = "Admin";
            break;
            case "checkers":
            modifiedResponse[i].group = "Checker";
            break;
            case "buyers":
            modifiedResponse[i].group = "Comprador";
            break;
            case "sellers":
              console.log("Si");
              modifiedResponse[i].group = "Vendedor";
            break;
            case false:
            modifiedResponse[i].group = "Baneado";
            break;
          }
        }        
        this.usersTable = modifiedResponse
    },
    async getUsers() {
      await axios.get("http://127.0.0.1:8000/api/users",{
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
      const originalResponse = response.data.slice()
      this.users = originalResponse
      console.log(response.data)
      return originalResponse
    }).catch(error =>  {console.log(error)})
    },

    async updateUserInApi(Id) {
      let newUserGroup = this.editUserData.group
      this.editUserData.change_group = newUserGroup
      delete this.editUserData.shares_count
      delete this.editUserData.purchases_count
      delete this.editUserData.last_login
      delete this.editUserData.createdAt
      console.log(this.editUserData)
      await axios.put(`http://127.0.0.1:8000/api/users/${Id}?roles=true`,this.editUserData,{
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {console.log(response.data); this.formatData()})
      .catch(error => {console.log(error.response.data); this.error= error.response.data})
    },

    async deleteCatTransactions(id,checker=false) {
      let url = ""
      if (checker) {
        url = `http://127.0.0.1:8000/api/transact_categories/user/${id}?checker=t`
      } 
      else {
        url = `http://127.0.0.1:8000/api/transact_categories/user/${id}`
      }

      await axios.delete(url, {
        headers: {
          Authorization: `Token ${Cookies.get('token')}`
        }
      })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.log(error.response.data)
      })
    },
  
    async editUser(user) {
      this.usersTable = [user]
      console.log(this.usersTable)
      await this.getUsers()
      let originalUserId  = this.users.findIndex(us => us.id === user.id)
      this.editUserData = { ...this.users[originalUserId] };
      console.log(this.editUserData)
    },
    updateUserInTable() {
      const userIndex = this.users.findIndex(user => user.id === this.editUserData.id);
      const oldUser= this.users[userIndex]
      console.log(this.editUserData)
      if (userIndex !== -1) {
        console.log(this.editUserData,oldUser)
        if (confirm("¿Estás seguro de que deseas actualizar los datos del usuario?")) {
          if(oldUser.group == "sellers" && this.editUserData.group == "buyers") {
            if(confirm("¿Desea hacer que el usuario deba comprar las categorias de nuevo para volver al rol?")) {
              this.deleteCatTransactions(this.editUserData.id)
            }
          }
        if(oldUser.group =="checkers" && this.editUserData.group == "buyers") {
          console.log(2)
          if(confirm('¿Desea hacer que el usuario debar comprar la categoria checker para volver al rol?')) {
            this.deleteCatTransactions(this.editUserData.id, true)
          }
        }
          this.updateUserInApi(this.editUserData.id)
          this.error = null
          console.log("Usuario actualizado correctamente");
          this.editUserData=false
        } else {
          console.log("Actualización de usuario cancelada");
        }
      } else {
        console.error("Error: No se encontró el usuario en la lista");
      }
    },

    updateGroupUser(event) {
      this.editUserData.group = event.target.value
    },


    async deleteUser(userId) {
      console.log(userId)
      const userIndex = this.users.findIndex(user => user.id === userId);
      if(confirm("¿Esta seguro que quiere eliminar este usuario?")) {
        if (userIndex !== -1) {
        await axios.delete(`http://127.0.0.1:8000/api/users/${userId}`,{
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        })
        .catch(error => {console.log(error) }) 
        this.usersTable.splice(userIndex, 1);
        console.log("Usuario eliminado correctamente");
        } else {
         console.error("Error: No se encontró el usuario en la lista");
      }
      }

    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      console.log(this.currentPage)
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
