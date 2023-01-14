# Loop
莫狗健身，全名为莫狗AI智能健身系统(Loop)，它基于MediaPipe和PyQt6进行开发，取名为莫狗之意为莫做细狗（好吧其实不是这个意思 XD）。<br/>

## 应用截图
![image](https://user-images.githubusercontent.com/25573004/212470990-f8b1ba70-ee2b-4527-a7c0-dca35be8b2b9.png)
![image](https://user-images.githubusercontent.com/25573004/212470997-8cf0e1d2-eb96-4e5b-afce-33aa65ca89f6.png)
![image](https://user-images.githubusercontent.com/25573004/212470999-940bd818-cca4-4e85-89af-986808775032.png)

## 文件结构
```
Loop
│  index_page.py                      主页界面
│  login_page.py                      登录界面
│  main.py                            入口函数
│  messagebox.py                      信息提示框
│  play_page.py                       运动界面
│  request.py                         网络请求类库           
│  utils.py                           杂类库
│
├─poses_csvs                          这里存放着姿态识别的landmark文件
│
├─pose_detection                      这里是姿态识别类库
│
├─user                                user文件夹放置用户配置文件，用于存储用户账号密码
│      user_config.ini
│
├─window                              这里放置的是UI文件
│  │  index_history_item.py
│  │  index_window.py
│  │  login_window.py
│  │  messagebox_error.py
│  │  messagebox_success.py
│  │  message_ui.py
│  │  play_window.py
│  │  start_widget.py
│  │
│  ├─icons
│  │
│  ├─images
│  │
│  └─ui_source                         .ui文件源码在这里
│
└─
```
如果您需要预览.ui文件，您首先需要把对应的文件和qrc文件从ui_source文件夹中移动至window文件夹下，也就是挪到ui_source文件夹的上一层目录，这样才能正确的加载图标

## 配套的Server
本应用需要搭配对应的服务端才能够正常的使用，[服务端的链接在这里](https://github.com/Creayhhh/LoopServer)

## 代码引用
本应用的运动计数状态功能代码来源于CSDN博主“[再游于北方知寒](https://blog.csdn.net/m0_57110410?type=blog)”，其项目的[CSDN链接在这里](https://blog.csdn.net/m0_57110410/article/details/125569971)，[GitHub链接在这里](https://github.com/MichistaLin/mediapipe-Fitness-counter)，如果侵犯了作者的权益，请联系我。

## 致谢
感谢PyQt5学习爱好群[“罪人”大佬](https://github.com/LX-sys)和“讨厌自己”大佬，以及群里的其他同伴们，他们给予了本项目很大很大的帮助，感谢！