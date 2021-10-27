import numpy as np
class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        For efficiency, flatten the image by concatinating rows to create long array.
        Compute run length encoding on the long array.
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        rle_code = []
        for i in binary_image:
            c = 0
            initial_value = i[0]
            rle_code.append(initial_value)
            for k in i:
                if k == initial_value:
                    c = c + 1
                else:
                    rle_code.append(c)
                    c = 1
                    initial_value = k
            rle_code.append(c)

        return rle_code
        #return np.zeros(100)  # replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Since the image was flattened during the encoding, use the hight and width to reconstruct the image
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        l1 = []
        l2 = []
        l3 = []
        final = np.zeros([height, width])
        i = 0
        r1 = 0
        c1 = 0
        c = 0
        for k in rle_code:
            if k == 255 or k == 0:
                l1.append(k)
                l3.append(l2)
                l2 = []
            else:
                l2.append(k)
        l3 = l3[1:]
        for k in l3:
            value = l1[i]
            for h in k:
                while c < h:
                    final[r1, c1] = value
                    c1 = c1 + 1
                    c = c + 1
                if value == 255:
                    value = 0
                    c = 0
                else:
                    value = 255
                    c = 0
            r1 = r1 + 1
            i = i + 1
            c1 = 0
        #return  np.zeros((100,100), np.uint8)  # replace zeros with image reconstructed from rle_Code
        return final
