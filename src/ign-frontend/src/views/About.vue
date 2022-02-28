<template>
  <div class="about container">
    <Main
        h1="About"
        h2="Who are we and why this project?"
      />
      <div class="description">
        <p>
          We are in love with <a href="https://www.nordtheme.com/" class="external-link-color" target="_blank">Nordtheme</a>, by Artic Studio.
          One big problem that we had was searching hard for icons, wallpapers,
          profile picture created in the nord palette.
          These resources are not existing or they are unsearchable.
          <br/><br/>
          In order to solve this problem we wanted to create a tool,
          not graphic, to convert images in the north palette.
          <br/><br/>
          We are hoping that this project can bring tons
          of nord resources on the web in a free-to-use license.
          <br/><br/>
          Authors: <a class="external-link-color" href="https://github.com/TheJoin95" target="_blank">@thejoin</a> and <a class="external-link-color" href="https://github.com/Wabri" target="_blank">@wabri</a>
        </p>
      </div>
  </div>
</template>
<script>
import Main from '@/components/Main.vue';

export default {
  name: 'About',
  components: {
    Main,
  },
};
</script>

<style scoped lang="scss">
.about {
  .description {
    margin: auto;
    max-width: 640px;
    padding: 0 .5em;
    p {
      font-size: 1.4em;
    }
  }
}
</style>
