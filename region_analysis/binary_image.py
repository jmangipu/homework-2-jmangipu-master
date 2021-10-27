import numpy as np
class BinaryImage:
    def __init__(self):
        pass

    def mean(self, l):
        q = sum(l)
        if (q == 0):
            return 0
        result = 0
        for i in range(0, len(l)):
            result = result + ((i * l[i]) / q)
        return result

    def var(self, l, result):
        q = sum(l)
        if (q == 0):
            return 0
        vs = 0
        for i in range(0, len(l)):
            vs = vs + (((i - result) ** 2) * l[i]) / q
        return vs
    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""
        hist = [0]*256
        r1 = image.shape[0]
        c1 = image.shape[1]
        x = np.zeros(256)
        for i in range(256):
            c = 0
            for j in range(r1):
                for q in range(c1):
                    if(image[j,q]==i):
                        c+=1
                x[i] =c
        return x

    def find_otsu_threshold(self, hist):
        """analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal.
        takes as input
        hist: a histogram
        returns: an optimal threshold value (otsu's threshold)"""

        threshold = 0
        minimum = 10000000000
        length = len(hist)
        for i in range(0,length):
            p = self.mean(hist[0:i+1])
            s = self.var(hist[0:i+1], p)
            o = sum(hist[0:i+1])
            xl = self.mean(hist[i+1:length])
            yl = self.var(hist[i+1:length],xl)
            zl = sum(hist[i+1:length])
            Res = (s*o)+(yl*zl)
            if(minimum>Res and Res!=0):
                minimum = Res
                threshold = i

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        Make calls to the compute_histogram and find_otsu_threshold methods as needed.
        take as input
        image: an grey scale image
        returns: a binary image"""

        hist = self.compute_histogram(image)
        thresh = self.find_otsu_threshold(hist)

        binary_image = image.copy()
        r1 = binary_image.shape[0]
        c1 = binary_image.shape[1]
        for i in range(0, r1):
            for j in range(0, c1):
                if (binary_image[i, j] < thresh):
                    binary_image[i, j] = 255
                else:
                    binary_image[i, j] = 0
        return binary_image
