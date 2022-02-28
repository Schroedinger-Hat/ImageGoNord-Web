import os
from ImageGoNord import GoNord

import praw
import hashlib
import base64
import requests

REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME', 'schrodinger_hat')
REDDIT_PASSWORD = os.environ.get('REDDIT_PASSWORD', '')
REDDIT_APP_ID = os.environ.get('REDDIT_APP_ID', '')
REDDIT_APP_SECRET = os.environ.get('REDDIT_APP_SECRET', '')
SUBREDDIT = os.environ.get('SUBREDDIT', 'imagegonord')

FLAIR_IDS={
  'NORD': '4ae25402-0e3a-11ec-a7a5-f6bad6da933e',
  'CHALLENGER': '76a1a10c-0e43-11ec-98fe-82fbd4bb720f',
  'DRACULA': '814aa96e-0e43-11ec-ba7a-a626868b292a',
  'GOTHAM': '8b56be70-0e43-11ec-a045-863bbc2baff3',
  'GRUVBOX': '91acbffe-0e43-11ec-8dd8-a60d64b7c633',
  'MOLOKAI': '985ab3d8-0e43-11ec-8037-5e0347bd6e7a',
  'MONOKAI': '9efa6544-0e43-11ec-9fea-beffa6e6bacf',
  'OCEANIC': 'a6a7b0e4-0e43-11ec-8fea-a626868b292a',
  'ONEDARK': 'be8b5878-0e43-11ec-855d-92be80335bba',
  'SOLARIZED': 'c2f516d8-0e43-11ec-9b15-f2c258f403df',
  'SONOKAI': 'c819e31e-0e43-11ec-b30d-5a631dd7072a',
  'TOKYO': 'ccc6e9f2-0e43-11ec-9715-1ea24e7b246f',
  'VAPORWAVE': 'd84eab48-0e43-11ec-811e-4edcb0b81b7f',
  'VIM': 'e99ae150-0e43-11ec-aad0-6e6c5b7d00e0'
}

IGN_TITLE_SUFFIX = ' With ImageGoNord'
WALLPAPER_SUBREDDIT = 'wallpaper+wallpapers'
MAX_POST_TO_PUBLISH = 1
REPOST_SUBREDDIT = ['wallpapers', 'wallpaper', 'minimalwallpaper']
REPOST_FREQUENCY = 8

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
        'author': str(submission.author),
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
    print('Processing ' + sub['title'])
    try:
      go_nord.convert_image(im, save_path=img_path)
      print('Uploading ' + sub['title'])
      reddit_sub = imagegonord_subreddit.submit_image(sub['title'] + IGN_TITLE_SUFFIX, image_path=img_path, flair_id=FLAIR_IDS.NORD)

      print('Commenting')
      reddit_sub.reply('The ImageGoNord website is available [here](https://ign.schrodinger-hat.it/), try it and share the result in [r/ImageGoNord](https://www.reddit.com/r/ImageGoNord/)!\nOriginal image made by ['+sub['author']+'](https://www.reddit.com/user/'+sub['author']+') available [here](' + sub['url'] + ').')
      published_post = published_post + 1

      if (published_post % REPOST_FREQUENCY == 0):
        for crossposting_subreddit in REPOST_SUBREDDIT:
          print('Crossposting in ' + crossposting_subreddit)
          reddit_sub.crosspost(subreddit=crossposting_subreddit)
    except Exception as e:
      print(e)
