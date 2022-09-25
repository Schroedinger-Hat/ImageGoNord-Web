# ImageGoNord - RGB image to Nordtheme palette

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

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

### License

[MIT license](https://github.com/Schrodinger-Hat/ImageGoNord/blob/master/LICENSE)
