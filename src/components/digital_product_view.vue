<template>
    <div class="container px-4 mx-auto">
      <div class="sm:flex sm:items-center sm:justify-between">
        <div>
          <div class="flex items-center gap-x-3">
            <h2 class="text-lg font-medium text-gray-800 dark:text-white">Customers</h2>
            <span class="px-3 py-1 text-xs text-blue-600 bg-blue-100 rounded-full dark:bg-gray-800 dark:text-blue-400">240 vendors</span>
          </div>
          <p class="mt-1 text-sm text-gray-500 dark:text-gray-300">These companies have purchased in the last 12 months.</p>
        </div>
  
        <div class="flex items-center mt-4 gap-x-3">
          <button class="flex items-center justify-center w-1/2 px-5 py-2 text-sm text-gray-700 transition-colors duration-200 bg-white border rounded-lg gap-x-2 sm:w-auto dark:hover:bg-gray-800 dark:bg-gray-900 hover:bg-gray-100 dark:text-gray-200 dark:border-gray-700">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g clip-path="url(#clip0_3098_154395)">
                <path d="M13.3333 13.3332L9.99997 9.9999M9.99997 9.9999L6.66663 13.3332M9.99997 9.9999V17.4999M16.9916 15.3249C17.8044 14.8818 18.4465 14.1806 18.8165 13.3321C19.1866 12.4835 19.2635 11.5359 19.0351 10.6388C18.8068 9.7417 18.2862 8.94616 17.5555 8.37778C16.8248 7.80939 15.9257 7.50052 15 7.4999H13.95C13.6977 6.52427 13.2276 5.61852 12.5749 4.85073C11.9222 4.08295 11.104 3.47311 10.1817 3.06708C9.25943 2.66104 8.25709 2.46937 7.25006 2.50647C6.24304 2.54358 5.25752 2.80849 4.36761 3.28129C3.47771 3.7541 2.70656 4.42249 2.11215 5.23622C1.51774 6.04996 1.11554 6.98785 0.935783 7.9794C0.756025 8.97095 0.803388 9.99035 1.07431 10.961C1.34523 11.9316 1.83267 12.8281 2.49997 13.5832" stroke="currentColor" stroke-width="1.67" stroke-linecap="round" stroke-linejoin="round"/>
              </g>
              <defs>
                <clipPath id="clip0_3098_154395">
                  <rect width="20" height="20" fill="white" transform="translate(0.666626 2.49988)"/>
                </clipPath>
              </defs>
            </svg>
            <span>Import</span>
          </button>
          <button class="flex items-center justify-center w-1/2 px-5 py-2 text-sm font-medium text-white transition-colors duration-200 bg-blue-600 border border-transparent rounded-lg gap-x-2 sm:w-auto hover:bg-blue-700">
            <svg width="20" height="20" fill="currentColor" class="w-4 h-4" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M12 4a8 8 0 100 16 8 8 0 000-16zm0 14a6 6 0 100-12 6 6 0 000 12zm0-5a3 3 0 110-6 3 3 0 010 6z" clip-rule="evenodd"></path>
            </svg>
            <span>Add Vendor</span>
          </button>
        </div>
      </div>
  
      <div class="mt-6">
        <div class="flex items-center gap-x-3">
          <button class="px-4 py-2 text-sm font-medium text-white transition-colors duration-200 bg-blue-600 border border-transparent rounded-lg hover:bg-blue-700">View all</button>
          <button class="px-4 py-2 text-sm font-medium text-gray-600 transition-colors duration-200 bg-white border border-transparent rounded-lg hover:bg-gray-100 dark:text-gray-400 dark:border-gray-700 dark:hover:bg-gray-800">Monitored</button>
          <button class="px-4 py-2 text-sm font-medium text-gray-600 transition-colors duration-200 bg-white border border-transparent rounded-lg hover:bg-gray-100 dark:text-gray-400 dark:border-gray-700 dark:hover:bg-gray-800">Unmonitored</button>
        </div>
      </div>
  
      <div class="mt-6">
        <div class="flex items-center gap-x-3">
          <div class="relative">
            <input type="text" class="block w-full px-4 py-2 pr-10 text-sm text-gray-700 placeholder-gray-400 bg-white border border-gray-300 rounded-lg dark:bg-gray-800 dark:text-gray-200 dark:border-gray-700 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring" placeholder="Search" />
            <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
              <svg width="20" height="20" fill="currentColor" class="w-4 h-4 text-gray-400" viewBox="0 0 20 20">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M9 17C12.8659 17 16 13.8659 16 10C16 6.13401 12.8659 3 9 3C5.13401 3 2 6.13401 2 10C2 13.8659 5.13401 17 9 17ZM9 15C11.7614 15 14 12.7614 14 10C14 7.23858 11.7614 5 9 5C6.23858 5 4 7.23858 4 10C4 12.7614 6.23858 15 9 15Z" />
                <path fill-rule="evenodd" clip-rule="evenodd" d="M9 19C13.4183 19 17 15.4183 17 11C17 6.58172 13.4183 3 9 3C4.58172 3 1 6.58172 1 11C1 15.4183 4.58172 19 9 19ZM9 21C14.5228 21 19 16.5228 19 11C19 5.47715 14.5228 1 9 1C3.47715 1 0 5.47715 0 11C0 16.5228 3.47715 21 9 21Z" />
              </svg>
            </div>
          </div>
          <div>
            <label for="status" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Status:</label>
            <select id="status" class="block w-full px-4 py-2 pr-8 text-sm text-gray-700 bg-white border border-gray-300 rounded-lg dark:bg-gray-800 dark:text-gray-200 dark:border-gray-700 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring">
              <option value="all">All</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>
          </div>
        </div>
      </div>
  
      <div class="mt-6">
        <div class="overflow-hidden border rounded-lg dark:border-gray-700">
          <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
            <thead class="bg-gray-50 dark:bg-gray-800">
              <tr>
                <th class="px-6 py-3 text-xs font-medium tracking-wider text-left text-gray-500 dark:text-gray-300 uppercase">Company</th>
                <th class="px-6 py-3 text-xs font-medium tracking-wider text-left text-gray-500 dark:text-gray-300 uppercase">Status</th>
                <th class="px-6 py-3 text-xs font-medium tracking-wider text-left text-gray-500 dark:text-gray-300 uppercase">Last Purchase</th>
                <th class="px-6 py-3"></th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200 dark:bg-gray-900 dark:divide-gray-700">
              <tr>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 w-10 h-10">
                      <img class="w-full h-full rounded-md" src="company1.png" alt="Company 1" />
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900 dark:text-white">Company 1</div>
                      <div class="text-sm text-gray-500 dark:text-gray-400">customer@example.com</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs text-green-800 bg-green-100 rounded-full dark:bg-green-800 dark:text-green-400">Active</span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-500 dark:text-gray-300">2022-05-12</td>
                <td class="px-6 py-4 text-sm font-medium text-right whitespace-nowrap">
                  <a href="#" class="text-blue-600 hover:text-blue-500">View</a>
                </td>
              </tr>
              <tr>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 w-10 h-10">
                      <img class="w-full h-full rounded-md" src="company2.png" alt="Company 2" />
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900 dark:text-white">Company 2</div>
                      <div class="text-sm text-gray-500 dark:text-gray-400">customer@example.com</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs text-red-800 bg-red-100 rounded-full dark:bg-red-800 dark:text-red-400">Inactive</span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-500 dark:text-gray-300">2022-03-28</td>
                <td class="px-6 py-4 text-sm font-medium text-right whitespace-nowrap">
                  <a href="#" class="text-blue-600 hover:text-blue-500">View</a>
                </td>
              </tr>
              <!-- More rows... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CustomerList',
  };
  </script>
  
  <style scoped>
  /* Tailwind CSS classes go here */
  </style>
  