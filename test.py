import numpy as np
import skimage as ski
import medialaxis3d
import napari

rng = np.random.default_rng(1278)

image = ski.data.binary_blobs(length = 128,
                              blob_size_fraction = 0.2,
                              n_dim = 3,
                              volume_fraction = 0.6,
                              rng = rng)

skeleton, distance = medialaxis3d.medial_axis_3d(image, return_distance = True, size = 8, rng = rng)

viewer = napari.Viewer()
viewer.add_image(image.astype(bool),
                 rendering = "attenuated_mip",
                 attenuation = 0.5,
                 scale = [1, 1, 1])
viewer.add_image(skeleton.astype(bool),
                 interpolation3d = "nearest",
                 colormap = "magenta",
                 scale = [1, 1, 1])
viewer.add_image(((skeleton*distance) / (skeleton*distance).max() * 255).astype(np.uint8),
                 interpolation3d = "nearest",
                 colormap = "turbo",
                 scale = [1, 1, 1])
napari.run()
