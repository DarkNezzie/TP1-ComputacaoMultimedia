from math import log10, sqrt
import cv2
import numpy as np
cars_codificadas = np.array(['hevc/cars_out1.png','hevc/cars_out2.png','hevc/cars_out3.png','hevc/cars_out4.png','jp2/cars_out1.png','jp2/cars_out2.png','jp2/cars_out3.png','jp2/cars_out4.png','vp9/cars_out1.png','vp9/cars_out2.png','vp9/cars_out3.png','vp9/cars_out4.png'])
horses_codificadas = np.array(['hevc/horses_out1.png','hevc/horses_out2.png','hevc/horses_out3.png','hevc/horses_out4.png','jp2/horses_out1.png','jp2/horses_out2.png','jp2/horses_out3.png','jp2/horses_out4.png','vp9/horses_out1.png','vp9/horses_out2.png','vp9/horses_out3.png','vp9/horses_out4.png'])
mountain_codificadas = np.array(['hevc/mountain_out1.png','hevc/mountain_out2.png','hevc/mountain_out3.png','hevc/mountain_out4.png','jp2/mountain_out1.png','jp2/mountain_out2.png','jp2/mountain_out3.png','jp2/mountain_out4.png','vp9/mountain_out1.png','vp9/mountain_out2.png','vp9/mountain_out3.png','vp9/mountain_out4.png'])
barco_codificadas = np.array(['hevc/barco_out1.png','hevc/barco_out2.png','hevc/barco_out3.png','hevc/barco_out4.png','jp2/barco_out1.png','jp2/barco_out2.png','jp2/barco_out3.png','jp2/barco_out4.png','vp9/barco_out1.png','vp9/barco_out2.png','vp9/barco_out3.png','vp9/barco_out4.png'])

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
def main():
     original = cv2.imread("cars.png")
     compressed = cv2.imread("hevc/cars_out2.png", 1)
     value = PSNR(original, compressed)
     print(f"PSNR value is {value} dB")
       
if __name__ == "__main__":
    main()