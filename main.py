from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty


class Calculator(Widget):
    points = StringProperty()

    plowed_fields = ObjectProperty()
    fenced_pastures = ObjectProperty()
    grain = ObjectProperty()
    vegetables = ObjectProperty()
    sheep = ObjectProperty()
    wild_boar = ObjectProperty()
    cows = ObjectProperty()

    unused_fields = ObjectProperty()
    fenced_stables = ObjectProperty()
    clay_rooms = ObjectProperty()
    stone_rooms = ObjectProperty()
    family_members = ObjectProperty()
    begging_cards = ObjectProperty()
    card_points = ObjectProperty()
    bonus_points = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.display_result, 0.5)

    def display_result(self, *args, **kwargs):
        points = 0
        for element in [self.plowed_fields, self.fenced_pastures, self.grain, self.vegetables, self.sheep,
                        self.wild_boar, self.cows]:
            points += self.points_toggle_button(element)

        points += self.multiply_points(self.unused_fields, -1)
        points += self.multiply_points(self.fenced_stables, 1)
        points += self.multiply_points(self.clay_rooms, 1)
        points += self.multiply_points(self.stone_rooms, 2)
        points += self.multiply_points(self.family_members, 3)
        points += self.multiply_points(self.begging_cards, -3)
        points += self.multiply_points(self.card_points, 1)
        points += self.multiply_points(self.bonus_points, 1)
        self.points = str(points)
        return self.points

    def points_toggle_button(self, instance):
        for element in instance.children:
            if element.state == 'down':
                return int(element.text_hint)
        return 0

    def multiply_points(self, field, multiplier):
        if field.text == '':
            return 0
        return int(field.text) * multiplier

    def reset_toggle_buttons(self, instance):
        for element in instance.children:
            element.state = 'normal'

    def reset(self):
        for element in [self.plowed_fields, self.fenced_pastures, self.grain, self.vegetables, self.sheep,
                        self.wild_boar, self.cows]:
            self.reset_toggle_buttons(element)

        for element in [self.unused_fields, self.fenced_stables, self.clay_rooms, self.stone_rooms,
                        self.family_members, self.begging_cards, self.card_points, self.bonus_points]:
            element.text = ''


class MainApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    MainApp().run()
