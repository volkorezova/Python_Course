# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
# і повернення значення timingExbytes/incoming результат виведіть у консоль
# через логер на рівні інфо

import logging
import xml.etree.ElementTree as ET

# logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_incoming_by_group_number(xml_file, group_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                logger.info(incoming.text)
                return incoming.text

    logger.info("Group or incoming not found")

get_incoming_by_group_number("groups.xml", 2)