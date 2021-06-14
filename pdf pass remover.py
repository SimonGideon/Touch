import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("wordlist.txt")]
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("D:\DESKTOP\MPESA_Statement_20210301_to_20210601_254707455652", password=password) as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:

        continue
