from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Náhled mobilu na PC
Window.size = (360, 640)


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        title = Label(
            text="MathBot",
            font_size=32,
            size_hint_y=None,
            height=80
        )

        layout.add_widget(title)

        kalkulacka = Button(
            text="KALKULACKA",
            font_size=20,
            size_hint_y=None,
            height=70
        )

        kalkulacka.bind(on_press=self.otevri_kalkulacku)

        layout.add_widget(kalkulacka)

        # Vytvoří volné místo
        layout.add_widget(Label())

        menu = Button(
            text="MENU",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        menu.bind(on_press=self.otevri_nastaveni)

        layout.add_widget(menu)

        self.add_widget(layout)

    def otevri_kalkulacku(self, instance):
        self.manager.current = "kalkulacka"

    def otevri_nastaveni(self, instance):
        self.manager.current = "nastaveni"


class KalkulackaScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        layout.add_widget(Label(
            text="KALKULACKA",
            font_size=30,
            size_hint_y=None,
            height=70
        ))

        layout.add_widget(Label(
            text="0",
            font_size=40
        ))

        zpet = Button(
            text="ZPET",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        zpet.bind(on_press=self.zpet)

        layout.add_widget(zpet)

        self.add_widget(layout)

    def zpet(self, instance):
        self.manager.current = "menu"


class NastaveniScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        layout.add_widget(Label(
            text="NASTAVENI",
            font_size=30,
            size_hint_y=None,
            height=70
        ))

        white = Button(
            text="WHITE MODE",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        dark = Button(
            text="DARK MODE",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        zpet = Button(
            text="ZPET",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        white.bind(on_press=self.white_mode)
        dark.bind(on_press=self.dark_mode)
        zpet.bind(on_press=self.zpet)

        layout.add_widget(white)
        layout.add_widget(dark)

        # Volné místo
        layout.add_widget(Label())

        layout.add_widget(zpet)

        self.add_widget(layout)

    def white_mode(self, instance):
        Window.clearcolor = (1, 1, 1, 1)

    def dark_mode(self, instance):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)

    def zpet(self, instance):
        self.manager.current = "menu"


class MathBotApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            MenuScreen(name="menu")
        )

        manager.add_widget(
            KalkulackaScreen(name="kalkulacka")
        )

        manager.add_widget(
            NastaveniScreen(name="nastaveni")
        )

        return manager


MathBotApp().run()
