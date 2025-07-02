# auto-telegram-bot-checkin
利用github中的Action功能自动执行python脚本
自动给telegram中指定的机器人发送指定的命令

## 使用步骤：
1. 首先在 https://my.telegram.org/ 中获取api和hash，并将代码中的信息替换为你自己的 API 密钥和hash
2. 先在本地跑通，进行验证，获取chat_name.session（在你运行的文件夹下），上传到github中 。其中chat_name可以自定义
3. 首次使用需要将代码打包下载下来后输入手机号和验证码（code）获取账号相关session值自动保存在本地文件夹，记得加上手机区号，如+86
4. 根据需要调整代码。目前代码是向我指定的机器人发送一个/checkin指令。
5. 记得把github action中的定时注释取消。默认在UTC的4.01运行，北京时间00.01，可以自行修改。
6. 在Actions中运行，确保正常
7. 请将仓库设置为private

## 定时Action脚本代码：
```yaml
name: Scheduled Job

on:
  schedule:
     - cron: '1 16 * * *'
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


若使用本人脚本导致被API滥用触发封号规则与本人无关，后果自负，本项目为教学项目，请下载后24小时内删除
