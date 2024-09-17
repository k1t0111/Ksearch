# Auther: K1t0
# Time: 2024/9/17
# Description: 去重和识别重复的domain和ip

import argparse

# 函数功能: 接收参数并解释
def main():
    parser = argparse.ArgumentParser(description='[+] K-Search-1nfo')
    # 接收参数
    parser.add_argument('-I','--IP', type=str, nargs='?', const='default_value',help='判断IP是否重复')
    parser.add_argument('-D', '--Domain', type=str,nargs='?', const='default_value', help='判断域名是否重复')
    parser.add_argument('-C', '--Clean', type=str, nargs='?', const='default_value',help='!!!清除所有数据,项目完成之后使用。谨慎!!!')
    args = parser.parse_args()
    #条件判断进入那一个模块
    if args.IP != None:
        IP()
        print()
    if args.Domain != None:
        Domain()
    if args.Clean != None:
        Clean()
    return True
# 函数功能: 判断IP 是否重复无重复则输出
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

# 函数功能: 判断Domain 是否重复无重复则输出
def Domain():
    with open("domain.txt","r") as file:
        old=file.read()
    with open("add_domain.txt", "r") as file1:
        with open("domain.txt", "a") as file:
           # file.write("\n")
            new = file1.readline()
            print("[+] 可用domain:")
            # 判定 新ip是否重复
            while new:
                if new not in old:
                    print(new,end="")
                    file.write(new)
                new = file1.readline()
    # 清除 新ip
    with open("add_domain.txt","w") as file:
        pass
    return True

#函数功能:清理所有文件
def Clean():
    with open("ip.txt","w") as file:
        pass
    with open("add_domain.txt","w") as file:
        pass
    return True

if __name__ == '__main__':
    main()
