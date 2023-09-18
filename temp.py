import os

dir = './mask/label_img'
imgList = os.listdir(dir)
#print(imgList)
imgList.sort(key=lambda x: int(x.replace("frame", "").split('.')[0]))  # 按照数字进行排序后按顺序读取文件夹下的图片
print(imgList)
for count in range(0, len(imgList)):
    im_name = imgList[count]
    im_path = os.path.join(dir, im_name)
    print(im_path)