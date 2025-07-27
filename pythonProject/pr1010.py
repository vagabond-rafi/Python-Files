line1 = input().split()
line2 = input().split()

qty1 = int(line1[1])
price1 = float(line1[2])

qty2 = int(line2[1])
price2 = float(line2[2])

total = (qty1*price1) + (qty2*price2)

print(f"VALOR A PAGAR: R$ {total:.2f}")