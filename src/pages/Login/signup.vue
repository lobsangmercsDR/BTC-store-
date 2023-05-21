

<template>
    <div>
        <navbar-component></navbar-component>
        <main>
            <section class="absolute w-full h-full">
                <div class="absolute top-0 w-full h-full bg-gray-900"
                    style="background-size: 100%; background-repeat: no-repeat;">
                <div class="container mx-auto px-4 h-full">
                    <div class="flex content-center items-center justify-center h-full loginContainer">
                        <div class="w-full lg:w-4/12 px-4">
                            <div class="relative 
                                        flex 
                                        flex-col
                                        min-w-0 
                                        break-words 
                                        w-full mb-6 
                                        shadow-lg 
                                        rounded-lg 
                                        bg-gray-300 
                                        border-0 
                                        loginContainer">
                                <div class="rounded-t mb-0 px-6 py-6">
                                    <div class="text-center mb-3">
                                        <h6 class="text-gray-600 text-sm font-bold">
                                            Register
                                        </h6>
                                    </div>
                                    <hr class="mt-6 border-b-1 border-gray-400" />
                                </div>
                                <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
                                    <div class="text-gray-500 text-center mb-3 font-bold">
                                        <small>Create a new account</small>
                                    </div>
                                    <form>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-name">UserName</label>
                                            <div v-if="error && error.hasOwnProperty('name')" class="text-red-500 errorText"> 
                                                <small>{{ error.name[0] }}</small>
                                            </div>
                                            <input type="text"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Your name" v-model="name" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('name')}"/>
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-name">Email</label>
                                            <div v-if="error && error.hasOwnProperty('email')" class="text-red-500 errorText"> 
                                                <small>{{ error.email[0] }}</small>
                                            </div>
                                            <input type="text"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Your email" v-model="email" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('email')}"/>
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-email">Invitation Code</label>
                                            <div v-if="error && error.hasOwnProperty('invitation_code')" class="text-red-500 errorText"> 
                                                <small>{{ error.invitation_code[0] }}</small>
                                            </div>
                                            <input type="email"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Your invitation codes" v-model="invitation_code" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('invitation_code')}"/>
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password">Password</label>
                                            <div v-if="error && error.hasOwnProperty('password')" class="text-red-500 errorText"> 
                                                <small>{{ error.password[0] }}</small>
                                            </div>
                                            <input type="password"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Password"  v-model="password" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('password')}"/>
                                        </div>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password-confirm" >Confirm Password</label>
                                            <div v-if="error && error.hasOwnProperty('confirm_pass')" class="text-red-500 errorText"> 
                                                <small>{{ error.confirm_pass[0] }}</small>
                                            </div>
                                            <input type="password" v-model="confirm_pass"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Confirm Password" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('confirm_pass')}"/>
                                        </div>
                                        <div class="flex justify-between items-center mb-3">
                                            <div>
                                                <label class="inline-flex items-center cursor-pointer"><input
                                                        id="customCheckRegister" type="checkbox"
                                                        class="form-checkbox border-0 rounded text-gray-800 ml-1 w-5 h-5"
                                                        style="transition: all 0.15s ease 0s;" /><span
                                                        class="ml-2 text-sm font-semibold text-gray-700">I agree to the <a
                                                            href="#terms-of-service"
                                                            class="text-gray-500 hover:text-gray-800 font-semibold">terms of
                                                            service</a></span></label>
                                            </div>
                                            <div>
                                                <router-link to="/login" class="link"
                                                    style="transition: all 0.15s ease 0s;">
                                                    Have a account?
                                                </router-link>

                                            </div>
                                        </div>
                                        <div class="text-center">
                                            <button
                                                class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                                                type="button" @click="register"  style="transition: all 0.15s ease 0s;">
                                                Register
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <footer-component></footer-component>
            </div>
            </section>
        </main>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return {
            name:'',
            email: '',
            password: '',
            confirm_pass:'',
            invitation_code: '',
            error: null
        };
    },

    methods: {
        async register() {
        try  {
            const response =  await axios.post("http://127.0.0.1:8000/api/users", {
                name: this.name,
                email: this.email,
                password: this.password,
                confirm_pass: this.confirm_pass,
                invitation_code: this.invitation_code
            })
            console.log(response.data)
            }
            catch(error) {
                this.error = error.response.data
                console.log(error.response.data)
            }
        }
    }
};

</script>

  