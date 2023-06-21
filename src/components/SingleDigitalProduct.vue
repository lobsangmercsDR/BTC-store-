<template>
  <div class="container">
    <div class="bg-white card rounded-lg shadow-md p-4 md:p-8 transition-colors duration-500 hover:bg-blue-50 mx-auto">
      <div v-if="product" class="flex flex-col md:flex-row">
        <div class="w-full md:w-1/2">
          <div class="bg-gray-200 rounded-lg h-[250px] md:h-[500px]">
            <h3 class="text-xl font-semibold mb-2 text-left">Preview:</h3>
            <p class="text-gray-600 text-lg text-left">{{ product.additional_details }}</p>
            <p v-if="!hasPurchased" class="text-red-500 text-sm mt-2">For complete view buy the product</p>
          </div>
          <div class="flex items-center mb-2">
            <p class="text-2xl font-semibold mr-2">Categorias:</p>
            <p class="text-green-500 text-lg font-extrabold">Subcate</p>
          </div>
        </div>
        <div class="w-full md:w-1/2 md:pl-8 text-left">
          <h2 class="text-3xl font-semibold mb-4 text-orange-600 hover:text-purple-800 transition-colors duration-300">
            {{ product.name }}
          </h2>
          <div class="mt-8 flex items-center space-x-4"></div>
          <div class="mt-4">
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Tienda:</span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold"></span>
              <span class="text-lg">{{ product.brand }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Fecha de Publicacion:</span>
              <span class="text-lg">{{ product.release_data }}</span>
            </div>
            <div class="flex items-center mb-2">
              <span class="text-gray-600 text-lg mr-2 font-semibold">Cantidad</span>
              <span class="text-lg">{{ product.quantity }}</span>
            </div>
            <div class="flex items-center mb-2">
              <p class="text-2xl font-semibold mr-2">{{ product.price.toFixed(0)}}</p>
              <p v-if="!needChecker" class="ml-2 text-gray-600 text-sm">(+{{ product.checkerPrice.toFixed(2) }} del Checker)</p>
            </div>

            <!-- Botón Need checker -->
            <div class="flex items-center mb-2">
              <button
                v-if="needChecker"
                @click="openCheckerModal"
                class="bg-red-500 hover:bg-green-600 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500 mr-2"
              >
                Necesita verificacion
              </button>
              <button
                v-else
                class="bg-green-500 text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 mr-2"
                disabled
              >
                Verificado
              </button>
            </div>

            <div class="flex mt-4 justify-end">
              <button
                @click="addToCart"
                class="bg-[#f76108] hover:bg-[#fa7328] text-white py-2 px-4 rounded font-semibold uppercase tracking-wide transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#f76108] mr-2"
              >
                Comprar ahora
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="text-center py-8">
        <p class="text-lg text-gray-600">Cargando datos del producto...</p>
      </div>
    </div>

    <!-- Ventana emergente de pago -->
    <transition name="modal">
      <div v-if="showPaymentModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Confirmar compra</h2>
          <p>Producto: {{ product.name }}</p>
          <p>Cantidad: {{ quantity }}</p>
          <p>Precio total: {{ (product.price * quantity * btcPrice).toFixed(8) }} BTC / ${{ (product.price * quantity).toFixed(2) }} USD</p>
          <p>
            <input type="checkbox" v-model="addChecker" class="mr-2" :disabled="needChecker" />
            <span>Agregar Checker (+{{ product.checkerPrice.toFixed(8) }} BTC)</span>
          </p>
          <p v-if="addChecker" class="text-red-500 text-sm">Los productos digitales comprados sin checker no tienen derecho a garantía.</p>
          <hr class="my-4">
          <p>Username: {{ user.username }}</p>
          <p>Saldo disponible en BTC: <span class="text-green-500">{{ user.balanceBTC.toFixed(8) }} BTC</span></p>
          <p>Equivalente en USD: ${{ (user.balanceBTC * btcPrice).toFixed(2) }} USD</p>
          <div class="flex justify-end mt-4">
            <button @click="showPaymentModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cancelar</button>
            <button @click="confirmPayment" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Confirmar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de pago exitoso -->
    <transition name="modal">
      <div v-if="showSuccessModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Pago Exitoso</h2>
          <p>¡Gracias por tu compra!</p>
          <div class="mt-4">
            <h3 class="text-xl font-semibold mb-2">Factura:</h3>
            <p>Orden: {{ orderNumber }}</p>
            <p>Producto: {{ product.name }}</p>
            <p>Cantidad: {{ quantity }}</p>
            <p>Tienda: {{ product.brand }}</p>
            <p>Dirección de la transacción: {{ transactionAddress }}</p>
          </div>
          <div class="flex justify-end mt-4">
            <button @click="showSuccessModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
            <button @click="downloadInvoice" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Descargar Factura</button>
            <button @click="downloadContent" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Descargar Contenido</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de transacción declinada -->
    <transition name="modal">
      <div v-if="showDeclinedModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Transacción declinada</h2>
          <p>Lo sentimos, no tienes fondos suficientes para completar la compra.</p>
          <div class="flex justify-end mt-4">
            <button @click="showDeclinedModal = false" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
          </div>
        </div>
      </div>
    </transition>

    <!-- Ventana emergente de Need Checker -->
    <transition name="modal">
      <div v-if="showCheckerModal" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white rounded-lg p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-semibold mb-4">Need Checker</h2>
          <p v-if="needChecker" class="text-red-500">Este producto requiere el uso de un checker.</p>
          <p v-else class="text-green-500">Este producto ya ha sido verificado.</p>
          <textarea v-model="checkerInput" class="border border-gray-300 rounded-lg p-2 mb-4 w-full h-32 resize-none" placeholder="Introduce tu texto..."></textarea>
          <div class="flex justify-end mt-4">
            <button @click="closeCheckerModal" class="text-gray-500 hover:text-gray-700 mr-2">Cerrar</button>
            <button v-if="needChecker" @click="sendCheckerRequest" class="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded">Enviar</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import jsPDF from "jspdf";

export default {
  data() {
    return {
      product: null,
      hasPurchased: false,
      quantity: 1,
      btcPrice: 40000,
      user: {
        username: "JohnDoe",
        balanceBTC: 0.5,
      },
      showPaymentModal: false,
      showSuccessModal: false,
      showDeclinedModal: false,
      showCheckerModal: false,
      needChecker: false,
      checkerInput: "",
      addChecker: false,
      orderNumber: "",
      transactionAddress: "",
    };
  },
  mounted() {
    this.product = {
      name: 'Pack 100000 cuentas de GMAIL',
      description: 'Compra lass cuentas',
      price: 0.011,
      likes: 0,
      dislikes: 0,
      additionalDetails:
        'Super Blends were carefully crafted to mimic the live resin experience. We drew our inspiration from the cannabis plant. Creating unique cannabinoid formulas with terpene profiles that mirror today’s most popular strains.',
      release_data: "Aqui fecha",
      quantity: 0,
      category: [],
      subcategory: [],
      seller_username: "Djangolapara",
      checkerPrice: 10, // Precio adicional del checker
    };
    this.productPriceBTC = this.product.price * this.btcPrice;
  },
  methods: {
    incrementLikes() {
      this.product.likes++;
    },
    incrementDislikes() {
      this.product.dislikes++;
    },
    convertToDollars(price) {
      return price * this.btcPrice;
    },
    addToCart() {
      console.log(`Agregando ${this.quantity} unidades del producto al carrito`);
    },
    buyNow() {
      this.showPaymentModal = true;
    },
    confirmPayment() {
      // Verificar si el usuario tiene fondos suficientes
      if (this.user.balanceBTC >= this.product.price * this.quantity) {
        console.log(`Comprando ${this.quantity} unidades del producto`);

        // Lógica adicional para procesar el pago

        // Mostrar el modal de éxito
        this.showPaymentModal = false;
        this.showSuccessModal = true;

        // Generar número de orden y dirección de la transacción
        this.orderNumber = Math.floor(Math.random() * 1000000);
        this.transactionAddress = "0x123abc...";

        // Resetear el estado
        this.quantity = 1;
        this.addChecker = false;
      } else {
        // Mostrar el modal de transacción declinada
        this.showPaymentModal = false;
        this.showDeclinedModal = true;
      }
    },
    downloadInvoice() {
      const doc = new jsPDF();
      doc.setFontSize(18);
      doc.text("Factura de Compra", 20, 20);
      doc.setFontSize(12);
      doc.text(`Orden: ${this.orderNumber}`, 20, 30);
      doc.text(`Producto: ${this.product.name}`, 20, 40);
      doc.text(`Cantidad: ${this.quantity}`, 20, 50);
      doc.text(`Tienda: ${this.product.brand}`, 20, 60);
      doc.text(`Dirección de la Transacción: ${this.transactionAddress}`, 20, 70);
      doc.save("invoice.pdf");
    },
    downloadContent() {
      const text = this.product.additionalDetails;
      const element = document.createElement("a");
      const file = new Blob([text], { type: "text/plain" });
      element.href = URL.createObjectURL(file);
      element.download = "content.txt";
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    },
    closeCheckerModal() {
      this.showCheckerModal = false;
    },
    openCheckerModal() {
      this.showCheckerModal = true;
    },
    sendCheckerRequest() {
      // Lógica para enviar la solicitud del checker

      // Cerrar el modal después de enviar la solicitud
      this.showCheckerModal = false;
    },
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.bg-white {
  margin: 0 auto;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.select-variant {
  text-align: left;
  width: 100%;
}

.fixed {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.bg-black {
  background-color: #000;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-4 {
  padding: 1rem;
}

.md\:p-8 {
  padding: 2rem;
}

.transition-colors {
  transition-property: color;
  transition-duration: 0.5s;
}

.hover\:bg-blue-50:hover {
  background-color: #f0f4ff;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.text-left {
  text-align: left;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.card {
  width: 985px;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-orange-600 {
  color: #fb923c;
}

.hover\:text-purple-800:hover {
  color: #6b46c1;
}

.mt-8 {
  margin-top: 2rem;
}

.space-x-4 > * {
  margin-right: 1rem;
}

.mt-4 {
  margin-top: 1rem;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.mr-2 {
  margin-right: 0.5rem;
}

.text-green-500 {
  color: #84cc16;
}

.font-extrabold {
  font-weight: 800;
}

.text-red-500 {
  color: #f87171;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.mt-4 {
  margin-top: 1rem;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-[#f76108] {
  background-color: #f76108;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #fa7328;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.text-white {
  color: #fff;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #d836e8;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

.bg-white {
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-gray-600 {
  color: #718096;
}

.mt-8 {
  margin-top: 2rem;
}

.justify-end {
  justify-content: flex-end;
}

.mt-4 {
  margin-top: 1rem;
}

.px-8 {
  padding-left: 2rem;
  padding-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-4 {
  margin-bottom: 1rem;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2.25rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tracking-wide {
  letter-spacing: 0.025em;
}

.ml-2 {
  margin-left: 0.5rem;
}

.text-gray-600 {
  color: #718096;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.flex {
  display: flex;
}

.justify-end {
  justify-content: flex-end;
}

.mr-2 {
  margin-right: 0.5rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.rounded {
  border-radius: 0.25rem;
}

.uppercase {
  text-transform: uppercase;
}

.focus\:outline-none:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}

.bg-red-500 {
  background-color: #f87171;
}

.hover\:bg-green-600:hover {
  background-color: #047857;
}

.text-white {
  color: #fff;
}

.hover\:bg-[#fa7328]:hover {
  background-color: #f87171;
}

.bg-green-500 {
  background-color: #84cc16;
}

.hover\:bg-[#d836e8]:hover {
  background-color: #6b46c1;
}

.bg-[#ac15c1] {
  background-color: #ac15c1;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-purple-800 {
  color: #6b46c1;
}

.focus\:ring-red-500:focus {
  box-shadow: 0 0 0 3px rgba(248, 113, 113, 0.5);
}

</style>
