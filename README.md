# DatasetGenerator

This repo should include a tool to download images from a Bing image search(since the google one is depreciated), and a tool to tag photos.

## Installation
Install the bing image downloader
```
pip install bing-image-downloader
```
Install labelImg
```
pip3 install labelImg
```
## Instruction
1) Download images: Edit bing_downloader to change the parameters. Run the file to download images
```
python3 bing_downloader.py
```
2) Create label classes: Create a text file in the directory of the images you want to tag. Example:
```
car
bicycle
plane
apple
```
3: Start the labelling:
```
labelImg <image path> <path of class file> 
```
You can choose different output format either in yolo or VOC