text = input("Введіть рядок для аналізу: ")

vowels = "аеєиіїоуюяaueio"
consonants = "бвгґдзжйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

v_count = sum(1 for c in text.lower() if c in vowels)
c_count = sum(1 for c in text.lower() if c in consonants)
other_count = len(text) - v_count - c_count
total = len(text)

print("\n" + "=" * 42)
print(f"{'Категорія':<20} | {'Кількість':<8} | {'Частка':<8}")
print("-" * 42)
if total > 0:
    print(f"{'Голосні':<20} | {v_count:<8} | {v_count/total*100:>6.1f}%")
    print(f"{'Приголосні':<20} | {c_count:<8} | {c_count/total*100:>6.1f}%")
    print(f"{'Інші символи':<20} | {other_count:<8} | {other_count/total*100:>6.1f}%")
print("=" * 42)