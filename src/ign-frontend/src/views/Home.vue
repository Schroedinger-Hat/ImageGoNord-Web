<template>
  <div class="home">
    <div class="container">
      <Main msg="Welcome to Your Vue.js App"/>
    </div>
    <Contributing />
  </div>
</template>

<script>
import Main from '@/components/Main.vue';
import Contributing from '@/components/Contributing.vue';

export default {
  name: 'Home',
  components: {
    Main,
    Contributing,
  },
};
</script>
