import asyncio
from googletrans import Translator

async def translate_text(src,lang):
    async with Translator() as translator:
        result = await translator.translate(src, dest='lang')
        print(f'번역>>>원문: {src},{lang}:{result.text}')

while True:
    lang=input("도착어를 선택해주십시오. ")
    if lang=="종료":
        print("종료합니다. ")
        break
    elif lang=="영어":
        lang="en"
    elif lang=="일본어":
        lang="ja"
    elif lang=="독일어":
        lang="de"
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue
    src=input("번역할 내용을 입력하세요: ")
    asyncio.run(translate_text(src,lang))