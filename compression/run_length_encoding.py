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
        rle_code = [];
        width, height = binary_image.shape;
        for x in range(width):
            fir = binary_image[x, 0];
            rle_code.append(fir);
            count = 1;
            lk = 0;
            for y in range(height):
                if (binary_image[x, y] == fir):
                    if ((count == 1) and (y != 0)):
                        rle_code.append(lk);
                    count = count + 1;
                    lk = 0;
                else:
                    if ((lk == 0) and (y != 0)):
                        rle_code.append(count - 1);
                    lk = lk + 1;
                    count = 1;
            if (lk == 0):
                rle_code.append(count - 1);
            else:
                rle_code.append(lk);

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
        re_image = np.zeros((height, width))
        x1, y1 = re_image.shape;
        r1 = 0;
        ele1 = 0;
        c1 = 0;
        i = 0;
        while (i < len(rle_code) - 1):
            if ((rle_code[i] == 255) or (rle_code[i] == 0)):
                next_rle = i + 1;
                ele = rle_code[i];
                while ((rle_code[next_rle] != 255) and (rle_code[next_rle] != 0) and (next_rle < len(rle_code) - 1)):
                    for num in range(0, int(rle_code[next_rle])):
                        re_image[r1][c1] = ele;
                        if ((width - 1) > c1):
                            c1 = c1 + 1;
                        else:
                            c1 = 0;
                            r1 = r1 + 1
                        ele1 = ele;
                    if (ele1 == 0):
                        ele = 255;
                    elif (ele1 == 255):
                        ele = 0;

                    next_rle = next_rle + 1;
            i = next_rle;
        return re_image