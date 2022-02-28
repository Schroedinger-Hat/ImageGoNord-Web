<template>
  <div id="app">
    <alert />
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
import Alert from './components/Alert.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Contributing,
    Footer,
    Alert,
  },
};
</script>
