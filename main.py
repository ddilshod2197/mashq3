ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingiz nechada? "))
shahar = input("Qaysi shaharda yashaysiz? ")

print("\nSiz haqingizda qisqacha ma'lumot:")
print(f"Ism: {ism}")
print(f"Yosh: {yosh}")
print(f"Shahar: {shahar}")

if yosh < 18:
    print("→ Siz hali yoshsiz!")
elif 18 <= yosh <= 30:
    print("→ Eng faol yoshdasiz! 🚀")
else:
    print("→ Tajribali odamsiz! 💪")
