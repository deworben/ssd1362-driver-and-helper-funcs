# my_string = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111000000011111111111111111111111111111111111100011111111111111111111111111111111111110001100000000000000000000000000000000011100110011111011111011111001111101111101110011001111101111101111100111110111110111001100111110111110111110011111011111011100110011111011111011111001111101111101111111001111101111101111100111110111110111111100111110111110111110011111011111011111110011111011111011111001111101111101111111001111101111101111100111110111110111111100111110111110111110011111011111011111110011111011111011111001111101111101111111001111101111101111100111110111110111111100111110111110111110011111011111011100110011111011111011111001111101111101110011001111101111101111100111110111110111001100000000000000000000000000000000011100111111111111111111111111111111111111100001111111111111111111111111111111111110000001111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

# print(int(list(my_string)))

bin_arr = [[1, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]]
bin_str = "" 
big_out_arr = []
new_arr = []
for sub_arr in bin_arr:
    for i,bin in enumerate(sub_arr):
        if i%3 == 0 and not i==0:
            new_arr.append(hex(int(bin_str, 2)))
            bin_str = "" + str(bin)
        else:
            bin_str = bin_str + str(bin)

    new_arr.append(hex(int(bin_str, 2)))
    big_out_arr.append(new_arr)
    new_arr = []

print(big_out_arr)
# Printing list using map
# print('[%s]' % ', '.join(map(str, new_arr)))