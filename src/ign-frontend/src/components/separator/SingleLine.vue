<template>
  <div class="separator-single-line">
    <div class="background-svg">
      <svg viewBox="0 0 2000 242" xmlns="http://www.w3.org/2000/svg">
        <path class="single-line" d="M 2001.456 168.668 C 1770.825 242.097 1418.009 208.72 1245.935
        205.417 C 952.501 199.785 810.181 145.365 345.281 86.887 C 181.207 66.249 125.825 82.728 0
        129.035 L 0 242 L 2000 242 L 2001.456 168.668 Z"/>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SeparatorSingleLine',
  props: {},
};
</script>

<!-- da rifare -->
<style scoped lang="scss">

.separator-single-line {
  .background-svg {
    width: 100%;
    margin-bottom: -15px;

    .single-line {
      fill: $bg-secondary;
    }
  }
}

@media (min-width: 56.25em) {
  .separator-single-line {
    .background-svg {
      margin-bottom: -5px;
    }
  }
}

.#{$dark-mode-class} {
  .separator-single-line {
    .background-svg {
      margin-bottom: -5px;
      .single-line {
        fill: $dark-bg-secondary;
      }
    }
  }
}

</style>
