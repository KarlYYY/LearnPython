# Python Environment(Windows 64-bit)
	\python-3.7.0-amd64.exe
	
# Text Editor
	\NotePad++\npp.7.5.7.Installer.exe
	markdown-plus-plus-master
	NppMarkdown.dll
	
	https://blog.csdn.net/hbiao68/article/details/52943555
	
## pip更新
进入cmd，将python36/Scripts/pip.exe拖进来回车，然后运行
```
python -m intstall --upgrade pip
```
安装之后可以用
```
pip --version
```
来看pip版本，目前最新版是18.0.

## 解决python “No module named pip”
python 升级后导致不能使用原来的pip命令
windows平台，cmd中敲命令：
```
python -m ensurepip
```
得到pip的setuptools，然后就可以用：
```
easy_install pip
```
# Tensorflow安装
python3.7目前还不支持，在 https://pypi.org/project/tensorflow/#files 可以看到目前Tensorflow支持的各平台版本，目前win64最新的是tensorflow-1.9.0-cp36-cp36m-win_amd64.whl，即只支持python3.6。
在cmd中进入\Python\Python36\Scripts目录，把tf的安装包whl文件拷贝到这里，然后运行命令
```
pip install tensorflow-1.9.0-cp36-cp36m-win_amd64.whl
```