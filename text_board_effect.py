word = input("Input a word: ")
width = int(input("Input a width (need to be > to word's length): "))
height = int(input("Input an height (>=3 and %2==1): "))-3

lines = "\n".join(["#" + " " * (width-2) + "#"] * int((height/2)))
spaces_prefix = int((width-len(word))/2)-1

print("\n".join(
    ["#"*width, lines, # 1 will print all first lines except the one with the word
    "#" + " " * spaces_prefix + word + " " * (width-spaces_prefix-len(word)-2) + "#", # 2 will print the word centered
    lines,"#"*width])) # 3 same as 1 reverted