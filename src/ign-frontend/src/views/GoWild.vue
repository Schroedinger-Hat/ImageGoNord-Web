<template>
  <div class="gowild">
    <div class="container">
      <Main
        h1="Image Go Wild - Convert anything in the most popular palettes"
        h2="Transform each wallpaper, icon, image into your fav palette over the internet"
      />
    </div>
    <SeparatorDoubleLine />
    <section class="slider-section">
      <center class="container">
        <h3>We want to make your favorite image your personal wallpaper in you favorite color scheme as easy as uploading an image</h3>
      </center>
      <div class="container">
        <div class="slider-item">
          <ImgCompare
            className="demo-gruvbox"
            :after="imgCompareGruvbox.after"
            :width="500"
            :height="320"
            :before="imgCompareGruvbox.before"
          />
          <div class="slider-text">
            <h3>Customize your profile picture using your palette</h3>
            <p>
              Everyone needs a profile picture.<br/>
              You can convert fully in your palette color
            </p>
          </div>
        </div>
      </div>
      <SeparatorDoubleLine />
      <div class="container">
        <div class="slider-item">
          <div class="slider-text">
            <h3>Set your favorites wallpaper in a color scheme environment</h3>
            <p>Forget the endless search to find a color sceme wallpaper.<br/>
              Convert your favorite wallpapers into a color scheme instead</p>
          </div>
          <ImgCompare
            className="demo-vap"
            :after="imgCompareFlyVap.after"
            :before="imgCompareFlyVap.before"
            :width="500"
            :height="320"
          />
        </div>
      </div>
    </section>
    <section class="gallery-section">
      <SeparatorDoubleLine />
      <center>
        <h3>Available Palettes</h3>
        <p>
          Here are the available palette collected from the top usage.<br/>
          You are not finding your fav palette? Reach us on our social!
        </p>
      </center>
      <div class="palette-grid container">
        <div @click="selectedPalette = palette.file" :class="{'palette-post': true, 'current-palette': (selectedPalette === palette.file)}" v-for="palette in palettes" :key="palette.name">
          <div class="palette-img" :style="`background-image: url(${require('../assets/' + palette.img)})`"/>
          <span class="palette-title">{{ palette.name }}</span>
        </div>
      </div>
      <br/>
      <SeparatorDoubleLine />
    </section>
    <section class="demo-section">
      <center>
        <h3>Try it yourself</h3>
        <p>Upload a picture and test it out</p>
        <div class="relative">
          <span><b>API Status</b>:</span>
          <div :class="`ring-container ${apiStatus}`">
              <div class="ringring"></div>
              <div class="circle"></div>
          </div>
        </div>
      </center>
      <Demo :selectedPalette="`${(selectedPalette !== '') ? selectedPalette : []}`" />
    </section>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';
import Demo from '@/components/Demo.vue';
import SeparatorDoubleLine from '@/components/separator/DoubleLine.vue';
import ImgCompare from '@/components/ImgCompare.vue';
import json from '../assets/palettes/available-palettes.json';

export default {
  name: 'GoWild',
  data() {
    return {
      apiStatus: 'success',
      palettes: json,
      selectedPalette: '',
      imgCompareFlyVap: {
        after: 'demo/fly-vaporwave.png',
        before: 'demo/fly-before.jpg',
      },
      imgCompareGruvbox: {
        after: 'demo/fly-gruvbox.png',
        before: 'demo/fly-before.jpg',
      },
    };
  },
  mounted() {
    const self = this;
    setInterval(() => {
      fetch('https://ign-api.schrodinger-hat.it/v1/status')
        .then(() => { self.apiStatus = 'success'; })
        .catch(() => { self.apiStatus = 'failed'; });
    }, 8000);
  },
  components: {
    Main,
    Demo,
    SeparatorDoubleLine,
    ImgCompare,
  },
};
</script>
<style scoped lang="scss">
.canvas-container {
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

.slider-section {
  background: $nord5;
  padding: 3em .3em;

  h3 {
    font-weight: bold;
    font-size: 2em;
  }

  .slider-item {
    text-align: center;
    .slider-text {
      padding: 0 .5em;
    }

    p {
      margin: .8em 0;
      font-size: 1.3em;
    }

    h3 {
      font-size: 1.6em;
      margin: .3em 0;
    }
  }
}

.gallery-section {
  background: $nord5;

  h3 {
    font-size: 2em;
    margin: .3em 0;
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

  .separator-double-line {
    margin-bottom: -3em;
  }
  .ring-container {
    display: inline-block;
    position: relative;
    top: -35px;
    left: -10px;
  }

  .circle {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    position: absolute;
    top: 23px;
    left: 23px;
  }

  .ringring {
    -webkit-border-radius: 30px;
    height: 25px;
    width: 25px;
    position: absolute;
    left: 15px;
    top: 15px;
    -webkit-animation: pulsate 1s ease-out;
    -webkit-animation-iteration-count: infinite;
    opacity: 0.0;
  }

  .ring-container.success {
    .circle {
      background-color: #62bd19;
    }
    .ringring {
      border: 3px solid #62bd19;
    }
  }

  .ring-container.failed {
    .circle {
      background-color: #bd3219;
    }
    .ringring {
      border: 3px solid #bd3219;
    }
  }
}

.palette-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-gap: 1em;
  box-sizing: border-box;
  padding: 0 1em;

  .palette-post {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    border: 8px solid transparent;
    cursor: pointer;
    &:hover, &:focus, &:active, &.current-palette {
      border-color: $nord12;
      .palette-img {
        filter: brightness(0.6) blur(0);
      }
    }

    .palette-title {
      font-size: 25px;
      text-align: center;
      font-weight: bold;
      color: $nord4;
      position: absolute;
    }

    .palette-img {
      width: 100%;
      aspect-ratio: 4/3;
      object-fit: cover;
      background-size: cover;
      filter: brightness(0.3) blur(2px);
      overflow: hidden;
    }

  }
}

@media (min-width: 56.25em) {
  .slider-section {
    .slider-item {
      text-align: left;
      display: flex;
      justify-content: space-between;
      align-items: center;

      &:last-child {
        margin-top: 4em;
      }
    }
  }
}

.#{$dark-mode-class} {
  .demo-section, .slider-section, .gallery-section {
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

@-webkit-keyframes pulsate {
  0% {-webkit-transform: scale(0.1, 0.1); opacity: 0.0;}
  50% {opacity: 1.0;}
  100% {-webkit-transform: scale(1.1, 1.1); opacity: 0.0;}
}

</style>
