word = input("Input a word: ")
width = int(input("Input a width (need to be > to word's length): "))
height = int(input("Input an height (>=3 and %2==1): "))-3

lines = "\n".join(["#" + " " * (width-2) + "#"] * int((height/2)))
spaces_prefix = int((width-len(word))/2)-1

print("#"*width)
print(lines)
print("#" + " " * spaces_prefix + word + " " * (width-spaces_prefix-len(word)-2) + "#")
print(lines)
print("#"*width)