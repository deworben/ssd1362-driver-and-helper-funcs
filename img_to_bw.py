
import cv2
import numpy as np
import time

def binary_2_hex(masked):
    bin_str = "" 
    big_out_arr = []
    new_arr = []
    for sub_arr in masked:
        for i,bin in enumerate(sub_arr):
            # print(bin_str)
            if i%8 == 0 and not i==0:
                # Convert the last string into a 4 dig hex in case it's 3
                hex_num = hex(int(bin_str.ljust(8, '0') , 2))
                if len(str(hex_num)) == 3 :
                    hex_num = "0x0" + hex_num[2]
                new_arr.append(hex_num)
                bin_str = "" + str(bin)
            else:
                bin_str = bin_str + str(bin)
        
        # Convert the last string into a 4 dig hex in case it's 3
        hex_num = hex(int(bin_str.ljust(8, '0') , 2))
        if len(str(hex_num)) == 3 :
            hex_num = "0x0" + hex_num[2]

        new_arr.append(hex_num) #pad with 0's right
        bin_str = ""
        big_out_arr.append(new_arr)
        new_arr = []
        # print("------------")
    
    return big_out_arr

    # print(big_out_arr)
def my_flatten(big_out_arr):
    one_d_out_arr = []
    for row in big_out_arr:
        for elem in row:
            one_d_out_arr.append(elem)

    return one_d_out_arr
  
############ Script params, please feel free to edit
# Default params for swoop logo
# new_size = (25, 35)  
# graphic_file = 'swoop_logo.png'
# show_img = False # Show what the final image will look like
# write_to_file = True
# invert_colour_selection = False
# array_name = "swoop_logo"

# Default params for battery
new_size = (100, 50)  
graphic_file = 'battery-full.png'
show_img = False # Show what the final image will look like
write_to_file = True
invert_colour_selection = True
array_name = "battery_full"

############ Start of the script
# read the image file
img = cv2.imread(graphic_file, 2)

# rescale and convert to binary
bw_img = cv2.resize(img, dsize=new_size, interpolation = cv2.INTER_AREA)  
ret, bw_img = cv2.threshold(bw_img, 70, 255, cv2.THRESH_BINARY)

# Show image 
if show_img == True:
    cv2.imshow("Binary", bw_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Convert 255's to 1's. 3 is a temporary number
masked = np.int32(bw_img)
if invert_colour_selection == True:
    masked[masked==255] = 3
    masked[masked==0] = 1
    masked[masked==3] = 0
else:
    masked[masked==255] = 1



# Group the 1's into 8 for hex conversion
masked = binary_2_hex(masked)
masked = my_flatten(masked)
# masked = masked.flatten(order='C') #<- for use with numpy - now deprecated

# Print in a form that directly copy-pastes
print('[%s]' % ', '.join(map(str, masked)))
print(len(list(masked)))

if write_to_file == True:
    with open("image_hex.txt", "w") as hex_img_file:
        hex_img_file.write("static const uint8_t {}[{}] PROGMEM = {{\n\t".format(array_name, len(list(masked)) ))
        for i, hex_code in enumerate(masked):
            if i==(len(masked)-1): #if its the last number, dont add a comma after
                hex_img_file.write(str(hex_code))
            else:
                hex_img_file.write(str(hex_code)+", ")

        hex_img_file.write("\n};\n")





