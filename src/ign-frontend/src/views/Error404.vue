<template>
  <div class="documentation">
    <div class="container">
      <Main
        h1="404 Not found"
      />
      <center>Nothing to see here</center>
    </div>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';

export default {
  name: 'Error404',
  components: {
    Main,
  },
};
</script>
