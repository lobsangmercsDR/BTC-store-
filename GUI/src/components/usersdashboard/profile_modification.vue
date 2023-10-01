<template>
  <div class="container mx-auto py-8">
    <div class="max-w-4xl mx-auto">
      <div class="bg-white shadow-md rounded-lg p-6 formCont">
        <div class="mb-4 allie">
          <label for="name" class="text-lg">Nombre:</label>
          <input v-model="user.name" id="name" type="text" class="form-input">
        </div>

        <div class="mb-4">
          <label for="email" class="text-lg">Correo Electrónico:</label>
          <input v-model="user.email" id="email" type="email" class="form-input">
        </div>

        <div class="mb-4">
          <label for="address" class="text-lg">Dirección:</label>
          <input v-model="user.direction" id="address" type="text" class="form-input">
        </div>

        <div class="mb-4">
          <label for="phone" class="text-lg">Teléfono:</label>
          <input v-model="user.phoneNumber" id="phone" type="text" class="form-input">
        </div>

        <div class="mb-4">
          <label for="bitcoin-wallet" class="text-lg">Wallet de Bitcoin:</label>
          <input v-model="user.wallet_address" id="bitcoin-wallet" type="text" class="form-input" readonly>
        </div>

        <div class="mb-4">
          <label for="invitation-code" class="text-lg">Código de Invitación:</label>
          <input v-model="user.invitationCode" id="invitation-code" type="text" class="form-input" readonly>
        </div>

        <div class="flex justify-end">
          <button @click="saveChanges" class="btn-save-changes">
            Guardar Cambios
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  created() {
    this.getUserData()
  },

  data() {
    return {
      user: {
        name: true,
        email: true,
        phoneNumber: true,
        direction:true,
        wallet_address: true,
        invitationCode: true
      }
    };
  },
  methods: {
    async saveChanges() {
      const propiedadesAEliminar = ['group', 'is_active'];
      propiedadesAEliminar.forEach((prop) => {
          delete this.user[prop];
      });
        await axios.put(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`,this.user,
        {
          headers:{
            Authorization:`Token ${Cookies.get('token')}`
          }
        })
        .then(response => {})
        .catch(error => {console.log(error.response.data)})
    },

    async getUserData() { 
        await axios.get(`http://127.0.0.1:8000/api/users/${Cookies.get('svg')}`, {
          headers:{
            Authorization: `Token ${Cookies.get('token')}`
        }})
        .then(response => {this.user = response.data})
        .catch(error => {console.log(error.response.data)})

        await axios.get(`http://127.0.0.1:8000/api/userbased/invitation/${Cookies.get('svg')}`, {
          headers: {
            Authorization: `Token ${Cookies.get('token')}`
          }
        })
        .then(response => {this.user.invitationCode = response.data[0].invitationCodes})
        .catch(error=> {console.log(error)})
    }
  }
};
</script>

<style>

@media (max-width:650px) {
    .formCont  {
      max-width: 345px;
    }
}


.btn-save-changes {
  background-color: #4C51BF;
  color: white;
  font-weight: bold;
  padding: 0.75rem 1rem;
  border-radius: 0.375rem;
  transition: background-color 0.3s;
}

.btn-save-changes:hover {
  background-color: #4338CA;
}

.btn-save-changes:active {
  background-color: #372F9A;
}

.form-input {
  border: 1px solid #CBD5E0;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: border-color 0.3s;
}

.form-input:focus {
  outline: none;
  border-color: #4C51BF;
  box-shadow: 0 0 0 3px rgba(76, 81, 191, 0.3);
}
</style>
