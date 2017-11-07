#you should first create directory of 'train' and 'test'
import os
from PIL import Image
from PIL import ImageDraw

from xml.etree import ElementTree

train_XML_src_dir = 'train.xml' #the path of train.xml
test_XML_src_dir = 'test.xml'

images_src_dir = 'img'

with open(test_XML_src_dir) as f:
    tree = ElementTree.parse(f)
count = 0

for node in tree.iter('image'):
    #img_name = [] # 记录保存图像名
    for each_image in node:
        if each_image.tag == 'imageName':
            img_name=each_image.text.split('/')[1] # 记录保存图像名

            tmp_img = Image.open( os.path.join(images_src_dir,img_name))

        if each_image.tag == 'taggedRectangles':
            
            # count the number of taggedRectangle
            x = []; y = []
            width = []; height = []
            for each_taggedRect in each_image:
                z=each_taggedRect.find('tag')
                count = count + 1
                tmp_dict = each_taggedRect.attrib # 获取坐标信息，得到的为字典
                x.append(tmp_dict['x']); tmp_x = int(tmp_dict['x'])
                y.append(tmp_dict['y']); tmp_y = int(tmp_dict['y'])
                width.append(tmp_dict['width']); tmp_w = int(tmp_dict['width'])
                height.append(tmp_dict['height']); tmp_h = int(tmp_dict['height'])
                zz=tmp_img.crop((tmp_x, tmp_y, tmp_x + tmp_w, tmp_y + tmp_h))
                zz.save(os.path.join('test',str(count)+'_'+z.text+'_.jpg'))
