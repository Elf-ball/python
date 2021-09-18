## PyQt5使用说明
#### 安装PyQt5
- 使用命令pip install PyQt5
  - 如果始终无法安装成功，使用pip3 install PyQt5-tools -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com
  - 借鉴地址：[跳转连接](https://blog.csdn.net/weixin_43985262/article/details/103963134)
#### 安装Pyqt5中的designer和uic
- 安装成功后，在python安装目录\Lib\site-packages下找到对应库，进入查看是否存在designer.exe
  - 如无法找到exe文件，可直接搜索designer.exe文件(一般会在pyqt5-tools中)
  - 在pycharm setting-tools-external tools中新增qtdesigner和pyuci
    - 新增designer时只需要填写name,program,working directory(依次对应名称，exe所处路径 + designer.exe,exe所处路径)
    - 新增uic时需要填写，name,program,arguments,working directory(依次对应名称，exe所处路径 + designer.exe,$FileName$ -o $FileNameWithoutExtension$.py,$FileDir$)
    - 新增uic时网上资料很杂，有的说路径填写python.exe路径，有的又说uic.exe路径，有的有时pyuic5.exe（亲测pyuic5.exe才是对的，可能和安装方式有关系）
#### 使用designer和uic
- 鼠标右键点击python项目名称，选择external tools->designer（这个是自己安装designer时填写的名称）
  - 此时将会弹出designer页面，如未弹出，请检查安装是否正确
  - 在designer中创建mainwindow，然后拖动空间到画布上
  - 保存文件为.ui格式并存放到python项目目录中
  - 右键点击.ui文件，选择external tools->uic
  - 点击之后，目录中将新增一个和.ui文件同名的.py文件（懂的同学可自行修改py文件，初学者不建议动这个文件）
  - 创建新的py文件，调用上述py文件（具体实现请看代码）
#### 打包py文件为exe
- 安装PyInstaller
  - pip install PyInstaller（如安装失败，可多次执行命令安装）
  - 安装成功后，进入到需要打包的项目目录，执行命令pyinstaller -F xxx.py或pyinstaller -F -w xxx.py(不加-w打包exe后，运行exe文件会弹出命令窗口，里面会显示代码中打印的日志)
