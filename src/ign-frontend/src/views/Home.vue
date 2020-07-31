<template>
  <div class="home">
    <div class="container">
      <img alt="SH logo" src="../assets/logo.png">
      <HelloWorld msg="Welcome to Your Vue.js App"/>
    </div>
    <Contributing />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import Contributing from '@/components/Contributing.vue';

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Contributing,
  },
};
</script>
