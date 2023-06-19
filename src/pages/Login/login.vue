

<template>
    <div>
        <navbar-component></navbar-component>
        <main>
            <section class="absolute w-full h-full">
                <div class="absolute top-0 w-full h-full bg-gray-900"
                    style="background-size: 100%; background-repeat: no-repeat;"></div>
                <div class="container mx-auto px-4 h-full">
                    <div class="flex content-center items-center justify-center h-full  loginContainer">
                        <div class="w-full lg:w-4/12 px-4">
                            <div
                                class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0 loginContainer ">
                                <div class="rounded-t mb-0 px-6 py-6">
                                    <div class="text-center mb-3">
                                        <h6 class="text-gray-600 text-sm font-bold">
                                            Sign in
                                        </h6>
                                    </div>
                                    <hr class="mt-6 border-b-1 border-gray-400" />
                                </div>
                                <div class="flex-auto px-4 lg:px-10 py-10 pt-0 loginContainer">
                                    <div class="text-gray-500 text-center mb-3 font-bold">
                                        <small>Sign in with your credentials</small>
                                    </div>
                                    <form>
                                        <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password">Username</label>
                                            <div v-if="error && error.hasOwnProperty('email')" class="text-red-500 errorText"> 
                                                <small>{{ error.email[0] }}</small>
                                            </div>
                                            <input type="email"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Email" v-model="email" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('email')}"/>
                                        </div>
                                            <div class="relative w-full mb-3">
                                            <label class="block uppercase text-gray-700 text-xs font-bold mb-2"
                                                for="grid-password">Password</label>
                                            <div v-if="error && error.hasOwnProperty('password')" class="text-red-500 errorText"> 
                                                <small>{{ error.password[0] }}</small>
                                            </div>
                                            <input type="password"
                                                class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                                placeholder="Password" v-model="password" style="transition: all 0.15s ease 0s;"  :class="{'errorInput' : error && error.hasOwnProperty('password')}"/>
                                        </div>
                                        <div class="flex justify-between items-center mb-3">
                                            <div>
                                                <label class="inline-flex items-center cursor-pointer"><input
                                                        id="customCheckLogin" type="checkbox"
                                                        class="form-checkbox border-0 rounded text-gray-800 ml-1 w-5 h-5"
                                                        style="transition: all 0.15s ease 0s;" /><span
                                                        class="ml-2 text-sm font-semibold text-gray-700">Remember
                                                        me</span></label>
                                            </div>
                                            <div>
                                                <router-link to="/resetpass" class="link"
                                                    style="transition: all 0.15s ease 0s;">
                                                    Reset Password
                                                </router-link>


                                            </div>
                                        </div>
                                        <div v-if="error && error.hasOwnProperty('non_field_errors')" class="text-red-500 errorLoginBox"> 
                                                {{ error.non_field_errors[0] }}
                                            </div>
                                        <div class="text-center">
                                            <button
                                                class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                                                type="button"  @click="login" style="transition: all 0.15s ease 0s;">
                                                Sign In
                                            </button>
                                            <router-link to="/signup"
                                                class="bg-gray-500 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
                                                style="transition: all 0.15s ease 0s;">
                                                Register
                                            </router-link>

                                        </div>
                                    </form>
                                </div>
                            </div>
                            <div class="flex flex-wrap mt-6">
                                <div class="w-1/2">
                                    <a href="#forgot-password" class="text-gray-500"><small>Forgot password?</small></a>
                                </div>
                                <div class="w-1/2 text-right">
                                    <a href="#register" class="text-gray-500"><small>Create new account</small></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <footer-component></footer-component>
            </section>
        </main>
    </div>
</template>


<script>
import axios from 'axios';
import Cookies from 'js-cookie'
export default {
    data(){
        return {
            email: '',
            password: '',
            error: null
        };
    },

    methods: {
        async login() {
            try  {
                const response =  await axios.post("http://127.0.0.1:8000/api/users/authenticate", {
                    email: this.email,
                    password: this.password
                })
                Cookies.set('token', response.data.token, {expires: 1, secure:true, sameSite: 'strict'}, null, null, true)
                Cookies.set('svg', response.data.user,  {expires: 1, secure:true, sameSite: 'strict'}, null, null, true)
                this.$router.push('/')
            }
            catch(error) {
                // this.error = error.response.data
                console.log(error)
            }
        }
    }
};
</script>
  