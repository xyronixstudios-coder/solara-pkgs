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
            lines = [line.rstrip('\n') for line in f.readlines()]
    
    print(f"=== SOLPAD v2.0 [{filename}] ===")
    print("Metni doğrudan yaz. Kaydetmek için sadece bir satıra ':w', çıkmak için ':q' yaz.")
    print("-" * 40)
    
    for i, line in enumerate(lines):
        print(f"{i+1}: {line}")
        
    print("-" * 40)
    print("Yeni satırları ekle (Bitince kaydetmek için ':w', çıkmak için ':q' yaz):")
    
    while True:
        try:
            line = input()
            if line == ":w":
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
                print(f"[✓] Başarıyla kaydedildi: {filename}")
            elif line == ":q":
                break
            elif line == ":wq":
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines) + "\n")
                print(f"[✓] Kaydedildi ve çıkılıyor: {filename}")
                break
            else:
                lines.append(line)
        except KeyboardInterrupt:
            print("\nÇıkış yapıldı.")
            break

if __name__ == "__main__":
    main()
