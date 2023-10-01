<template>
  <div class="wrapper">
    <div class="search-bar">
      <InputText v-model="searchQuery" placeholder="Buscar productos..." />
      <Button class="p-button-rounded p-button-info search-button" @click="filterData">
        <i class="pi pi-search"></i>
        Buscar
      </Button>
    </div>
    <DataTable :value="pagedData" :rows="pageSize" :paginator="true" :currentPage="currentPage" @onPage="handlePageChange"
      class="p-datatable-striped">
      <Column field="product" header="Productos"></Column>
      <Column field="remaining" header="Productos Restantes"></Column>
      <Column field="priceBTC" header="Precio en BTC"></Column>
      <Column field="equivalentUSD" header="Equivalente en Dólares"></Column>
      <Column header="Acciones">
        <template #body="rowData">
          <Button class="p-button-rounded p-button-success p-button-sm" @click="buyProduct(rowData)">
            <i class="pi pi-shopping-cart"></i>
            Ver producto
          </Button>
        </template>
      </Column>
    </DataTable>
    <div class="pagination">
      <Button @click="handlePrevPage" :disabled="currentPage === 1" class="p-button-rounded p-button-secondary p-button-sm pagination-button">
        Anterior
      </Button>
      <Button @click="handleNextPage" :disabled="currentPage * pageSize >= filteredData.length" class="p-button-rounded p-button-secondary p-button-sm pagination-button">
        Siguiente
      </Button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

export default {
  components: {
    DataTable,
    Column,
    InputText,
    Button,
  },
  data() {
    return {
      searchQuery: '',
      tableData: [
        {
          product: 'Producto 1',
          remaining: 10,
          priceBTC: 0.001,
          equivalentUSD: 50,
        },
        {
          product: 'Producto 2',
          remaining: 5,
          priceBTC: 0.002,
          equivalentUSD: 100,
        },
        {
          product: 'Producto 3',
          remaining: 8,
          priceBTC: 0.003,
          equivalentUSD: 150,
        },
        // Agregar más datos...
      ],
      filteredData: [],
      pageSize: 15,
      currentPage: 1,
    };
  },
  computed: {
    pagedData() {
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.filteredData.slice(start, end);
    },
  },
  created() {
    this.filteredData = this.tableData;
  },
  methods: {
    buyProduct(rowData) {
      rowData.remaining--;
      alert('Compraste ' + rowData.product);
    },
    filterData() {
      this.currentPage = 1; // Restablecer a la primera página
      this.filteredData = this.tableData.filter((row) =>
        row.product.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    handlePrevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    handleNextPage() {
      if (this.currentPage * this.pageSize < this.filteredData.length) {
        this.currentPage++;
      }
    },
    handlePageChange(event) {
      this.currentPage = event.page + 1;
    },
  },
};
</script>

<style scoped>
.wrapper {
  width: 90%;
  margin: 0 auto;
  background-color: #fff;
  border: 1px solid #f66305;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.search-bar {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.search-button {
  margin-left: 10px;
  padding: 8px 16px;
}

.pagination {
  margin-top: 20px;
  text-align: right;
}

.pagination-button {
  margin-left: 5px;
  padding: 8px 12px;
}

.p-datatable-striped .p-datatable-tbody > tr:nth-child(odd) {
  background-color: #f6f6f6;
}

.p-button-rounded {
  border-radius: 20px;
}

.p-button-info {
  background-color: #f66305;
  color: #fff;
}

.p-button-info:hover {
  background-color: #ab16be;
}

.p-button-success {
  background-color: #4caf50;
  color: #fff;
}

.p-button-success:hover {
  background-color: #45a049;
}

.p-button-secondary {
  background-color: #ccc;
  color: #fff;
}

.p-button-secondary:hover {
  background-color: #999;
}
</style>
