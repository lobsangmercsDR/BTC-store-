<template>
    <div>
      <navbar-component></navbar-component>
      <main>
        <section class="absolute w-full h-full">
          <div class="absolute top-0 w-full h-full bg-gray-900" style="background-size: 100%; background-repeat: no-repeat;">
            <div class="container mx-auto px-4 h-full">
              <div class="flex content-center items-center justify-center h-full loginContainer">
                <div class="w-full lg:w-4/12 px-4">
                  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0 loginContainer">
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
                      <form @submit.prevent="register">
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-name">UserName</label>
                          <div v-if="error && error.hasOwnProperty('name')" class="text-red-500 errorText">
                            <small>{{ error.name[0] }}</small>
                          </div>
                          <input type="text" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Your name" v-model="name" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('name')}"/>
                        </div>
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-name">Email</label>
                          <div v-if="error && error.hasOwnProperty('email')" class="text-red-500 errorText">
                            <small>{{ error.email[0] }}</small>
                          </div>
                          <input type="text" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Your email" v-model="email" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('email')}"/>
                        </div>
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-email">Invitation Code</label>
                          <div v-if="error && error.hasOwnProperty('invitation_code')" class="text-red-500 errorText">
                            <small>{{ error.invitation_code[0] }}</small>
                          </div>
                          <input type="text" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Your invitation code" v-model="invitation_code" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('invitation_code')}"/>
                        </div>
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-password">Password</label>
                          <div v-if="error && error.hasOwnProperty('password')" class="text-red-500 errorText">
                            <small>{{ error.password[0] }}</small>
                          </div>
                          <input type="password" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Password" v-model="password" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('password')}"/>
                        </div>
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-password-confirm">Confirm Password</label>
                          <div v-if="error && error.hasOwnProperty('confirm_pass')" class="text-red-500 errorText">
                            <small>{{ error.confirm_pass[0] }}</small>
                          </div>
                          <input type="password" v-model="confirm_pass" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Confirm Password" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('confirm_pass')}"/>
                        </div>
                        <div class="relative w-full mb-3">
                          <label class="block uppercase text-gray-700 text-xs font-bold mb-2" for="grid-captcha">Enter the position of 'X'</label>
                          <div class="captcha-board">
                            <div v-for="(row, rowIndex) in captcha.board" class="captcha-row">
                              <div v-for="(cell, colIndex) in row" class="captcha-cell" @click="selectCell(rowIndex, colIndex)">{{ cell }}</div>
                            </div>
                          </div>
                        </div>
                        <div v-if="captchaResult" class="relative w-full mb-3">
                          <div :class="{'text-green-500': captchaResult === 'Correct', 'text-red-500': captchaResult === 'Incorrect'}">
                            <small>{{ captchaResult }}</small>
                          </div>
                        </div>
                        <div class="flex justify-between items-center mb-3">
                          <div>
                            <label class="inline-flex items-center cursor-pointer">
                              <input id="customCheckRegister" type="checkbox" class="form-checkbox border-0 rounded text-gray-800 ml-1 w-5 h-5" style="transition: all 0.15s ease 0s;" />
                              <span class="ml-2 text-sm font-semibold text-gray-700">I agree to the <a href="#terms-of-service" class="text-gray-500 hover:text-gray-800 font-semibold">terms of service</a></span>
                            </label>
                          </div>
                          <div>
                            <router-link to="/login" class="link" style="transition: all 0.15s ease 0s;">
                              Have an account?
                            </router-link>
                          </div>
                        </div>
                        <div class="text-center">
                          <button :disabled="captchaResult !== 'Correct'" class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1" type="submit" style="transition: all 0.15s ease 0s;">
                            Register
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <footer-component></footer-component>
        </section>
  
        <transition name="fade">
          <div class="modal-wrapper" v-if="showLoadingModal">
            <div class="modal-content">
              <div class="spinner"></div>
              <p>Creating user...</p>
            </div>
          </div>
        </transition>
  
        <transition name="fade">
          <div class="modal-wrapper" v-if="showSuccessModal">
            <div class="modal-content">
              <h2 class="text-2xl font-bold mb-4">User Created</h2>
              <p>Cart ID: {{ cartId }}</p>
              <p>BTC Wallet: <input type="text" v-model="btcWallet" class="border p-1"></p>
              <button class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mt-4" @click="closeSuccessModal">Close</button>
            </div>
          </div>
        </transition>
      </main>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: '',
        confirm_pass: '',
        invitation_code: '',
        error: null,
        captcha: {
          board: [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
          ],
          position: '',
        },
        captchaResult: '',
        btcWallet: '',
        cartId: '',
        showLoadingModal: false,
        showSuccessModal: false,
      };
    },
    mounted() {
      this.generateCaptcha();
    },
    methods: {
      generateCaptcha() {
        const randomRow = Math.floor(Math.random() * 3);
        const randomCol = Math.floor(Math.random() * 3);
        this.captcha.board[randomRow][randomCol] = 'X';
        this.captcha.position = `${String.fromCharCode(65 + randomRow)}${randomCol + 1}`;
      },
      selectCell(rowIndex, colIndex) {
        if (this.captcha.board[rowIndex][colIndex] === 'X') {
          this.captchaResult = 'Correct';
        } else {
          this.captchaResult = 'Incorrect';
        }
      },
      async register() {
        try {
          if (this.captchaResult !== 'Correct') {
            alert('Please complete the CAPTCHA correctly.');
            return;
          }
  
          this.showLoadingModal = true;
  
          await new Promise(resolve => setTimeout(resolve, 4000));
  
          this.cartId = this.generateCartId();
  
          this.showLoadingModal = false;
          this.showSuccessModal = true;
  
          this.name = '';
          this.email = '';
          this.password = '';
          this.confirm_pass = '';
          this.invitation_code = '';
          this.captchaResult = '';
          this.btcWallet = '';
        } catch (error) {
          this.error = error.response.data;
          console.log(error.response.data);
        }
      },
      closeSuccessModal() {
        this.showSuccessModal = false;
      },
      generateCartId() {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
  
        for (let i = 0; i < 8; i++) {
          result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
  
        return result;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos personalizados */
  .modal-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 9999;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    text-align: center;
  }
  
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s;
  }
  
  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }
  
  .spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #edf2f7;
    animation: spin 1s infinite linear;
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  
  .captcha-board {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .captcha-row {
    display: flex;
  }
  
  .captcha-cell {
    width: 3rem;
    height: 3rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #000;
    cursor: pointer;
  }
  
  .errorText {
    margin-top: 0.25rem;
    color: red;
  }
  
  .errorInput {
    border-color: red;
  }
  </style>
  