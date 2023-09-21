import os
import sys
import fitz

#PyMuPDF的版本为 1.18.14

def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath + str(pg) + ".png")
    pdf.close()




if __name__=='__main__':
    pdf_image(r"E:\\download\\铭湖健身数据分析.pdf", r"e:/temp/pdf_to_images/", 10, 10, 0)
