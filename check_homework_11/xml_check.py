import logging
import xmltodict

def return_incoming_grop_number(file_input: str, group_number: str):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console_handler)

    try:
        with open(file=file_input) as xml_file:
            data = xmltodict.parse(xml_file.read())
    except FileNotFoundError as e:
        logging.warning(f"{e}")
        return None

    found_group = False

    for number in (data['groups']['group']):
        if number['number'] == group_number:
            found_group = True
            try:
                incoming = number['timingExbytes']['incoming']
                logging.info(f"timingExbytes/incoming for group/number {group_number} is {incoming}")
                return incoming
            except KeyError as e:
                logging.info(f"timingExbytes/incoming for group/number {group_number} is empty")

    if not found_group:
        logging.warning(f"Group with number {group_number} not found.")
    return None
print(return_incoming_grop_number(file_input='xml_files/groups.xml', group_number='5'))