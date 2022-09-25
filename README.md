# ImageGoNord - RGB image to Nordtheme palette
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

A tool that can convert your rgb images to [Nordtheme](https://www.nordtheme.com/) palette.

This repository is:
- CLI utility, written in python, that can convert any sort of image into a [nordtheme](https://github.com/arcticicestudio/nord) palette image;
- an API hosted on Heroku that is using the [ImageGoNord Python package](https://github.com/Schrodinger-Hat/ImageGoNord-pip) written in Flask;
- a demo website hosted on Netlify made using the Nordtheme and VueJS;

**Are you looking for the python package?**

The official python package's repository is [ImageGoNord-pip](https://github.com/Schrodinger-Hat/ImageGoNord-pip). You are welcome :)

<!--
@TODO
- Describe very briefly but clearly what the project does.
- State if it is out-of-the-box user-friendly, so it’s clear to the user.
- List its most useful/innovative/noteworthy features.
- State its goals/what problem(s) it solves.
- Note and briefly describe any key concepts (technical, philosophical, or both) important to the user’s understanding.
- Link to any supplementary blog posts or project main pages.
- Note its development status.
- Include badges.
- If possible, include screenshots and demo videos.
-->

### Inspiration

We are in love with Nordtheme, that is why we created this repository.

[![Nord Color Palette Overview](https://raw.githubusercontent.com/arcticicestudio/nord-docs/develop/assets/images/nord/repository-color-palettes.svg?sanitize=true)](https://www.nordtheme.com/docs/colors-and-palettes)

Our goal is to make a shortcut to convert anything into this theme, by starting from the images.
<br>An example could be an awesome wallpaper converted into the Nordtheme palette.

We checked the commnunity and we did not find anything similar or any project that can accomplish this task. So, here we are.

### Core Technical Concepts

We are using the PIL because it is the most simple library and it is very useful when you need to manipulate some images.

Our goal is also to make this project open source and maintainable by the community. We would love to.

*We believe in the open source community.*

### Getting Started

Include any essential instructions for:

- Getting it:
  ```
  git clone https://github.com/Schrodinger-Hat/ImageGoNord
  ```
- Enter to the folder
  ```
  cd ImageGoNord
  ```
- Installing It
  ```
  pip install -r requirements.txt
  ```
- Running it
  ```
  python src/cli.py --img='<path_to_your_image>' 
  ```

The algorithm can takes some time (we are working on improving it), you can find the result with the name *nord.png*.

You can define some more configuration and use different palettes, find more using:

```
python src/cli.py --help
```

### Testing
- Tests **TODO**

### Contributing
- Follow the contributor guidelines
- Follow the code style / requirements
- Format for commit messages

### TODO
- Portable environemnt
- Testing
- Improvements on image quality and supporting any image format
- Make contributing guidelines
- API / UI

# Authors

[TheJoin95](https://github.com/TheJoin95) & [Wabri](https://github.com/Wabri)

**NOTE**: we are not (yet) affiliated with the Nordtheme or [Arcticicestudio](https://github.com/arcticicestudio).

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.linkedin.com/in/%F0%9F%90%A7gabriele-puliti-b62915a9/"><img src="https://avatars.githubusercontent.com/u/12409541?v=4?s=100" width="100px;" alt=""/><br /><sub><b>GabrielePuliti</b></sub></a><br /><a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=Wabri" title="Code">💻</a> <a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=Wabri" title="Documentation">📖</a> <a href="#design-Wabri" title="Design">🎨</a> <a href="#ideas-Wabri" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-Wabri" title="Maintenance">🚧</a> <a href="#projectManagement-Wabri" title="Project Management">📆</a></td>
      <td align="center"><a href="https://www.mikilombardi.com"><img src="https://avatars.githubusercontent.com/u/6616203?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Miki Lombardi</b></sub></a><br /><a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=TheJoin95" title="Code">💻</a> <a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=TheJoin95" title="Documentation">📖</a> <a href="#design-TheJoin95" title="Design">🎨</a> <a href="#ideas-TheJoin95" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-TheJoin95" title="Maintenance">🚧</a> <a href="#projectManagement-TheJoin95" title="Project Management">📆</a></td>
      <td align="center"><a href="https://github.com/BugliL"><img src="https://avatars.githubusercontent.com/u/3107276?v=4?s=100" width="100px;" alt=""/><br /><sub><b>BugliL</b></sub></a><br /><a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=BugliL" title="Code">💻</a> <a href="#design-BugliL" title="Design">🎨</a> <a href="#ideas-BugliL" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-BugliL" title="Maintenance">🚧</a> <a href="#projectManagement-BugliL" title="Project Management">📆</a></td>
      <td align="center"><a href="http://abod1960.cf"><img src="https://avatars.githubusercontent.com/u/79435005?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdullah Omar</b></sub></a><br /><a href="#design-Abod1960" title="Design">🎨</a></td>
      <td align="center"><a href="https://github.com/jlc893"><img src="https://avatars.githubusercontent.com/u/77926457?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jason</b></sub></a><br /><a href="#design-jlc893" title="Design">🎨</a> <a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=jlc893" title="Documentation">📖</a> <a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=jlc893" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/senali-d"><img src="https://avatars.githubusercontent.com/u/52546856?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Senali</b></sub></a><br /><a href="https://github.com/Schrodinger-Hat/ImageGoNord/commits?author=senali-d" title="Documentation">📖</a></td>
      <td align="center"><a href="https://juancldcmt.github.io"><img src="https://avatars.githubusercontent.com/u/72336775?v=4?s=100" width="100px;" alt=""/><br /><sub><b>JuanCC</b></sub></a><br /><a href="#design-JuanCldCmt" title="Design">🎨</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

### License

[MIT license](https://github.com/Schrodinger-Hat/ImageGoNord/blob/master/LICENSE)
