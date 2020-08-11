<template>
  <div class="getting-started">
    <Main
        h1="Getting started"
        h2="You can download the tool or you can use our API"
        link1="/installation"
        link2="/documentation"
        btn1="Install locally"
        btn2="API Documentation"
      />
    <div class="canvas-container">
      <svg viewBox="0 -20 700 110" width="100%" height="110" preserveAspectRatio="none">
        <path transform="translate(0, -20)" d="M0,10 c80,-22 240,0 350,18 c90,17 260,7.5
        350,-20 v50 h-700" />
        <path d="M0,10 c80,-18 230,-12 350,7 c80,13 260,17 350,-5 v100 h-700z" />
      </svg>
    </div>
    <section class="demo-section">
      <Demo />
    </section>
  </div>
</template>
<script>
import Demo from '@/components/Demo.vue';
import Main from '@/components/Main.vue';

export default {
  name: 'GettingStarted',
  components: {
    Demo,
    Main,
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
