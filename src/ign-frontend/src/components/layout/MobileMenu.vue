<template>
  <div class="mobile-menu-container">
    <nav>
      <div class="close-icon"><i @click="closeMobileMenu" class="fa fa-times"></i></div>
      <div class="navbar">
        <router-link to="/getting-started">Getting Started</router-link>
        <router-link to="/installation">Installation</router-link>
        <router-link to="/documentation">Documentation</router-link>
        <router-link to="/color-schemes">ImageGoWild</router-link>
        <router-link to="/wallpaper">Wallpaper</router-link>
        <router-link to="/about">About</router-link>
        <a href="https://github.com/Schrodinger-Hat/ImageGoNord" target="_blank">GitHub</a>
      </div>
    </nav>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.component('MobileMenu', {
  props: {},
  methods: {
    closeMobileMenu() {
      document.querySelector('.mobile-menu-icon.fa-hamburger').parentNode.click();
    },
  },
  watch: {
    $route() {
      if (document.querySelector('.mobile-menu-container.loaded') !== null) {
        document.querySelector('.mobile-menu-icon.fa-hamburger').parentNode.click();
      }
    },
  },
});
</script>

<style scoped lang="scss">

.mobile-menu-container {
  //display: none;
  position: fixed;
  width: 100%;
  bottom: 100%;
  opacity: 0;
  background: $bg-primary;
  z-index: 1;
  left: 0;
  height: 100%;
  transition: all .4s ease-in 0s;

  nav {
    .close-icon {
      text-align: right;
      i {
        padding: .8em;
        font-size: 1.4em;
      }
    }

    .navbar {
      text-align: center;
      a {
        padding: .8em 0;
        display: block;
        font-size: 1.3em;
        border-bottom: 1px solid $bg-secondary;

        &:last-child {
          border-bottom: none;
        }
      }
    }
  }
}

.loaded {
  &.mobile-menu-container {
    bottom: 0;
    opacity: 1;
    transition: bottom .25s ease-out 0s, opacity .3s ease-in-out 0s;
  }
}

.#{$dark-mode-class} {
  .mobile-menu-container {
    background: $dark-bg-primary;
  }
}

</style>
