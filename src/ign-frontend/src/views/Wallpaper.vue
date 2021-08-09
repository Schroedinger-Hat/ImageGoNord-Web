<template>
    <div class="wallpaper">
        <Main
            h1="Wallpaper"
            h2="Find your wallpaper and consider on supporting us on <a class='external-link-color' href='https://opencollective.com/schrodinger-hat' target='_blank'>open collective</a>"
            link1="https://reddit.com/r/imagegonord/"
            btn1="Wallaper Subreddit"
            link2="https://opencollective.com/schrodinger-hat"
            btn2="OpenCollective"
        />
        <div class="wallpaper-grid container">
            <div class="wallpaper-post" v-for="post in reddit_posts" :key="post.url">
                <a :href="post.permalink" target="_blank">
                    <img :src="post.urlImg" :alt="post.title" />
                </a>
            </div>
        </div>
        <div class="text-center container">
            <div class="btn btn-info" @click="fetchRedditPosts()" href="#">Load more images</div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import Main from '../components/Main.vue';

export default Vue.component('Wallpaper', {
  props: {},
  components: {
    Main,
  },
  data() {
    return {
      reddit_posts: [],
      lastId: null,
    };
  },
  methods: {
    async fetchRedditPosts() {
      const self = this;
      let posts = [];
      try {
        const after = (self.lastId !== null) ? `&after=${self.lastId}` : '';
        const latestPosts = await fetch(`https://www.reddit.com/r/imagegonord/new.json?limit=30${after}`);
        const post = await latestPosts.json();
        self.lastId = post.data.after;
        posts = post.data.children.map(
          ({
            data: {
              author,
              name,
              created_utc: createdUtc,
              num_comments: numComments,
              title,
              url,
              url_overridden_by_dest: urlImg,
              permalink,
            },
          }) => ({
            author,
            name,
            created: createdUtc,
            numComments,
            title,
            url,
            urlImg,
            permalink: `https://www.reddit.com${permalink}`,
          }),
        );
      } catch (error) {
        console.error(
          'Unexpected problems while fetching content data from Reddit!',
          error,
        );
      }
      const filteredPosts = posts
        .filter((o) => (o.urlImg !== undefined && o.urlImg.search(/(jpg)|(png)|(gif)|jpeg/) !== -1));
      self.reddit_posts = Object.assign(self.reddit_posts.concat(filteredPosts));
    },
  },
  created() {
    this.fetchRedditPosts();
  },
});
</script>
<style lang="scss" scoped>
.text-center {
    text-align: center;
}

.wallpaper-grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;

  .wallpaper-post {
    display: none;
    text-align: center;

    img {
      max-width: 100%;
      max-height: 215px;
      border: 6px solid $nord4;
      border-radius: 5px;
    }
  }
}

@media (min-width: 56.25em) {
  .wallpaper-grid {
    .wallpaper-post {
      display: inline-block;
      width: 33%;
    }
  }
}
</style>
