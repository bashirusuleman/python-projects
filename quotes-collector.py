new_quote = input("Enter your favourite quote: ") + "\n"



file = open("quotes.txt", 'a')
collected_quote = file.writelines(new_quote)
file.close()

file = open("quotes.txt", 'r')
collected_quote = file.readlines()
file.close()

print("All saved quotes:")
for index, quote in enumerate(collected_quote):
    print(f"{index + 1}.{quote}")