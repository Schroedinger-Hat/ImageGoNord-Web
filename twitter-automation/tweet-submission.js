const Twit = require('twit');
const snoowrap = require('snoowrap');

const IGNSUBREDDIT = 'imagegonord'
const reddit = new snoowrap({
  userAgent: 'GitHub action by /u/thejoin',
  clientId: process.env.REDDIT_APP_ID,
  clientSecret: process.env.REDDIT_APP_SECRET,
  username: 'schrodinger_hat',
  password: process.env.REDDIT_PASSWORD
});

const twitter = new Twit({
  consumer_key:         process.env.TWITTER_API_KEY,
  consumer_secret:      process.env.TWITTER_API_KEY_SECRET,
  access_token:         process.env.TWITTER_ACCESS_TOKEN,
  access_token_secret:  process.env.TWITTER_ACCESS_TOKEN_SECRET,
  timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
  strictSSL:            true,     // optional - requires SSL certificates to be valid.
});

reddit.getSubreddit(IGNSUBREDDIT).fetch().then((r) => {
  r.getNew().then((s) => {
    for (let key in s) {
      let status = 'Take a look of what we made with ImageGoNord on Reddit: ' + 'https://reddit.com' + s[key].permalink;
      console.log('Tweeting: ' + status);
      twitter.post('statuses/update', { status: status }, function(err, data, response) {
        console.log(data)
      });
      break;
    }
  });
});