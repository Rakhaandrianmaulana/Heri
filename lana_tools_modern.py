import qrcode
import os
import sys
import time
from colorama import init, Fore, Style
from pyfiglet import Figlet
from tqdm import tqdm

# --- Inisialisasi Colorama ---
# autoreset=True agar warna kembali normal setelah setiap print()
init(autoreset=True)

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Menampilkan menu utama dengan ASCII Art."""
    
    # Membuat ASCII Art "LANA" dengan font 'slant'
    f = Figlet(font='slant')
    ascii_art = f.renderText('LANA')
    
    # Mencetak ASCII Art dengan warna cerah
    print(Fore.CYAN + Style.BRIGHT + ascii_art)
    
    # Mencetak menu
    print(Fore.YELLOW + "="*50)
    print(Fore.YELLOW + "      LANA MODERN TOOLS v3.0")
    print(Fore.YELLOW + "="*50)
    print(Fore.WHITE + "  /menu         -> Menampilkan menu ini")
    print(Fore.WHITE + "  /generate_qr  -> Membuat file QR Code (.png)")
    print(Fore.WHITE + "  /bruteforce   -> Simulasi Brute Force dengan Progress Bar")
    print(Fore.WHITE + "  /theme [color] -> Mengubah tema warna (green, red, reset)")
    print(Fore.WHITE + "  /tqto         -> Menampilkan ucapan terima kasih")
    print(Fore.WHITE + "  /exit         -> Keluar dari program")
    print(Fore.YELLOW + "="*50 + "\n")

def generate_qr_tool():
    """Fungsi untuk membuat file gambar QR Code."""
    print(Fore.GREEN + "[*] Tools: Generate QR Code")
    data = input("Masukkan teks atau URL untuk diubah menjadi QR Code: ")
    filename = input("Masukkan nama file untuk menyimpan QR Code (e.g., my_qr.png): ")

    if not filename:
        filename = "qrcode_default.png"
    if not filename.endswith('.png'):
        filename += '.png'
        
    try:
        # Membuat objek QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Membuat gambar dari objek QR Code
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        print(Fore.GREEN + Style.BRIGHT + f"\n[+] Sukses! QR Code telah disimpan sebagai '{filename}'")
        print(Fore.YELLOW + f"Lokasi file: {os.path.abspath(filename)}")
    except Exception as e:
        print(Fore.RED + f"\n[!] Gagal membuat QR Code. Error: {e}")

def bruteforce_simulation_tool():
    """Fungsi untuk simulasi Brute Force dengan progress bar TQDM."""
    print(Fore.GREEN + "[*] Tools: Simulasi Brute Force (Edukasi)")
    print(Fore.YELLOW + "PERINGATAN: Ini hanyalah simulasi untuk menunjukkan konsep.")
    
    target_username = input("Masukkan target username (contoh: lana_admin): ")
    
    # Contoh wordlist yang lebih besar
    passlist = ['123456', 'password', 'qwerty', 'admin', 'root', 'secret', 
                'dragon', 'sunshine', '112233', 'football', 'lana123', 'shadow'] 
    
    print(f"\n[*] Memulai simulasi serangan ke target '{target_username}' dengan {len(passlist)} password.")
    time.sleep(1)
    
    # Menggunakan TQDM untuk membuat progress bar
    for password in tqdm(passlist, desc="Mencoba Password", unit="pass", 
                         bar_format="{l_bar}{bar:20}{r_bar}", colour="red"):
        time.sleep(0.3) # Jeda untuk simulasi
        if password == 'lana123':
            # Hentikan progress bar sebelum mencetak hasil
            tqdm.write(Fore.GREEN + Style.BRIGHT + f"\n[+] SUKSES! Password ditemukan: '{password}'")
            return
            
    print(Fore.RED + f"\n[!] GAGAL. Password tidak ditemukan di dalam wordlist.")


def show_tqto():
    """Menampilkan bagian terima kasih."""
    print(Fore.MAGENTA + "\n" + "~"*30)
    print(Fore.WHITE + Style.BRIGHT + "       Special Thanks To")
    print(Fore.MAGENTA + "~"*30)
    print(Fore.CYAN + "  - Dev: Lana")
    print(Fore.YELLOW + "  - Thanks to God")
    print(Fore.GREEN + "  - My Parents")
    print(Fore.MAGENTA + "~"*30 + "\n")

def main():
    """Fungsi utama untuk menjalankan program."""
    current_theme = Fore.WHITE
    clear_screen()
    show_menu()
    
    while True:
        try:
            # Menggabungkan warna tema dengan style BRIGHT untuk prompt
            prompt = current_theme + Style.BRIGHT + "lana-tools>" + Style.RESET_ALL + " "
            command_input = input(prompt).strip().lower()

            parts = command_input.split()
            command = parts[0] if parts else ""
            
            if command == '/menu':
                show_menu()
            elif command == '/generate_qr':
                generate_qr_tool()
            elif command == '/bruteforce':
                bruteforce_simulation_tool()
            elif command == '/tqto':
                show_tqto()
            elif command == '/theme':
                if len(parts) > 1:
                    theme_color = parts[1]
                    if theme_color == 'green':
                        current_theme = Fore.GREEN
                        print(Fore.GREEN + "Tema diubah menjadi hijau.")
                    elif theme_color == 'red':
                        current_theme = Fore.RED
                        print(Fore.RED + "Tema diubah menjadi merah.")
                    elif theme_color == 'reset':
                        current_theme = Fore.WHITE
                        print("Tema direset ke default.")
                    else:
                        print(Fore.RED + f"[!] Warna '{theme_color}' tidak valid. Pilihan: green, red, reset.")
                else:
                    print(Fore.YELLOW + "[!] Gunakan: /theme [green|red|reset]")
            elif command == '/exit':
                print(Fore.CYAN + "Terima kasih telah menggunakan tools ini. Sampai jumpa!")
                sys.exit()
            else:
                if command:
                    print(Fore.RED + f"[!] Perintah '{command_input}' tidak dikenali. Ketik /menu untuk bantuan.")
        except KeyboardInterrupt:
            print(Fore.CYAN + "\n\nProgram dihentikan. Sampai jumpa!")
            sys.exit()

if __name__ == "__main__":
    main()