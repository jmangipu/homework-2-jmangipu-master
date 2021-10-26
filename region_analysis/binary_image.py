import numpy as np

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        width, height = image.shape
        for i in range(width):
            for j in range(height):
                k = image[i,j]
                hist[k] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal.
        takes as input
        hist: a histogram
        returns: an optimal threshold value (otsu's threshold)"""

        def mean_calculation(a, b, hist):
            total = 0
            sum_of_freq = sum(hist[a:b])
            if sum_of_freq == 0:
                return 0
            else:
                for i in range(a, b):
                    total = total + (hist[i] * i)
                return total / sum_of_freq

        def variance_calculation(a, b, hist, m):
            var = 0
            if sum(hist[a:b]) == 0:
                return 0
            else:
                for i in range(a, b):
                    var = var + (((i - m) ** 2) * hist[i])
                return var / sum(hist[a:b])

        def weight_calculation(a, b, hist):
            weight = 0
            for i in range(a, b):
                weight = sum(hist[a:b]) / sum(hist)
            return weight

        f_values = [0] * len(hist)
        for i in range(0, len(hist)):
            mean1 = mean_calculation(0, i, hist)
            mean2 = mean_calculation(i, len(hist), hist)
            variance1 = variance_calculation(0, i, hist, mean1)
            variance2 = variance_calculation(i, len(hist), hist, mean2)
            weight1 = weight_calculation(0, i, hist)
            weight2 = weight_calculation(i, len(hist), hist)
            f = (weight1 * variance1) + (weight2 * variance2)
            f_values[i] = f

        min_value_pos = f_values.index(min(f_values))
        threshold = min_value_pos



        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        Make calls to the compute_histogram and find_otsu_threshold methods as needed.
        takes as input
        image: an grey scale image
        returns: a binary image"""
        optimumthreshold = 0
        bin_img = image.copy()
        width, height = bin_img.shape
        print(width, height)
        for i in range(width):
            for j in range(height):
                if bin_img[i, j] < optimumthreshold:
                    bin_img[i, j] = 255
                else:
                    bin_img[i, j] = 0

        return bin_img


