import json
import xml.etree.ElementTree as ET
import os

def json2customxml(j_dir,x_dir,files):
    with open(j_dir+files, 'r') as f:
        data = json.load(f)

    # Create the root element of the XML document
    root = ET.Element('annotation')

    # Create the folder element and set its value
    folder = ET.SubElement(root, 'folder')
    folder.text = 'images'

    filename = ET.SubElement(root, 'filename')
    filename.text = data['imagePath']
    size = ET.SubElement(root, 'size')

    width = ET.SubElement(size, 'width')
    width.text = str(data['imageWidth'])
    height = ET.SubElement(size, 'height')
    height.text = str(data['imageHeight'])
    depth = ET.SubElement(size, 'depth')
    depth.text = '3'


    segmented = ET.SubElement(root, 'segmented')
    segmented.text = '0'

    # Iterate over the shapes in the JSON data
    for shape in data['shapes']:

        obj = ET.SubElement(root, 'object')

        name = ET.SubElement(obj, 'name')
        name.text = shape['label']

        pose = ET.SubElement(obj, 'pose')
        pose.text = 'Unspecified'

        truncated = ET.SubElement(obj, 'truncated')
        truncated.text = '0'

        occluded = ET.SubElement(obj, 'occluded')
        occluded.text = '0'

        difficult = ET.SubElement(obj, 'difficult')
        difficult.text = '0'

        bndbox = ET.SubElement(obj, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        xmax = ET.SubElement(bndbox, 'xmax')
        ymin = ET.SubElement(bndbox, 'ymin')
        ymax = ET.SubElement(bndbox, 'ymax')
        # print(float(shape['points'][0][0]))
        # print(float(shape['points'][1][0]))
        # print(float(shape['points'][1][0]))
        # print(float(shape['points'][1][1]))
        if (float(shape['points'][0][0]) >= float(shape['points'][1][0])):
            xmin.text = str(shape['points'][1][0])
            xmax.text = str(shape['points'][0][0])
        else:
            xmin.text = str(shape['points'][0][0])
            xmax.text = str(shape['points'][1][0])


        if (float(shape['points'][0][1]) >= float(shape['points'][1][1])):
            ymin.text = str(shape['points'][1][1])
            ymax.text = str(shape['points'][0][1])
        else:
            ymin.text = str(shape['points'][0][1])
            ymax.text = str(shape['points'][1][1])
    output = files.replace('json','')
    ET.ElementTree(root).write(x_dir+output+'xml')

if __name__ == '__main__':

    # transfer multi files
    # pre-processing:
    j_dir = r"D:\\Python_learning\\NYCU_DL\\Deep_learning\\Mask_Project\\dataset\\json\\"
    x_dir = r"D:\\Python_learning\\NYCU_DL\\Deep_learning\\Mask_Project\\dataset\\xml\\"
    files = os.listdir(j_dir)
    for file in files:
        file_list=file.split(".")
        if(file_list[-1] == 'json'):
            json2customxml(j_dir,x_dir,file)
