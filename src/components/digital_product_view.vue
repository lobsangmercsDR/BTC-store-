<template>
  <div class="wrapper">
    <div class="search-bar">
      <input
        class="search-input"
        type="text"
        placeholder="Buscar productos..."
        v-model="searchQuery"
      />
      <button class="search-button" @click="filterData">Buscar</button>
    </div>
    <table>
      <thead>
        <tr>
          <th>Productos</th>
          <th>Productos Restantes</th>
          <th>Precio en BTC</th>
          <th>Equivalente en Dólares</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in filteredData" :key="index">
          <td>{{ item.product }}</td>
          <td>{{ item.remaining }}</td>
          <td>{{ item.priceBTC }}</td>
          <td>{{ item.equivalentUSD }}</td>
          <td>
            <button class="button-buy" @click="buyProduct(index)">Ver producto</button>
          </td>
        </tr>
        <tr v-if="filteredData.length === 0 && searchQuery !== ''">
          <td colspan="5" class="no-results">No se encontró el producto.</td>
        </tr>
      </tbody>
    </table>
    <div class="pagination">
      <button @click="handlePrevPage" :disabled="currentPage === 1" class="pagination-button">Anterior</button>
      <button @click="handleNextPage" :disabled="currentPage * pageSize >= filteredData.length" class="pagination-button">Siguiente</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      tableData: [
        {
          product: 'Producto 1',
          remaining: 10,
          priceBTC: 0.001,
          equivalentUSD: 50
        },
        {
          product: 'Producto 2',
          remaining: 5,
          priceBTC: 0.002,
          equivalentUSD: 100
        },
        {
          product: 'Producto 3',
          remaining: 8,
          priceBTC: 0.003,
          equivalentUSD: 150
        },
        // Agregar más datos...
      ],
      filteredData: [],
      pageSize: 15,
      currentPage: 1
    }
  },
  computed: {
    pagedData() {
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.filteredData.slice(start, end);
    }
  },
  created() {
    this.filteredData = this.tableData;
  },
  methods: {
    buyProduct(index) {
      const realIndex = (this.currentPage - 1) * this.pageSize + index;
      this.filteredData[realIndex].remaining--;
      alert('Compraste ' + this.filteredData[realIndex].product);
    },
    filterData() {
      this.currentPage = 1; // Restablecer a la primera página
      this.filteredData = this.tableData.filter(row =>
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
    }
  }
}
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
  background-color: #f66305;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #ab16be;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table th,
table td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

.no-results {
  text-align: center;
  color: #f66305;
  font-weight: bold;
}

.pagination {
  margin-top: 20px;
  text-align: right;
}

.pagination-button {
  margin-left: 5px;
  padding: 8px 12px;
  background-color: #f66305;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.pagination-button:hover {
  background-color: #ab16be;
}
</style>
