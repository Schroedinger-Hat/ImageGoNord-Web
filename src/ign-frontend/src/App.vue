<template>
  <div id="app">
    <Navbar />
    <router-view />
    <Contributing />
    <Footer />
  </div>
</template>

<style lang="scss">
/* app */
</style>

<script>
import Navbar from '@/components/layout/Navbar.vue';
import Contributing from '@/components/Contributing.vue';
import Footer from '@/components/layout/Footer.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Contributing,
    Footer,
  },
};
</script>
