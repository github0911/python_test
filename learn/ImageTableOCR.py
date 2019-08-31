# -*- coding: utf-8 -*-
import cv2
import pytesseract
import numpy as np

# 识别图片通过opencv
class ImageTableOCR(object):

    def __init__(self, imagePath):
        self.image = cv2.imread(imagePath, 1)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BAYER_BG2GRAY)


    def horizontal_line_detect(self):
        # 图像二值化
        ret,thresh1 = cv2.threshold(self.gray, 240, 255, cv2.THRESH_BINARY)
        # 进行两次中值滤波
        blur = cv2.medianBlur(thresh1, 3)
        # 模板大小 3*3
        blur = cv2.medianBlur(blur, 3)
        h, w = self.gray.shape
        # 横向直线列表
        horizontal_lines = []
        for i in range(h - 1):
            if abs(np.mean(blur[i, :])- np.mean(blur[i + 1, :])) > 120:
                horizontal_lines.append([0, i, w, i])
                cv2.line(self.image, (0, i), (w, i), (0, 255, 0), 2)
                horizontal_lines = horizontal_lines[1:]
        return horizontal_lines

    def vertical_line_detect(self):
        edges = cv2.Canny(self.gray, 30, 240)
        min_line_length = 500
        max_line_gap = 30
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, min_line_length, max_line_gap).toList()
        lines.append([[13, 937, 13, 102]])
        lines.append([[756, 937, 756, 102]])
        sorted_lines = sorted(lines,key= lambda x: x[0])
        vertical_lines = []
        for line in sorted_lines:
            for x1, y1, x2 y2 in line:
                if x1 == x2
                print(line)
                vertical_lines.append(x, y1, x2, y2)
                cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        return vertical_lines