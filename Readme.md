# 蛋白质翻译器使用指南

### (1)使用方法：

​    1.运行 *polypeptide_translator.py(exe)* ,输入需要翻译的文本。*(支持多语种)*

​    2.运行完成后界面上会出现翻译得到的蛋白质的相关数据。

​    3.运行结束后会生成 *输入内容_d.txt* 和 *输入内容_t.mol* 两个文件，内容如下：

​		***输入内容_d.txt***  ：获得的多肽信息

```
DeoxyriboNucleic Acid       : TACCTTTAGCTTGACCTGGTAGGTTGGCTGGTAGTTAGGCTGGTTCTTCTGATC, GATCAGAAGAACCAGCCTAACTACCAGCCAACCTACCAGGTCAAGCTAAAGGTA
Messenger Ribonucleic Acid  : AUGGAAAUCGAACUGGACCAUCCAACCGACCAUCAAUCCGACCAAGAAGACUAG
polypeptide                 : MEIELDHPTDHQSDQED.
Chemical formula            : H125 C83 N23 O36 S1 
```

​		第一行：DNA结构

​		第二行：第一行DNA转录得的mRNA结构

​		第三行：mRNA翻译得到的肽链的氨基酸组成

​		第四行：肽链的分子式

​		***输入内容_t.mol***  ：获得的多肽空间结构

```
 
KingDraw2D

  0  0  0     0  0              0 V3000
M  V30 BEGIN CTAB
M  V30 COUNTS 178 180 0 0 0
M  V30 BEGIN ATOM
M  V30 1 C 0.0 -0.0 0.0 0
M  V30 2 N -0.82102 -0.006354 0.0 0
M  V30 3 H -1.60102 -0.006354 0.0 0 VAL=1
...
M  V30 END ATOM
M  V30 BEGIN BOND
M  V30 1 1 1 6
M  V30 2 1 1 2
M  V30 3 1 2 3
...
M  V30 END BOND
M  V30 END CTAB
M  END

```

​		这里的mol文件为标准的molV3000文件，可以使用绝大部分化学画板打开，我这里使用的是 **KingDraw** 测试正常。

(2)注意事项

​    1.建议在使用时带上icon文件夹 *（能让UI好看一点）*

​    2.主要程序在 *encode.py* 内， *polypeptide_translator.py* 只是一个UI壳子。

​    3. *encode.py* 内保存有关于氨基酸空间结构的字典，建议不要随意改动。因为这些氨基酸有一些没有格式化，我单独拿出来在程序中做了连接方法的判断，代码可读性不高，能用就好。

​    4.mol文件的空间结构不一定对，请自行或使用软件进行格式化（如有生物方面的错误请提出）

​    5.推荐使用 **KingDraw** 对mol文件进行查看（这个软件支持格式化化学式、生成3D球棒或空间填充模型，还免费）

(3)更新

​	由于第一版编码无法做到解码（相同氨基酸对应多个密码子）因此更新了long版本以解决这一问题，但long版本在精氨酸和亮氨酸相关的肽链解码时可能会出现差错（原因看算法就明白了），目前暂且搁置，没有想到更好的编码方式，decode是解码方案，longencode已经作为一个函数加入encode.py中了，欢迎调试（longencode生成的文件会多一个l标示，如"输入内容\_ld.txt","输入内容\_lt.mol"）
