"""створіть функцію
пошуку по group/number і повернення значення timingExbytes/incoming
результат виведіть у консоль через логер на рівні інфо
"""

import pprint

import xmltodict
from pathlib import Path
import logging

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(logging.INFO)

# Створення обробника для виводу в stdout
console_handler = logging.StreamHandler()

# Налаштування рівня логування для обробника
console_handler.setLevel(logging.INFO)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Додавання обробника до логера
logger.addHandler(console_handler)

path_to_xml = Path("xml_files/groups.xml")


def open_xml(xml_path):
    with open(xml_path, "r") as file:
        xml_string = file.read()
        xml_converted: dict = xmltodict.parse(xml_string)
        return xml_converted


# pprint.pprint(open_xml(path_to_xml))


data = open_xml(path_to_xml)

groups = data["groups"]["group"]


# print(groups)


def get_incoming_by_group_number(xml: str, number_in_group):
    for xml_group in groups:
        number = xml_group.get("number")
        if str(number) == str(number_in_group):
            timing_exbyte = xml_group.get("timingExbytes")
            if "incoming" in timing_exbyte:
                incoming_number = timing_exbyte["incoming"]
                logger.info(f"incoming number in group with number: {number_in_group}, is {incoming_number}")
                # print(incoming_number)


get_incoming_by_group_number(groups, 0)