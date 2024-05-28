<template>
  <div class="getting-started">
    <Main
        h1="Image Go AI 🤖"
        h2="Use the power of the PaletteNet to recolor your images"
      />
    <center>
      <a class="github-button" href="https://github.com/Schrodinger-Hat/ImageGoNord" data-color-scheme="no-preference: light; light: light; dark: dark;" data-size="large" data-show-count="true" aria-label="Star Schrodinger-Hat/ImageGoNord on GitHub">Star</a>
    </center>
    <div class="canvas-container">
      <svg viewBox="0 -20 700 110" width="100%" height="110" preserveAspectRatio="none">
        <path transform="translate(0, -20)" d="M0,10 c80,-22 240,0 350,18 c90,17 260,7.5
        350,-20 v50 h-700" />
        <path d="M0,10 c80,-18 230,-12 350,7 c80,13 260,17 350,-5 v100 h-700z" />
      </svg>
    </div>
    <section class="demo-section">
      <center>
        <h3>Select a palette & Upload your image</h3>
        <p>Look to your fav palette by using the browser search</p>
      </center>
      <div class="palette-grid container">
        <div @click="selectedPalette = palette.name" :class="{'palette-post': true, 'current-palette': (selectedPalette === palette.name)}" v-for="palette in availablePalettes" :key="palette.name">
          <div class="palette-img" :style="`background: linear-gradient(to right, ${palette.colors[0]} 16.65%, ${palette.colors[1]} 16.65% 33.3%, ${palette.colors[2]} 33.3% 49.95%, ${palette.colors[3]} 49.95% 66.55%, ${palette.colors[4]} 66.55% 83.2%, ${palette.colors[5]} 83.2%
          );`"/>
          <span class="palette-title">{{ palette.name }}</span>
        </div>
      </div>
      <Demo :isAi="true" :selectedPalette="`${(selectedPalette !== '') ? selectedPalette : []}`" />
    </section>
  </div>
</template>
<script>
import Demo from '@/components/Demo.vue';
import Main from '@/components/Main.vue';
import json from '../assets/palettes/ai-palettes/6x-palette.json';

export default {
  name: 'ImagIA',
  data() {
    return {
      availablePalettes: json,
      selectedPalette: '',
    };
  },
  components: {
    Demo,
    Main,
  },
};
</script>
<style scoped lang="scss">
.canvas-container {
  margin-top: 2em;
  svg {
    margin-bottom: -5px;
    path:nth-of-type(1) {
      fill: $nord4;
    }
    path:nth-of-type(2) {
      fill: $nord5;
    }
  }
}

.demo-section {
  min-height: 500px;
  background: $nord5;
  margin-bottom: -13em;
  margin-top: -1.5em;
  padding: 5em 0;

  h3 {
    font-size: 2em;
    margin: .3em 0;
  }

  p {
    margin: .3em 0;
  }

}

.#{$dark-mode-class} {
  .demo-section {
    background: $nord2;
  }

  .canvas-container {
    svg {
      path:nth-of-type(1) {
        fill: $dark-bg-secondary;
      }
      path:nth-of-type(2) {
        fill: $nord2;
      }
    }
  }
}

</style>
