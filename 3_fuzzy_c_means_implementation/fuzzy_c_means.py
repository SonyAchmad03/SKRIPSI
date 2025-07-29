# --------------------------------------------------------------------------
# Implementasi Algoritma Fuzzy C-Means
# --------------------------------------------------------------------------
#
# File ini akan berisi implementasi inti dari algoritma Fuzzy C-Means (FCM)
# sesuai dengan yang dijelaskan dalam proposal skripsi.
#
# Referensi: Bab 3 & 4 dari proposal.
#
# --------------------------------------------------------------------------

import numpy as np
import pandas as pd

def load_data(file_path):
    """
    Fungsi untuk memuat data dari file.
    TODO: Sesuaikan dengan format data yang akan digunakan (misal: .csv, .xlsx).
    """
    print(f"Memuat data dari {file_path}...")
    # Contoh: return pd.read_csv(file_path)
    pass

def initialize_u_matrix(num_data_points, num_clusters):
    """
    Inisialisasi matriks keanggotaan U secara acak.
    """
    print("Inisialisasi matriks U...")
    u_matrix = np.random.rand(num_data_points, num_clusters)
    # Normalisasi sehingga jumlah setiap baris adalah 1
    u_matrix = u_matrix / np.sum(u_matrix, axis=1, keepdims=True)
    return u_matrix

def calculate_cluster_centers(data, u_matrix, m):
    """
    Menghitung pusat cluster (centroid).
    """
    print("Menghitung pusat cluster...")
    um = u_matrix ** m
    centers = (data.T @ um / np.sum(um, axis=0)).T
    return centers

def update_u_matrix(data, centers, m):
    """
    Memperbarui matriks keanggotaan U.
    """
    print("Memperbarui matriks U...")
    # TODO: Implementasikan logika pembaruan matriks U
    pass

def fuzzy_c_means(data, num_clusters, m=2, max_iters=100, tolerance=1e-5):
    """
    Fungsi utama untuk menjalankan algoritma Fuzzy C-Means.
    """
    print("Memulai algoritma Fuzzy C-Means...")
    # 1. Inisialisasi
    num_data_points = data.shape[0]
    u_matrix = initialize_u_matrix(num_data_points, num_clusters)

    for i in range(max_iters):
        print(f"Iterasi ke-{i+1}...")
        # 2. Hitung pusat cluster
        centers = calculate_cluster_centers(data, u_matrix, m)

        # 3. Update matriks U
        # u_new = update_u_matrix(data, centers, m)

        # 4. Cek konvergensi
        # if np.linalg.norm(u_new - u_matrix) < tolerance:
        #     print("Konvergensi tercapai.")
        #     break
        # u_matrix = u_new

    # return centers, u_matrix
    print("Placeholder: Implementasi FCM belum lengkap.")
    return None, None


if __name__ == "__main__":
    # --- Langkah-langkah Eksekusi ---
    # 1. Muat data dari folder 1_data_collection
    # data = load_data("../1_data_collection/nama_file_data.csv")

    # 2. Lakukan pra-pemrosesan jika diperlukan (dari folder 2_data_preprocessing)

    # 3. Tentukan parameter
    # num_clusters = 4 # Contoh jumlah TPS
    # fuzziness_m = 2.0 # Parameter m

    # 4. Jalankan algoritma FCM
    # cluster_centers, u_matrix = fuzzy_c_means(data, num_clusters, m=fuzziness_m)

    # 5. Lakukan analisis dan visualisasi (output ke folder 4 dan 5)
    print("Script utama untuk menjalankan proses clustering.")
    print("Silakan lengkapi implementasi dan alur kerja sesuai kebutuhan.")
