<template>
  <div class="bg-white rounded shadow">
    <div class="px-4 py-3 border-b">
      <h2 class="text-lg font-semibold">Órdenes de venta</h2>
    </div>
    <div class="p-4">
      <div v-if="physicalOrders.length === 0 && digitalOrders.length === 0" class="text-gray-600">
        No hay órdenes disponibles.
      </div>
      <div>
        <div>
          <h3 @click="toggleOrderSection('physical')" class="text-lg font-semibold mt-4 cursor-pointer">
            Órdenes de productos físicos
            <span v-if="isOrderSectionOpen('physical')" class="text-sm ml-2">[-]</span>
            <span v-else class="text-sm ml-2">[+]</span>
          </h3>
          <ul v-show="isOrderSectionOpen('physical')">
            <li v-for="order in physicalOrders" :key="order.id" class="border-b py-3">
              <div @click="toggleOrderDetails(order)" class="cursor-pointer">
                <div class="flex items-center justify-between">
                  <div>
                    <span class="font-semibold">ID de orden:</span> {{ order.id }}
                  </div>
                  <div>
                    <span class="font-semibold">Fecha:</span> {{ order.date }}
                  </div>
                  <div>
                    <span class="font-semibold">Estado:</span> {{ order.status }}
                  </div>
                </div>
                <div v-if="order.showDetails" class="mt-2">
                  <table class="table-auto w-full">
                    <thead>
                      <tr>
                        <th class="px-4 py-2">Nombre</th>
                        <th class="px-4 py-2">Precio</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Número de orden:</td>
                        <td class="border px-4 py-2">{{ order.id }}</td>
                      </tr>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Comprador:</td>
                        <td class="border px-4 py-2">{{ order.buyerUsername }}</td>
                      </tr>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Dirección de envío del comprador:</td>
                        <td class="border px-4 py-2">{{ order.shippingAddress }}</td>
                      </tr>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Zona de entrega:</td>
                        <td class="border px-4 py-2">{{ order.deliveryZone }}</td>
                      </tr>
                      <tr v-for="product in order.products" :key="product.id">
                        <td class="border px-4 py-2">{{ product.name }}</td>
                        <td class="border px-4 py-2">{{ product.price }}</td>
                      </tr>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Total:</td>
                        <td class="border px-4 py-2 font-semibold">{{ calculateTotalPrice(order.products) }}</td>
                      </tr>
                    </tbody>
                  </table>
                  <div v-if="order.status === 'Pendiente aprobación de vendedor'" class="mt-4">
                    <button @click="openModal(order)" class="px-4 py-2 bg-green-500 text-white rounded">Aceptar</button>
                    <button @click="declineOrder(order)" class="px-4 py-2 bg-red-500 text-white rounded">Declinar</button>
                  </div>
                </div>
              </div>
              <div v-if="order.status === 'Aceptada' && order.company && order.trackingNumber" class="mt-4">
                <h3 class="text-lg font-semibold">Detalles de envío:</h3>
                <p><strong>Compañía de envío:</strong> {{ order.company }}</p>
                <p><strong>Número de seguimiento:</strong> {{ order.trackingNumber }}</p>
              </div>
            </li>
          </ul>
        </div>
        <div>
          <h3 @click="toggleOrderSection('digital')" class="text-lg font-semibold mt-4 cursor-pointer">
            Órdenes de productos digitales
            <span v-if="isOrderSectionOpen('digital')" class="text-sm ml-2">[-]</span>
            <span v-else class="text-sm ml-2">[+]</span>
          </h3>
          <ul v-show="isOrderSectionOpen('digital')">
            <li v-for="order in digitalOrders" :key="order.id" class="border-b py-3">
              <div @click="toggleOrderDetails(order)" class="cursor-pointer">
                <div class="flex items-center justify-between">
                  <div>
                    <span class="font-semibold">ID de orden:</span> {{ order.id }}
                  </div>
                  <div>
                    <span class="font-semibold">Fecha:</span> {{ order.date }}
                  </div>
                  <div>
                    <span class="font-semibold">Estado:</span> Completada
                  </div>
                </div>
                <div v-if="order.showDetails" class="mt-2">
                  <table class="table-auto w-full">
                    <thead>
                      <tr>
                        <th class="px-4 py-2">Nombre</th>
                        <th class="px-4 py-2">Precio</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="product in order.products" :key="product.id">
                        <td class="border px-4 py-2">{{ product.name }}</td>
                        <td class="border px-4 py-2">{{ product.price }}</td>
                      </tr>
                      <tr>
                        <td class="border px-4 py-2 font-semibold">Total:</td>
                        <td class="border px-4 py-2 font-semibold">{{ calculateTotalPrice(order.products) }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <transition name="fade">
      <div class="fixed inset-0 flex items-center justify-center z-50" v-if="showModal">
        <div class="bg-white rounded shadow p-4">
          <h3 class="text-lg font-semibold mb-4">Ingresar detalles de envío</h3>
          <div class="mb-4">
            <label class="block text-sm font-semibold mb-1">Compañía de envío:</label>
            <input v-model="shippingDetails.company" type="text" class="w-full border-gray-300 rounded p-2" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-semibold mb-1">Número de seguimiento:</label>
            <input v-model="shippingDetails.trackingNumber" type="text" class="w-full border-gray-300 rounded p-2" />
          </div>
          <div class="flex justify-end">
            <button @click="acceptOrderWithDetails()" class="px-4 py-2 bg-green-500 text-white rounded">Aceptar</button>
            <button @click="closeModal()" class="px-4 py-2 bg-red-500 text-white rounded">Cancelar</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      orders: [
        {
          id: 1,
          date: "2023-05-24",
          status: "Pendiente aprobación de vendedor",
          type: "física",
          shippingAddress: "Dirección 1",
          deliveryZone: "Zona 1",
          products: [
            { id: 1, name: "Producto 1", price: "$10.00" },
            { id: 2, name: "Producto 2", price: "$15.00" },
          ],
          buyerUsername: "comprador1",
          showDetails: false,
        },
        {
          id: 2,
          date: "2023-05-23",
          status: "Completada",
          type: "digital",
          products: [
            { id: 3, name: "Producto 3", price: "$20.00" },
            { id: 4, name: "Producto 4", price: "$12.00" },
          ],
          buyerUsername: "comprador2",
          showDetails: false,
        },
        {
          id: 3,
          date: "2023-05-22",
          status: "Pendiente aprobación de vendedor",
          type: "física",
          shippingAddress: "Dirección 2",
          deliveryZone: "Zona 2",
          products: [
            { id: 5, name: "Producto 5", price: "$8.00" },
            { id: 6, name: "Producto 6", price: "$18.00" },
          ],
          buyerUsername: "comprador3",
          showDetails: false,
        },
      ],
      openOrderSections: [],
      showModal: false,
      currentOrder: null,
      shippingDetails: {
        company: "",
        trackingNumber: "",
      },
      acceptedOrder: null,
    };
  },
  computed: {
    physicalOrders() {
      return this.orders.filter((order) => order.type === "física");
    },
    digitalOrders() {
      return this.orders.filter((order) => order.type === "digital");
    },
  },
  methods: {
    toggleOrderDetails(order) {
      order.showDetails = !order.showDetails;
    },
    toggleOrderSection(section) {
      if (this.isOrderSectionOpen(section)) {
        this.openOrderSections = this.openOrderSections.filter((s) => s !== section);
      } else {
        this.openOrderSections.push(section);
      }
    },
    isOrderSectionOpen(section) {
      return this.openOrderSections.includes(section);
    },
    openModal(order) {
      this.currentOrder = order;
      this.showModal = true;
    },
    closeModal() {
      this.currentOrder = null;
      this.showModal = false;
    },
    acceptOrderWithDetails() {
      if (this.shippingDetails.company && this.shippingDetails.trackingNumber) {
        this.currentOrder.status = "Aceptada";
        this.currentOrder.showDetails = true;
        this.currentOrder.shippingStatus = "Enviado";
        this.currentOrder.company = this.shippingDetails.company;
        this.currentOrder.trackingNumber = this.shippingDetails.trackingNumber;
        this.acceptedOrder = Object.assign({}, this.currentOrder);
        this.closeModal();
      }
    },
    declineOrder(order) {
      order.status = "Declinada";
    },
    calculateTotalPrice(products) {
      let totalPrice = 0;
      products.forEach((product) => {
        const price = parseFloat(product.price.replace("$", ""));
        totalPrice += price;
      });
      return "$" + totalPrice.toFixed(2);
    },
  },
};
</script>

<style>
.table-auto {
  width: auto;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
