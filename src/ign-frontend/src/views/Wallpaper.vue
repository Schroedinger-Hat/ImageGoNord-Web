<template>
    <div class="wallpaper">
        <Main
            h1="Wallpaper"
            h2="Find your wallpaper and consider on supporting us on <a class='external-link-color' href='https://opencollective.com/schrodinger-hat' target='_blank'>open collective</a>"
            link1="https://reddit.com/r/imagegonord/"
            btn1="Wallpaper Subreddit"
            link2="https://opencollective.com/schrodinger-hat"
            btn2="OpenCollective"
        />
        <div class="wallpaper-filters container">
          <span @click="toggleFilteringRedditPosts(palette)" :class="`wallpaper-filter ${palette.filtering}`" v-for="palette in palettes" :key="palette.name">
              {{ palette.name }}
            </span>
        </div>
        <div class="wallpaper-grid container">
            <div class="wallpaper-post" v-for="post in reddit_posts" :key="post.url">
                <a :href="post.permalink" target="_blank">
                    <img :src="post.urlImg" :alt="post.title" />
                </a>
            </div>
        </div>
        <div class="text-center container">
            <div class="btn btn-info" @click="fetchRedditPosts();" href="#">Load more images</div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import Main from '../components/Main.vue';
import json from '../assets/palettes/available-palettes.json';

export default Vue.component('Wallpaper', {
  props: {},
  components: {
    Main,
  },
  data() {
    return {
      reddit_posts: [],
      filteredPalettes: [],
      palettes: json,
      lastId: null,
    };
  },
  methods: {
    toggleFilteringRedditPosts(palette) {
      /* eslint-disable no-confusing-arrow */
      let activePalettes = this.palettes.filter((p) => p.filtering === 'active').map((p) => (p.name !== null) ? p.name.toUpperCase() : p);

      if (activePalettes.indexOf(palette.name.toUpperCase()) === -1) {
        /* eslint-disable no-restricted-syntax */
        for (const key in this.palettes) {
          if (this.palettes[key].name === palette.name) {
            this.palettes[key].filtering = 'active';
            activePalettes.push(palette.name.toUpperCase());
          }
        }

        if (palette.name === 'Nord') {
          activePalettes.push(null);
        }
      } else {
        for (const key in this.palettes) {
          if (this.palettes[key].name === palette.name) {
            this.palettes[key].filtering = '';
            for (const it in activePalettes) {
              if (activePalettes[it] === palette.name.toUpperCase()) {
                activePalettes = activePalettes.filter((v) => v !== palette.name.toUpperCase());
              }
            }
          }
        }

        if (palette.name === 'Nord') {
          activePalettes = activePalettes.filter((v) => v !== null);
        }
      }

      console.log(activePalettes);
      console.log(this.rawRedditPosts);

      if (activePalettes.length > 0) {
        this.reddit_posts = this.rawRedditPosts.filter((v) => activePalettes.indexOf(v.linkFlairText) !== -1);
      } else {
        this.reddit_posts = this.rawRedditPosts;
      }
    },
    filteringPosts() {
      const activePalettes = this.palettes.filter((p) => p.filtering === 'active').map((p) => (p.name !== null) ? p.name.toUpperCase() : p);
      if (activePalettes.length > 0) {
        this.reddit_posts = this.rawRedditPosts.filter((v) => activePalettes.indexOf(v.linkFlairText) !== -1);
      } else {
        this.reddit_posts = this.rawRedditPosts;
      }
    },
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
              link_flair_text: linkFlairText,
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
            linkFlairText,
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
      self.rawRedditPosts = self.reddit_posts;
      self.filteringPosts();
    },
  },
  created() {
    this.fetchRedditPosts();
    this.palettes.push({ name: 'Nord' });
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

.wallpaper-filters {
  text-align: center;
}

.wallpaper-filter {
  margin: 5px 5px;
  padding: 5px;
  background: $nord3;
  display: inline-block;
  border-radius: 5px;
  color: $nord5;
  cursor: pointer;
}

.wallpaper-filter.active {
  background: $nord9;
}

@media (min-width: 56.25em) {
  .wallpaper-grid {
    .wallpaper-post {
      display: inline-block;
      width: 33%;
    }
  }
}

.#{$dark-mode-class} {
  .wallpaper-filter {
    color: $nord6;
  }
}
</style>
