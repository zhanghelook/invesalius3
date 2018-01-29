import os
import SimpleITK as sitk
import numpy as np
import skimage.color
import skimage.io

OUT_DIR = "./out/"
INPUT_RAW_FILE = "E:\\Workspace\\Archaic\\Holoeyes\\Data\\Results@160x\\raw\\Train\\Case48_result.mhd"


def raw2png(raw_file):
    print "Convert raw2png ..."

    itkimage = sitk.ReadImage(raw_file)

    # Convert the image to a numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    ct_scan = sitk.GetArrayFromImage(itkimage)
    # Read the origin of the ct_scan, will be used to convert the coordinates from world to voxel and vice versa.
    origin = np.array(list(reversed(itkimage.GetOrigin())))
    # Read the spacing along each dimension
    spacing = np.array(list(reversed(itkimage.GetSpacing())))

    raw = skimage.io.imread(raw_file, plugin='simpleitk')
    print "Shape: ", raw.shape

    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    # Save series of images here
    for z in range(0, raw.shape[0]):
        # print raw[z]
        # img = skimage.color.rgb2gray(raw[z])
        img = raw[z]
        skimage.io.imsave(OUT_DIR + "%d.png" % z, img, plugin='simpleitk')

        # np.savetxt(OUT_DIR + "%d.csv" % z, img, delimiter=",")

    # # Convert raw value to colored image
    # target_png = scipy.misc.toimage(
    #     pixel_array,
    #     cmin=0,
    #     cmax=1).convert(mode=1)  # .convert(mode='RGB')

    # Save pixels as PNG
    # target_png.save(OUT_DIR + "segmented.png")


# Run conversion
raw2png(INPUT_RAW_FILE)
