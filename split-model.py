import pysd
import re
import argparse
import xml.etree.ElementTree as ET
from lib.xmile import clean_xmile
import logging
logging.basicConfig(format='%(name)s:%(levelname)s:%(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("xmile_file", help="Filename of XMILE-file to parse", type=argparse.FileType('r', encoding="utf-8"))
args = parser.parse_args()

ET.register_namespace('', 'http://docs.oasis-open.org/xmile/ns/XMILE/v1.0')
ET.register_namespace('isee', 'http://iseesystems.com/XMILE')
ns = {
    'xmile': 'http://docs.oasis-open.org/xmile/ns/XMILE/v1.0',
    'isee': 'http://iseesystems.com/XMILE',
}

model_tree = ET.parse(args.xmile_file)
model_root = model_tree.getroot()

new_modelname_array = []
for model in model_root.findall('.//xmile:model[@name]', ns):
    new_modelname_array.append(model.attrib["name"])

# Split files
for new_model_name in new_modelname_array:
    args.xmile_file.seek(0, 0)
    submodel_tree = ET.parse(args.xmile_file)
    submodel_root = submodel_tree.getroot()

    for model in submodel_root.findall('.//xmile:model', ns):
        if "name" in model.attrib.keys() :
            if model.attrib["name"] != new_model_name:
                submodel_root.remove(model)
        else:
            submodel_root.remove(model)

        for child in model:
            if child.tag == "xmile:views":
                model.remove(child)

    ofn = 'tmp/test-%s.xmile' % (new_model_name.lower())

    submodel_tree.write(ofn,
        xml_declaration = True,
        encoding = 'utf-8',
        method = 'xml')

    try:
        cfn = clean_xmile(ofn)
        model = pysd.read_xmile(cfn)
        print("{0}: OK".format(new_model_name))
    except Exception as ex:
        print ("{0}: Error ({1})".format(new_model_name, ex))



# model = pysd.read_xmile('test.xmile')
# print(model.doc())
# stocks = model.run()
# print (stocks)