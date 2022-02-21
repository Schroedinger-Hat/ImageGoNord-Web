import os
from ImageGoNord import GoNord

import praw
import hashlib
import base64
import requests
import re

post_regex = r"( With ImageGoNord)|(\[CHALLENGER\] |\[NORD\] |\[DRACULA\] |\[GOTHAM\] |\[GRUVBOX\] |\[MOLOKAI\] |\[MONOKAI\] |\[OCEANIC\] |\[ONEDARK\] |\[SOLARIZED\] |\[SONOKAI\] |\[TOKYO\] |\[VAPORWAVE\] |\[CATPPUCCIN\] |\[VIM\] )"


REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME', 'schrodinger_hat')
REDDIT_PASSWORD = os.environ.get('REDDIT_PASSWORD', '6E3oMMV^P4RcX9jA$v!R')
REDDIT_APP_ID = os.environ.get('REDDIT_APP_ID', '-5re3mJsv5Dd0Q')
REDDIT_APP_SECRET = os.environ.get('REDDIT_APP_SECRET', 'T7rfiTMTN88cSo5zDIw_JlvP8beq-g')
SUBREDDIT = os.environ.get('SUBREDDIT', 'imagegonord')

FLAIR={
  'NORD': {'id':'4ae25402-0e3a-11ec-a7a5-f6bad6da933e', 'hex_colors': ['#BF616A','#D08770','#EBCB8B','#A3BE8C','#B48EAD','#8FBCBB','#88C0D0','#81A1C1','#5E81AC','#2E3440','#3B4252','#434C5E','#4C566A','#D8DEE9','#E5E9F0','#ECEFF4']},
  # 'CHALLENGER': {'id': '76a1a10c-0e43-11ec-98fe-82fbd4bb720f', 'hex_colors': ["#565575","#100e23","#ff8080","#ff5458","#95ffa4","#62d196","#ffe9aa","#ffb378","#91ddff","#65b2ff","#c991e1","#906cff","#aaffe4","#63f2f1","#cbe3e7","#a6b3cc"]},
  'DRACULA': {'id': '814aa96e-0e43-11ec-ba7a-a626868b292a', 'hex_colors': ["#282a36","#44475a","#44475a","#6272a4","#8be9fd","#50fa7b","#ffb86c","#ff79c6","#bd93f9","#ff5555","#f1fa8c"]},
  'GOTHAM': {'id': '8b56be70-0e43-11ec-a045-863bbc2baff3', 'hex_colors': ["#0c1014","#c23127","#11151c","#d26937","#091f2e","#edb443","#0a3749","#888ca6","#245361","#4e5166","#599cab","#195466","#99d1ce","#33859E","#d3ebe9","#2aa889"]},
  'GRUVBOX': {'id': '91acbffe-0e43-11ec-8dd8-a60d64b7c633', 'hex_colors': ["#282828","#1d2021","#32302f","#3c3836","#504945","#665c54","#7c6f64","#fbf1c7","#ebdbb2","#d5c4a1","#bdae93","#a89984","#cc241d","#98971a","#d79921","#458588","#b16286","#689d6a","#d65d0e","#928374","#fb4934","#b8bb26","#fabd2f","#83a598","#d3869b","#8ec07c","#f38019","#a89984"]},
  # 'MOLOKAI': {'id': '985ab3d8-0e43-11ec-8037-5e0347bd6e7a', 'hex_colors': ["#1B1D1E","#080800","#F8F8F0","#C4BE89","#66D9EF","#13354A","#293739","#7E8E91","#A6E22E","#E6DB74","#FD971F","#FF0000","#F92672","#232526","#272822","#75715E","#808080","#BCBCBC"]},
  # 'MONOKAI': {'id': '9efa6544-0e43-11ec-9fea-beffa6e6bacf', 'hex_colors': ["#abb2bf","#282c34","#528bff","#e06c75","#56b6c2","#98c379","#c678dd","#d19a66","#e5c07b","#61afef","#5c6370"]},
  'OCEANIC': {'id': 'a6a7b0e4-0e43-11ec-8fea-a626868b292a', 'hex_colors': ["#1b2b34","#343d46","#4f5b66","#65737e","#a7adba","#c0c5ce","#cdd3de","#d8dee9","#ec5f67","#f99157","#fac863","#99c794","#62b3b2","#6699cc","#c594c5","#ab7967"]},
  # 'ONEDARK': {'id': 'be8b5878-0e43-11ec-855d-92be80335bba', 'hex_colors': ["#282c34","#e06c75","#98c379","#e5c07b","#61afef","#c678dd","#56b6c2","#abb2bf"]},
  # 'SOLARIZED': {'id': 'c2f516d8-0e43-11ec-9b15-f2c258f403df', 'hex_colors': ["#002b36","#073642","#586e75","#657b83","#839496","#93a1a1","#b58900","#cb4b16","#dc322f","#d33682","#6c71c4","#268bd2","#2aa198","#859900"]},
  # 'SONOKAI': {'id': 'c819e31e-0e43-11ec-b30d-5a631dd7072a', 'hex_colors': ["#181a1c","#828a9a","#ff6578","#ff6578","#9dd274","#9dd274","#eacb64","#eacb64","#72cce8","#72cce8","#ba9cf3","#ba9cf3","#f69c5e","#f69c5e","#e1e3e4","#e1e3e4"]},
  # 'TOKYO': {'id': 'ccc6e9f2-0e43-11ec-9715-1ea24e7b246f', 'hex_colors': ["#1a1b26","#4e5173","#F7768E","#F7768E","#9ECE6A","#9ECE6A","#E0AF68","#E0AF68","#7AA2F7","#7AA2F7","#9a7ecc","#9a7ecc","#4abaaf","#4abaaf","#acb0d0","#acb0d0"]},
  'VAPORWAVE': {'id': 'd84eab48-0e43-11ec-811e-4edcb0b81b7f', 'hex_colors': ["#94D0FF", "#8795E8", "#966bff", "#AD8CFF", "#C774E8"]},
  'CATPPUCCIN': {'id': 'e62951d2-7a09-11ec-abde-ca9aae39851e', 'hex_colors': ["#F5E0DC", "#F2CDCD", "#DDB6F2", "#F5C2E7", "#E8A2AF", "#F28FAD", "#F8BD96", "#FAE3B0", "#ABE9B3", "#B5E8E0", "#96CDFB", "#89DCEB", "#C9CBFF", "#161320","#1A1826","#1E1E2E","#302D41","#575268","#6E6C7E","#988BA2","#C3BAC6","#D9E0EE"]},
  # 'VIM': {'id': 'e99ae150-0e43-11ec-aad0-6e6c5b7d00e0', 'hex_colors': ["#0184bc","#4078f2","#a626a4","#50a14f","#e45649","#ca1243","#986801","#c18401","#fafafa","#9e9e9e","#f0f0f0"]}
}

