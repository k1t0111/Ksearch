# Ksearch
> 平常针对多资产批量信息收集时候，批量域名和批量ip。总是会有重复收集浪费时间，因此Ksearch 可以进行一些操作。

### Usage
ip.txt domain.txt存放初始ip和domain
add_ip.txt add.domain.txt 存放新收集的对应 ip和域名进行判重，并且进行利用

```shell 

usage: Ksearch.py [-h] [-I [IP]] [-D [DOMAIN]] [-C [CLEAN]]

[+] K-Search-1nfo

options:
  -h, --help            show this help message and exit
  -I [IP], --IP [IP]    判断IP是否重复
  -D [DOMAIN], --Domain [DOMAIN]
                        判断域名是否重复
  -C [CLEAN], --Clean [CLEAN]
                        !!!清除所有数据,项目完成之后使用。谨慎!!!
```
##### 利用截图
```shell
python Ksearch.py -I -D # ip 域名判重
```
  ![image.png](https://raw.githubusercontent.com/k1t0111/blog/main/image/20240919193957.png)

```shell
python Ksearch.py -C   # 清理所有文件
```


