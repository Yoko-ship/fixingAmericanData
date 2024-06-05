import os
import shutil
import zipfile
import re

searching = re.compile(r"""^(.*?)
                    ((0|1)? \d)-
                    ((0|1|2|3)? \d)-
                    ((19|20)\d\d)
                    (.*?)$
""",re.VERBOSE)

finding = True
while finding:


    def findingDates():
        userInput = input("Напишите путь папки где вы хотите изменить Американскую дату файла на Европейскую дату: ")
        try:
            for folderName in os.listdir(userInput):
                mo = searching.search(folderName)
                if mo == None:
                    continue
                    
                beforePart = mo.group(1)
                monthPart = mo.group(2)
                dayPart = mo.group(4)
                yearPart = mo.group(6)
                afterPart = mo.group(8)

                euroFileName = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
                absWorkingDir = os.path.abspath(userInput)  # abspath это получение абсолютной пути от относительного 
                folderName = os.path.join(absWorkingDir,folderName)
                euroFileName = os.path.join(absWorkingDir,euroFileName)
                relativePathFolderName = os.path.basename(folderName)
                relativePathEuroFile = os.path.basename(euroFileName)
                print('Заменяем имя ', relativePathFolderName, 'на', relativePathEuroFile)
                shutil.move(folderName,euroFileName)

        except FileNotFoundError:
            print("Указанная папка не существует")

        try:
            match = re.match(searching,folderName)
            if not match:
                print("Некоторые файлы внутри заданной папки не соответствуют к критериям")
        except NameError:
            None

    findingDates()
    eXit = input("Напишите слово 'exit' чтобы покинуть программу: || проигнорьте чтобы продолжить ")
    if eXit.lower() == "exit":
        finding = False
    else:
        findingDates()







