<template>
  <div class="separator-double-line">
    <div class="canvas-container">
      <svg viewBox="0 -20 700 110" width="100%" height="110" preserveAspectRatio="none">
        <path transform="translate(0, -20)" d="M0,10 c80,-22 240,0 350,18 c90,17 260,7.5
        350,-20 v50 h-700" />
        <path d="M0,10 c80,-18 230,-12 350,7 c80,13 260,17 350,-5 v100 h-700z" />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SeparatorDoubleLine',
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

.#{$dark-mode-class} {
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
