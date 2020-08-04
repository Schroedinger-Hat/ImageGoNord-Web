<template>
  <section class="contributing-container">
    <NyanCat />
    <div class="background-svg">
      <svg viewBox="0 0 2000 242" xmlns="http://www.w3.org/2000/svg">
        <path class="single-line" d="M 2001.456 168.668 C 1770.825 242.097 1418.009 208.72 1245.935
        205.417 C 952.501 199.785 810.181 145.365 345.281 86.887 C 181.207 66.249 125.825 82.728 0
        129.035 L 0 242 L 2000 242 L 2001.456 168.668 Z"/>
      </svg>
    </div>
    <div class="bg-secondary">
      <div class="container contributing-container-text">
        <div class="inner-text">
          <h4>Contributing</h4>
          <p><b>ImageGoNord</b> is open source and <a class="external-link-color" href="https://github.com/Schrodinger-Hat/ImageGoNord" target="_blank">hosted on GitHub</a>.</p>
          <a class="github-button" href="https://github.com/Schrodinger-Hat/ImageGoNord" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" data-show-count="true" aria-label="Star Schrodinger-Hat/ImageGoNord on GitHub">Star</a>
          <p>If you find a bug or have an idea for a new feature, please <a class="external-link-color" target="_blank" href="https://github.com/Schrodinger-Hat/ImageGoNord/issues">open an issue on GitHub</a>.</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import NyanCat from '@/components/NyanCat.vue';

export default {
  name: 'Contributing',
  props: {},
  components: {
    NyanCat,
  },
};
</script>

<!-- da rifare -->
<style scoped lang="scss">

.contributing-container {
  position: relative;

  .background-svg {
    width: 100%;
    margin-bottom: -15px;

    .single-line {
      fill: $bg-secondary;
    }
  }

  .bg-secondary {
    background-color: $bg-secondary;
    padding: 2em 0 0 0;
  }
}

.contributing-container-text {
  width: 100%;
  text-align: center;
  margin: 0px auto;

  .inner-text {
    padding: 0 .5em;
    h4 {
      font-size: 2.2em;
      margin: 0 0;
    }
  }
}

@media (min-width: 56.25em) {
  .contributing-container {
    .background-svg {
      margin-bottom: -5px;
    }

    .bg-secondary {
      padding: 2em 0 12em 0;
    }
  }
}

.#{$dark-mode-class} {
  .contributing-container {
    .background-svg {
      margin-bottom: -5px;
      .single-line {
        fill: $dark-bg-secondary;
      }
    }

    .bg-secondary {
      background-color: $dark-bg-secondary;
    }
  }
}

</style>
