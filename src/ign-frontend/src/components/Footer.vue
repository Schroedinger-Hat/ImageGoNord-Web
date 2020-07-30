<template>
  <footer>
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
  max-width: 75em;
  margin: auto;
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

    .logo {
      display: flex;
      -webkit-box-align: center;
      align-items: center;

      span {
        font-size: 2em;
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
