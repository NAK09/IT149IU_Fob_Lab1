amount = int(input("Amount (VND): "))

n500 = amount // 500000
amount %= 500000

n200 = amount // 200000
amount %= 200000

n100 = amount // 100000
amount %= 100000

n50 = amount // 50000

print(f"500,000 x {n500}")
print(f"200,000 x {n200}")
print(f"100,000 x {n100}")
print(f" 50,000 x {n50}")