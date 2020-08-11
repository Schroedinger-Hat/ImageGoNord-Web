<template>
  <div :class="`img-compare container ${className}`">
    <div class="img-compare-wrapper">
      <div class="img-comp-img">
        <img :src="require(`../assets/${after}`)" width="500" height="350">
      </div>
      <div class="img-comp-slider"></div>
      <div class="img-comp-img img-comp-overlay">
        <img :src="require(`../assets/${before}`)"  width="500" height="350">
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.component('ImgCompare', {
  props: {
    before: String,
    after: String,
    className: String,
  },
  data() {
    return {
      clicked: 0,
      slider: null,
      img: null,
      w: 0,
      h: 0,
    };
  },
  methods: {
    slideFinish() {
      this.clicked = 0;
      console.log('finish');
    },
    slideReady(e) {
      e.preventDefault();
      this.clicked = 1;
      console.log('ready');
    },
    slideMove(e) {
      let pos;
      if (this.clicked === 0) return false;
      pos = this.getCursorPos(e);
      if (pos < 0) pos = 0;
      if (pos > this.w) pos = this.w;
      console.log(pos);
      this.slide(pos);
      return true;
    },
    getCursorPos(event) {
      let a = 0;
      let x = 0;
      let e = event;
      e = e || window.event;
      a = this.img.getBoundingClientRect();
      x = e.pageX - a.left;
      x -= window.pageXOffset;
      return x;
    },
    slide(x) {
      this.img.style.width = `${x}px`;
      this.slider.style.left = `${this.img.offsetWidth - (this.slider.offsetWidth / 2)}px`;
    },
  },
  mounted() {
    // eslint-disable-next-line
    this.$nextTick(function () {
      this.slider = document.querySelector(`.${this.className} .img-comp-slider`);
      this.img = document.querySelector(`.${this.className} .img-comp-overlay`);
      this.w = this.img.offsetWidth;
      this.h = this.img.offsetHeight;
      this.img.style.width = `${(this.w / 2)}px`;

      this.slider.style.top = `${(this.h / 2) - (this.slider.offsetHeight / 2)}px`;
      this.slider.style.left = `${((this.w / 2) - (this.slider.offsetWidth / 2))}px`;

      this.slider.addEventListener('mousedown', this.slideReady);
      window.addEventListener('mouseup', this.slideFinish);
      this.slider.addEventListener('touchstart', this.slideReady);
      window.addEventListener('touchend', this.slideFinish);
      window.addEventListener('mousemove', this.slideMove);
      window.addEventListener('touchmove', this.slideMove);
    });
  },
});
</script>

<style scoped lang="scss">

.img-compare {
  padding: 8em 0;

  .img-compare-wrapper {
    position: relative;
    height: 350px;

    .img-comp-img {
      position: absolute;
      width: auto;
      height: auto;
      overflow: hidden;
      transition: all 0ms;

      img {
        display: block;
        vertical-align: middle;
      }
    }

    .img-comp-slider {
      position: absolute;
      z-index:9;
      cursor: ew-resize;
      width: 40px;
      height: 40px;
      background-color: $nord7;
      opacity: 0.7;
      border-radius: 50%;
      transition: all 0ms;
    }
  }
}

@media (min-width: 56.25em) {
  .img-compare {
    .img-compare-wrapper {
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
  .img-compare {
    .img-compare-wrapper {
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
