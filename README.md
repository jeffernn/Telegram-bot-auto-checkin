# auto-telegram-bot-checkin
利用github中的Action功能自动执行python脚本
自动给telegram中指定的机器人发送指定的命令

## 使用步骤：
1. 首先在 https://my.telegram.org/ 中获取api和hash，并将代码中的信息替换为你自己的 API和hash
2. 先在本地跑通（下载整个项目，运行main.py），进行验证(输入手机号和验证码)，获取chat_name.session（自动生成在你的文件夹下），上传整个项目到github中。其中chat_name可以自定义名字
3. 首次使用需要将代码打包下载下来后输入手机号和验证码（code）获取账号相关session值自动保存在本地文件夹，记得加上手机区号，如+86
4. 根据需要调整代码。目前代码是向我指定的机器人发送一个/checkin指令，你可以改为你需要的机器人指令
5. 默认在UTC的4:01运行，北京时间00:01，可以自行修改
6. 在Actions中运行，验证是否部署成功
7. 请将仓库设置为private，确保你的私有密钥不会公开
8. 给本项目点个Star，支持下本项目
## 相关代码展示：
<img width="782" alt="image" src="https://github.com/user-attachments/assets/28ed0076-489a-475a-b5ce-ef9584abbb03" />

## 定时Action脚本代码：
```yaml
name: Scheduled Job

on:
  schedule:
     - cron: "1 16 * * *"
  workflow_dispatch:
  
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install telethon

    - name: Run script
      run: python main.py





⚠️⚠️⚠️若使用本人脚本导致被API滥用触发封号规则与本人无关，后果自负，本项目为教学项目，请下载后24小时内删除
