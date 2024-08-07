while True:
    decrypt_or_encrypt = input("\t\t1. Encrypt\n\t\t2. Decrypt\nwhat you want do do? : ")

    if decrypt_or_encrypt == "1":
        # encryption
        cmd = input("Input Text: ").lower()

        cmd_list = []
        for x in cmd:
            cmd_list.append(x)

        from Encrypt import encrypt

        encrypt(cmd_list)

        cmd_list_str = "".join(cmd_list)
        print(f"\n{cmd_list_str}\n")

    elif decrypt_or_encrypt == "2":
        # decryption
        cmd = input("Input Decrypted Text: ")

        cmd_list = []
        for x in cmd:
            cmd_list.append(x)

        from Decrypt import decrypt

        decrypt(cmd_list)

        cmd_list_str = "".join(cmd_list)
        print(f"\n{cmd_list_str}\n")
    else:
        pass
