<template>
  <div class="demo container">
    <div class="demo-wrapper">
      <div class="preview">
        <div class="preview-wrapper">
          <Loader />
          <input type="file" accept="image/*, video/*" id="file" @change="loadFile" style="display:none;">
          <label for="file"></label>
          <canvas width="450" height="450" id="img-preview"></canvas>
        </div>
      </div>
      <div class="params">
        <h3>Palette</h3>
        <div class="palette" v-if="palette !== ''">
          <span>{{ palette.name }}</span>
          <span v-for="color in palette.colors" :key="color" :data-hex="color" class="highlighted color-element nord0"></span>
        </div>
        <div class="palette" v-if="palette === ''">
          <span>Polar Night</span>
          <div class="polar">
            <span data-hex="#2e3440" class="highlighted color-element nord0"></span>
            <span data-hex="#3b4252" class="highlighted color-element nord1"></span>
            <span data-hex="#434c5e" class="highlighted color-element nord2"></span>
            <span data-hex="#4c566a" class="highlighted color-element nord3"></span>
          </div>
          <span>Snow Storm</span>
          <div class="snow">
            <span data-hex="#d8dee9" class="highlighted color-element nord4"></span>
            <span data-hex="#e5e9f0" class="highlighted color-element nord5"></span>
            <span data-hex="#eceff4" class="highlighted color-element nord6"></span>
          </div>
          <span>Frost</span>
          <div class="frost">
            <span data-hex="#8fbcbb" class="highlighted color-element nord7"></span>
            <span data-hex="#88c0d0" class="highlighted color-element nord8"></span>
            <span data-hex="#81a1c1" class="highlighted color-element nord9"></span>
            <span data-hex="#5e81ac" class="highlighted color-element nord10"></span>
          </div>
          <span>Aurora</span>
          <div class="aurora">
            <span data-hex="#bf616a" class="highlighted color-element nord11"></span>
            <span data-hex="#d08770" class="highlighted color-element nord12"></span>
            <span data-hex="#ebcb8b" class="highlighted color-element nord13"></span>
            <span data-hex="#a3be8c" class="highlighted color-element nord14"></span>
            <span data-hex="#b48ead" class="highlighted color-element nord15"></span>
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
              <input type="checkbox" v-model="is_filter" :checked="is_filter === true">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="blur space-between">
            <span>
              Blur<br/>
              <small>Apply a blur on output</small>
            </span>
            <label class="switch">
              <input type="checkbox" v-model="blur" :checked="blur === true">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="ai space-between">
            <span>
              AI<br/>
              <small>Use AI on output</small>
            </span>
            <label class="switch">
              <input type="checkbox" v-model="ai" :checked="ai === true">
              <span class="slider round"></span>
            </label>
          </div>
          <div class="avg" v-if="!ai">
            <p>
              AVG pixel area<br/>
              <small>Enable avg algorithm</small>
            </p>
            <input class="range-input" v-model="avg_index" :disabled="is_filter === true"
              type="range" step="1" min="-5" max="5" value="0"
            >
          </div>
          <div class="process-image">
            <span @click="processImage" class="btn btn-primary">Process</span>
          </div>
          <div class="download-image">
            <span class="btn btn-primary">Download</span>
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
import Loader from './Loader.vue';
import CookieManager from '../utility/CookieManager';

