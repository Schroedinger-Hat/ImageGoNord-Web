<template>
  <footer>
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
    <div class="footer-container container">
      <div class="inner-footer-container">
        <div class="logo">
          <router-link to="/">
            <img alt="SH logo" width="36" src="../assets/logo-64.png">
            <span>S<i class="title-part-1">chrödinger</i> H<i class="title-part-2">at</i></span>
          </router-link>
        </div>
        <nav>
          <div class="navbar">
            <span>&copy;2020 Schrödinger Hat 2020</span>
          </div>
        </nav>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  props: {},
};
</script>

<!-- La navbar potrebbe essere un componente a sè, per maggior leggibilità -->
<!-- Il logo potrebbe essere un componente a sè -->
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
