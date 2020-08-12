import pathlib
from setuptools import setup

ROOT = pathlib.Path('../..')
README = (ROOT / "README.md").read_text()

setup(
    name="image-go-nord",
    version="0.0.1",
    description="A tool for converting RGB image to Nordtheme palette",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Schrodinger-Hat/ImageGoNord",
    download_url = 'https://github.com/Schrodinger-Hat/ImageGoNord/releases',
    keywords = ['nordtheme', 'pillow', 'image', 'conversion', 'rgb'], 
    author="Schrodinger Hat",
    author_email="schrodinger.hat.show@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ImageGoNord"],
    include_package_data=True,
    install_requires=["Pillow", "html2text"],
)