import os
import os.path
import xml.etree.ElementTree as ET
import csv
# from arcpy import CheckOutExtension
# arcpy.CheckOutExtension('Datareviewer')
# from arcpy import GeodatabaseSchemaCompare_Reviewer
# arcpy.env.overwriteOutput = True

print "arcpy imported"

base_gdb = r'C:\Users\Bennett\Documents\Testing\Base.gdb'
test_gdb = r'C:\Users\Bennett\Documents\Testing\Test.gdb'
output_dir = r'C:\Users\Bennett\Documents\Testing'

def parse_xml_to_csv(input_xml, output):
    output_csv = os.path.join(output,'differences.csv')
    with open(output_csv, 'w') as csvfile:
        fieldnames = ['Type', 'Category', 'Message', 'CatalogPath',
                      'FeatureDataset', 'ShapeType']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        tree = ET.parse(input_xml)
        root = tree.getroot()
        difference_tags = root.findall('.//Difference')
        for tag in difference_tags:
            elements = tag.findall('.//')
            print elements


def Schema_Compare(base, test, output):
    base_name = os.path.basename(base).split('.')[0]
    test_name = os.path.basename(test).split('.')[0]

    output_folder_name = "SchemaCompare_{}_to_{}".format(base_name, test_name)

    output_folder_location = os.path.join(output, output_folder_name)

    if not os.path.exists(output_folder_location):
        os.makedirs(output_folder_location)

    # result = GeodatabaseSchemaCompare_Reviewer(base, test, output_folder_location)
    # print result.getMessages()

    difference_xml = os.path.join(output_folder_location,'SchemaCompare','difference.xml')
    return difference_xml

differences = Schema_Compare(base_gdb, test_gdb, output_dir)
parse_xml_to_csv(differences, output_dir)