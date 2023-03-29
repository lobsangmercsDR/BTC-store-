<template>
    <header class="bg-gray-800 text-white">
      <div class="container mx-auto flex items-center justify-between py-4">
        <div class="flex items-center">
          <h1 class="ml-2 font-bold text-xl">My Store</h1>
        </div>
        <div class="flex-grow">
          <form class="relative">
            <input type="text" class="bg-gray-700 text-white rounded-full py-2 px-4 w-full" placeholder="Search...">
            <button type="submit" class="absolute right-0 top-0 mt-2 mr-4">
              <svg class="text-gray-400 h-4 w-4 fill-current" viewBox="0 0 20 20">
                <path
                  d="M14.65,12.35c-1.15,1.52-3.08,2.44-5.15,2.44c-3.26,0-5.91-2.65-5.91-5.91s2.65-5.91,5.91-5.91
                  s5.91,2.65,5.91,5.91C15.06,9.27,14.92,10.74,14.65,12.35z M11.5,5.5c-2.21,0-4,1.79-4,4s1.79,4,4,4s4-1.79,4-4S13.71,5.5,11.5,5.5z">
                </path>
              </svg>
            </button>
          </form>
        </div>
        <div>
          <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full">
            Cart (0)
          </button>
        </div>
      </div>
    </header>
  </template>
  