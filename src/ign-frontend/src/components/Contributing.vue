<template>
  <section class="contributing-container">
    <NyanCat />
    <SeparatorSingleLine />
    <div class="bg-secondary">
      <div class="container contributing-container-text">
        <div class="inner-text">
          <h4>Contributing</h4>
          <p>
            <b>ImageGoNord</b> is open source and
            <a
              class="external-link-color"
              href="https://github.com/Schroedinger-Hat/ImageGoNord-web"
              target="_blank"
              >hosted on GitHub</a
            >.
          </p>
          <a
            class="github-button"
            href="https://github.com/Schroedinger-Hat/ImageGoNord-web"
            data-color-scheme="no-preference: light; light: light; dark: dark;"
            data-size="large"
            data-show-count="true"
            aria-label="Star
                                                                                Schroedinger-Hat/ImageGoNord-web on GitHub"
            >Star</a
          >
          <p>
            If you find a bug or have an idea for a new feature, please
            <a
              class="external-link-color"
              target="_blank"
              href="https://github.com/Schroedinger-Hat/ImageGoNord-web/issues"
              >open an issue on GitHub</a
            >.
          </p>
          <p class="social">
            <a
              target="_blank"
              href="https://opencollective.com/schrodinger-hat"
            >
              <i class="fas fa-donate external-link-color"></i>
            </a>
            <a href="https://www.facebook.com/schrodingerhat" target="_blank">
              <i class="fab fa-facebook external-link-color"></i>
            </a>
            <a href="https://twitter.com/schrodinger_hat" target="_blank">
              <i class="fab fa-twitter external-link-color"></i>
            </a>
            <a
              href="https://www.linkedin.com/company/schroedinger-hat/"
              target="_blank"
            >
              <i class="fab fa-linkedin external-link-color"></i>
            </a>
            <a
              href="https://www.instagram.com/schrodinger_hat/"
              target="_blank"
            >
              <i class="fab fa-instagram external-link-color"></i>
            </a>
            <a
              href="https://www.youtube.com/channel/UC1QLLgrGrPmlaFhS0orykCA"
              target="_blank"
            >
              <i class="fab fa-youtube external-link-color"></i>
            </a>
            <a href="https://discord.gg/RTXr8A3eFn" target="_blank">
              <i class="fab fa-discord external-link-color"></i>
            </a>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import NyanCat from "@/components/NyanCat.vue";
import SeparatorSingleLine from "@/components/separator/SingleLine.vue";

export default {
  name: "Contributing",
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

  .social {
    a {
      padding: 0 0.5em;
      font-size: 1.2em;
    }
  }
}

.contributing-container-text {
  width: 100%;
  text-align: center;
  margin: 0px auto;

  .inner-text {
    padding: 0 0.5em;
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
