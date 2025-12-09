import cv2
import os
import numpy as np

BASE = r"C:\Users\narut\Desktop\Diat\sem 1\Robot vision\Assignemnt\Q4"
os.makedirs(BASE, exist_ok=True)

IMG5 = "img5.tif"
IMG6 = "img6.tif"
IMG7 = "img7.tif"
IMG8 = "img8.tif"

MEDIAN_KSIZE = 3                # median kernel (must be odd)
ERODE_KERNEL = (3, 3)           # erosion kernel
ERODE_ITER = 1                  # number of erosion iterations

def safe_read_gray(path):
    if not os.path.isfile(path):
        print(f"[MISSING] {path}")
        return None
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"[ERROR] failed to load: {path}")
    return img

def write_img(img, path):
    cv2.imwrite(path, img)
    print("Saved:", path)

# -------- PROCESS img5 & img6: median(3) only --------
for name in [IMG5, IMG6]:
    path = os.path.join(BASE, name)
    img = safe_read_gray(path)
    if img is None:
        continue

    med = cv2.medianBlur(img, MEDIAN_KSIZE)
    out = os.path.join(BASE, name.replace(".tif", f"_median{MEDIAN_KSIZE}.png"))
    write_img(med, out)

# -------- PROCESS img7 & img8: median(3) -> erosion --------
kernel_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ERODE_KERNEL)

for name in [IMG7, IMG8]:
    path = os.path.join(BASE, name)
    img = safe_read_gray(path)
    if img is None:
        continue

    # median 3x3
    med = cv2.medianBlur(img, MEDIAN_KSIZE)
    med_out = os.path.join(BASE, name.replace(".tif", f"_median{MEDIAN_KSIZE}.png"))
    write_img(med, med_out)

    # erosion
    eroded = cv2.erode(med, kernel_erode, iterations=ERODE_ITER)
    eroded_out = os.path.join(BASE, name.replace(".tif", f"_median{MEDIAN_KSIZE}_eroded_k{ERODE_KERNEL[0]}x{ERODE_KERNEL[1]}.png"))
    write_img(eroded, eroded_out)

print("Processing complete.")
