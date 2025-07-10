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
                print(f"Disalin ke Invoice ATU: {full_path}")

    print(f"\n✅ Semua file ATU sudah disalin ke: {target_folder}")
    return target_folder

def kloning_dan_ganti_file(source_folder, encrypted_folder):
    parent_dir = os.path.dirname(source_folder)
    folder_nama = os.path.basename(source_folder.rstrip("\\/"))
    done_folder = os.path.join(parent_dir, f"{folder_nama} Done")
    masking_folder = os.path.join(parent_dir, "Masking")

    # Hapus jika sudah ada
    if os.path.exists(done_folder):
        shutil.rmtree(done_folder)
    os.makedirs(done_folder, exist_ok=True)

    if os.path.exists(masking_folder):
        shutil.rmtree(masking_folder)
    os.makedirs(masking_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        rel_path = os.path.relpath(root, source_folder)
        target_root = os.path.join(done_folder, rel_path)
        os.makedirs(target_root, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)

            # ➡️ File ATM → simpan ke folder flat Masking
            if "002-Invoice-Data-ATM Platform" in file and file.endswith(".txt"):
                dst_masking_file = os.path.join(masking_folder, file)
                if os.path.exists(dst_masking_file):
                    # Tambahkan penanda agar tidak tertimpa kalau ada nama duplikat
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dst_masking_file):
                        dst_masking_file = os.path.join(masking_folder, f"{base}_{counter}{ext}")
                        counter += 1
                shutil.copy2(src_file, dst_masking_file)
                print(f"➡️ Dipindah ke Masking: {dst_masking_file}")
            else:
                shutil.copy2(src_file, os.path.join(target_root, file))

    print(f"\n✅ Folder dikloning ke: {done_folder}")
    print(f"✅ File ATM disendirikan (tanpa subfolder) ke: {masking_folder}")

    # 🔁 Ganti file ATU dengan versi terenkripsi
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
                print(f"🔁 Diganti dengan versi terenkripsi: {dst_path}")

    print("\n✅ Semua file ATU diganti dengan versi terenkripsi.")

if __name__ == "__main__":
    folder_sumber = input("Masukkan path folder sumber (misalnya: C:\\Users\\Kamu\\Documents\\Maret 2025): ").strip()
    folder_sumber = os.path.abspath(folder_sumber)

    if not os.path.isdir(folder_sumber):
        print("❌ Folder tidak ditemukan. Pastikan path benar.")
        exit(1)

    folder_enkripsi = cari_dan_salin_file(folder_sumber)

    input("\n🔐 Silakan lakukan proses enkripsi terlebih dahulu di folder tersebut.\nTekan ENTER jika sudah selesai...")

    kloning_dan_ganti_file(folder_sumber, folder_enkripsi)
