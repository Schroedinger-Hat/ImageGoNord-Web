<template>
  <div class="home">
    <div class="container">
      <Main
        h1="A tool to bring any image to the nord palette"
        h2="Transform each wallpaper, icon, image into the smoothest palette on the internet"
        link1="/getting-started"
        link2="/documentation"
        btn1="Getting Started"
        btn2="Documentation"
      />
    </div>
    <SeparatorDoubleLine />
    <section class="slider-section">
      <center>
        <h3>Nordify every image</h3>
      </center>
      <div class="container">
        <div class="slider-item">
          <ImgCompare
            className="wabri"
            :after="imgCompareWabri.after"
            :width="350"
            :height="350"
            :before="imgCompareWabri.before"
          />
          <div class="slider-text">
            <h3>Customize your profile picture using nordtheme's palette</h3>
            <p>
              Everyone needs a profile picture.<br/>
              You can apply a filter on your profile picture or you can convert fully in nordtheme.
            </p>
          </div>
        </div>
      </div>
      <SeparatorDoubleLine />
      <div class="container">
        <div class="slider-item">
          <div class="slider-text">
            <h3>Set your favorites wallpaper in a nordtheme environment</h3>
            <p>Forget the endless search to find a nord wallpaper.<br/>
              Convert your favorite wallpapers to nordtheme</p>
          </div>
          <ImgCompare
            className="car"
            :after="imgCompareCar.after"
            :before="imgCompareCar.before"
            :width="500"
            :height="350"
          />
        </div>
      </div>
    </section>
    <section class="demo-section">
      <!-- <SeparatorDoubleLine /> -->
      <center>
        <h3>Try it yourself</h3>
        <p>Upload a picture and test it out</p>
      </center>
      <Demo />
    </section>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';
import Demo from '@/components/Demo.vue';
import SeparatorDoubleLine from '@/components/separator/DoubleLine.vue';
import ImgCompare from '@/components/ImgCompare.vue';

export default {
  name: 'Home',
  data() {
    return {
      imgCompareCar: {
        after: 'demo/car-after.png',
        before: 'demo/car-before.png',
      },
      imgCompareWabri: {
        after: 'demo/wabri-after.jpg',
        before: 'demo/wabri-before.jpg',
      },
    };
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
  .demo-section, .slider-section {
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
