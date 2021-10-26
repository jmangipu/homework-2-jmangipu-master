import cv2
import numpy as np

class CellCounting:
    def __init__(self):
        pass
    region_stat = {};
    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window and assigns region names
        takes a input:
        image: binary image
        return: a list/dict of regions"""
        width, height = image.shape;
        k = 1;
        regions = np.zeros((width, height), np.uint32)
        for y in range(0, height):
            for x in range(0, width):
                if (image[x, y] == 255):
                    if (((x - 1) >= 0) and ((y - 1) >= 0)):
                        if ((image[x - 1, y] == 0) and (image[x, y - 1] == 0)):
                            regions[x, y] = k;
                            k = k + 1;
                        if ((image[x - 1, y] == 255) and (image[x, y - 1] == 0)):
                            regions[x, y] = regions[x - 1, y];
                        if ((image[x - 1, y] == 0) and (image[x, y - 1] == 255)):
                            regions[x, y] = regions[x, y - 1];
                        if ((image[x - 1, y] == 255) and (image[x, y - 1] == 255)):
                            regions[x, y] = regions[x, y - 1];
                            if (regions[x - 1, y] != regions[x, y - 1]):
                                regions[x - 1, y] = regions[x, y - 1];
                                b = 2;
                                f = 0;
                                while f == 0:
                                    if image[x - b, y] != 0:
                                        regions[x - b, y] = regions[x - b + 1, y]
                                        b = b + 1
                                    else:
                                        f = 1
                    if ((x == 0) and (y != 0)):
                        if ((image[x, y - 1]) == 0):
                            regions[x, y] = k;
                            k = k + 1;
                        if(regions[x,y-1]>0):
                            regions[x, y] = regions[x, y - 1];

                    if ((x != 0) and (y == 0)):
                        if ((image[x - 1, y]) == 0):
                            regions[x, y] = k;
                            k = k + 1;
                        if(regions[x-1,y]>0):
                            regions[x, y] = regions[x - 1, y];

        # pixels count
        count = [0] * k;
        for x in range(0, width):
            for y in range(0, height):
                if (regions[x, y] > 0):
                    count[regions[x, y]] = count[regions[x, y]] + 1;

        # regions
        coordinates = {};
        for x in range(0, width):
            for y in range(0, height):
                if regions[x, y] != 0:
                    if regions[x, y] in coordinates:
                        coordinates[regions[x, y]].append([x, y]);
                    else:
                        coordinates[regions[x, y]] = [[x, y]];

        # centroid
        index = 1;
        for a in coordinates.keys():
            first = 0;
            for coord in coordinates[a]:
                if (first == 0):
                    x1 = coord[0];
                    x2 = coord[0];
                    y1 = coord[1];
                    y2 = coord[1];
                    first = 1;
                else:
                    if (x1 > coord[0]):
                        x1 = coord[0];
                    elif (x2 < coord[0]):
                        x2 = coord[0];
                    if (y1 > coord[1]):
                        y1 = coord[1];
                    elif (y2 < coord[1]):
                        y2 = coord[1];
            x_difference = x2 - x1
            Xcenter = x1 + (x_difference / 2)
            y_difference = y2 - y1
            Ycenter = y1 + (y_difference / 2)
            index = index + 1;
            if (len(coordinates[a]) > 15):
                self.region_stat[index] = [a, len(coordinates[a]), [Xcenter, Ycenter]]
        # stats printing
        for a in self.region_stat.keys():
            print("Region, Area, Centroid:", self.region_stat[a])

                   
                    
        regions = dict()

        return regions

    def compute_statistics(self, region):
        """Computes cell statistics area and location
        takes as input
        region: list regions and corresponding pixels
        returns: stats"""
        stats = self.region_stat

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text. 
        takes as input
        image: Input binary image
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for key in stats.keys():
            cv2.putText(image, '*' + repr(stats[key][0])+ ',' +repr(stats[key][1]), (int(stats[key][2][1]), int(stats[key][2][0])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.3, 100)
        return image

