import gmpy2
read_loc = "/Users/mac/Documents/python/all-image-generator/calc.txt"

def write_output_to_file(file_name, input):
    file = open("/path/to/file/"+file_name, 'w')
    file.write(str(input))

n_colors = 256
x_image = 1920
y_image = 1080

# Set the precision level (number of bits)
gmpy2.get_context().precision = 1000

# Perform calculations
a = gmpy2.mpz(n_colors) ** 3
b = gmpy2.mpz(x_image) * gmpy2.mpz(y_image)
c = a ** b

print("a:", a)
print("b:", b)

# I need to save a file because the number is pretty big
# write_output_to_file("calc.txt",c)

result = open(read_loc, "r").read()

digits = len(result)

result_e = (str(int(result[:2])/10))+"e"+str((digits-1))
print(result_e)