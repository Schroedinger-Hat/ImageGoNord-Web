logs = {

    "img": [
        "[INFO] Loading input image: {}",
        "[ERROR] On '{}': you need to pass the image path!",
        "\te.g. --img='Pictures/notNord.jpg'"
    ],

    "out": [
        "[INFO] Set output image name: {}",
        "[ERROR] On '{}': no output filename specify!",
        "\te.g. --out='Pictures/nord.jpg'"
    ],

    "navg": [
        "[INFO] No average pixels selected for algorithm optimization",
        "[ERROR] On '{}': the average pixels do not take any values!",
        "\te.g. --no-average"
    ],

    "pxls": [
        "[INFO] Set up pixels width area: {}",
        "[INFO] Set up pixels height area: {}",
        "[ERROR] On '{}': no value specify within the area pixels!",
        "\te.g. --pixels-area=2 or -pa=-4,-3"
    ],

    "blur": [
        "[INFO] Blur enabled",
        "[ERROR] On '{}': the blur argument do not take any values!",
        "\te.g. --blur"
    ],

    "pals": [
        "[INFO] Use all color set: {}",
        "[INFO] Use palette set: {}",
        "\t {} \u2713",
        "\t {} \u2718",
        "[WARNING] No theme specified, use default Nord theme",
        "[WARNING] No set found for: {} \u2753",
    ],

    "err": [
        "[INFO] No image created, solve all ERROR and retry."
    ]

}
