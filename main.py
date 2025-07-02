from telethon import TelegramClient, events
import asyncio

# 替换为你自己的 API 信息
api_id = 24191107
api_hash = 'f08f30015647d9d1af0ac9941d4dfbff'
CHANNEL_ID = '@GetfreeCloud_Bot'

async def main():
    async with TelegramClient('chat_name', api_id, api_hash) as client:
        # 发送 '/checkin'
        await client.send_message(CHANNEL_ID, '/checkin')

        # 定义一个 future 用于等待消息
        future = asyncio.get_event_loop().create_future()

        @client.on(events.NewMessage(incoming=True, chats=CHANNEL_ID))
        async def handler(event):
            print("收到回复:", event.text)
            if not future.done():
                future.set_result(True)  # 收到消息后设置 future 完成

        # 等待 future 完成（即收到一条消息后退出）
        await future

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except SystemExit:
        print('finished')
