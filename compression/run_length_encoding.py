import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        For efficiency, flatten the image by concatinating rows to create one long array, and
        compute run length encoding.
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        rle_code = [];
        width, height = binary_image.shape;
        for x in range(width):
            first = binary_image[x, 0];
            rle_code.append(first);
            c = 1;
            l = 0;
            for y in range(height):
                if (binary_image[x, y] == first):
                    if ((c == 1) and (y != 0)):
                        rle_code.append(l);
                    c = c + 1;
                    l = 0;
                else:
                    if ((l == 0) and (y != 0)):
                        rle_code.append(c - 1);
                    l = l + 1;
                    c = 1;
            if (l == 0):
                rle_code.append(c - 1);
            else:
                rle_code.append(l);

        return rle_code  # replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Since the image was flattened during the encoding, use the hight and width to reconstruct the image
        Reconstructs original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """

        re_image = np.zeros((height, width))
        x1, y1 = re_image.shape;
        row = 0;
        element1 = 0;
        column = 0;
        i = 0;
        while (i < len(rle_code) - 1):
            if ((rle_code[i] == 255) or (rle_code[i] == 0)):
                next_rle = i + 1;
                element = rle_code[i];
                while ((rle_code[next_rle] != 255) and (rle_code[next_rle] != 0) and (next_rle < len(rle_code) - 1)):
                    for num in range(0, int(rle_code[next_rle])):
                        re_image[row][column] = element;
                        if ((width - 1) > column):
                            column = column + 1;
                        else:
                            column = 0;
                            row = row + 1
                        element1 = element;
                    if (element1 == 0):
                        element = 255;
                    elif (element1 == 255):
                        element = 0;

                    next_rle = next_rle + 1;
            i = next_rle;
        return re_image  # replace zeros with image reconstructed from rle_Code





        




