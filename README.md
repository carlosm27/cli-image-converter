# cli-image-converter
This is CLI tool to convert images with .webp extension to .png, .jpg extension to .png, .webp extension to .jpg and .jpg to .png

### How to use it

1 - Clone this repository.

2 - Open your cmd, create a virtual enviroment `py -m venv ./venv`, then  write `cd venv/Scripts` and `activate`.

3 - Install the requirements `python -m pip install -r requirements.txt` .

4 - To convert an image .webp or .jpg to .png `py main.py png <your image path>` if it is a folder of images `py main.py png <your folder path>`.

   -  To convert an image .webp or .png to .jpg `py main.py jpg <your image path>` if it is a folder of images `py main.py png <your folder path>`.

The images will be saved in the same folder where the app is running.
