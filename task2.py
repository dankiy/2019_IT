import matplotlib.pyplot as plt
import numpy as np


def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return


def get_kernel(windos_size, stdev):
    gauss = lambda a: e**(-(a[0]*a[0]+a[1]*a[1])/(2*stdev*stdev))/((2*pi*stdev*stdev))
    kernel = np.array([[gauss((x-int(windos_size/2), y-int(windos_size/2))) for y in range(windos_size)]
                       for x in range(windos_size)])
    return kernel


def filter(img, window_size=3, stdev=1):
    img2 = np.zeros_like(img)
    kernel = get_kernel(window_size, stdev)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