IGN_TITLE_SUFFIX = ' With ImageGoNord'
WALLPAPER_SUBREDDIT = 'wallpaper+wallpapers'
MAX_POST_TO_PUBLISH = 2
REPOST_SUBREDDIT = ['wallpapers', 'wallpaper', 'minimalwallpaper']
REPOST_FREQUENCY = 50

if REDDIT_USERNAME == None or REDDIT_PASSWORD == None or REDDIT_APP_ID == None or REDDIT_APP_SECRET == None:
  raise("Error: you need to specify every REDDIT_* secrets in your repository")

def get_image_from_subreddit(subreddit):
  submissions = []
  for submission in subreddit.new(limit=None):
    if (submission.url.endswith('jpg') or submission.url.endswith('png') or submission.url.endswith('jpeg') or submission.url.endswith('bmp')):
      ign_submission_title = re.sub(post_regex, '', submission.title, 0)
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

    for palette_key in FLAIR:
      go_nord.reset_palette()
      IGN_TITLE_PREFIX = '[' + palette_key + '] '
      for hex_color in FLAIR[palette_key]['hex_colors']:
        go_nord.add_color_to_palette(hex_color)

      im = go_nord.base64_to_image(base64.b64encode(requests.get(sub['url']).content))

      img_path = 'images/' + sub['uniqid'] + '.' + sub['url'][-3:]
      print('Processing ' + sub['title'])
      try:
        go_nord.convert_image(im, save_path=img_path)
        print('Uploading ' + sub['title'])
        reddit_sub = imagegonord_subreddit.submit_image(IGN_TITLE_PREFIX + sub['title'] + IGN_TITLE_SUFFIX, image_path=img_path, flair_id=FLAIR[palette_key]['id'])

        print('Commenting')
        reddit_sub.reply('The ImageGoWild website is available [here](https://ign.schrodinger-hat.it/color-schemes) as part of ImageGoNord project, try it and share the result in [r/ImageGoNord](https://www.reddit.com/r/ImageGoNord/)!\nOriginal image made by ['+sub['author']+'](https://www.reddit.com/user/'+sub['author']+') available [here](' + sub['url'] + ').')
      except Exception as e:
        print(e)

    published_post = published_post + 1
