import xmltodict

# ------------------------------------------- read xml as python dict
with open('files/homework.xml') as xml_file:
    data = xmltodict.parse(xml_file.read())

print(data)  # Весь XML як Python-словник