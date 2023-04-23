<template>
    <div class="mx-auto max-w-500 px-4 overflow-x-auto">
        <table class="table-fixed w-full border-collapse border-gray-300 rounded-lg overflow-hidden bg-blue-900 text-white">
            <thead>
                <tr>
                    <td colspan="5" class="py-2 text-center">
                        <h2 class="text-lg font-medium">Ultimas compras</h2>
                    </td>
                </tr>
                <tr class="bg-gray-100 border-b border-gray-300 text-left">
                    <th class="w-1/5 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider font-bold">
                        Producto</th>
                    <th class="w-1/5 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">Vendedor</th>
                    <th class="w-1/5 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider font-bold">Precio
                    </th>
                    <th class="w-1/5 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">Última venta</th>
                    <th class="w-1/5 px-2 py-2 text-xs font-medium text-gray-500 uppercase tracking-wider">Total vendido
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(product, index) in products" :key="index"
                    :class="index % 2 === 0 ? 'bg-white hover:bg-gray-200' : 'bg-gray-50 hover:bg-gray-200'">
                    <td class="w-1/5 px-2 py-0.5 border-b border-gray-300">
                        <a :href="product.url" class="text-xs font-medium hover:underline text-black">{{ product.name }}</a>
                    </td>
                    <td class="w-1/5 px-2 py-0.5 border-b border-gray-300">
                        <div class="text-xs text-black">{{ product.seller }}</div>
                    </td>
                    <td class="w-1/5 px-2 py-0.5 border-b border-gray-300">
                        <div class="text-xs font-bold text-black">{{ product.price }}</div>
                    </td>
                    <td class="w-1/5 px-2 py-0.5 border-b border-gray-300">
                        <div class="text-xs text-black">{{ product.lastSold }}</div>
                    </td>
                    <td class="w-1/5 px-2 py-0.5 border-b border-gray-300">
                        <div class="text-xs text-black">{{ product.totalSold }}</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
  
  

<script>

