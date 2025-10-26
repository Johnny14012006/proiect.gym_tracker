from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from database.db_manager import get_all_exercises

class HistoryScreen(Screen):
    def go_back(self, instance):
        self.manager.current = "add"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.scroll = ScrollView()
        self.content = BoxLayout(orientation="vertical", size_hint_y=None)
        self.content.bind(minimum_height=self.content.setter('height'))

        self.scroll.add_widget(self.content)
        self.layout.add_widget(Label(text="📋 Istoric exerciții", font_size=22, bold=True))
        self.layout.add_widget(self.scroll)

        btn_back = Button(text="⬅️ Înapoi", size_hint_y=None, height=50)
        btn_back.bind(on_press=self.go_back)
        self.layout.add_widget(btn_back)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        self.content.clear_widgets()
        exercises = get_all_exercises()
        if not exercises:
            self.content.add_widget(Label(text="Nicio înregistrare găsită."))
            return

        for date, exercise, weight, reps in exercises:
            text = f"[{date}] {exercise} - {weight}kg ({reps or '-'} reps)"
            self.content.add_widget(Label(text=text, size_hint_y=None, height=30))
