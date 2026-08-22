#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Kullanım: solpad <dosya_adı>")
        sys.exit(1)
    
    filename = sys.argv[1]
    lines = []
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    
    print(f"=== SOLPAD v1.0 | Düzenlenen: {filename} ===")
    print("Komutlar: :w (kaydet), :q (çık), :wq (kaydet ve çık), :add <metin> (satır ekle), :view (göster)\n")
    
    for i, line in enumerate(lines):
        print(f"{i+1:3d} | {line.rstrip()}")

    while True:
        try:
            cmd = input("solpad> ")
            if cmd == ":q":
                break
            elif cmd == ":w":
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print(f"[✓] Kaydedildi: {filename}")
            elif cmd == ":wq":
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print(f"[✓] Kaydedildi ve çıkılıyor: {filename}")
                break
            elif cmd.startswith(":add "):
                lines.append(cmd[5:] + "\n")
                print(f"Eklendi (Toplam: {len(lines)} satır)")
            elif cmd == ":view":
                for i, line in enumerate(lines):
                    print(f"{i+1:3d} | {line.rstrip()}")
            else:
                print("Geçersiz komut! (:w, :q, :wq, :add <metin>, :view)")
        except KeyboardInterrupt:
            print("\nÇıkış yapıldı.")
            break

if __name__ == "__main__":
    main()
