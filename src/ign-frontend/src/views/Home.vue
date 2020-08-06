<template>
  <div class="home">
    <div class="container">
      <Main />
    </div>
    <SeparatorDoubleLine />
    <section class="demo-section">
      <Demo />
    </section>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';
import Demo from '@/components/Demo.vue';
import SeparatorDoubleLine from '@/components/separator/DoubleLine.vue';

export default {
  name: 'Home',
  components: {
    Main,
    Demo,
    SeparatorDoubleLine,
  },
};
</script>
<style scoped lang="scss">
.canvas-container {
  svg {
    margin-bottom: -5px;
    path:nth-of-type(1) {
      fill: $nord4;
    }
    path:nth-of-type(2) {
      fill: $nord5;
    }
  }
}

.demo-section {
  min-height: 500px;
  background: $nord5;
  margin-bottom: -13em;
  margin-top: -1.5em;
  padding: 5em 0;
}

.#{$dark-mode-class} {
  .demo-section {
    background: $nord2;
  }

  .canvas-container {
    svg {
      path:nth-of-type(1) {
        fill: $dark-bg-secondary;
      }
      path:nth-of-type(2) {
        fill: $nord2;
      }
    }
  }
}

</style>
