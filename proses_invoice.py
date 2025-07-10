import os
import shutil

def cari_dan_salin_file(source_folder):
    folder_nama = os.path.basename(source_folder.rstrip("\\/"))
    target_folder = os.path.join(os.path.dirname(source_folder), f"Invoice ATU {folder_nama}")
    os.makedirs(target_folder, exist_ok=True)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if "002-Invoice-Data-ATU Platform" in file and file.endswith(".txt"):
                full_path = os.path.join(root, file)
                shutil.copy2(full_path, target_folder)
                print(f"Disalin: {full_path} → {target_folder}")

    print(f"Semua file sudah disalin ke {target_folder}")
    return target_folder

def kloning_dan_ganti_file(source_folder, encrypted_folder):
    parent_dir = os.path.dirname(source_folder)
    folder_nama = os.path.basename(source_folder.rstrip("\\/"))
    done_folder = os.path.join(parent_dir, f"{folder_nama} Done")

    if os.path.exists(done_folder):
        shutil.rmtree(done_folder)
    shutil.copytree(source_folder, done_folder)
    print(f"Folder dikloning ke: {done_folder}")

    encrypted_files = {
        f: os.path.join(encrypted_folder, f)
        for f in os.listdir(encrypted_folder)
        if "002-Invoice-Data-ATU Platform" in f and f.endswith(".txt")
    }

    for root, _, files in os.walk(done_folder):
        for file in files:
            if file in encrypted_files:
                dst_path = os.path.join(root, file)
                shutil.copy2(encrypted_files[file], dst_path)
                print(f"Diganti dengan versi terenkripsi: {dst_path}")

    print("Semua file berhasil diganti dengan versi terenkripsi.")

if __name__ == "__main__":
    # Ganti path sesuai dengan direktori Anda
    # folder_sumber = r"C:\Users\NamaAnda\Documents\Maret 2025"

    folder_sumber = input("Masukkan path folder sumber (misalnya: C:\\Users\\Kamu\\Documents\\Maret 2025): ").strip()
    folder_sumber = os.path.abspath(folder_sumber)

    if not os.path.isdir(folder_sumber):
        print("Folder tidak ditemukan. Pastikan path benar.")
        exit(1)

    # Step 1 & 2: Cari & salin file ke Invoice ATU
    folder_enkripsi = cari_dan_salin_file(folder_sumber)

    # === Lakukan proses enkripsi manual terhadap file dalam folder_enkripsi ===

    input("\nTekan ENTER setelah file terenkripsi sudah siap di folder tersebut...")

    # Step 3, 4, 5: Kloning dan ganti file
    kloning_dan_ganti_file(folder_sumber, folder_enkripsi)
