import os

folder = "my_test_files"
print("--- Запуск шифровальщика ---")
if os.path.exists(folder):
    for name in os.listdir(folder):
        if name.endswith(".txt"):
            old_path = os.path.join(folder, name)
            new_path = old_path + ".LOCKED"
            os.rename(old_path, new_path)
            print(f"Файл {name} -> ЗАБЛОКИРОВАН")
else:
    print(f"Ошибка: папка {folder} не найдена!")

print("--- Конец симуляции ---")
