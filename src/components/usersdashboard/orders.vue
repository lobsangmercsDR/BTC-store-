<template>
  <div class="bg-white rounded shadow">
    <div class="px-4 py-3 border-b">
      <h2 class="text-lg font-semibold">Mis órdenes</h2>
    </div>
    <div class="p-4">
      <div v-if="orders.length === 0" class="text-gray-600">
        No hay órdenes disponibles.
      </div>
      <div v-for="(orderList, orderType) in ordersByType" :key="orderType">
        <h3 @click="toggleOrderSection(orderType)" class="text-lg font-semibold mt-4 cursor-pointer">
          Órdenes de productos {{ orderType === 'physical' ? 'físicos' : 'digitales' }}
          <span v-if="isOrderSectionOpen(orderType)" class="text-sm ml-2">[-]</span>
          <span v-else class="text-sm ml-2">[+]</span>
        </h3>
        <table v-show="isOrderSectionOpen(orderType)" class="table-auto w-full text-left">
          <thead>
            <tr>
              <th class="px-4 py-2">ID de orden</th>
              <th class="px-4 py-2">Fecha</th>
              <th class="px-4 py-2">Estado</th>
              <th class="px-4 py-2">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in orderList" :key="order.id" class="cursor-pointer">
              <td class="border px-4 py-2">{{ order.id }}</td>
              <td class="border px-4 py-2">{{ order.date }}</td>
              <td class="border px-4 py-2">{{ order.status }}</td>
              <td class="border px-4 py-2">
                <button @click.stop="openReportModal(order)" class="px-2 py-1 bg-red-500 text-white rounded">Reportar problema</button>
                <button @click.stop="openDetailsModal(order)" class="px-2 py-1 bg-blue-500 text-white rounded ml-2">Ver detalles</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <transition name="modal">
      <div class="fixed z-10 inset-0 overflow-y-auto" v-if="detailsModalOpen">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <h3 class="text-lg leading-6 font-medium text-gray-900">Detalles de la orden</h3>
              <p>{{ selectedOrder.details }}</p>
            </div>
            <div class="px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button @click.stop="closeDetailsModal" type="button" class="px-4 py-2 bg-blue-500 text-white rounded">Cerrar</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <transition name="modal">
      <div class="fixed z-10 inset-0 overflow-y-auto" v-if="reportModalOpen">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 transition-opacity">
            <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
          </div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <h3 class="text-lg leading-6 font-medium text-gray-900">Reportar problema</h3>
              <p>{{ selectedOrder.type === 'physical' ? 'Quejas físicas' : 'Quejas virtuales' }}</p>
            </div>
            <div class="px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button @click.stop="closeReportModal" type="button" class="px-4 py-2 bg-red-500 text-white rounded">Cerrar</button>
            </div>
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
          id: '1',
          type: 'physical',
          date: '2023-05-01',
          status: 'Entregado',
          details: 'Detalles de la orden física 1'
        },
        {
          id: '2',
          type: 'virtual',
          date: '2023-05-02',
          status: 'Descargado',
          details: 'Detalles de la orden virtual 2'
        },
        // Más órdenes...
      ],
      orderSections: {
        physical: true,
        virtual: true,
      },
      detailsModalOpen: false,
      reportModalOpen: false,
      selectedOrder: null,
    };
  },
  computed: {
    ordersByType() {
      return {
        physical: this.orders.filter((order) => order.type === 'physical'),
        virtual: this.orders.filter((order) => order.type === 'virtual'),
      };
    },
  },
  methods: {
    toggleOrderSection(orderType) {
      this.orderSections[orderType] = !this.orderSections[orderType];
    },
    isOrderSectionOpen(orderType) {
      return this.orderSections[orderType];
    },
    openDetailsModal(order) {
      this.selectedOrder = order;
      this.detailsModalOpen = true;
    },
    closeDetailsModal() {
      this.selectedOrder = null;
      this.detailsModalOpen = false;
    },
    openReportModal(order) {
      this.selectedOrder = order;
      this.reportModalOpen = true;
    },
    closeReportModal() {
      this.selectedOrder = null;
      this.reportModalOpen = false;
    },
  },
};
</script>


<style scoped>
.table-auto {
  width: 100%;
  max-width: 100%;
  margin-bottom: 1rem;
  border-collapse: collapse;
}

.table-auto th,
.table-auto td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table-auto thead th {
  border-bottom: 2px solid #dee2e6;
}

.table-auto tbody+tbody {
  border-top: 2px solid #dee2e6;
}
</style>
