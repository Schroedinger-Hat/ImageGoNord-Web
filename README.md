# ImageGoNord Website - RGB image to Nordtheme palette
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Image Go Nord is a tool that can convert your rgb images to not only [Nordtheme](https://www.nordtheme.com/) palette.
**IGN is a tool that can convert your rgb images to any palette!**

This repository is:
- an API hosted on K8s that is using the [ImageGoNord Python package](https://github.com/schroedinger-hat/ImageGoNord-pip) written in Flask;
- a demo website made in VueJS hosted on Netlify which can convert your image or video into any palette!

**Are you looking for the python package?**

The official python package's repository is [ImageGoNord-pip](https://github.com/schroedinger-hat/ImageGoNord-pip). You are welcome :)

## Recap

- [Inspiration](#inspiration)
- [Core Technical Concepts](#core-technical-concepts)
- [Getting Started](#getting-started)
- [Running `ign-api` locally with Docker](#running-ign-api-locally-with-docker)
- [How to add a new palette on the website?](#how-to-add-a-new-palette-on-the-website)
- [Contributing](#contributing)

### Inspiration

We are in love with Nordtheme and Linux Rice, that is why we created this repository.

Our goal is to make a shortcut to convert image or video into any theme.
<br>An example could be an awesome wallpaper converted into the Nordtheme palette.

<img src="https://raw.githubusercontent.com/schroedinger-hat/ImageGoNord-web/master/images/ign-demo-image.gif">

<br>Or an example of an image converted into the Gruvbox palette

<img src="https://raw.githubusercontent.com/schroedinger-hat/ImageGoNord-web/master/images/ign-demo-gruvbox.gif">

<br>

We checked the commnunity and we did not find anything similar or any project that can accomplish this task. So, here we are.

### Core Technical Concepts

We are using the PIL because it is the most simple library and it is very useful when you need to manipulate some images.

Redis is our Pub/Sub store and queue management.

With Gunicorn we're executing our Flask API which is posting in a queue some convert jobs from the frontend.

Then we have 3 workers that are running in background in our Docker container where are processing via ImageGoNord Python package the images.

Our goal is also to make this project open source and maintainable by the community. We would love to.

*We believe in the open source community.*

### Getting Started

Clone the repository then go to the `src/ign-frontend` folder

```npm install && npm run serve```

This will bring our website in your local.
By default we're using the same endpoint you'll find on the demo website.

To develop your API locally refer to the following.

### Running `ign-api` locally with Docker

#### 1. **Navigate to the Project Root**

  Ensure you are in the root directory of the project:

  ```sh
  cd ImageGoNord-web
  ```

#### 2. **Build the Docker Image**

  Build the Docker image for `ign-api`:

  ```sh
  docker-compose build
  ```

#### 3. **Start the Docker Containers**

  Start the Docker containers using Docker Compose:

  ```sh
  docker-compose up
  ```

  The API should now be running at `http://localhost:8000`.

#### **Stopping the Docker Containers**

To stop the Docker containers, run:

```sh
docker-compose down
```

#### **Rebuilding the Docker Image**

If you make changes to the Dockerfile or dependencies, you may need to rebuild the Docker image:

```sh
docker-compose build
```

#### **Accessing Logs**

To view the logs of the running containers, use:

```sh
docker-compose logs
```

--------

### How to add a new palette on the website?

It's very easy and you can refer to this [PR](https://github.com/schroedinger-hat/ImageGoNord-web/pull/150) as a sort of documentation.

**What I need to do?**
You need to create a JSON file in `src/ign-frontend/src/assets/palettes/[themeName].json` with the following format:

```
{
    "name": "yourThemeName",
    "colors": [
        "#FFFFFF",
        "#FFFFFF",
        "YOUR_HEXs"
    ]
}
```

After this, please find a good image (e.g. Dracula image) or a palette primary color image (you can use [coolors](https://coolors.co/)), then add it in the `src/ign-frontend/src/assets/palettes/img/[themeName].png` folder.

Then, you need to make this palette available in the demo website by upading the `src/ign-frontend/src/assets/palettes/available-palettes.json` with the following format:

```
{
    "name": "[themeName]",
    "img": "palettes/img/[themeName].png",
    "file": "palettes/[themeName].json"
}
```

Verify that everything is working great and open a PR :)

### Contributing
- Follow the contributor guidelines
- Follow the code style / requirements
- Format for commit messages

# Authors

[TheJoin95](https://github.com/TheJoin95) & [Wabri](https://github.com/Wabri)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.linkedin.com/in/%F0%9F%90%A7gabriele-puliti-b62915a9/"><img src="https://avatars.githubusercontent.com/u/12409541?v=4?s=100" width="100px;" alt=""/><br /><sub><b>GabrielePuliti</b></sub></a><br /><a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=Wabri" title="Code">💻</a> <a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=Wabri" title="Documentation">📖</a> <a href="#design-Wabri" title="Design">🎨</a> <a href="#ideas-Wabri" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-Wabri" title="Maintenance">🚧</a> <a href="#projectManagement-Wabri" title="Project Management">📆</a></td>
      <td align="center"><a href="https://www.mikilombardi.com"><img src="https://avatars.githubusercontent.com/u/6616203?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Miki Lombardi</b></sub></a><br /><a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=TheJoin95" title="Code">💻</a> <a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=TheJoin95" title="Documentation">📖</a> <a href="#design-TheJoin95" title="Design">🎨</a> <a href="#ideas-TheJoin95" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-TheJoin95" title="Maintenance">🚧</a> <a href="#projectManagement-TheJoin95" title="Project Management">📆</a></td>
      <td align="center"><a href="https://github.com/BugliL"><img src="https://avatars.githubusercontent.com/u/3107276?v=4?s=100" width="100px;" alt=""/><br /><sub><b>BugliL</b></sub></a><br /><a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=BugliL" title="Code">💻</a> <a href="#design-BugliL" title="Design">🎨</a> <a href="#ideas-BugliL" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-BugliL" title="Maintenance">🚧</a> <a href="#projectManagement-BugliL" title="Project Management">📆</a></td>
      <td align="center"><a href="http://abod1960.cf"><img src="https://avatars.githubusercontent.com/u/79435005?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdullah Omar</b></sub></a><br /><a href="#design-Abod1960" title="Design">🎨</a></td>
      <td align="center"><a href="https://github.com/jlc893"><img src="https://avatars.githubusercontent.com/u/77926457?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jason</b></sub></a><br /><a href="#design-jlc893" title="Design">🎨</a> <a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=jlc893" title="Documentation">📖</a> <a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=jlc893" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/senali-d"><img src="https://avatars.githubusercontent.com/u/52546856?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Senali</b></sub></a><br /><a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=senali-d" title="Documentation">📖</a></td>
      <td align="center"><a href="https://juancldcmt.github.io"><img src="https://avatars.githubusercontent.com/u/72336775?v=4?s=100" width="100px;" alt=""/><br /><sub><b>JuanCC</b></sub></a><br /><a href="#design-JuanCldCmt" title="Design">🎨</a></td>
    </tr>
    <tr>
      <td align="center"><a href="http://www.linkedin.com/in/veronica-papini-5a546b179"><img src="https://avatars.githubusercontent.com/u/86972949?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Veronica Papini</b></sub></a><br /><a href="https://github.com/schroedinger-hat/ImageGoNord-web/commits?author=VeroPap" title="Documentation">📖</a></td>
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

[MIT license](https://github.com/schroedinger-hat/ImageGoNord-web/blob/master/LICENSE)
