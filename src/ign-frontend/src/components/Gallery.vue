<template>
    <div class="gallery-grid container">
      <div class="gallery-post" v-for="post in reddit_posts" :key="post.url">
        <a :href="post.url" target="_blank">
          <img :src="post.urlImg" :alt="post.title" />
        </a>
      </div>
    </div>
</template>

<script>
import Vue from 'vue';

export default Vue.component('Gallery', {
  props: {},
  data() {
    return {
      reddit_posts: [],
    };
  },
  methods: {
    fetchRedditPosts: async () => {
      let posts = [];
      try {
        const latestPosts = await fetch('https://www.reddit.com/r/imagegonord/new.json?limit=9');
        const post = await latestPosts.json();
        posts = post.data.children.map(
          ({
            data: {
              author,
              created_utc: createdUtc,
              num_comments: numComments,
              title,
              url,
              url_overridden_by_dest: urlImg,
            },
          }) => ({
            author,
            created: createdUtc,
            numComments,
            title,
            url,
            urlImg,
          }),
        );
      } catch (error) {
        console.error(
          'Unexpected problems while fetching content data from Reddit!',
          error,
        );
      }
      return posts;
    },
  },
  created() {
    const self = this;
    this.fetchRedditPosts().then((r) => {
      self.reddit_posts = r;
    });
  },
});
</script>
<style lang="scss" scoped>
.gallery-grid {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;

  .gallery-post {
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
  .gallery-grid {
    .gallery-post {
      display: inline-block;
      width: 33%;
    }
  }
}
</style>
