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
## 相关代码截图：
<img width="782" alt="image" src="https://github.com/user-attachments/assets/28ed0076-489a-475a-b5ce-ef9584abbb03" />
