from pathlib import Path

current_path: Path = Path("/Users/milanstar/PycharmProjects/hillel_aqa_python/")


# print(current_path.parent) # на директорію вище
# print(current_path.name) # name of directory

# find files
# for some_obj in current_path.iterdir():
#     if some_obj.is_file():
#         print(some_obj)
#
# # find directories
# for some_obj in current_path.iterdir():
#     if some_obj.is_dir():
#         print(some_obj)
#         pass


lesson_13_dir: Path = Path.cwd() # поточна директорія
# print(lesson_13_dir)
# repository_dir = lesson_13_dir.parent
# print(repository_dir)
# bonus_lesson = repository_dir / "bonus_lesson"
#
#
# for obj in bonus_lesson.iterdir():
#     if obj.is_file():
#         print(obj.name)
#
#
# homework_file: Path = current_path / "homework_test.py"
# print(homework_file.is_dir()) # False
# print(homework_file.is_file()) # True
# print(homework_file.exists()) # чи файл або директорія існує (True)


# lesson_07: Path = lesson_13_dir.parent / "lesson_07"
# for obj in lesson_07.iterdir():
#     if obj.is_file() and obj.name == "exaMPLE.py":
#         print(obj)

all_directories: list[Path] = [obj for obj in Path.cwd().parent.iterdir() if obj.is_dir()]
# print(all_directories)


# repository_path: Path = Path.cwd().parent
# test_folder: Path = repository_path / "test_folder" / "inner_folder" / "test_folder"
# print(test_folder)
# test_folder.mkdir(parents=True, # parents - усі верхньорівневі директорії створити якщо їх немає
#                   exist_ok=True) # exist_ok - якщо папка вже існує то не треба помилки


# repository_path: Path = Path.cwd().parent
# lesson_04_dir: Path = repository_path / "lesson_04"
#
# xml_files: list[Path] = [file for file in lesson_04_dir.iterdir() if file.is_file() and file.suffix == ".xml"] # suffix це розширення
#
#
# print(xml_files)

print(Path.home()) # home directory


