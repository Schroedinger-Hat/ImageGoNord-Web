import os
from ImageGoNord import GoNord

import praw
import hashlib
import base64
import requests

REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME', 'schrodinger_hat')
REDDIT_PASSWORD = os.environ.get('REDDIT_PASSWORD', '6E3oMMV^P4RcX9jA$v!R')
REDDIT_APP_ID = os.environ.get('REDDIT_APP_ID', '-5re3mJsv5Dd0Q')
REDDIT_APP_SECRET = os.environ.get('REDDIT_APP_SECRET', 'T7rfiTMTN88cSo5zDIw_JlvP8beq-g')
SUBREDDIT = os.environ.get('SUBREDDIT', 'imagegonord')

IGN_TITLE_SUFFIX = ' With ImageGoNord'
WALLPAPER_SUBREDDIT = 'wallpaper'
MAX_POST_TO_PUBLISH = 20

if REDDIT_USERNAME == None or REDDIT_PASSWORD == None or REDDIT_APP_ID == None or REDDIT_APP_SECRET == None:
  raise("Error: you need to specify every REDDIT_* secrets in your repository")

def get_image_from_subreddit(subreddit):
  submissions = []
  for submission in subreddit.new(limit=None):
    if (submission.url.endswith('jpg') or submission.url.endswith('png') or submission.url.endswith('jpeg') or submission.url.endswith('bmp')):
      ign_submission_title = submission.title.replace(IGN_TITLE_SUFFIX, '')
      submissions.append({
        'title': ign_submission_title,
        'url': submission.url,
        'uniqid': hashlib.md5(ign_submission_title.encode()).hexdigest()
      })
  return submissions

reddit = praw.Reddit(
  client_id=REDDIT_APP_ID,
  client_secret=REDDIT_APP_SECRET,
  password=REDDIT_PASSWORD,
  user_agent="Github Action by u/thejoin",
  username=REDDIT_USERNAME,
)

if reddit.user.me() != REDDIT_USERNAME:
  raise("Something went wrong with your credentials...")

reddit.validate_on_submit = True
wallpaper_subreddit = reddit.subreddit(WALLPAPER_SUBREDDIT)
imagegonord_subreddit = reddit.subreddit(SUBREDDIT)

wallpaper_submissions = get_image_from_subreddit(wallpaper_subreddit)
ign_submissions = get_image_from_subreddit(imagegonord_subreddit)

wallpaper_ids = [sub['uniqid'] for sub in wallpaper_submissions]
ign_ids = [sub['uniqid'] for sub in ign_submissions]

wallpapers_to_process = [x for x in wallpaper_submissions if x['uniqid'] not in ign_ids]
print('Wallpaper processabili e unici: ' + str(len(wallpapers_to_process)))

if len(wallpapers_to_process) > 0:
  published_post = 0
  for sub in wallpapers_to_process:
    if published_post >= MAX_POST_TO_PUBLISH:
      break

    go_nord = GoNord()
    go_nord.set_default_nord_palette()
    go_nord.enable_avg_algorithm()
    im = go_nord.base64_to_image(base64.b64encode(requests.get(sub['url']).content))

    img_path = 'images/' + sub['uniqid'] + '.' + sub['url'][-3:]
    go_nord.convert_image(im, save_path=img_path)
    print('Uploading ' + sub['title'])
    reddit_sub = imagegonord_subreddit.submit_image(sub['title'] + IGN_TITLE_SUFFIX, image_path=img_path)

    print('Commenting')
    reddit_sub.reply('The ImageGoNord website is available [here](https://ign.schrodinger-hat.it/), try it and share the result in [r/ImageGoNord](https://www.reddit.com/r/ImageGoNord/)!\nOriginal image available [here](' + sub['url'] + ').')
    published_post = published_post + 1
