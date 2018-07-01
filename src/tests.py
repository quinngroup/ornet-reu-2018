import unittest
import numpy as np
import sys
sys.path.insert(0, '/Users/mojtaba/Downloads/ornet-reu-2018-master-2/src')
import raster_scan2 as raster_scan
import read_video

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

    
    def test_rasterscan_real(self):
        
        y = read_video.read_video('/Users/mojtaba/Desktop/OrNet Project/DAT VIDEOS/LLO/DsRed2-HeLa_2_21_LLO_Cell0.mov')
        y = np.array(y[1:])
        # Because of the output format of "read_video" module, we need to slice the "y"
        y = y[0,:,:,:]
        yt = self.manual_scan(y)
        yp = raster_scan.raster_scan(y)
        
        np.testing.assert_array_equal(yp, yt)

if __name__ == '__main__':
    unittest.main()