export default {
    data() {
        return {
            products: [
                {
                    id: 1,
                    name: 'T-Shirt',
                    seller: 'Fashion Co.',
                    price: '$25.99',
                    lastSold: '2023-04-15',
                    totalSold: 10,
                },
                {
                    id: 2,
                    name: 'Jeans',
                    seller: 'Denim Co.',
                    price: '$35.99',
                    lastSold: '2023-04-14',
                    totalSold: 20,
                },
                {
                    id: 3,
                    name: 'Sneakers',
                    seller: 'Footwear Co.',
                    price: '$59.99',
                    lastSold: '2023-04-12',
                    totalSold: 5,
                },
                {
                    id: 4,
                    name: 'Hoodie',
                    seller: 'Fashion Co.',
                    price: '$49.99',
                    lastSold: '2023-04-18',
                    totalSold: 15,
                },
                {
                    id: 5,
                    name: 'Shorts',
                    seller: 'Sports Co.',
                    price: '$29.99',
                    lastSold: '2023-04-17',
                    totalSold: 8,
                },
                {
                    id: 6,
                    name: 'Sandals',
                    seller: 'Footwear Co.',
                    price: '$19.99',
                    lastSold: '2023-04-16',
                    totalSold: 12,
                },
                {
                    id: 7,
                    name: 'Jacket',
                    seller: 'Fashion Co.',
                    price: '$79.99',
                    lastSold: '2023-04-19',
                    totalSold: 5,
                },
                {
                    id: 8,
                    name: 'Dress',
                    seller: 'Fashion Co.',
                    price: '$45.99',
                    lastSold: '2023-04-13',
                    totalSold: 10,
                },
                {
                    id: 9,
                    name: 'Hat',
                    seller: 'Fashion Co.',
                    price: '$12.99',
                    lastSold: '2023-04-17',
                    totalSold: 20,
                },
                {
                    id: 10,
                    name: 'Sweater',
                    seller: 'Fashion Co.',
                    price: '$39.99',
                    lastSold: '2023-04-15',
                    totalSold: 15,
                },
                {
                    id: 20,
                    name: 'Heels',
                    seller: 'Footwear Co.',
                    price: '$79.99',
                    lastSold: '2023-04-16',
                    totalSold: 10,
                },
            ],
            intervalId: null, // ID del intervalo para detenerlo más tarde
        }
    },
    created() {
        this.startInterval();
    },
    methods: {
        startInterval() {
            this.intervalId = setInterval(() => {
                this.updateTable();
            }, 3000); // Actualizar la tabla cada 30 segundos
        },
        pauseTable() {
            clearInterval(this.intervalId); // Detener la actualización automática
        },
        updateTable() {
            // Crea nuevos datos de producto aleatorios
            const newProducts = [
                {
                    id: 21,
                    name: 'Coat',
                    seller: 'Fashion Co.',
                    price: '$89.99',
                    lastSold: '2023-04-20',
                    totalSold: 5,
                },
                {
                    id: 22,
                    name: 'Sweatshirt',
                    seller: 'Fashion Co.',
                    price: '$32.99',
                    lastSold: '2023-04-20',
                    totalSold: 10,
                },
                {
                    id: 23,
                    name: 'Boots',
                    seller: 'Footwear Co.',
                    price: '$69.99',
                    lastSold: '2023-04-20',
                    totalSold: 8,
                },
                {
                    id: 24,
                    name: 'Dress',
                    seller: 'Fashion Co.',
                    price: '$59.99',
                    lastSold: '2023-04-20',
                    totalSold: 15,
                },
                {
                    id: 25,
                    name: 'Pants',
                    seller: 'Denim Co.',
                    price: '$39.99',
                    lastSold: '2023-04-20',
                    totalSold: 20,
                },
                {
                    id: 26,
                    name: 'Jacket',
                    seller: 'Fashion Co.',
                    price: '$79.99',
                    lastSold: '2023-04-20',
                    totalSold: 5,
                },
                {
                    id: 27,
                    name: 'Sunglasses',
                    seller: 'Accessories Co.',
                    price: '$24.99',
                    lastSold: '2023-04-20',
                    totalSold: 10,
                },
                {
                    id: 28,
                    name: 'T-Shirt',
                    seller: 'Fashion Co.',
                    price: '$19.99',
                    lastSold: '2023-04-20',
                    totalSold: 25,
                },
                {
                    id: 29,
                    name: 'Sandals',
                    seller: 'Footwear Co.',
                    price: '$29.99',
                    lastSold: '2023-04-20',
                    totalSold: 12,
                },
                {
                    id: 30,
                    name: 'Sneakers',
                    seller: 'Footwear Co.',
                    price: '$49.99',
                    lastSold: '2023-04-20',
                    totalSold: 5,
                },
            ];

            // Actualiza los datos de la tabla con nuevos productos aleatorios
            for (let i = 0; i < newProducts.length; i++) {
                const index = Math.floor(Math.random() * this.products.length);
                const productToUpdate = this.products[index];
                for (const [key, value] of Object.entries(newProducts[i])) {
                    if (key === 'lastSold') {
                        productToUpdate[key] = this.formatDate(value);
                    } else {
                        productToUpdate[key] = value;
                    }
                }
            }
        },
        formatDate(dateString) {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('en-US', options);
        },
    },
}
</script>



<style>
.table-fixed {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

.table-fixed th,
.table-fixed td {
    padding: 0.5rem;
    text-align: left;
    border: 1px solid #ccc;
}

.table-fixed th {
    background-color: #f2f2f2;
}

.bg-gray-50 {
    background-color: #f2f2f2;
}

.text-center {
    text-align: center;
}

.title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

@media screen and (max-width: 640px) {

    .table-fixed th,
    .table-fixed td {
        padding: 0.25rem;
    }

    .text-xs {
        font-size: 0.75rem;
    }

    .text-lg {
        font-size: 1.25rem;
    }

    .py-2 {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
    }

    .px-2 {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }

    .overflow-x-auto {
        overflow-x: auto;
    }
}

/* Clases de utilidad */
.mx-auto {
    margin-left: auto;
    margin-right: auto;
}

.max-w-500 {
    max-width: 500px;
}

.px-4 {
    padding-left: 1rem;
    padding-right: 1rem;
}

.overflow-x-auto {
    overflow-x: auto;
}</style>
