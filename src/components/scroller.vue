<template>
    <section v-if="orderType == 'virtual' && isOrderSectionOpen(orderType)" class="nav-arrows">
        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,-1)" :style="{color:previousArrowColor}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M15 18l-6-6 6-6"/>
        </svg> 
        <div  class="pageCounter"> <span>{{ pageInfoD.actualPage }}</span></div>

        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,1)" :style="{color:nextArrowColor}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 18l6-6-6-6"/>
        </svg>
</section>

<section v-if="orderType == 'physical' && isOrderSectionOpen(orderType)" class="nav-arrows">
        
        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,-1)" :style="{color:previousArrowColorF}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M15 18l-6-6 6-6"/>
        </svg> 
        <div  class="pageCounter"> <span>{{pageInfo.actualPage}}</span></div>

        <svg xmlns="http://www.w3.org/2000/svg" @click="handleChangePage(orderType,1)" :style="{color:nextArrowColorF}" class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 18l6-6-6-6"/>
        </svg>
</section>
      </div>
</template>