# This Source Code Form is subject to the terms of the Mozilla
# Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import kivy
import random
from Dictionary import ReturnRandomWord
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color, Canvas, CanvasBase
from threading import Timer


Config.set("graphics", 'resizable', "0")
Config.set("graphics", 'width', "600")
Config.set("graphics", 'hight', "600")

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: 30, 50, 30, 35
        spacing: 10
        Label:
            size_hint: 1, 0.4
            text: "WordGames"
            outline_color: 0,0,1
            outline_width: 5
            font_size: 32
        Button:
            text: "Fast game"
            on_press: root.manager.current = "choose_a_game"
        Button:
            text: "Settings"
            on_press: root.manager.current = "settings"
        Button:
            text: "Add new words"
            on_press: root.manager.current = "addwords"
        Button:
            text: "Quit"
            on_press: exit()

<FastGameChooseScreen>:
    id: FastGame
    BoxLayout:
        orientation: "vertical"
        padding: 30, 50, 30, 35
        spacing: 10
        Label:
            size_hint: 1, 0.4
            text: "Choose a game"
            font_size: 28
            color: 0, 0, 0, 1
        Button:
            text: "Tail words"
        Button:
            text: "Jotto"
            on_press: root.manager.current = "jotto"
        Button:
            text: "Word chain"
        Button:
            text: "Back to menu"
            on_press: root.manager.current = "menu"
            
<JottoScreen>:
    id: Jotto
    # canvas.before:
    #     Color:
    #         rgb: .20, .87, 1
    #     Rectangle:
    #         pos: self.pos
    #         size: self.size
    BoxLayout:
        id: JottoBox
        orientation: "vertical"
        padding: 25, 40, 25, 20
        spacing: 5
        Label:
            id: JottoLabel
            canvas.before:
                Color:
                    rgb: 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            text:  ""
            text_size: self.size
            color: 0, 0, 0, 1
        TextInput:
            id: JottoInput
            on_text_validate: root.IsItRight(self.text, root.dictionary); self.text = "" #JottoLabel.text += "\\n" + self.text
            size_hint: 1, 0.2
            multiline: False
        GridLayout:
            cols: 9
            rows: 3
            spacing: 5
            Button:
                id: A
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "A"
            Button:
                id: B
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "B"
            Button:
                id: C
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "C"
            Button:
                id: D
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "D"
            Button:
                id: E
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "E"
            Button:
                id: F
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "F"
            Button:
                id: G
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "G"
            Button:
                id: H
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "H"
            Button:
                id: I
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "I"
            Button:
                id: J
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "J"
            Button:
                id: K
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "K"
            Button:
                id: L
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "L"
            Button:
                id: M
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "M"
            Button:
                id: N
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "N"
            Button:
                id: O
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "O"
            Button:
                id: P
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "P"
            Button:
                id: Q
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "Q"
            Button:
                id: R
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "R"
            Button:
                id: S
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "S"
            Button:
                id: T
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "T"
            Button:
                id: U
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "U"
            Button:
                id: V
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "V"
            Button:
                id: W
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "W"
            Button:
                id: X
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "X"
            Button:
                id: Y
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "Y"
            Button:
                id: Z
                background_color: .85,.85,.85,1
                on_press: root.ChangeBColor(self)
                color: 0, 0, 0, 1
                font_size: 26
                text: "Z"
        BoxLayout:
            size_hint: 1, .15
            spacing: 5
            Button:
                text: "Back to menu or restart a session "
                on_press: root.BackToMenu() #TODO:сделай всплывающее меню для выхода в меню V prinvipe Vse!


<SettingsScreen>:
    id: Settings
    BoxLayout:
        orientation: "vertical"
        padding: 30, 50, 30, 35
        spacing: 5
        Label:
            size_hint: 1, 0.4
            text: "Settings"
            font_size: 28
            color: 0, 0 , 0, 1
        Label:
            size_hint: 1, 0.3
            text: "Change background color:"
            font_size: 30
        BoxLayout:
            padding: 8, 0, 8, 0
            size_hint: 1, 0.4
            spacing: 5
            Button:
                text: "Blue"
                font_size: 20
                color: .20, .87, 1, 1
                on_press: app.ColorCh (self, self.text)
            Button:
                text: "Violet"
                font_size: 20
                color: .255, .230, 1, 1
                on_press: app.ColorCh (self, self.text)
            Button:
                text: "Prussian Blue"
                font_size: 20
                color: 0, .19, .33, 1
                on_press: app.ColorCh (self, self.text)
        Label:
            size_hint: 1, 0.3
            text: "Change word length:"
            font_size: 30
        BoxLayout:
            padding: 8, 0, 8, 0
            size_hint: 1, 0.4
            spacing: 5
            Button:
                text: "WL"
                on_press: app.JottoLim(0)
            Button:
                text: "3"
                on_press: app.JottoLim(self.text)
            Button:
                text: "4"
                on_press: app.JottoLim(self.text)
            Button:
                text: "5"
                on_press: app.JottoLim(self.text)
            Button:
                text: "6"
                on_press: app.JottoLim(self.text)
            Button:
                text: "7"
                on_press: app.JottoLim(self.text)  
        Button:
            text: "Back to menu"
            on_press: root.manager.current = "menu"

