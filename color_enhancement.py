import cv2
import numpy as np

# --- 1. Membaca gambar ---
img = cv2.imread("Foto_Klasik.jpg")

# --- 2. Konversi BGR → HSV (lebih mudah manipulasi warna) ---
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# --- 3. Meningkatkan saturasi (agar lebih berwarna) ---
# nilai S (saturation) diperbesar
h, s, v = cv2.split(hsv)

s = cv2.multiply(s, 1.6)     # 1.0 = normal, 1.6 = lebih berwarna
s = np.clip(s, 0, 255)        # batas nilai pixel

# --- 4. Meningkatkan brightness sedikit ---
v = cv2.add(v, 25)            # +25 lebih terang
v = np.clip(v, 0, 255)

# --- 5. Gabungkan kembali hasil HSV ---
hsv_enhanced = cv2.merge([h, s, v])

# --- 6. Kembalikan ke RGB/BGR ---
colored = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

# --- 7. Smoothing ringan + sharpening ringan (agar natural) ---
blur = cv2.GaussianBlur(colored, (3, 3), 0)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
final = cv2.filter2D(blur, -1, kernel)

# --- 8. Simpan hasil akhir ---
cv2.imwrite("Foto_Berwarna_Modern.jpg", final)

print("Selesai! Hasil lebih berwarna disimpan sebagai Foto_Berwarna_Modern.jpg")
