numbers = [8, 12, 3,"abc"]
numbertext = "8, 12, 3, abc"
for number in numbers:
    print(f"{str(number).split("abc")}")

number_list = numbertext.split("")
print(number_list)
    # print(number)
    # numbers = int(number)
    # print(number>3)
