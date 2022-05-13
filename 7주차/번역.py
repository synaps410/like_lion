from googletrans import Translator

translator=Translator()
sentence=input('번역을 원하는 문장을 입력해 주세요! : ')
dest=input('번역되길 원하는 언어를 입력하라(국가 코드로 입력해라잉) : ')

result=translator.translate(sentence,dest)
detected=translator.detect(sentence)

print('======출력결과======')
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print('====================')