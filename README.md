*Scripts perform grayscale image denoising for microscopy / rice/diatom images.
Supports:

Median filtering for salt-and-pepper (impulsive) noise

Gaussian / NLM (and combinations) for Gaussian-like noise

Morphological ops (erosion / dilation / close) for structural cleanup**

I used img 5,6 that had light noise and img 7,8 heavy noise.
So name you file accordingly or change the file name in the code accordingly. Same goes for the imput image path and the output image path.

Methodology


1. Preprocessing and Grayscale Conversion
All input images (img5, img6, img7, img8) were loaded in grayscale to simplify noise-removal operations and ensure uniform processing.


Processing for img5 and img6 (Salt-and-Pepper Noise Removal)----IMAGE WITH LITTLE NOISE

2. Median Filtering (3×3 kernel)
    A 3×3 median filter was applied to remove salt-and-pepper noise.
    Median filtering replaces each pixel with the median of its neighborhood, making it highly effective for removing isolated white/black specks while preserving edges.
    This produced a cleaner, noise-free version of img5 and img6 without blurring major structures.


Processing for img7 and img8 (Stronger Noise + Structural Cleanup)-----IMAGE WITH LOTS OF NOISE

3. Median Filtering (3×3 kernel)
     The same 3×3 median filter was first applied to img7 and img8 to eliminate impulsive noise and smooth small intensity spikes.
4. Morphological Erosion
     After median filtering, a 3×3 morphological erosion operation was applied.
     Erosion helps remove small residual artifacts, thin tiny protrusions, and clean the shapes further. It reduces small unwanted noise clusters that remain after the median step.
     The erosion strength was kept minimal (1 iteration) to avoid excessive thinning of valid image structures.
5. Output Generation
     All processed images were saved with clear filenames indicating the applied operation (e.g., _median3.png, _median3_eroded.png).
     Intermediate and final results were preserved for comparison and validation.


To run
```python
python noise_removal.py
