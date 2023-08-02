<template>
  <div class="max-w-4xl mx-auto grid flex-col items-center containerInvDash">
    <!-- Campo de descripción y generación de código -->
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Descripción:</label>
      <input v-model="formData.description" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Ingrese una descripción" required>
    </div>
    <div class="mb-4">
      <label class="block text-gray-700 text-sm font-bold mb-2">Código generado:</label>
      <input type="text" :value="codigo" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" readonly>
    </div>
    <button @click="createInvitationCode" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">Generar</button>
    
    <!-- Tabla con códigos y descripciones generados previamente -->
    <div class="mt-8">
      <h2 class="text-lg font-bold mb-2">Códigos generados</h2>
      <table  v-if="!isWindowSmall" class="min-w-full bg-white border border-gray-300">
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
          <tr v-for="(item, index) in items" :key="item.id">
            <td class="px-4 py-2 border-b">{{ item.description }}</td>
            <td class="px-4 py-2 border-b">{{ item.invitationCodes }}</td>
            <td class="px-4 py-2 border-b">{{ item.created_at }}</td>
            <td class="px-4 py-2 border-b">{{ item.countUsers }}</td>
            <td class="px-4 py-2 border-b">{{ item.created_by.name}}</td>
            <td class="px-4 py-2 border-b">
              <button @click="deleteInvitationCode(item.id)" class="text-red-600 font-semibold hover:text-red-800">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!--Tabla de codigos responsive-->
      <table v-if="isWindowSmall" v-for="code in items" class="responsive-table-invitations">
        <tbody>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Withdrawal Order Number</td>
            <td class="py-2 px-4 border-b">{{ code.description }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Username</td>
            <td class="py-2 px-4 border-b">{{ code.invitationCodes }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Amount (BTC)</td>
            <td class="py-2 px-4 border-b">{{ code.created_at }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Amount (USD)</td>
            <td class="py-2 px-4 border-b">{{ code.countUsers }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Status</td>
            <td class="py-2 px-4 border-b">{{ code.created_by.name }}</td>
          </tr>
          <tr>
            <td class="py-2 px-4 bg-gray-100 border-b">Actions</td>
            <td class="px-4 py-2 border-b">
              <button @click="deleteInvitationCode(code.id)" class="text-red-600 font-semibold hover:text-red-800">Eliminar</button>
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
import axios from 'axios';
import Cookie from 'js-cookie'



export default {
  data() {
    return{
      isWindowSmall: false,
      items: [],
      formData: {
        description: ""
      },
      codigo: ""
    };
  },
  created() {
    this.getInvitationsCode()
    this.checkWindowSize();
    window.addEventListener('resize', this.checkWindowSize);
  },
  methods: {
    checkWindowSize() {
      this.isWindowSmall = window.innerWidth <= 800;
      console.log(this.isWindowSmall)
    }, 
    async getInvitationsCode() {
         await axios.get("http://127.0.0.1:8000/api/users/invitations", {
            headers: {
              Authorization: `Token ${Cookie.get('token')}`,
            },
          }).then(response => {console.log(response.data); this.items = response.data;})
          .catch(error => {console.log(error)});
      },

    async createInvitationCode() {
      await axios.post("http://127.0.0.1:8000/api/users/invitations",{description: this.formData.description} ,{
          headers: {
              Authorization: `Token ${Cookie.get('token')}`,
            },
      }).then(response => {console.log(response.data); this.getInvitationsCode(); this.codigo = response.data.invitationCodes})
      .catch(error => {console.log(error.response.data)});
      },

    async deleteInvitationCode(Id) {
      await axios.delete(`http://127.0.0.1:8000/api/users/invitations/${Id}`, {
        headers: {
          Authorization: `Token ${Cookie.get('token')}`
        }
      })
      .then(response => {console.log(response.data); this.getInvitationsCode()})
      .catch(error => {console.log(error.response.data)});
    }
    }
}
</script>
