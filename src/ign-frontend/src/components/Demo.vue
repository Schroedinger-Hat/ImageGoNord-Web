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
  methods: {
    loadFile: (event) => {
      console.log(event);
      const canvas = document.getElementById('img-preview');
      const ctx = document.getElementById('img-preview').getContext('2d');
      const img = new Image();

      img.onload = () => {
        ctx.drawImage(img, 0, 0, img.width, img.height,
          0, 0, canvas.width, canvas.height);
      };

      img.src = URL.createObjectURL(event.target.files[0]);
    },
  },
});
</script>

<style scoped lang="scss">

.demo {
  padding: 8em 0;
}

</style>
