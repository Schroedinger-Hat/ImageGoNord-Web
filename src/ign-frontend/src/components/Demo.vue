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
        <h3>Params</h3>
        <div class="palette">
          <div class="polar"></div>
          <div class="snow"></div>
          <div class="frost"></div>
          <div class="aurora"></div>
        </div>
        <div class="options">
          <div class="just-filter">
            <span>active just filter</span>
            <label class="switch">
              <input type="checkbox">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="blur">
            <span>blur</span>
            <label class="switch">
              <input type="checkbox">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="avg">
            <span>pixel avg</span>
            <input class="range-input" type="range" min="1" max="100" value="50">
          </div>
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
    console.log(this);
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
      width: 100%;
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
          position: absolute;
          left: 50%;
          margin-left: -4em;
          margin-top: 9em;
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
      width: 100%;
      padding: 0 1em;

      h3 {
        margin-top: .3em;
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
        }
      }
    }
  }
}
</style>
