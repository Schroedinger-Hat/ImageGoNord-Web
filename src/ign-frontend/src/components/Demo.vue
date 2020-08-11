<template>
  <div class="demo container">
    <div class="demo-wrapper">
      <div class="preview">
        <div class="preview-wrapper">
          <input type="file" accept="image/*" id="file" @change="loadFile" style="display:none;">
          <label for="file"></label>
          <canvas width="450" height="450" id="img-preview"></canvas>
        </div>
      </div>
      <div class="params">
        <h3>Palette</h3>
        <div class="palette">
          <span>Polar Night</span>
          <div class="polar">
            <span class="nord0"></span>
            <span class="nord1"></span>
            <span class="nord2"></span>
            <span class="nord3"></span>
          </div>
          <span>Snow Storm</span>
          <div class="snow">
            <span class="nord4"></span>
            <span class="nord5"></span>
            <span class="nord6"></span>
          </div>
          <span>Frost</span>
          <div class="frost">
            <span class="nord7"></span>
            <span class="nord8"></span>
            <span class="nord9"></span>
            <span class="nord10"></span>
          </div>
          <span>Aurora</span>
          <div class="aurora">
            <span class="nord11"></span>
            <span class="nord12"></span>
            <span class="nord13"></span>
            <span class="nord14"></span>
            <span class="nord15"></span>
          </div>
        </div>
        <h3>Params</h3>
        <div class="options">
          <div class="just-filter space-between">
            <span>
              Filtering<br/>
              <small>Change just the image palette</small>
            </span>
            <label class="switch">
              <input type="checkbox">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="blur space-between">
            <span>
              Blur<br/>
              <small>Apply a blur on output</small>
            </span>
            <label class="switch">
              <input type="checkbox">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="avg">
            <p>
              AVG pixel area<br/>
              <small>Enable avg algorithm</small>
            </p>
            <input class="range-input" type="range" step="1" min="-10" max="10" value="0">
          </div>
          <small>More info on
            <router-link class="external-link-color" to="/documentation"> documentation
            </router-link>
          </small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.component('Demo', {
  props: {},
  data() {
    return {
      img: null,
      imgData: null,
    };
  },
  methods: {
    loadFile(event) {
      const dropArea = document.querySelector('.preview-wrapper');
      dropArea.classList.add('uploaded');
      console.log(event.target.files);
      const [imgData] = event.target.files;
      const canvas = document.getElementById('img-preview');
      const ctx = document.getElementById('img-preview').getContext('2d');
      canvas.width = canvas.parentNode.offsetWidth * 0.8;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const img = new Image();

      img.onload = () => {
        const ratio = img.width / img.height;
        let newWidth = canvas.width;
        let newHeight = newWidth / ratio;
        if (newHeight > canvas.height) {
          newHeight = canvas.height;
          newWidth = newHeight * ratio;
        }
        this.img = img;
        this.imgData = imgData;
        ctx.drawImage(img, 0, 0, newWidth, newHeight);
      };

      img.src = URL.createObjectURL(event.target.files[0]);
    },
    preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
    },
    highlightDroparea() {
      const dropArea = document.querySelector('.preview-wrapper').parentNode;
      dropArea.classList.toggle('highlight');
    },
    unhighlightDroparea() {
      const dropArea = document.querySelector('.preview-wrapper').parentNode;
      dropArea.classList.toggle('highlight');
    },
    handleDroparea(e) {
      const dt = { target: e.dataTransfer };
      this.loadFile(dt);
    },
  },
  mounted() {
    const dropArea = document.querySelector('.preview-wrapper');

    dropArea.addEventListener('dragenter', this.preventDefaults);
    dropArea.addEventListener('dragover', this.preventDefaults);
    dropArea.addEventListener('dragleave', this.preventDefaults);
    dropArea.addEventListener('drop', this.preventDefaults);

    dropArea.addEventListener('dragenter', this.highlightDroparea);
    dropArea.addEventListener('dragover', this.highlightDroparea);

    dropArea.addEventListener('dragleave', this.unhighlightDroparea);
    dropArea.addEventListener('drop', this.unhighlightDroparea);

    dropArea.addEventListener('drop', this.handleDroparea);
  },
});
</script>

<style scoped lang="scss">

.demo {
  padding: 8em 0;

  .demo-wrapper {
    justify-items: center;
    margin-bottom: 5em;

    .preview {
      // width: 100%;
      padding: .8em;
      background: $bg-secondary;
      border-radius: .8em;

      &.highlight {
        background: $nord7;
      }

      .preview-wrapper {
        position: relative;
        background: $nord5;

        label {
          width: 100%;
          height: 100%;
          position: absolute;
          cursor: pointer;
        }

        &:before {
          content: 'Drop image here';
          font-size: 2em;
          color: #999;
          opacity: .7;
          position: absolute;
          left: 50%;
          margin-left: -4em;
          margin-top: 9rem;
        }

        &.uploaded:before {
          display: none;
        }

        #img-preview {
          width: 90%;
          max-height: 65vh;
        }
      }
    }

    .params {
      // width: 100%;
      padding: 0 1em;

      h3 {
        margin-top: 0;
        margin-bottom: .3em;
        font-size: 1.6em;

        &:nth-of-type(2) {
          margin-top: .5em;
        }
      }

      .palette {
        .polar, .snow, .frost, .aurora {
          span {
            width: 1.5em;
            height: 1.5em;
            display: inline-block;
            border: 1px solid #f2f2f2;
            margin: 0 .3em;

            &:first-child {
              margin-left: 0;
            }
          }
        }

        // TODO: map-values
        .nord0 {
          background: $nord0;
        }

        .nord1 {
          background: $nord1;
        }

        .nord2 {
          background: $nord2;
        }

        .nord3 {
          background: $nord3;
        }

        .nord4 {
          background: $nord4;
        }

        .nord5 {
          background: $nord5;
        }

        .nord6 {
          background: $nord6;
        }

        .nord7 {
          background: $nord7;
        }

        .nord8 {
          background: $nord8;
        }

        .nord9 {
          background: $nord9;
        }

        .nord10 {
          background: $nord10;
        }

        .nord11 {
          background: $nord11;
        }

        .nord12 {
          background: $nord12;
        }

        .nord13 {
          background: $nord13;
        }

        .nord14 {
          background: $nord14;
        }

        .nord15 {
          background: $nord15;
        }
      }

      .space-between {
        display: flex;
        padding: .6em 0;
        justify-content: space-between;
      }

      .avg {
        padding: .6em 0;
      }
    }
  }
}

@media (min-width: 56.25em) {
  .demo {
    .demo-wrapper {
      display: flex;
      .preview {
        width: 80%;
        padding: .8em;

        .preview-wrapper {
          &:before {
            margin-top: 8em;
          }
        }
      }

      .params {
        width: 20%;
      }
    }
  }
}

.#{$dark-mode-class} {
  .demo {
    .demo-wrapper {
      .preview {
        background: $dark-bg-secondary;
        .preview-wrapper {
          background: $nord2;

          &:before {
            color: $dark-text-primary;
          }
        }
      }
    }
  }
}
</style>
