<template>
  <div class="separator-triple-line">
    <div class="canvas-container">
      <svg viewBox="0 0 1920 250" xmlns="http://www.w3.org/2000/svg">
        <path d="M 1920 250 L 0 250 L 0 0 C 0 0 140.688 120.478 363.956 121.992 C 541.808 123.195
         783.006 24.64 973.681 35.749 C 1237.635 51.128 1299.819 73.888 1520.353 77.584 C 1740.88
          81.28 1785.829 16.176 1920 60.345" />
        <path d="M 1920 144 C 1920 144 1424.121 235.692 864.795 101.541 C 342.024 -23.843 0 45.578
         0 45.578 L 0 250 L 1920 250 L 1920 144 Z" />
        <path d="M0 195.553s208.547-75.581 701.325-20.768c376.707 41.908 520.834-67.962
        722.545-67.962 222.926 0 311.553 83.523 496.129 86.394V250H0v-54.447z"/>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SeparatorTripleLine',
  props: {},
};
</script>

<style scoped lang="scss">

.separator-triple-line {
  .canvas-container {
    position: absolute;
    bottom: 11em;
    left: 0;
    width: 100%;

    svg {
      path:nth-of-type(1) {
        fill: $nord4;
      }

      path:nth-of-type(2) {
        fill: $nord5;
      }

      path:nth-of-type(3) {
        fill: $nord6;
      }
    }
  }
}

@media (min-width: 56.25em) {
  .separator-triple-line {
    .canvas-container {
      bottom: 5em;
    }
  }
}

.#{$dark-mode-class} {
  .separator-triple-line {
    .canvas-container {
      svg {
        path:nth-of-type(1) {
          fill: $dark-bg-secondary;
        }

        path:nth-of-type(2) {
          fill: $nord2;
        }

        path:nth-of-type(3) {
          fill: $dark-bg-primary;
        }
      }
    }
  }
}

</style>