export default Vue.component('Demo', {
  props: {
    selectedPalette: String,
    isAi: Boolean,
  },
  components: {
    Loader,
  },
  data() {
    return {
      apiUrl: 'https://ign-api.schrodinger-hat.it/v1',
      img: null,
      imgData: null,
      selectedColor: [],
      blur: false,
      ai: this.isAi || false,
      is_filter: false,
      avg_index: 0,
      palette: '',
    };
  },
  watch: {
    selectedPalette(file) {
      try {
        // eslint-disable-next-line
        this.palette = require(`../assets/${file}`);
      } catch (e) {
        // eslint-disable-next-line
        this.palette = require('../assets/palettes/ai-palettes/6x-palette.json').find((p) => p.name === file);
      }
    },
    palette(p) {
      this.selectedColor = p?.colors;
    },
  },
  methods: {
    loadFile(event) {
      const dropArea = document.querySelector('.preview-wrapper');
      dropArea.classList.add('uploaded');

      const [imgData] = event.target.files;
      this.imgData = imgData;
      this.isVideo = true;

      if (event.target.files[0].type.indexOf('video') === -1) {
        this.isVideo = false;
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
      }
    },
    processImage(e) {
      e.preventDefault();
      const self = this;

      document.querySelector('.preview').classList.toggle('processing');

      if (this.imgData === null) {
        return false;
      }

      // eslint-disable-next-line prefer-destructuring
      const img = this.img;
      const endpoint = (this.is_filter === true) ? 'quantize' : 'convert-async';
      const avgW = -1;
      const avgH = 1;

      const formData = new FormData();
      formData.append('file', this.imgData);
      formData.append('b64_output', true);
      formData.append('palette_name', this.palette.name);
      formData.append('colors', this.selectedColor.filter((c) => c).join(','));

      if (this.avg_index !== 0) {
        formData.append('is_avg', true);

        formData.append('avg_box_width', avgW - parseInt(Math.abs(this.avg_index), 10));
        formData.append('avg_box_height', avgH + parseInt(Math.abs(this.avg_index), 10));
      }

      if (this.blur === true) {
        formData.append('blur', this.blur);
      }

      if (this.ai === true) {
        formData.append('is_ai', this.ai);
      }

      fetch(`${this.apiUrl}/${endpoint}`, {
        method: 'POST',
        body: formData,
      }).then((response) => {
        if (endpoint === 'quantize') {
          response.json().then((j) => {
            self.showResponseImage(img, j);
          });
          return true;
        }

        response.text().then((jobId) => {
          self.pollingAPI(jobId, img);
        });
        return true;
      }).catch(() => {
        document.querySelector('.preview').classList.toggle('processing');
      });

      return true;
    },
    pollingAPI(jobId, img) {
      const self = this;
      fetch(`${this.apiUrl}/get-job?job_id=${jobId}`)
        .then((r) => {
          const rClone = r.clone();
          r.json().then((jsonResponse) => {
            if (jsonResponse.status === 'finished') {
              self.showResponseImage(img, jsonResponse.result);
            } else if (jsonResponse.status === 'queued' || jsonResponse.status === 'started') {
              setTimeout(() => {
                self.pollingAPI(jobId);
              }, 8000);
            } else {
              document.querySelector('.preview').classList.toggle('processing');
              console.info('Something went wrong, please retry or write to us!');
            }
          }).catch(() => {
            if (self.isVideo) {
              rClone.blob().then((blob) => {
                const newBlob = new Blob([blob]);
                const blobUrl = window.URL.createObjectURL(newBlob);
                const link = document.createElement('a');
                link.href = blobUrl;
                link.setAttribute('download', 'converted-video.mp4');
                document.body.appendChild(link);
                link.click();
                link.parentNode.removeChild(link);

                window.URL.revokeObjectURL(blobUrl);
              });
            }
          });
        });
    },
    showResponseImage(img, r) {
      const self = this;
      const im = new Image();
      im.onload = () => {
        const conversionCount = CookieManager.getCookie('conversion-counter') || 0;
        CookieManager.setCookie('conversion-counter', parseInt(conversionCount, 10) + 1);
        window.gtag('event', 'converted-image', {
          event_category: 'converted-image',
          event_label: (this.palette.name || 'Nordtheme'),
          value: (this.palette.name || 'Nordtheme'),
        });
        document.querySelector('.preview').classList.toggle('processing');

        if (conversionCount === 0 || conversionCount % 3 === 0) {
          document.querySelector('.modal-window').classList.toggle('modal-window__active');
        }

        const canvas = document.getElementById('img-preview');
        const ctx = document.getElementById('img-preview').getContext('2d');
        const ratio = self.img.width / self.img.height;
        let newWidth = canvas.width;
        let newHeight = newWidth / ratio;
        if (newHeight > canvas.height) {
          newHeight = canvas.height;
          newWidth = newHeight * ratio;
        }
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(im, 0, 0, newWidth, newHeight);
      };
      im.src = `data:image/png;base64, ${r.b64_img}`;
      const responseImageBlob = this.b64ToBlob(r.b64_img);
      const responseImageUrl = URL.createObjectURL(responseImageBlob);
      const downloadBtn = document.querySelector('.download-image .btn');
      downloadBtn.parentNode.style.display = 'block';
      downloadBtn.setAttribute('onclick', `window.open('${responseImageUrl}', '_blank')`);
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
    toggleSelectedColors(e) {
      e.preventDefault();
      e.target.classList.toggle('highlighted');
      delete this.selectedColor[this.selectedColor.indexOf(e.target.getAttribute('data-hex'))];
    },
    b64ToBlob(b64Data, contentType = 'image/png', sliceSize = 512) {
      const byteCharacters = atob(b64Data);
      const byteArrays = [];

      for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
        const slice = byteCharacters.slice(offset, offset + sliceSize);

        const byteNumbers = new Array(slice.length);
        for (let i = 0; i < slice.length; i += 1) {
          byteNumbers[i] = slice.charCodeAt(i);
        }

        const byteArray = new Uint8Array(byteNumbers);
        byteArrays.push(byteArray);
      }

      const blob = new Blob(byteArrays, { type: contentType });
      return blob;
    },
  },
  mounted() {
    // eslint-disable-next-line
    this.$nextTick(function () {
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

      const colorElements = document.querySelectorAll('.color-element');
      for (let i = 0; i < colorElements.length; i += 1) {
        this.selectedColor.push(colorElements[i].getAttribute('data-hex'));
        colorElements[i].addEventListener('click', this.toggleSelectedColors);
      }
    });
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
      position: relative;
      padding: .8em;
      background: $bg-secondary;
      border-radius: .8em;

      &.highlight {
        background: $nord7;
      }

      &.processing {
        &:before {
          content: " ";
          position: absolute;
          top: 0;
          left: 0;
          display: block;
          width: 100%;
          height: 100%;
          background: #e5e9f087;
          z-index: 1;
        }
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

      .download-image {
        display: none;
      }

      .process-image, .download-image {
        margin-top: .5em;

        .btn {
          text-align: center;
          margin: auto;
          display: block;
        }
      }

      .palette {
        .polar, .snow, .frost, .aurora {
          span {
            width: 1.5em;
            height: 1.5em;
            display: inline-block;
            border: 2px solid #f2f2f2;
            cursor: pointer;
            margin: 0 .3em;

            &:first-child {
              margin-left: 0;
            }

            &:hover {
              border: 2px solid $nord13;
            }

            &.highlighted {
              border: 2px solid $nord13;

              &:hover {
                border-color: #f2f2f2;
              }
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
      align-items: center;
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
