import numpy as np

def raster_scan(video):
    """
    Converts a 3D video volume (with frames on the last axis) to a 2D
    matrix (with frames as rows, and pixels as columns).

    Parameters
    ----------
    video : array, shape (F, H, W)
        A NumPy array with F frames, H rows, and W columns.

    Returns
    -------
    matrix : array, shape (F, H * W)
        Raster-scanned (row-stacked) matrix where rows are frames.
    """
    b = np.reshape(video, (np.product(video.shape),)) # first we flatten the matrix 
    n_pixels = video.shape[1] * video.shape[2]
    n_frames = video.shape[0]

    matrix = np.reshape(b, (n_frames, n_pixels)) # Then we reshape it to the new dimensions 
    return matrix
