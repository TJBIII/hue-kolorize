import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

def get_colors(img, n_colors):
    """ Use KMeans clustering to get ``n_colors`` cluster centers from the provided image.

    Parameters:
        img: Pillow image object
        n_colors (int): number of clusters to form and centroids to generate (final colors)

    Returns:
        tuple: cluster centers and the dominant color from the image
    """

    # normalize rgb values between [0, 1] instead of the default 8 bit integer values
    img = np.array(img, dtype=np.float64) / 255

    # load image and transform to a 2D numpy array
    w, h, d = original_shape = tuple(img.shape)
    assert d == 3
    image_array = np.reshape(img, (w * h, d))

    # fit model on small sample of the image data
    t0 = time()
    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array_sample)

    # now convert back to 8 bit [0, 255] rgb value
    cluster_centers = [center * 255 for center in kmeans.cluster_centers_]
    print("fitting model took %0.3fs." % (time() - t0))

    # find most dominant color
    labels = kmeans.predict(image_array_sample)
    counts = np.bincount(labels)
    dominant_color = cluster_centers[np.argmax(counts)]

    return (cluster_centers, dominant_color)
