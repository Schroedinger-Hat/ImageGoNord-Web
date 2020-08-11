<template>
  <div class="installation">
    <div class="container">
      <Main
        h1="Installation"
        h2="Select your operating system"
      />
      <center>
        <div class="installation-tab linux">
          <div class="icon"><i class="fab fa-linux"></i></div>
          <div>
            <a class="btn btn-primary" @click="chooseOS" href="#linux">
              Install on Linux
            </a>
          </div>
        </div>
        <div class="installation-tab windows">
          <div class="icon"><i class="fab fa-windows"></i></div>
          <div>
            <a class="btn btn-primary" @click="chooseOS" href="#windows">
              Install on Windows
            </a>
          </div>
        </div>
        <div class="installation-tab macos">
          <div class="icon">
            <i class="fab fa-apple"></i>
          </div>
          <div>
            <a class="btn btn-primary" @click="chooseOS" href="#macos">
              Install on macOS
            </a>
          </div>
        </div>
      </center>
      <section class="installation-guides">
        <div class="guide linux">
          <h3>Install on Linux</h3>
        </div>
        <div class="guide windows">
          <h3>Install on Windows</h3>
        </div>
        <div class="guide macos">
          <h3>Install on macOS</h3>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';

export default {
  name: 'Installtion',
  components: {
    Main,
  },
  methods: {
    chooseOS(e) {
      e.preventDefault();
      const os = e.target.getAttribute('href').substr(1);
      const guides = document.querySelectorAll('.guide');
      for (let i = 0; i < guides.length; i += 1) {
        guides[i].style.display = 'none';
        if (guides[i].className.indexOf(os) !== -1) {
          guides[i].style.display = 'block';
        }
      }
    },
  },
};
</script>
<style scoped lang="scss">
.installation {
  center {
    .icon {
      margin-bottom: 1em;
      i {
        font-size: 5em;
        color: $text-primary;
      }
    }
    .installation-tab {
      margin-bottom: 1em;
    }
  }
  .installation-guides {
    padding: .8em;
    margin-top: 3em;
    background: $bg-secondary;
    &:before {
      content: 'Select an OS, instructions will show up here';
      color: $text-primary;
      padding: .3em 0;
    }
    .guide {
      display: none;
      background: $nord5;
      padding: .8em;
    }
  }
}

@media (min-width: 56.25em) {
  .installation {
    center {
      display: flex;
      justify-content: center;

      .icon {
        margin-bottom: 1em;
        i {
          font-size: 5em;
          color: $text-primary;
        }
      }

      .installation-tab {
        padding: 0 1em;
      }
    }
    .installation-guides {
      max-width: 860px;
      margin: auto;
      margin-top: 3em;

      .guide {
        background: $nord5;
        padding: .8em;
      }
    }
  }
}

.#{$dark-mode-class} {
  .installation {
    center {
      .icon {
        i {
          color: $dark-text-primary;
        }
      }
    }
    .installation-guides {
      background: $dark-bg-secondary;
      &:before {
        color: $dark-text-primary;
      }

      .guide {
        background: $dark-bg-primary;
      }
    }
  }
}
</style>
