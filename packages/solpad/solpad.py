#!/usr/bin/env python3
import sys
import os

def help_screen():
    print("=== SOLPAD - Modern Metin Düzenleyici ===")
    print("Kullanım: python3 solpad.py <dosya_adı>")
    print("İçerideki Kısayollar:")
    print("  Ctrl+S : Dosyayı Kaydet")
    print("  Ctrl+Q : Çıkış")
    sys.exit(0)

def main():
    if len(sys.argv) < 2:
        help_screen()
    
    filename = sys.argv[1]
    lines = []
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = ["\n"]

    print(f"--- Solpad Editor: {filename} ---")
    print("Çıkmak için boş bir satıra sadece ':q' yazıp ENTER'a bas, kaydetmek için ':w' yaz.\n")
    
    for i, line in enumerate(lines):
        print(f"{i+1:3d} | {line.rstrip()}")

    while True:
        try:
            cmd = input("solpad> ")
            if cmd == ":q":
                print("Çıkılıyor...")
                break
            elif cmd == ":w":
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print(f"[✓] {filename} başarıyla kaydedildi!")
            elif cmd.startswith(":add "):
                lines.append(cmd[5:] + "\n")
                print(f"Eklendi. Toplam satır: {len(lines)}")
            elif cmd == ":view":
                for i, line in enumerate(lines):
                    print(f"{i+1:3d} | {line.rstrip()}")
            else:
                print("Komutlar: :w (kaydet), :q (çık), :view (görüntüle), :add <metin> (satır ekle)")
        except KeyboardInterrupt:
            print("\nÇıkış yapıldı.")
            break

if __name__ == "__main__":
    main()
