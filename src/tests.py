import unittest

import numpy as np

import raster_scan2 as raster_scan

class RasterTest(unittest.TestCase):

    def manual_scan(self, video):
        """
        Manual, loop-based implementation of raster scanning.
        (reference implementation)
        """
        frames, height, width = video.shape
        raster = np.zeros(shape = (frames, height * width))

        for index, frame in enumerate(video):
            raster[index] = frame.flatten()

        return raster

    def test_rasterscan1(self):
        y = np.arange(18).reshape((3, 3, 2))
        yt = self.manual_scan(y)
        yp = raster_scan.raster_scan(y)

        np.testing.assert_array_equal(yp, yt)
