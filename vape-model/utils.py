import nibabel as nib
import matplotlib.pyplot as plt

def NII_image_shape(path):
    test_load = nib.load(f'{path}').get_fdata()
    return test_load.shape

def show_nii_3D(path):
    NII = nib.load(path).get_fdata()

    slice_x = int(NII.shape[0]/2)
    slice_y = int(NII.shape[1]/2)
    slice_z = int(NII.shape[2]/2)

    fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(10,4))
    ax1.imshow(NII[slice_x,:,:])
    ax1.set_title('X axis')
    ax1.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    ax2.imshow(NII[:,slice_y,:])
    ax2.set_title('Y axis')
    ax2.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    ax3.imshow(NII[:,:,slice_z])
    ax3.set_title('Z axis')
    ax3.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)

    print(f'for {path}')
    print(NII.shape)

    pass
