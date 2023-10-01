<template>
    <div>
        <main>
            <div class="absolute top-0 w-full h-full bg-gray-900"
                    style="background-size: 100%; background-repeat: no-repeat;"></div>
            <section class="absolute w-full h-full" style="min-width: 370px;padding: 20px;">
                    <div class="flex content-center items-center justify-center h-full">
                        <div style="max-width: 428px; min-width: 340px;">
                            <div
                                class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0" >
                                <div class="rounded-t mb-0 px-6 py-6" >
                                    <div class="text-center mb-3">
                                        <h6 class="text-gray-600 text-sm font-bold">
                                            Cambiar Contraseña
                                        </h6>
                                    </div>
                                    <hr class="mt-6 border-b-1 border-gray-400" />
                                </div>
                                <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
                                    <div class="text-gray-500 text-center mb-3 font-bold">
                                        <small>Ponga sus datos en los campos adecuados segun sea necesario</small>
                                    </div>
                                    <form>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-username">Username</label>
                                            <div v-if="error && error.hasOwnProperty('email')" class="text-red-500 errorText"> 
                                                <small>{{ error.email[0] }}</small>
                                            </div>
                                            <input type="text"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                autocomplete="usernm"  placeholder="Username" v-model="usrInp.email" :class="{'errorInput' : error && error.hasOwnProperty('email')}" style="transition: all 0.15s ease 0s;" />
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-invitation-code">Contraseña Previa</label>
                                            <div v-if="error && error.hasOwnProperty('oldPassword')" class="text-red-500 errorText"> 
                                                <small>{{ error.oldPassword[0] }}</small>
                                            </div>
                                            <input type="password"
                                                autocomplete="old-password" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Contraseña previa" v-model="usrInp.oldPassword"  :class="{'errorInput' : error && error.hasOwnProperty('oldPassword')}" style="transition: all 0.15s ease 0s;" />
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password">Nueva Contraseña</label>
                                            <div v-if="error && error.hasOwnProperty('newPassword')" class="text-red-500 errorText"> 
                                                <small>{{ error.newPassword[0] }}</small>
                                            </div>
                                            <input type="password"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                autocomplete="new-password" name="password" placeholder="Nueva contraseña" v-model="usrInp.newPassword" :class="{'errorInput' : error && error.hasOwnProperty('newPassword')}" style="transition: all 0.15s ease 0s;" />
                                        </div>

                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password-confirm">Confirmar nueva contraseña</label>
                                            <div v-if="error && error.hasOwnProperty('retPassword')" class="text-red-500 errorText"> 
                                                <small>{{ error.retPassword[0] }}</small>
                                            </div>
                                            <input type="password"
                                                autocomplete="rep-password" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Nueva contraseña" v-model="usrInp.retPassword"  :class="{'errorInput' : error && error.hasOwnProperty('retPassword')}" style="transition: all 0.15s ease 0s;" />
                                        </div>
                                        <div class="text-center">
                                            <button
                                                class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                                                type="button" style="transition: all 0.15s ease 0s;" @click="updatePasword()">
                                                Cambiar Contraseña
                                            </button>
                                        </div>
                                        <div v-if="error && error.hasOwnProperty('non_field_errors')" class="text-red-500 mt-2 errorLoginBox"> 
                                            {{ error.non_field_errors[0] }}
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
            </section>
        </main>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            usrInp: {
                email:'',
                oldPassword:'',
                newPassword:'',
                retPassword:''
            },
            error:null,
        }
    },

    methods: {
        async updatePasword() {
            await axios.put('http://127.0.0.1:8000/api/users/restpass', this.usrInp)
            .then(response => {
                this.$router.push('/login')
            })
            .catch(error => {
                this.error = error.response.data
                console.log(this.error)
            })
        }
    }
}
</script>