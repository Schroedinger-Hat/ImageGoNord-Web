<template>
  <div class="documentation">
    <div class="container">
      <Main
        h1="Documentation"
      />
      <center>
        <div class="installation-tab python">
          <div class="icon"><i class="fab fa-python"></i></div>
          <div>
            <router-link class="btn btn-primary" to="/documentation/python">
              Python Package
            </router-link>
          </div>
        </div>
        <div class="installation-tab api">
          <div class="icon"><i class="fas fa-book"></i></div>
          <div>
            <router-link class="btn btn-primary" to="/documentation/api">
              REST API
            </router-link>
          </div>
        </div>
      </center>
      <section class="documentation-guides">
        <div class="guide python markdown-body">
          <h1>Documentation Python Package</h1>
          <p>The documentation is under development (as the package) and it is
            <a href="https://ign.schrodinger-hat.it/documentation/python">available also on the website</a>.
          You can find some usage and some example under the example folder.</p>
          <h1 id="class-methods">Class &amp; Methods</h1>
          <h2 id="nordpalettefile-">NordPaletteFile:</h2>
          <p>A class used to map the nord color-scheme into files.
            Each file contains the hex code of the nord palette, divided into:</p>
          <ul>
          <li>AURORA.txt: Aurora color-palette</li>
          <li>FROST.txt: Frost color-palette</li>
          <li>POLAR_NIGHT.txt: Polar night color-palette</li>
          <li>SNOW_STORM.txt: Snow Storm color-palette</li>
          </ul>
          <h2 id="gonord">GoNord</h2>
          <p>A class used for converting image to the nord palette.
            It can be used also for converting image to other palette by loading different palette or hex color.
          This class needs Pillow and apply 3 different palette conversion algorithm:</p>
          <ul>
          <li>replace pixel by avg area pixel (convert method)</li>
          <li>replace pixel by pixel (convert method)</li>
          <li>apply a filter by using pillow features (quantize method)</li>
          </ul>
          <h3 id="gonord-attributes">GoNord Attributes</h3>
          <p><strong>PALETTE_LOOKUP_PATH</strong>: str - path to look for finding the palette files (.txt)</p>
          <p><strong>USE_GAUSSIAN_BLUR</strong>: bool - enable or disable the blur (in output)</p>
          <p><strong>USE_AVG_COLOR</strong>: bool - enable or disable avg algorithm</p>
          <p><strong>AVG_BOX_DATA</strong>: dict - params (width and height) of the avg area to be considered</p>
          <p><strong>AVAILABLE_PALETTE</strong>: list - loaded palette list</p>
          <p><strong>PALETTE_DATA</strong>: dict - available palette data in hex : rgb format</p>
          <h2 id="methods">Methods</h2>
          <h3 id="set_palette_lookup_path">set_palette_lookup_path</h3>
          <p>Set the base_path for the palette folder, if different from the default.</p>
          <p><code>set_palette_lookup_path(self, path)</code></p>
          <hr>
          <h3 id="set_default_nord_palette">set_default_nord_palette</h3>
          <p>Set available palette as the default palette.</p>
          <p>The default palette is the full Nordtheme palette.</p>
          <p><code>set_default_nord_palette(self)</code></p>
          <hr>
          <h3 id="get_palette_data">get_palette_data</h3>
          <p>Build the palette data from configuration</p>
          <p><code>get_palette_data(self)</code></p>
          <p><strong>Returns</strong>: dict - The palette data: keys are hex color code, values are rgb values</p>
          <hr>
          <h3 id="add_color_to_palette">add_color_to_palette</h3>
          <p>Add hex color to current palette</p>
          <p><code>add_color_to_palette(self, hex_color)</code></p>
          <hr>
          <h3 id="reset_palette">reset_palette</h3>
          <p>Reset the available_palette prop</p>
          <p><code>reset_palette(self)</code></p>
          <hr>
          <h3 id="add_file_to_palette">add_file_to_palette</h3>
          <p>Append a custom file to the available palette</p>
          <p><code>add_file_to_palette(self, file)</code></p>
          <hr>
          <h3 id="enable_gaussian_blur">enable_gaussian_blur</h3>
          <p>Enable blur filter</p>
          <p><code>enable_gaussian_blur(self)</code></p>
          <hr>
          <h3 id="disable_gaussian_blur">disable_gaussian_blur</h3>
          <p>disabled blur filter</p>
          <p><code>disable_gaussian_blur(self)</code></p>
          <hr>
          <h3 id="open_image">open_image</h3>
          <p>Load an image using Pillow utility</p>
          <p><code>open_image(self, path)</code></p>
          <p><strong>Parameters</strong>:</p>
          <ul>
          <li>path: str - the path and the filename where to save the image</li>
          </ul>
          <p><strong>Returns</strong>: pillow Image - the opened image</p>
          <hr>
          <h3 id="resize_image">resize_image</h3>
          <p>Resize an image using Pillow utility</p>
          <p><code>resize_image(self, image, w=0, h=0)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image: pillow image - The source pillow image</li>
          <li>w: int - New width</li>
          <li>h: int - New height</li>
          </ul>
          <p><strong>Returns</strong>: pillow image - the resized image</p>
          <hr>
          <h3 id="image_to_base64">image_to_base64</h3>
          <p>Convert a Pillow image to base64 string</p>
          <p>Available extension: <a href="https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html">https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html</a></p>
          <p><code>image_to_base64(self, image, extension)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image: pillow image - The source pillow image</li>
          <li>extension: str - The extension of the source image (mandatory)</li>
          </ul>
          <p><strong>Returns</strong>: pillow image - processed image</p>
          <hr>
          <h3 id="base64_to_image">base64_to_image</h3>
          <p>Convert a base64 string to a Pillow image</p>
          <p><code>base64_to_image(self, img_b64)</code></p>
          <p><strong>Parameters</strong>
          img_b64: str - The base64 string representation of the image</p>
          <p><strong>Returns</strong>: pillow image - The converted image from base64</p>
          <hr>
          <h3 id="load_pixel_image">load_pixel_image</h3>
          <p>Load the pixel map of a given Pillow image</p>
          <p><code>load_pixel_image(self, opened_image)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image: pillow image - The source pillow image</li>
          </ul>
          <p><strong>Returns</strong>: pillow image - pixel map of the opened image</p>
          <hr>
          <h3 id="enable_avg_algorithm">enable_avg_algorithm</h3>
          <p>Enable avg algorithm</p>
          <p><code>enable_avg_algorithm(self)</code></p>
          <hr>
          <h3 id="disable_avg_algorithm">disable_avg_algorithm</h3>
          <p>  Disabled avg algorithm</p>
          <p><code>disable_avg_algorithm(self)</code></p>
          <hr>
          <h3 id="set_avg_box_data">set_avg_box_data</h3>
          <p>Set the dimension of the AVG area box to use</p>
          <p><code>set_avg_box_data(self, w=-2, h=3)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>w: int - Box&#39;s width</li>
          <li>h: int - Box&#39;s height</li>
          </ul>
          <hr>
          <h3 id="quantize_image">quantize_image</h3>
          <p>Quantize a Pillow image by applying the available palette</p>
          <p><code>quantize_image(self, image, save_path=&#39;&#39;)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image: pillow image - The source pillow image</li>
          <li>fill_color: str - Default fill color as foreground</li>
          <li>save_path : str, optional - the path and the filename where to save the image</li>
          </ul>
          <p><strong>Returns</strong>: pillow image - quantized image</p>
          <hr>
          <h3 id="convert_image">convert_image</h3>
          <p>Process a Pillow image by replacing pixel or by avg algorithm</p>
          <p><code>convert_image(self, image, palettedata, save_path=&#39;&#39;)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image : pillow image - The source pillow image</li>
          <li>save_path : str, optional - the path and the filename where to save the image</li>
          </ul>
          <p><strong>Returns</strong>: pillow image - processed image</p>
          <hr>
          <h3 id="save_image_to_file">save_image_to_file</h3>
          <p>  Save a Pillow image to file</p>
          <p><code>save_image_to_file(self, image, path)</code></p>
          <p><strong>Parameters</strong></p>
          <ul>
          <li>image: pillow image - The source pillow image</li>
          <li>path: str - the path and the filename where to save the image</li>
          </ul>
          <hr>
          <h2 id="example">Example</h2>
          <h3 id="import-gonord-from-imagegonord-package">Import GoNord from ImageGoNord package</h3>
          <p>from ImageGoNord import NordPaletteFile, GoNord</p>
          <h3 id="use-replace-pixel-by-pixel-algorithm">Use replace pixel by pixel algorithm</h3>
          <pre><code>go_nord = GoNord()
          <span class="hljs-built_in">image</span> = go_nord.open_image(<span class="hljs-string">"images/test.jpg"</span>)
          go_nord.convert_image(<span class="hljs-built_in">image</span>, save_path=<span class="hljs-string">'images/test.processed.jpg'</span>)
          </code></pre>
          <h3 id="use-avg-algorithm-clean-default-palette-and-add-just-the-polar-night-and-snow-storm-colors">
            Use Avg algorithm, clean default palette and add just the POLAR NIGHT and SNOW STORM colors</h3>
          <pre><code>go_nord.enable_avg_algorithm()
          go_nord.reset_palette()
          go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
          go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
          <span class="hljs-comment">// You can add color also by their hex code</span>
          go_nord.add_color_to_palette(<span class="hljs-string">'#FF0000'</span>)

          <span class="hljs-built_in">image</span> = go_nord.open_image(<span class="hljs-string">"images/test.jpg"</span>)
          go_nord.convert_image(<span class="hljs-built_in">image</span>, save_path=<span class="hljs-string">'images/test.avg.jpg'</span>)
          </code></pre>
          <h3 id="resize-image-and-use-the-replace-pixel-by-pixel-algorithm-with-less-colors">
            Resize image and use the replace pixel by pixel algorithm with less colors</h3>
          <pre><code>go_nord.disable_avg_algorithm()
          go_nord.reset_palette()
          go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
          go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)

          <span class="hljs-built_in">image</span> = go_nord.open_image(<span class="hljs-string">"images/test.jpg"</span>)
          resized_img = go_nord.resize_image(<span class="hljs-built_in">image</span>)
          go_nord.convert_image(resized_img, save_path=<span class="hljs-string">'images/test.resized.jpg'</span>)
          </code></pre>
          <h3 id="use-quantize-method-for-rfiltering-an-image-with-the-current-palette">
            Use quantize method for rfiltering an image with the current palette</h3>
          <pre><code><span class="hljs-built_in">image</span> = go_nord.open_image(<span class="hljs-string">"images/test.jpg"</span>)
          go_nord.reset_palette()
          go_nord.set_default_nord_palette()
          quantize_image = go_nord.quantize_image(<span class="hljs-built_in">image</span>, save_path=<span class="hljs-string">'images/test.quantize.jpg'</span>)
          <span class="hljs-comment">// To base64</span>
          go_nord.image_to_base64(quantize_image, <span class="hljs-string">'jpeg'</span>)
          </code></pre>
        </div>
        <div class="guide api">
          <h3>Documentation REST API</h3>
          <p>Work in progress</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Main from '@/components/Main.vue';

export default {
  name: 'Documentation',
  components: {
    Main,
  },
  mounted() {
    this.chooseDoc();
  },
  methods: {
    chooseDoc() {
      let docType = 'python';

      if (window.location.pathname.indexOf('python') !== -1) {
        docType = 'python';
      } else if (window.location.pathname.indexOf('api') !== -1) {
        docType = 'api';
      }

      const guides = document.querySelectorAll('.guide');
      for (let i = 0; i < guides.length; i += 1) {
        guides[i].style.display = 'none';
        if (guides[i].className.indexOf(docType) !== -1) {
          guides[i].style.display = 'block';
        }
      }
    },
  },
  watch: {
    $route() {
      this.chooseDoc();
    },
  },
};
</script>
<style scoped lang="scss">
@import '@/styles/_md.scss';
.documentation {
  center {
    .icon {
      margin-bottom: 1em;
      i {
        font-size: 5em;
        color: $text-primary;
      }
    }
    .documentation-tab {
      margin-bottom: 1em;
    }
  }
  .documentation-guides {
    padding: .8em;
    margin: 3em .5em 0 .5em;
    background: $bg-secondary;
    &:before {
      content: 'Select a Doc, documentation will show up here';
      color: $text-primary;
      padding: .3em 0;
    }
    .guide {
      display: none;
      background: $nord5;
      padding: .8em;
    }
  }
}

@media (min-width: 56.25em) {
  .documentation {
    center {
      display: flex;
      justify-content: center;

      .icon {
        margin-bottom: 1em;
        i {
          font-size: 5em;
          color: $text-primary;
        }
      }

      .documentation-tab {
        padding: 0 1em;
      }
    }
    .documentation-guides {
      max-width: 860px;
      margin: auto;
      margin-top: 3em;

      .guide {
        background: $nord5;
        padding: .8em;
      }
    }
  }
}

.#{$dark-mode-class} {
  .documentation {
    center {
      .icon {
        i {
          color: $dark-text-primary;
        }
      }
    }
    .documentation-guides {
      background: $dark-bg-secondary;
      &:before {
        color: $dark-text-primary;
      }

      .guide {
        background: $dark-bg-primary;
      }
    }
  }
}
</style>
