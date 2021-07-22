file_builder = open("file builder/logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")

# file_builder.write("Hey, I'm in a file!")

file_builder.close()