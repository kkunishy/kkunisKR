import asyncio
from googletrans import Translator


async def translate_text():
    async with Translator() as translator:
        src=input('번역할 내용을 입력하세요: ')
        result = await translator.translate(src, dest='en')
        print(f'영어: {result.text}')

        result = await translator.translate(src, dest='ja')
        print(f'영어:{result.text}')

asyncio.run(translate_text())