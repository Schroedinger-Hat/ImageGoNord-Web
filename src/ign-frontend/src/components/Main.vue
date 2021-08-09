<template>
  <div class="main">
    <div class="middle-section">
      <h1 v-if="h1">{{ h1 }}</h1>
      <h2 v-if="h2" v-html="h2"></h2>
      <a v-if="btn1" class="btn btn-primary" :href="link1">{{ btn1 }}</a>
      <a v-if="btn2" class="btn btn-info" :href="link2">{{ btn2 }}</a>
      <a v-if="btn3" class="btn btn-primary" :href="link3">{{ btn3 }}</a>
      <a v-if="btn4" class="btn btn-primary" :href="link4">{{ btn4 }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
    h1: String,
    h2: String,
    link1: String,
    link2: String,
    btn1: String,
    btn2: String,
    link3: String,
    link4: String,
    btn3: String,
    btn4: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.middle-section {
  text-align: center;
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

@media (min-width: 56.25em) {
  .middle-section {
    padding: 5em;
  }
}
</style>
