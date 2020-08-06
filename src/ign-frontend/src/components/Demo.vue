<template>
  <div class="demo container">
    <input type="file" accept="image/*" id="file" @change="loadFile" style="display:none;">
    <p><label for="file" style="cursor: pointer;">Upload Image</label></p>
    <canvas width="450" height="450" id="img-preview"></canvas>
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
      const [imgData] = event.target.files;
      const canvas = document.getElementById('img-preview');
      const ctx = document.getElementById('img-preview').getContext('2d');
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
  },
});
</script>

<style scoped lang="scss">

.demo {
  padding: 8em 0;

  #img-preview {
    max-width: 100%;
  }
}

</style>
