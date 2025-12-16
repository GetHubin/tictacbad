from typing import List

import arcade
import arcade.gui
from random import randrange
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        #create the observer pattern
        self.manager = arcade.gui.UIManager()

        #makes the button but not on screen just make it a var
        switch_menu_button = arcade.gui.UIFlatButton(text="pause", width= 250)

        #does the thing when you click it
        @switch_menu_button.event("on_click")
        #this is that event on_click is not a part of the name just signifies it's on click event
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            menu_view = MenuView(self)
            self.window.show_view(menu_view)

        #this puts everything it in the code
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=switch_menu_button,
        )



    def on_show_view(self):
        arcade.set_background_color(arcade.color.BISQUE)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()


    def on_draw(self):
        self.clear()
        self.manager.draw()

class MenuView(arcade.View):
    def __init__(self, main_view):
        super().__init__()
        self.main_view = main_view

        self.manager = arcade.gui.UIManager()
        self.main_view = main_view
        resume = arcade.gui.UIFlatButton(text="Resume", width=150)
        start_new_game = arcade.gui.UIFlatButton(text="Start New Game", width=150)
        volume = arcade.gui.UIFlatButton(text="Volume", width=150)
        options = arcade.gui.UIFlatButton(text="Options", width=150)
        exit = arcade.gui.UIFlatButton(text="Exit", width=320)

        #grid for placing
        self.grid = arcade.gui.UIGridLayout(column_count=2, row_count=3, horizontal_spacing=20, vertical_spacing=20)
        self.grid.add(resume, 0, 0)
        self.grid.add(start_new_game, 1, 0)
        self.grid.add(volume, 0, 1)
        self.grid.add(options, 1, 1)
        self.grid.add(exit, 0, 2 , 2)

        @resume.event("on_click")
        def on_click_resume(event):
            self.window.show_view(self.main_view)

        @start_new_game.event("on_click")
        def on_click_start_new_game(event):
            main_view = MainView()
            self.window.show_view(main_view)

        @exit.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()

        @volume.event("on_click")
        def on_click_volume(event):
            volume_menu = SubMenu(
                "Volume Menu",
                "How do you like your volume?",
                "Enable Sound",
                ["Play: Rock", "Play: Punk", "Play: Pop"],
                "Adjust Volume",
            )
            self.manager.add(volume_menu, layer=1)

        @options.event("on_click")
        def on_click_options(event):
            options_menu = SubMenu("Funny Menu",
                "Too much fun here",
                "Fun?",
                ["Make Fun", "Enjoy Fun", "Like Fun"],
                "Adjust Fun",
            )
            self.manager.add(options_menu, layer=1)

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid
        )



    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.manager.enable()

    def on_draw(self):
        # Clear the screen
        self.clear()
        self.manager.draw()

class SubMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    """Acts like a fake view/window."""
    def __init__(
            self,
            title: str,
            input_text: str,
            toggle_label: str,
            dropdown_options: List[str],
            slider_label: str,
    ):
        super().__init__(size_hint=(1,1))

        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None))
        frame.with_padding(all=20)

        frame.with_background(
            texture=arcade.gui.NinePatchTexture(
                left=7,
                right=7,
                bottom=7,
                top=7,
                texture=arcade.load_texture(
                    ":resources:gui_basic_assets/window/dark_blue_gray_panel.png"
                ),
            )
        )

        title_label = arcade.gui.UILabel(text=title, align="center", font_size=20, multiline=False)
        # Adding some extra space around the title.
        title_label_space = arcade.gui.UISpace(height=30, color=arcade.color.DARK_BLUE_GRAY)
        input_text_widget = arcade.gui.UIInputText(text=input_text, width=250).with_border()
        back_button = arcade.gui.UIFlatButton(text="Back", width=250)

        #The type of event listener we used earlier for the button will not work here.
        back_button.on_click = self.on_click_back_button
        # Load the on-off textures.
        on_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_on.png"
        )
        off_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_off.png"
        )
        toggle_label = arcade.gui.UILabel(text=toggle_label)
        toggle = arcade.gui.UITextureToggle(on_texture=on_texture, off_texture=off_texture, width=20, height=20)
        toggle_group = arcade.gui.UIGridLayout(column_count=2, horizontal_spacing=5)

        toggle_group.add(toggle, 0, 0)
        toggle_group.add(toggle_label, 1, 0)

        dropdown_options = arcade.gui.UIDropdown(defult=dropdown_options[0], options=dropdown_options, height= 20, width=250)
        slider_label = arcade.gui.UILabel(text=slider_label)
        pressed_style = arcade.gui.UISlider.UIStyle(filled_track=arcade.color.GREEN, unfilled_track=arcade.color.RED)
        default_style = arcade.gui.UISlider.UIStyle()
        style_dict = {
            "press": pressed_style,
            "normal": default_style,
            "hover": default_style,
            "disabled": default_style,
        }
        # Configuring the styles is optional.
        slider = arcade.gui.UISlider(value=50, width=250, style=style_dict)

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(title_label)
        widget_layout.add(title_label_space)
        widget_layout.add(input_text_widget)
        widget_layout.add(back_button)
        widget_layout.add(toggle_group)
        widget_layout.add(dropdown_options)
        widget_layout.add(slider_label)
        widget_layout.add(slider)

        frame.add(child=widget_layout, anchor_x="center_x", anchor_y="top")

    def on_click_back_button(self, event):
        self.parent.remove(self)








def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "make menu", resizable=True)
    window.show_view(MainView())
    arcade.run()

if __name__ == "__main__":
    main()