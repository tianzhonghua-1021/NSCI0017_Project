# About the Myriad
## Step.1 VPN
download link: https://liveuclac.sharepoint.com/sites/ISD.Website/WiFi%20%20Networks/Forms/AllItems.aspx?id=%2Fsites%2FISD%2EWebsite%2FWiFi%20%20Networks%2Fcisco%2Dsecure%2Dclient%2Dwin%2D5%2E1%2E15%2E287%2Dcore%2Dvpn%2Dpredeploy%2Dk9%201%2Emsi&parent=%2Fsites%2FISD%2EWebsite%2FWiFi%20%20Networks
guide link: https://www.ucl.ac.uk/isd/how-to/connecting-to-ucl-vpn-microsoft-windows

## Step.2 How to login Myriad
### Terminal 
键盘 `Win+R`，然后写`cmd`，打开命令行
![fig](/Myriad/cmd.png)
然后输入`ssh xxxxxx@myriad.rc.ucl.ac.uk`，登陆Myriad平台，然后输入密码后回车，进入Myriad平台
![fig](/Myriad/ssh.png)
登陆进入Myriad后，输入`pwd`可以看到每个人自己的**初始路径**
![fig](/Myriad/myriad.png)
然后下载teams中的示例文件
![fig](/Myriad/teams.png)
下载后放到桌面（Desktop）
重新开一个cmd窗口，编写远程复制指令`scp -r 文件夹名称 abcdef@myriad.rc.ucl.ac.uk:/home/abcdef`，将本地桌面的文件复制到远程Myriad的根目录中
![fig](/Myriad/scp.png)
回到Myriad的cmd界面，输入`ls`或者`ll`，这两个指令是以列表形式查看当前目录的，文件夹已经被复制过来
![fig](/Myriad/test.png)
通过`cd test`进入这个文件夹确认文件都被复制过来了
![fig](/Myriad/check.png)
提交任务，使用`qsub submit_array.sh`
![fig](/Myriad/qsub.png)
然后使用`qstat`指令查看当前服务器提交队列的情况，确认任务已经提交
![fig](/Myriad/qstat.png)
**以上是用CMD命令行使用Myriad平台的操作步骤，无需下载任何其他软件，只需要确保在学校WIFI环境或者VPN环境**
### VS Code
如果使用VS code，会更加适合后面运行模型的代码
首先要构建ssh的远程访问连接，选择左侧远程访问模块，点击`SSH`后面的`+`标志
![fig](/Myriad/vs1.png)
然后输入`ssh abcdef@myriad.rc.ucl.ac.uk`，构建连接
![fig](/Myriad/vs2.png)
构建连接后，左侧的`SSH`下面会出现新的远程服务名称，然后点击小齿轮符号，然后点击`~/.ssh/config`，弹出画面，包含了`Host`（可以自定义名称方便自己看）`HostName`是域名，`User`是自己的用户名，这两个不可以更改！
![fig](/Myriad/vs4.png)
确认无误后，点击“$\rightarrow$”就可以访问远程服务器了
![fig](/Myriad/vs5.png)
然后弹出窗口选择`Allow`就行了，不必管
![fig](/Myriad/vs6.png)
再选择左侧工具栏的文件模块，点击`open folder`，就可以看到`test`这个文件了，用VS code方便的地方就是可以直接看到代码，方便后面运行机器学习模型和调整代码
![fig](/Myriad/vs7.png)
![fig](/Myriad/vs8.png)
然后点击最上方工具栏的`terminal`或者`...`，找到`New terminal`打开终端，还是输入`qsub submit_array.sh`以及`qstat`来查看任务提交情况
![fig](/Myriad/vs9.png)
**以上就是如何用VS Code连接Myriad**

### WinSCP
直接在浏览器里搜索`Winscp`和`PuTTy`，然后下载即可
打开软件后，输入域名、用户名、密码，然后点击保存或者登陆
![fig](/Myriad/winscp1.png)
登陆进去后，可以看到类似于windows系统的文件系统
![fig](/Myriad/winscp2.png)
打开`test`文件夹也能看到
![fig](/Myriad/winscp3.png)
如果使用`PuTTy`打开，和terminal、cmd终端打开是一样的
![fig](/Myriad/winscp4.png)
**Winscp的连接比较简单，但是后面还是依赖Linux语言的一些指令才能上传任务，并且使用代码的时候不如vs code方便**

## Gaussian support
如果提交过程中，提示需要申请`Gaussian`的使用权，就需要发邮件申请：
![fig](/Myriad/it.jpg)
发送邮箱`rc-support@ucl.ac.uk`然后说明自己的用户名`ucaxxx`以及学号，描述一下自己的老师和课题需要使用即可。