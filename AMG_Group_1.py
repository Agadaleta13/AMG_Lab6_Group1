def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_selection = input("Please enter an option: ")
        if menu_selection == "1":
            encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print(encoded_password)
        elif menu_selection == "2":
            original_password = decode(input("Please enter your password to decode: "))
            print(f"The encoded password is {encode(original_password)}, and the orignal password is {original_password}.")
        elif menu_selection == "3":
            exit()

def encode(input_text):
    result = []
    for char in input_text:
        temp_digit = (int(char) +3) % 10
        result.append(temp_digit)
    result_string = "".join(str(num) for num in result)
    return result_string
def decode(txt):
  r = ""
  for i in txt:
    r +=  str((int(i) - 3) % 10)
  return r
main()
