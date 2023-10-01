<template>
    <div class="flex items-center justify-center min-h-screen bg-white-900">
      <div class="col-span-9/12">
        <div class="overflow-auto lg:overflow-visible">
          <table class="table text-gray-400 border-separate space-y-6 text-sm">
            <thead class="bg-gray-800 text-gray-500">
              <tr>
                <th class="p-3">Brand</th>
                <th class="p-3 text-left">Category</th>
                <th class="p-3 text-left">Price</th>
                <th class="p-3 text-left">Status</th>
                <th class="p-3 text-left">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in products" :key="index" class="bg-gray-800">
                <td class="p-3">
                  <div class="flex items-center">
                    <img class="rounded-full h-9 w-9 object-cover" :src="product.image" alt="Product image">
                    <div class="ml-3">
                      <div class="">{{ product.brand }}</div>
                      <div class="text-gray-500">{{ product.email }}</div>
                    </div>
                  </div>
                </td>
                <td class="p-3">
                  {{ product.category }}
                </td>
                <td class="p-3 font-bold">
                  {{ product.price }}
                </td>
                <td class="p-3">
                  <span :class="getStatusClass(product.status)">{{ product.status }}</span>
                </td>
                <td class="p-3">
                  <a href="#" class="text-gray-400 hover:text-gray-100 mr-2" @click="viewProduct(index)">
                    <i class="material-icons-outlined text-base">visibility</i>
                  </a>
                  <a href="#" class="text-gray-400 hover:text-gray-100 mx-2" @click="editProduct(index)">
                    <i class="material-icons-outlined text-base">edit</i>
                  </a>
                  <a href="#" class="text-gray-400 hover:text-gray-100 ml-2" @click="deleteProduct(index)">
                    <i class="material-icons-round text-base">delete_outline</i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: [
          {
            brand: "Apple",
            category: "Technology",
            price: "200.00$",
            status: "available",
            image: "https://images.unsplash.com/photo-1613588718956-c2e80305bf61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80",
            email: "mail@rgmail.com"
          },
          {
            brand: "Realme",
            category: "Technology",
            price: "200.00$",
            status: "no stock",
            image: "https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80",
            email: "mail@rgmail.com"
          },
          {
            brand: "Samsung",
            category: "Technology",
            price: "200.00$",
            status: "start sale",
            image: "https://images.unsplash.com/photo-1600856209923-34372e319a5d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2135&q=80",
            email: "mail@rgmail.com"
          }
        ]
      };
    },
    methods: {
      getStatusClass(status) {
        if (status === "available") {
          return "bg-green-400 text-gray-50 rounded-md px-2";
        } else if (status === "no stock") {
          return "bg-red-400 text-gray-50 rounded-md px-2";
        } else if (status === "start sale") {
          return "bg-yellow-400 text-gray-50 rounded-md px-2";
        }
        return "";
      },
      viewProduct(index) {
        // Implement your logic for viewing a product
      },
      editProduct(index) {
        // Implement your logic for editing a product
      },
      deleteProduct(index) {
        // Implement your logic for deleting a product
      }
    }
  };
  </script>
  
  <style>
  .table {
    border-spacing: 0 15px;
  }
  
  i {
    font-size: 1rem !important;
  }
  
  .table tr {
    border-radius: 20px;
  }
  
  tr td:nth-child(n+5),
  tr th:nth-child(n+5) {
    border-radius: 0 .625rem .625rem 0;
  }
  
  tr td:nth-child(1),
  tr th:nth-child(1) {
    border-radius: .625rem 0 0 .625rem;
  }
  </style>
  