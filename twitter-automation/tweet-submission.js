const twit = require('twit');
const snoowrap = require('snoowrap');

const IGNSUBREDDIT = 'imagegonord'
const reddit = new snoowrap({
  userAgent: 'GitHub action by /u/thejoin',
  clientId: process.env.REDDIT_APP_ID,
  clientSecret: process.env.REDDIT_APP_SECRET,
  username: 'schrodinger_hat',
  password: process.env.REDDIT_PASSWORD
});

reddit.getSubreddit(IGNSUBREDDIT).fetch().then((r) => {
  r.getTop().then((t) => {
    console.log(t);
  })
});