import numpy as np
import cv2

class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""
        r1, c1 = np.shape(image)
        k_val = np.zeros((r1, c1))
        s = 1
        for i in range(0, r1):
            for j in range(0, c1):
                if i == 0 and j == 0:
                    if image[i][j] == 255:
                        k_val[i][j] = s
                        s = s+1
                elif i == 0:
                    if image[i][j] == 255:
                        if image[i][j-1] == 255:
                            k_val[i][j] = k_val[i][j-1]
                        else:
                            k_val[i][j] = s
                            s = s+1
                elif j == 0:
                    if image[i][j] == 255:
                        if image[i-1][j] == 255:
                            k_val[i][j] = k_val[i-1][j]
                        else:
                            k_val[i][j] = s
                            s = s + 1
                elif image[i-1][j] == 0 and image[i][j-1] == 0 and image[i][j] == 255:
                    k_val[i][j] = s
                    s = s+1
                elif image[i-1][j] == 255 and image[i][j-1] == 0 and image[i][j] == 255:
                    k_val[i][j] = k_val[i-1][j]
                elif image[i-1][j] == 0 and image[i][j-1] == 255 and image[i][j] == 255:
                    k_val[i][j] = k_val[i][j-1]
                elif image[i-1][j] == 255 and image[i][j-1] == 255 and image[i][j] == 255:
                    k_val[i][j] = k_val[i-1][j]
                    if k_val[i][j-1] != k_val[i-1][j]:
                        x = i
                        y = j
                        while image[x, y] == 255:
                            y = y - 1
                            if image[x, y] != 0:
                                A = x
                                B = y
                                k_val[x, y] = k_val[i, j]
                                while image[A, B] == 255:
                                    A = A - 1
                                    if image[A, B] != 0:
                                        k_val[A, B] = k_val[x, y]
                        s = s - 1
        return k_val

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: list regions and corresponding pixels
        returns: stats"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)
        statistics_1 = {}
        r1, c1 = region.shape
        for i in range(r1):
            for j in range(c1):
                if region[i][j] not in statistics_1:
                    statistics_1[region[i][j]] = 1
                else:
                    statistics_1[region[i][j]] = statistics_1[region[i][j]] + 1

        statistics = {}
        for key, value in statistics_1.items():
            if key != 0.0 and value > 15:
                statistics[key] = value
        lp = {}
        for key, value in statistics.items():
            x_cor = 0
            y_cor = 0
            countvalue = 0
            for i in range(r1):
                for j in range(c1):
                    if region[i][j] !=0:
                        if key == region[i][j]:
                            x_cor = x_cor + i
                            y_cor = y_cor + j
                            countvalue = countvalue + 1
            lp[key] = (round(x_cor/countvalue), round(y_cor/countvalue))

        return statistics, lp

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text.
        takes as input
        image: Input binary image
        stats: stats regarding location and area
        returns: image marked with center and area"""
        dict1 = {}
        dict2 = {}
        dict1 = stats[0]
        dict2 = stats[1]

        for key, value in dict1.items():
            print("Region: " + str(round(key)) + ",Area: " + str(dict1[key]) + ",Centroid: " + str(dict2[key]))

        image1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        for key, value in dict1.items():
            (y, x) = (dict2[key][1], dict2[key][0])
            image = cv2.circle(image1, (y, x), 1, (0, 0, 255), 1)
            image = cv2.putText(image1, str(round(key)) + ", " + str(dict1[key]), (y+2, x+2), cv2.FONT_HERSHEY_SIMPLEX, 0.2,
            (0, 0, 0), 1)
        return image
