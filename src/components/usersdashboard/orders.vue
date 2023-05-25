<template>
  <div class="bg-white rounded shadow">
    <div class="px-4 py-3 border-b">
      <h2 class="text-lg font-semibold">Órdenes</h2>
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
                  <span class="font-semibold">Productos:</span>
                  <ul>
                    <li v-for="product in order.products" :key="product.id">
                      {{ product.name }} - {{ product.price }}
                    </li>
                  </ul>
                </div>
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
                    <span class="font-semibold">Estado:</span> {{ order.status }}
                  </div>
                </div>
                <div v-if="order.showDetails" class="mt-2">
                  <span class="font-semibold">Productos:</span>
                  <ul>
                    <li v-for="product in order.products" :key="product.id">
                      {{ product.name }} - {{ product.price }}
                    </li>
                  </ul>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
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
          products: [
            { id: 1, name: "Producto 1", price: "$10.00" },
            { id: 2, name: "Producto 2", price: "$15.00" },
          ],
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
          showDetails: false,
        },
      ],
      openOrderSections: [],
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
        this.openOrderSections = this.openOrderSections.filter(
          (s) => s !== section
        );
      } else {
        this.openOrderSections.push(section);
      }
    },
    isOrderSectionOpen(section) {
      return this.openOrderSections.includes(section);
    },
  },
};
</script>

<style>
/* Agrega cualquier estilo adicional que desees */
</style>
