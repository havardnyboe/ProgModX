kjor = True
sum_input = 0

while kjor:
    br_input = int(input("Skriv inn et positivt tall: "))
    if br_input < 0:
        kjor = False
        break
    else:
        sum_input += br_input
        
print("\nSummen av tallene er {}\n".format(sum_input))