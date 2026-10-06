# -*- coding: utf-8 -*-
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Triangle, Ellipse, Rectangle, Line
from kivy.core.window import Window

WISHES = [
    "Пусть учебный год принесёт море радости! 🎉",
    "Пусть удача никогда не покидает тебя! 🎯",
]


class ElkaApp(App):
    def build(self):
        Window.clearcolor = (0.04, 0.12, 0.24, 1)

        self.layout = FloatLayout()

        with self.layout.canvas:
            Color(1, 1, 1, 0.9)
            for _ in range(60):
                x = random.random()
                y = random.random()
                r = random.uniform(0.002, 0.005)
                Ellipse(pos=(x * Window.width - r * Window.width,
                             y * Window.height - r * Window.height),
                        size=(r * Window.width * 2, r * Window.height * 2))

        self.draw_tree()

        self.wish_label = Label(
            text="",
            font_size='18sp',
            color=(1, 0.84, 0, 1),
            halign='center',
            valign='middle',
            size_hint=(0.9, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.12},
        )
        self.wish_label.bind(size=self.wish_label.setter('text_size'))
        self.layout.add_widget(self.wish_label)

        btn = Button(
            text="🎁 Новое пожелание",
            font_size='18sp',
            background_color=(0.75, 0.22, 0.17, 1),
            color=(1, 1, 1, 1),
            size_hint=(0.7, 0.09),
            pos_hint={'center_x': 0.5, 'y': 0.02},
        )
        btn.bind(on_press=self.new_wish)
        self.layout.add_widget(btn)

        self.new_wish(None)
        return self.layout

    def draw_tree(self):
        w = Window.width
        h = Window.height
        cx = w / 2

        with self.layout.canvas:
            Color(0.42, 0.23, 0.12, 1)
            Rectangle(pos=(cx - w * 0.03, h * 0.28),
                      size=(w * 0.06, h * 0.08))

            Color(0.06, 0.48, 0.18, 1)
            Triangle(points=[
                cx, h * 0.72,
                cx - w * 0.28, h * 0.30,
                cx + w * 0.28, h * 0.30,
            ])
            Color(0.08, 0.61, 0.23, 1)
            Triangle(points=[
                cx, h * 0.85,
                cx - w * 0.22, h * 0.48,
                cx + w * 0.22, h * 0.48,
            ])
            Color(0.11, 0.75, 0.29, 1)
            Triangle(points=[
                cx, h * 0.95,
                cx - w * 0.16, h * 0.65,
                cx + w * 0.16, h * 0.65,
            ])

            Color(1, 0.84, 0, 1)
            Triangle(points=[
                cx, h * 0.99,
                cx - w * 0.04, h * 0.93,
                cx + w * 0.04, h * 0.93,
            ])
            Triangle(points=[
                cx, h * 0.90,
                cx - w * 0.04, h * 0.945,
                cx + w * 0.04, h * 0.945,
            ])

            ornaments = [
                (cx - w * 0.12, h * 0.36, (1, 0.2, 0.2)),
                (cx + w * 0.12, h * 0.36, (0.2, 0.5, 1)),
                (cx, h * 0.40, (1, 1, 0.2)),
                (cx - w * 0.10, h * 0.52, (0.7, 0.3, 1)),
                (cx + w * 0.10, h * 0.52, (0.2, 1, 1)),
                (cx, h * 0.56, (1, 0.6, 0.1)),
                (cx - w * 0.07, h * 0.70, (1, 0.4, 0.7)),
                (cx + w * 0.07, h * 0.70, (1, 1, 1)),
                (cx, h * 0.74, (1, 0.2, 0.2)),
                (cx, h * 0.88, (1, 0.2, 1)),
            ]
            for x, y, col in ornaments:
                Color(*col, 1)
                r = w * 0.02
                Ellipse(pos=(x - r, y - r), size=(r * 2, r * 2))
                Color(1, 1, 1, 1)
                Line(circle=(x, y, r), width=1)

    def new_wish(self, instance):
        self.wish_label.text = random.choice(WISHES)


if __name__ == "__main__":
    ElkaApp().run()