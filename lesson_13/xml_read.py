import xmltodict
from pprint import pprint

"""
XML (eXtensible Markup Language) — це формат текстових файлів для збереження та передачі структурованих даних.
Він виглядає як HTML, але не для відображення сторінок, а для зберігання даних у структурі “дерева”
- Передача даних між системами
- Конфігураційні файли Налаштування тестів, середовищ, даних часто описуються через XML (testng.xml в Java, Jenkins-пайплайни)
- Репорти тестування
- Тестові дані
"""
# ------------------------------------------- read xml file as python dict
# with open('files/xmlfile.xml') as xml_file:
#     xml_string = xml_file.read()
#     data = xmltodict.parse(xml_string)
#
# pprint(data['soapenv:Envelope']['soapenv:Body']["myg:GetAccountMovementsRequestIo"]["myg:accountMovementFilterIo"]["myg:accountNumber"])  # Весь XML як Python-словник

xml_string: str = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:myg="http://www.mygemini.com/schemas/mygemini"
                  xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soapenv:Header>
        <wsse:Security>
            <wsse:UsernameToken>
                <wsse:Username>******</wsse:Username>
                <wsse:Password>******</wsse:Password>
                <wsse:Nonce>******</wsse:Nonce>
            </wsse:UsernameToken>
        </wsse:Security>
    </soapenv:Header>
    <soapenv:Body>
        <myg:GetAccountMovementsRequestIo>
            <myg:accountMovementFilterIo>
                <myg:pager>
                    <myg:pageIndex>0</myg:pageIndex>
                    <myg:pageSize>700</myg:pageSize>
                </myg:pager>
                <myg:accountNumber>GE16TB7739436090000001</myg:accountNumber>
                <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
                <myg:periodFrom>2025-03-19T00:00:00</myg:periodFrom>
                <myg:periodTo>2025-03-20T23:00:00</myg:periodTo>
            </myg:accountMovementFilterIo>
        </myg:GetAccountMovementsRequestIo>
    </soapenv:Body>
</soapenv:Envelope>"""


# ------------------------------------------- read xml string as python dict
# xml_converted_to_dict: dict = xmltodict.parse(xml_string)
# pprint(xml_converted_to_dict)

# ------------------------------------------- write xml from python dict
data: dict = {
    "root": {
        "child": "Hello from dict!",
        "name": "Semen",
        "age": 0.5
    }
}

xml_string = xmltodict.unparse(data, pretty=True)

with open('files/output.xml', 'w') as xml_file:
    xml_file.write(xml_string)

