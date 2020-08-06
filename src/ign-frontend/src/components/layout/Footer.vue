<template>
  <footer>
    <SeparatorTripleLine />
    <div class="footer-container container">
      <div class="inner-footer-container">
        <div class="logo">
          <router-link to="/">
            <img alt="SH logo" width="36" src="../../assets/logo-64.png">
            <span>S<i class="title-part-1">chrödinger</i> H<i class="title-part-2">at</i></span>
          </router-link>
        </div>
        <nav>
          <div class="navbar">
            <span>&copy;2020 Schrödinger Hat</span>
          </div>
        </nav>
      </div>
    </div>
  </footer>
</template>

<script>
import SeparatorTripleLine from '@/components/separator/TripleLine.vue';

export default {
  name: 'Footer',
  props: {},
  components: {
    SeparatorTripleLine,
  },
};
</script>

<style scoped lang="scss">

footer {
  position: relative;
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

.footer-container {
  margin: auto;
  padding: 8em 0 0 0 !important;
  text-align: left;
  height: 5em;
  display: flex;

  .inner-footer-container {
    width: 100%;
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: justify;
    justify-content: space-between;
    margin: 0px auto;
    padding: 0 .5em;

    .logo {
      display: flex;
      -webkit-box-align: center;
      align-items: center;

      span {
        display: none;
        font-size: 1.5em;
        font-weight: 600;
        margin-left: 0.3em;
        vertical-align: super;
        transition: opacity 200ms ease-in-out 0s;

        i {
          position: absolute;
          z-index: -1;
          opacity: 0;
          transition: all 300ms ease-in-out 0s;
        }

        .title-part-1 {
          margin-left: -90px;
        }

        .title-part-2 {
          margin-left: 90px;
        }

        &:hover {
          i {
            position: relative;
            z-index: 0;
            opacity: 1;
            font-style: normal;
            margin-left: 0;
            transition: all 300ms ease-in-out 0s;
          }
        }
      }
    }

    nav {
      display: flex;

      .navbar {
        list-style: none;
        -webkit-box-pack: justify;
        justify-content: space-between;

        a {
          border-radius: 0.25em;
          margin: 0 0.25em;
          padding: 0.2em 0.5em;
          transition: background-color 100ms ease-in-out 0s;
          cursor: pointer;
          font-size: 1.2em;

          &:hover {
            background-color: $bg-secondary;
          }
        }
      }
    }
  }
}

@media (min-width: 56.25em) {
  .footer-container {
    .inner-footer-container {
      .logo {
        span {
          display: inline;
          font-size: 2em;
        }
      }
    }
  }

  footer {
    .canvas-container {
      bottom: 5em;
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

      path:nth-of-type(3) {
        fill: $dark-bg-primary;
      }
    }
  }
}

</style>
