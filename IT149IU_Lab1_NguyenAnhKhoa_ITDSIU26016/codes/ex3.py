left_operands = [-5, 0, 5, 7.5]

print("1. Compare / vs // on negative numbers:")
print(f"{'-5 / 2':<10} = {-5 / 2}")
print(f"{'-5 // 2':<10} = {-5 // 2}")

print("\n2. Square roots via exponent (a ** 0.5):")
for a in left_operands:
    if a >= 0:
        print(f"sqrt({a:<4}) = {a ** 0.5:.4f}")
    else:
        print(f"sqrt({a:<4}) = {a ** 0.5}")

print("\n3. Formatted table using f-strings:")
print(f"{'a':>6} | {'a+2':>7} | {'a-2':>7} | {'a*2':>7} | {'a/2':>7} | {'a//2':>7} | {'a**2':>7}")
print("-" * 60)
for a in left_operands:
    print(f"{a:6.1f} | {a+2:7.2f} | {a-2:7.2f} | {a*2:7.2f} | {a/2:7.2f} | {a//2:7.2f} | {a**2:7.2f}")