<AddWordsScreen>:
    id: AddWord
    BoxLayout:
        orientation: "vertical"
        padding: 30, 50, 30, 35
        spacing: 5
        TextInput:
            id: addwordtextinput
            multiline: False
            on_text_validate: self.text = "" #TODO: добавь функции для добавления слова в дневник
        Button:
            text: "Add Word"
            on_press: addwordtextinput.text = ""
            on_release:  addwordtextinput.focus = True
        Button:
            text: "Back to Menu"
            on_press: root.manager.current = "menu"
""")

# def ColorCh(instance):
#     instance.canvas.before.add(Rectangle())
#     instance.canvas.before.add(Color(1, 1, 1))

# Declare screens
class AddWordsScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class FastGameChooseScreen(Screen):
    pass

class JottoScreen(Screen):
    dictionary = random.choice(ReturnRandomWord())
    
    def __init__(self, **kwargs):
        super(JottoScreen, self).__init__(**kwargs)

    def IsItRight(instance, text, dictionary):
        text = text.capitalize()
        dejavu = ""
        correctnumber = 0
        letter = None
        for letter in dictionary:
            if text.lower().count(letter) != 0:
                if dejavu.count(letter) < 1:
                    correctnumber += 1
            dejavu += letter

        if text.lower() == dictionary:
            instance.ids["JottoLabel"].text += "\n" + "You won!!!" + "\nThe correct answer is: " + text.capitalize()   
        else:
            instance.ids["JottoLabel"].text +="\n" + text + " " + str(correctnumber)
        

    def ChangeBColor(instance, self): 
        if self.background_color[0] == .85:
            self.background_color = (204, 0, 0, 1)
        elif self.background_color[0] == 204:
            self.background_color = (.51, 153, 0, 1)
        elif self.background_color[0] == .51:
            self.background_color = (.85, .85, .85, 1)

    def ClearButtonsColor (instance):
        x = None
        for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            instance.ids[x].background_color = (.85, .85, .85, 1)
        instance.dictionary = random.choice(ReturnRandomWord())

    def BackToMenu(instance):

        ## TODO: Сделай чтобы был таймер и если игрок за 2 (прим) сек нажимает 2а раза то выход
        #instance.ClearButtonsColor() 
        instance.remove_widget(instance.ids["JottoBox"])
        BoxToMenu = BoxLayout(orientation = "vertical",
        padding = (40, 40, 40, 40),
        spacing = 10)
        BoxToMenu.add_widget(Button (text = "Go out",
        on_press = lambda x: ClearAndQuit())
        )
        BoxToMenu.add_widget(Button (text = "Resume",
        on_press = (lambda x: ReturnToGame()
        )))
        BoxToMenu.add_widget(Button (text = "Restart",
        on_press = lambda x: RestartASession()))

        def ReturnToGame():
            instance.add_widget(instance.ids["JottoBox"])
            instance.remove_widget(BoxToMenu)
        
        def ClearAndQuit():
            instance.ClearButtonsColor()
            instance.ids["JottoLabel"].text = ""
            instance.ids["JottoInput"].text = ""
            sm.current = "menu"
            instance.add_widget(instance.ids["JottoBox"])
            instance.remove_widget(BoxToMenu)

            global dictionary
            dictionary = random.choice(ReturnRandomWord())

        def RestartASession():
            instance.ClearButtonsColor()
            instance.ids["JottoLabel"].text = ""
            instance.ids["JottoInput"].text = ""
            instance.add_widget(instance.ids["JottoBox"])
            instance.remove_widget(BoxToMenu)
            
            global dictionary
            dictionary = random.choice(ReturnRandomWord())


        instance.add_widget(BoxToMenu)

    def LimitWordFunc(instance, limitnum):
        limitnum = int(limitnum)
        instance.dictionary = random.choice(ReturnRandomWord())
        print(instance.dictionary)
        if limitnum == 0:
            pass
        elif len(instance.dictionary) != limitnum:
            JottoScreen.LimitWordFunc(instance, limitnum)
class SettingsScreen(Screen):
    pass


menu = MenuScreen(name = "menu")
jotto = JottoScreen(name = "jotto")
# Create the screen manager
sm = ScreenManager(size_hint = (1, 1), size = (600, 600))
sm.canvas.before.add(Color(.20, .87, 1))
sm.canvas.before.add(Rectangle(size = sm.size))
sm.add_widget(menu)
sm.add_widget(FastGameChooseScreen(name = "choose_a_game"))
sm.add_widget(jotto)
sm.add_widget(SettingsScreen(name = "settings", id = "Settings"))
sm.add_widget(AddWordsScreen(name = "addwords"))


class WordGamesApp(App):
    def JottoLim(instance, limitnum):
        JottoScreen.LimitWordFunc(jotto, limitnum)

    def ColorCh(instance, button, text):
        textcolor = None
        if text == "Blue":
            textcolor = (.20, .87, 1)
        elif text == "Violet":
            textcolor = (.255, .230, 230)
        elif text == "Prussian Blue":
            textcolor = (0, .19, .33)
        
        with sm.canvas.before:
            Color(textcolor[0], textcolor[1], textcolor[2])
            Rectangle(size = (600, 600))

    def build(self):
        return sm


# WordGamesApp.ColorCh(menu)

if __name__ == '__main__':
    WordGamesApp().run()
    
    