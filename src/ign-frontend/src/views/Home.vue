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
    <section>
      <ImgCompare
        className="wabri"
        :after="imgCompareWabri.after"
        :width="300"
        :height="250"
        :before="imgCompareWabri.before"
      />
    </section>
    <section>
      <ImgCompare
        className="car"
        :after="imgCompareCar.after"
        :before="imgCompareCar.before"
        :width="500"
        :height="350"
      />
    </section>
    <section class="demo-section">
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

.demo-section {
  min-height: 500px;
  background: $nord5;
  margin-bottom: -13em;
  margin-top: -1.5em;
  padding: 5em 0;
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
