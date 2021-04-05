import cv2
import numpy as np 
import os

# 定义待批量裁剪图像的路径地址
image_input_path = 'C:/Users/Liu Group/Desktop/image/'   #输入图像文件夹位置
image_output_path = 'C:/Users/Liu Group/Desktop/imageoutput/' #输出图像文件夹位置
def read_path(file_pathname,file_out_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        #print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        cropImg = img[0:769,0:1024] #修改裁剪区域，先y方向，后x方向
        cv2.imwrite(image_output_path+'/'+filename,cropImg)
        #print(img)
    print('----------all works down----------')
        #cv2.namedWindow("Image")
        #cv2.imshow("Image",img)
        #cv2.waitKey(0)
        # #释放窗口
        #cv2.destroyAllWindows()
# 主程序        
if __name__ == "__main__":
    read_path(image_input_path,image_output_path)
    #print(img)
