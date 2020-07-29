<template>
  <header>
    <div class="inner-header-container">
      <div class="logo">
        <a href="/">
          <img alt="SH logo" width="36" src="../assets/logo-64.png">
          <span>S<i class="title-part-1">chrödinger</i> H<i class="title-part-2">at</i></span>
        </a>
      </div>
      <nav>
        <div class="navbar">
          <a>Demo</a>
          <router-link to="/installation">Installation</router-link>
          <router-link to="/documentation">Documentation</router-link>
          <router-link to="/about">About</router-link>
          <a href="https://github.com/Schrodinger-Hat/ImageGoNord" target="_blank">GitHub</a>
          <a>
            <i class="dark-mode-icon fas fa-moon"></i>
          </a>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

a {
  text-decoration: none;
  color: inherit;
}

header {
  max-width: 75em;
  margin: auto;
  text-align: left;
  height: 80px;
  display: flex;

  .inner-header-container {
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
        font-weight: 500;
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

</style>
