<template>
  <div class="main">
    <div class="middle-section">
      <h1>A tool to bring any image to the nord palette</h1>
      <h2>Transform each wallpaper, icon, image into the smoothest palette on the internet</h2>
      <router-link class="btn btn-primary" to="/getting-started">Getting Started</router-link>
      <router-link class="btn btn-info" to="/documentation">Documentation</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.middle-section {
  text-align: center;
  padding: 5em;
  h1 {
    font-weight: bold;
    font-size: 3em;
    margin-bottom: 0;
  }
  h2 {
    font-weight: 100;
    margin-top: .3em;
  }
}
</style>
