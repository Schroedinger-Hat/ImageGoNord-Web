<template>
  <div class="home">
    <div class="container">
      <Main
        h1="A tool to bring any image to the nord palette"
        h2="Transform each wallpaper, icon, image into the smoothest palette on the internet"
        link1="/color-schemes"
        link2="/documentation"
        btn1="More Palettes"
        btn2="Documentation"
      />
    </div>
    <SeparatorDoubleLine />
    <section class="slider-section">
      <center>
        <h3>Nordify every image</h3>
        <a href="https://www.producthunt.com/posts/imagegonord?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-imagegonord" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=348145&theme=neutral" alt="ImageGoNord - Convert&#0032;your&#0032;images&#0032;into&#0032;your&#0032;fav&#0032;color&#0032;palette&#0033; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
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
    <section class="gallery-section">
      <SeparatorDoubleLine />
      <center>
        <h3>Gallery</h3>
        <p>
          Here are some images converted with IGN from our community.<br/>
          You can find more on our <a class="external-link-color" href="/wallpaper">Wallpaper page</a>
        </p>
      </center>
      <Gallery />
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
          <div>
            <strong>Total converted images: </strong>{{ apiCount.toString().replace(/[^\d]|[\']/g, '') }}
          </div>
        </div>
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
import Gallery from '@/components/Gallery.vue';

export default {
  name: 'Home',
  data() {
    return {
      apiStatus: 'success',
      apiCount: 99999,
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
  mounted() {
    const self = this;
    setInterval(() => {
      fetch('https://ign-api.schroedinger-hat.org/v1/status')
        .then((r) => { self.apiStatus = 'success'; r.json().then((j) => { self.apiCount = j.count; }); })
        .catch(() => { self.apiStatus = 'failed'; });
    }, 8000);
  },
  components: {
    Main,
    Demo,
    SeparatorDoubleLine,
    ImgCompare,
    Gallery,
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
