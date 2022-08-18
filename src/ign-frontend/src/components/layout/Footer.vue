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
            <span>&copy;{{ new Date().getFullYear() }} Schrödinger Hat</span>
          </div>
        </nav>
      </div>
    </div>
    <div id="open-modal" class="modal-window">
      <div>
        <a href="#" title="Close" @click="closeModal" class="modal-close">Close</a>
        <h3>Thank you for using our tool & service!</h3>
        <div>
          <small>Please, consider on support us via a donation on <a class="external-link-color" target="_blank" href="https://opencollective.com/schrodinger-hat">OpenCollective <i class='fas fa-external-link-alt '></i></a>
           or <a class="external-link-color" href='https://twitter.com/schrodinger_hat' target="_blank">reach us<i class='fas fa-external-link-alt '></i></a> in order to sponsor the project.
           <br /><br />Share the love & credits</small>
        </div>
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
  methods: {
    closeModal: (e) => {
      e.preventDefault();
      document.querySelector('.modal-window').classList.toggle('modal-window__active');
    },
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
  padding: 7em 0 0 0 !important;
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
      bottom: 8em;
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
