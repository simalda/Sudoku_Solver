from tkinter import *
from SudokuBoard import SudokuBoard
from SudokuGame import SudokuGame


class Language(object):
    def __init__(self, lang = None):
        self.langDict = {
            "Русский": {'NewGame' : 'Новая Игра',
        'File' : 'Файл',
        'Easy' : 'Легко',
        'Medium' : 'Средне',
        'Hard' : 'Тяжело',
        'LoadGame' : 'Загрузить игру',
        'ChoseYourLanguage' : 'Выбери язык',
        'SaveGame' : 'Сохранить игру',
        'ClearAnswers' : 'Очистить ответы',
        'ShowSolution' : 'Показать решение',
        'WIN': 'Молодчик, мамгин!'},
                  "English": {'NewGame' : 'New Game',
        'File' : 'File',
        'Easy' :'Easy',
        'Medium' : 'Medium',
        'Hard' : 'Hard',
        'LoadGame' : 'Load Game',
        'ChoseYourLanguage' : 'Chose Your Language',
        'SaveGame' : 'Save Game',
        'ClearAnswers' :'Clear Answers',
        'ShowSolution' :'Show Solution',
                            'WIN': "YOU WIN!!!"}}

        self.SetLang(lang)#!!!!



    def SetLang(self, language):
        #attributes = dir(self)
        #myAttributes = [a for a in dir(attributes) if not a.startswith('__') and not callable(getattr(obj,a))]

        for attributeName in self.langDict[language].keys():
            setattr(self, attributeName, self.langDict[language][attributeName])

        # self.NewGame = langDict[language]['NewGame']
        # self.File = langDict[language][File]
        # self.Easy = langDict[language][Easy]
        # self.Medium = langDict[language][Medium]
        # self.Hard = langDict[language][Hard]
        # self.LoadGame = langDict[language][LoadGame]
        # self.ChoseYourLanguage = langDict[language][ChoseYourLanguage]
        # self.SaveGame = langDict[language][SaveGame]
        # self.ClearAnswers = langDict[language][ClearAnswers]
        # self.ShowSolution = langDict[language][ShowSolution]


    def HebrewLang(self):
        pass

    def GetAvailibleLangueages(self):
        return self.langDict.Keys()