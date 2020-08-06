<template>
  <section class="contributing-container">
    <NyanCat />
    <SeparatorSingleLine />
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
import SeparatorSingleLine from '@/components/separator/SingleLine.vue';

export default {
  name: 'Contributing',
  props: {},
  components: {
    NyanCat,
    SeparatorSingleLine,
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
