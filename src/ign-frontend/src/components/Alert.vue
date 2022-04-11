<template>
    <div class="notification-top-bar">
      <p>The website will go down on <b>May 1st</b> because of insuffient funds for running on a OVH VPS. Please, consider on support us on <small><a target="_blank" href="https://opencollective.com/schrodinger-hat">OpenCollective <i class='fas fa-external-link-alt '></i></a></small> or <a href='https://twitter.com/schrodinger_hat' target="_blank">reach us<i class='fas fa-external-link-alt '></i></a> in order to sponsor the project.<br />Share the love & credits. Thank you</p>
    </div>
</template>

<script>
import Vue from 'vue';

export default Vue.component('Alert', {
  props: {},
});
</script>
<style lang="scss">

.notification-top-bar {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  height: 50px;
  line-height: 20px;
  width: 100%;
  padding-top: 10px;
  background: $nord11;
  text-align: center;
  font-family: sans-serif;
  font-weight: lighter;
  font-size: 14px;
  z-index: 99999;
}
.notification-top-bar p {
  padding: 0;
  color: $text-secondary;
  margin: 0;
}
.notification-top-bar p a {
  padding: 5px 10px;
  border-radius: 3px;
  background: $nord12;
  color: $text-secondary;
  font-weight: bold;
  text-decoration: none;
}

@media (min-width: 56.25em) {
  .notification-top-bar {
    display: block;
  }
}

</style>
