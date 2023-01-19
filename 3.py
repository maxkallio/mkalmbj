min_number = 0
max_number = 0

while True:
    try:
        number = input("Syöttäkää satunnainen numero: ")
        if number == "":
            break

        else:
            number = int(number)
            if max_number > number > min_number:
                pass
            if number > max_number:
                max_number = number

            if number < min_number:
                min_number = number

            continue

    except:
        print("Syötetty numero on virheellinen")
        continue

print(f"Pienin numero {min_number}")
print(f"Isoin numero {max_number}")
