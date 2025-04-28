# def is_json_file_valid(file_path: str):
#     try:
#         with open("person_dict.json", "r") as json_file:
#             data = json.load(json_file)
#         print(f"Json file is validates succesfully: {file_path}")
#     except JSONDecodeError:
#         logger.error(f"File invalid!, file_path: {file_path}")
import logging
import xmltodict


def get_incoming_by_group_number(group_number: int) -> str:
    with open("tratata.xml", "r") as file:
        xml_string = file.read()
        xml_converted: dict = xmltodict.parse(xml_string)
        ...
        incoming_number: 7678783
        logging.info(f"Incoming number: {incoming_number} for group number {group_number}")