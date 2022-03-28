import itk
import matplotlib.pyplot as plt
import itkpocus.sonoque as sonoque
import numpy as np



def video_save(orig_img, path, acc):
    orig_img = itk.array_from_image(orig_img)
    shape = orig_img.shape
    print(shape)
    #save(png_path+acc+'.npy', video)

    for i in range(orig_img.shape[0]):
        png_path = path
        image_2d = orig_img[i,:,:,0]
        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        # onvert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)
        # Write the PNG file
        pngfile  = png_path+acc+'_'+str(i)+'.png'
        with open(pngfile , 'wb') as png_file:
            w = png.Writer(shape[2], shape[1], greyscale=True)
            w.write(png_file, image_2d_scaled)
    
    return 
