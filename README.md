# ssd1362-driver-and-helper-funcs


Code in "OLED_Show" directory will run out of the box and display something to an oled display with an ssd1262 chip. Currrently it will show an image of a battery.

OLED_Show/OLED_Show.ino is the main script to upload to arduino. 

## Python code
The python code is used to convert images into an array of hex values that help display the image. 

So, to use a custom image:
1. Save image to the root of this repository
2. open "img_to_bw.py" and change "graphic_file" variable to path of your image. Change size of image if required but other settings should work as default
3. Run the script
4. Copy the contents of image_hex.txt into OLED_Show/Show_Lib.h. Now the image is saved to arduino
5. To use image, run print_custom_bitmap(xPos, yPos, img_name, width, heigh); in OLED_Show/OLED_Show.ino

