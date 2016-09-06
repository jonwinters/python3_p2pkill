# python3_p2pkill

p2pkill

Useage:
 
 p2pkill try to kill terminal p2p process like ThunderPaltform.exe
 
 when main process like Thunder is already exit,
 
 but his child process is still on you PC
 
 waste your CPU and RAM resources

 if you want to clean their children process,just write someline in foo.txt like next:

 Thuder.exe:ThuderPaltform.exe
 BaiduYunxxx.exe:baiduPaltformxxx.exe

用法：

配置foo.txt（如果没有主进程，随便 编一个主进程名就好了，另外配置文件 注意区分大小写）
主进程名:P2P进程名

然后启动python脚本在后台运行就好了，默认会定时自动杀死这些占用CPU宽带的P2P的进程，只要他们的主进程不存在了。
目前是0.01版，以后有空再撸，国内软件的win后台着实令人蛋疼，太浪费笔记本资源了。
