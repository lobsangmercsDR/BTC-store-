<template>
    <div class="container mx-auto">
        <h1 class="text-3xl font-bold mb-4">Valor en tiempo real del Bitcoin</h1>
        <div class="mb-4">{{ bitcoinValue }}</div>
        <h2 class="text-2xl font-bold mb-4">Gráfico de Blockchain</h2>
        <canvas id="chart"></canvas>
        <h2 class="text-2xl font-bold mb-4">Administrar carteras</h2>
        <form class="mb-4">
            <input type="text" placeholder="Buscar cartera" class="w-full p-2 border border-gray-300 rounded">
        </form>
        <table class="w-full border border-gray-300">
            <thead>
                <tr>
                    <th class="border border-gray-300 p-2">#</th>
                    <th class="border border-gray-300 p-2">Username</th>
                    <th class="border border-gray-300 p-2">Dirección de cartera</th>
                    <th class="border border-gray-300 p-2">Fecha de asignación</th>
                    <th class="border border-gray-300 p-2">Último movimiento</th>
                    <th class="border border-gray-300 p-2">Estado</th>
                    <th class="border border-gray-300 p-2">Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(cartera, index) in carteras" :key="cartera.id">
                    <td class="border border-gray-300 p-2">{{ index + 1 }}</td>
                    <td class="border border-gray-300 p-2">{{ cartera.username }}</td>
                    <td class="border border-gray-300 p-2">{{ cartera.direccion_de_cartera }}</td>
                    <td class="border border-gray-300 p-2">{{ cartera.fecha_de_asignacion }}</td>
                    <td class="border border-gray-300 p-2">{{ cartera.ultimo_movimiento }}</td>
                    <td class="border border-gray-300 p-2">{{ cartera.estado }}</td>
                    <td class="border border-gray-300 p-2">
                        <button @click="eliminarCartera(index)"
                            class="bg-red-500 text-white px-4 py-2 rounded">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>

    </div>
</template>
<script>

</script>
  