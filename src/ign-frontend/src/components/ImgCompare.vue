<template>
  <div :class="`img-compare ${className}`">
    <div class="img-compare-wrapper">
      <div class="img-comp-img">
        <img
          :src="require(`../assets/${after}`)"
          :width="getWidth(width)"
          :height="getHeight(height)"
        />
      </div>
      <div class="img-comp-slider"></div>
      <div class="img-comp-img img-comp-overlay">
        <img
          :src="require(`../assets/${before}`)"
          :width="getWidth(width)"
          :height="getHeight(height)"
        />
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
    width: Number,
    height: Number,
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
    getWidth() {
      return (window.screen.width < 768) ? (this.width / 2) : this.width;
    },
    getHeight() {
      return (window.screen.width < 768) ? (this.height / 2) : this.height;
    },
    slideFinish() {
      this.clicked = 0;
    },
    slideReady(e) {
      e.preventDefault();
      this.clicked = 1;
    },
    slideMove(e) {
      let pos;
      if (this.clicked === 0) return false;
      pos = this.getCursorPos(e);
      if (pos < 0) pos = 0;
      if (pos > this.w) pos = this.w;
      this.slide(pos);
      return true;
    },
    getCursorPos(event) {
      let a = 0;
      let x = 0;
      let e = event;
      e = e || window.event;
      let pageX = 0;
      if (e.pageX !== undefined) {
        pageX = e.pageX;
      }

      if (e.touches !== undefined) {
        pageX = e.touches[0].pageX;
      }

      a = this.img.getBoundingClientRect();
      x = pageX - a.left;
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
      const wrapper = document.querySelector(`.${this.className} .img-compare-wrapper`);
      this.slider = document.querySelector(`.${this.className} .img-comp-slider`);
      this.img = document.querySelector(`.${this.className} .img-comp-overlay`);

      wrapper.style.width = `${this.getWidth(this.width)}px`;
      wrapper.style.height = `${this.getHeight(this.height)}px`;

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
  padding: .8em;
  background: $bg-secondary;
  display: inline-block;

  .img-compare-wrapper {
    position: relative;
    width: 500px;
    max-width: 100%;
    height: 350px;

    .img-comp-img {
      position: absolute;
      width: 100%;
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
    // nope
  }
}

.#{$dark-mode-class} {
  .img-compare {
    background: $dark-bg-secondary;
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
