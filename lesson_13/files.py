from pathlib import Path
filename = "test_file.txt"
filename_append = "test_file_append.txt"


# ------------------------------------ mode = "w" - перезаписує файл кожний раз
with open(filename, mode="w") as file:
    file.write("hello world")
    file.write("\nsecond line")
    file.write("\n\\n - next line enter\n")
    file.write(r'\n - "nextline" enter')
    file.write("\n\\n - next line enter")
    file.write(f"This file is {Path.cwd() / filename}")



# ------------------------------------ mode = "a" - НЕ перезаписує файл кожний раз
with open(filename_append, mode="a") as file:
    file.write("hello world")
    file.write("\nsecond line")
    file.write("\n\\n - next line enter\n")
    file.write(r'\n - "nextline" enter')
    file.write("\n\\n - next line enter")
    file.write(f"This file is {Path.cwd() / filename}")


# # ------------------------------------- mode = "r" - зчитування з файла
# with open(filename_append, mode="r") as file:
#     file_text = file.read()
#     print(file_text)

# ------------------------------------- mode = "r" - зчитування з файла
with open(filename_append, mode="r") as file:
    file_text: list[str] = file.readlines()
text = file_text
print(text)

# ------------------------------------ mode = "w" - перезаписує файл кожний раз
with open("test_test.txt", mode="w", encoding="utf-8") as file:
    file.writelines(text)