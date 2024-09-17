def IP():
    with open("ip.txt","r") as file:
        old=file.read()
    with open("add_ip.txt", "r") as file1:
        with open("ip.txt", "a") as file:
           # file.write("\n")
            new = file1.readline()
            print("[+] 可用ip:")
            # 判定 新ip是否重复
            while new:
                if new not in old:
                    print(new,end="")
                    file.write(new)
                new = file1.readline()
    # 清除 新ip
    with open("add_ip.txt","w") as file:
        pass
    return True


IP()