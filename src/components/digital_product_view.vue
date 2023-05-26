<template>
    <div class="wrapper">
      <el-input
        class="search-input"
        placeholder="Buscar productos..."
        v-model="searchQuery"
        @input="filterData"
        clearable
      >
        <template #prefix>
          <i class="el-input__icon el-icon-search"></i>
        </template>
      </el-input>
      <el-table :data="pagedData" style="width: 100%">
        <el-table-column prop="product" label="Productos"></el-table-column>
        <el-table-column prop="remaining" label="Productos Restantes"></el-table-column>
        <el-table-column prop="priceBTC" label="Precio en BTC"></el-table-column>
        <el-table-column prop="equivalentUSD" label="Equivalente en Dólares"></el-table-column>
        <el-table-column label="Acciones">
          <template #default="scope">
            <el-button class="button-buy" type="primary" @click="buyProduct(scope.$index)">Ver producto</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination">
        <el-button @click="handlePrevPage" :disabled="currentPage === 1">Anterior</el-button>
        <el-button @click="handleNextPage" :disabled="currentPage * pageSize >= filteredData.length">Siguiente</el-button>
      </div>
    </div>
  </template>
  
  <script>
  import { ElTable, ElTableColumn, ElButton, ElInput } from 'element-plus'
  
  export default {
    components: {
      ElTable,
      ElTableColumn,
      ElButton,
      ElInput
    },
    data() {
      return {
        searchQuery: '',
        tableData: [
        { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
          { product: 'Producto 1', remaining: 10, priceBTC: 0.001,equivalentUSD: 50},
         
          // otros productos...
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
        this.currentPage = 1; // reset to first page
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
  
  .search-input {
    margin-bottom: 20px;
  }
  
  .button-buy {
    background-color: #f66305;
    color: #fff;
    transition: background-color 0.3s ease;
  }
  
  .button-buy:hover {
    background-color: #ab16be;
  }
  
  .pagination {
    margin-top: 20px;
    text-align: right;
  }
  </style>
  