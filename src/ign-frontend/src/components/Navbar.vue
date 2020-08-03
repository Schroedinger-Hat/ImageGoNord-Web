<template>
  <header class="container">
    <div class="inner-header-container">
      <div class="logo">
        <router-link to="/">
          <img alt="SH logo" width="36" src="../assets/logo-64.png">
          <span>S<i class="title-part-1">chrödinger</i> H<i class="title-part-2">at</i></span>
        </router-link>
      </div>
      <nav>
        <div class="navbar">
          <a href="#try">Try it</a>
          <router-link to="/installation">Installation</router-link>
          <router-link to="/documentation">Documentation</router-link>
          <router-link to="/about">About</router-link>
          <a href="https://github.com/Schrodinger-Hat/ImageGoNord" target="_blank">GitHub</a>
          <a @click="toggleMobileMenu" href="#">
            <i class="mobile-menu-icon fas fa-hamburger"></i>
          </a>
          <a @click="toggleDarkMode" href="#">
            <i class="dark-mode-icon fas fa-moon"></i>
          </a>
        </div>
      </nav>
    </div>
    <MobileMenu />
  </header>
</template>

<script>
import Vue from 'vue';
import MobileMenu from '@/components/MobileMenu.vue';

export default Vue.component('Navbar', {
  props: {},
  components: {
    MobileMenu,
  },
  mounted() {
    if (localStorage.getItem('darkMode') === 'yes') {
      document.querySelector('.dark-mode-icon').parentNode.click();
    }
  },
  methods: {
    toggleMobileMenu: (event) => {
      event.preventDefault();
      document.querySelector('.mobile-menu-container').classList.toggle('loaded');
      document.body.classList.toggle('overflow-hidden');
    },
    toggleDarkMode: (event) => {
      event.preventDefault();
      document.body.parentNode.classList.toggle('dark-theme');
      let iconElement = event.target;
      iconElement = (iconElement.tagName === 'A') ? iconElement.children[0] : iconElement;

      let darkModeValue = 'yes';
      darkModeValue = (localStorage.getItem('darkMode') === 'yes' && iconElement.className.indexOf('fa-sun') !== -1) ? 'no' : 'yes';

      iconElement.classList.toggle('fa-moon');
      iconElement.classList.toggle('fa-sun');

      localStorage.setItem('darkMode', darkModeValue);
    },
  },
});
</script>

<!-- La navbar potrebbe essere un componente a sè, per maggior leggibilità -->
<!-- Il logo potrebbe essere un componente a sè -->
<style scoped lang="scss">

header {
  margin: auto;
  text-align: left;
  height: 5em;
  display: flex;
  padding: 0 !important;

  .inner-header-container {
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
        font-size: 1.8em;
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

          &:nth-child(-n+5) {
            display: none;
          }

          &:hover {
            background-color: $bg-secondary;
          }
        }
      }
    }
  }
}

@media (min-width: 56.25em) {
  header {
    .inner-header-container {
      padding: 0 0;

      .logo {
        span {
          font-size: 2em;
        }
      }

      nav {
        .navbar {
          a {
            &:nth-child(-n+5) {
              display: inline;
            }
            &:nth-child(6) {
              display: none;
            }
          }
        }
      }
    }
  }
}

.#{$dark-mode-class} {
  header {
    .inner-header-container {
      nav {
        .navbar {
          a {
            &:hover {
              background-color: $dark-bg-secondary;
            }
          }
        }
      }
    }
  }
}

</style>
