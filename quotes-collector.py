new_quote = input("Enter your favourite quote: ") + "\n"



with open("quotes.txt", 'a') as file:
    collected_quote = file.writelines(new_quote)


with open("quotes.txt", 'r') as file:
    collected_quote = file.readlines()


print("All saved quotes:")
for index, quote in enumerate(collected_quote):
    print(f"{index + 1}.{quote}")