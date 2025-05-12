import sys
import os


sys.path.append("/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/")

from lesson_17.connections import mobile

# wifi.connect_to_wifi()
sys.path.extend(['/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/work', '/Users/milanstar/PycharmProjects/hillel_aqa_python', '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm_display', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python313.zip', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload', '/Users/milanstar/PycharmProjects/hillel_aqa_python/.venv/lib/python3.13/site-packages', '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm_matplotlib_backend', '/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm_plotly_backend', '/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/'])
mobile.connect_through_mobile()
#
# """
# 🔸 Навіщо тоді __init__.py?
# 	1.	Для явного контролю: хочеш зробити з папки саме звичайний (а не namespace) пакет.
# 	2.	Щоб виконати код під час імпорту (наприклад, налаштувати логіку, імпортувати підмодулі).
# 	3.	Щоб визначити __all__ — які об’єкти будуть доступні при from my_package import *.
# 	4.	Сумісність зі старим кодом / інструментами, які очікують наявність __init__.py.
# """


# # from lesson_17.connections.wifi import port
# from lesson_17.connections import mobile as mb, cable
# from lesson_17.connections import wifi as wf
# from lesson_17.connections import cable as c
#
# mb.connect_through_mobile()
# # wf.connect_to_wifi()
# # c.connect_to_cable()
# print(port)
#
#
# from lesson_17.connections.mobile import connect_through_mobile
#
# connect_through_mobile()


# from lesson_17.connections.wifi import connect_to_wifi
# print(connect_to_wifi())


# from lesson_17.conneimport sys
# import os


# sys.path.append("/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/")
#
# from connections import mobile
#
# # wifi.connect_to_wifi()
# mobile.connect_through_mobile()
#
# """
# 🔸 Навіщо тоді __init__.py?
# 	1.	Для явного контролю: хочеш зробити з папки саме звичайний (а не namespace) пакет.
# 	2.	Щоб виконати код під час імпорту (наприклад, налаштувати логіку, імпортувати підмодулі).
# 	3.	Щоб визначити __all__ — які об’єкти будуть доступні при from my_package import *.
# 	4.	Сумісність зі старим кодом / інструментами, які очікують наявність __init__.py.
# """


# # from lesson_17.connections.wifi import port
# from lesson_17.connections import mobile as mb, cable
# from lesson_17.connections import wifi as wf
# from lesson_17.connections import cable as c
#
# mb.connect_through_mobile()
# # wf.connect_to_wifi()
# # c.connect_to_cable()
# print(port)
#
#
# from lesson_17.connections.mobile import connect_through_mobile
#
# connect_through_mobile()


# from lesson_17.connections.wifi import connect_to_wifi
# print(connect_to_wifi())

# sys.path.append('/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17')
# sys.path.append('/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/connections')
# sys.path.append('/Users/milanstar/PycharmProjects/hillel_aqa_python/lesson_17/work')
#
#
# print(sys.path)
#
# from connections import mobile
#
#
#
# mobile.connect_through_mobile()







