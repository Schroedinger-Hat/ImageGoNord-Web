module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "@/styles/global.scss";`
      }
    }
  }
};