<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view />
    <NyanCat></NyanCat>
    <Footer></Footer>
  </div>
</template>

<style lang="scss">
/* app */
</style>

<script>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import NyanCat from '@/components/NyanCat.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
    NyanCat,
  },
};
</script>
