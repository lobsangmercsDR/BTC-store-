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
                          <input type="email" class="border-0 px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full" placeholder="Your invitation codes" v-model="invitation_code" style="transition: all 0.15s ease 0s;" :class="{'errorInput' : error && error.hasOwnProperty('invitation_code')}"/>
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
                          <button :disabled="captchaResult !== 'Correct'" class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1" type="button" @click="register" style="transition: all 0.15s ease 0s;">
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
  
      <div v-if="loading" class="modal">
        <div class="modal-content">
          <div class="spinner"></div>
          <p>Creando cuenta...</p>
        </div>
      </div>
  
      <div v-if="registrationSuccess" class="modal">
        <div class="modal-content">
          <h2>Registro exitoso</h2>
          <p>Los datos del registro son:</p>
          <ul>
            <li><strong>Nombre:</strong> {{ registrationData.name }}</li>
            <li><strong>Email:</strong> {{ registrationData.email }}</li>
            <li><strong>Dirección de la cartera:</strong> {{ registrationData.walletAddress }}</li>
            <li><strong>Balance de la cartera:</strong> {{ registrationData.walletBalance }}</li>
          </ul>
          <button class="close-btn" @click="closeModal">Cerrar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        name: 'Juas',
        email: 'Juas@gmail.com',
        password: '12345',
        confirm_pass: '12345',
        invitation_code: 'aoqkWnzgprvWqbB',
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
        loading: false,
        registrationSuccess: false,
        registrationData: {},
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
  
          this.loading = true; // Mostrar el modal de carga
  
          // Crear cartera de BTC en block.io
          const blockIOResponse = await axios.post('https://block.io/api/v2/get_new_address', {
            api_key: '005d-5ad1-f083-a252',
            label: this.name,
            currency: 'btc',
          }).then(response => {console.log(response)})
          .catch(error => {console.log(error)})
  
          // Obtener la dirección de la cartera y su saldo
          const walletAddress = blockIOResponse.data.data.address;
          const walletBalance = blockIOResponse.data.data.balance;
  
          // Enviar los datos a la API
          const response = await axios.post('http://127.0.0.1:8000/api/users', {
            name: this.name,
            email: this.email,
            password: this.password,
            confirm_pass: this.confirm_pass,
            invitation_code: this.invitation_code,
          });
  
          this.registrationData = {
            ...response.data,
            walletAddress,
            walletBalance,
          }; // Almacenar los datos del registro exitoso
          this.registrationSuccess = true; // Mostrar el segundo modal
        } catch (error) {
          this.error = error;
          console.log(error);
        } finally {
          this.loading = false; // Ocultar el modal de carga
        }
      },
      closeModal() {
        this.registrationSuccess = false;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos CSS personalizados */
  .captcha-board {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .captcha-row {
    display: flex;
    justify-content: center;
  }
  
  .captcha-cell {
    width: 30px;
    height: 30px;
    border: 1px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5px;
    cursor: pointer;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: white;
    padding: 20px;
    border-radius: 5px;
  }
  
  .spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #f3f3f3;
    border-top: 5px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  
  .modal h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .modal ul {
    list-style: none;
    padding: 0;
  }
  
  .modal li {
    margin-bottom: 0.5rem;
  }
  
  .close-btn {
    background-color: #3498db;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
  