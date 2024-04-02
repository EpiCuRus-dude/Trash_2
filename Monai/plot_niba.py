import nibabel as nib
import matplotlib.pyplot as plt

def plot_nifti_slices(nifti_file, slice_indices, axis=0):
    
    nifti_image = nib.load(nifti_file)

    
    image_data = nifti_image.get_fdata()

    
    fig, axes = plt.subplots(1, len(slice_indices), figsize=(15, 5))
    for i, slice_index in enumerate(slice_indices):
        if axis == 0:
            slice_data = image_data[slice_index, :, :]
        elif axis == 1:
            slice_data = image_data[:, slice_index, :]
        else:
            slice_data = image_data[:, :, slice_index]
        
        ax = axes[i] if len(slice_indices) > 1 else axes
        ax.imshow(slice_data.T, cmap='gray', origin='lower')
        ax.axis('off')
        ax.set_title(f'Slice {slice_index}')

    plt.show()


nifti_file = ....
slice_indices = [50, 100, 150] 
plot_nifti_slices(nifti_file, slice_indices, axis=2)
