<template>
    <div class="notification-top-bar">
      <p>This is an open source project and the service is running on OVH VPS. Please, consider on support us on <small><a target="_blank" href="https://opencollective.com/schrodinger-hat">OpenCollective</a></small>. Thank you</p>
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
  height: 40px;
  line-height: 40px;
  width: 100%;
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
