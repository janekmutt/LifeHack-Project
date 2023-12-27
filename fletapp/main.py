import flet as ft
import views as views_handle

def main(page: ft.Page):
    
    #defining the fonts
    page.fonts = {
        "SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
    }
    
    #defining the window size
    page.window_min_width = 425
    page.window_width = 425
    page.window_min_height = 820
    page.window_height = 820

    page.title = "Project 334 Appication"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.scroll = ft.ScrollMode.HIDDEN
    page.padding = 0
    page.bgcolor = "#ddf7f1"

    page.theme = ft.Theme(font_family="SF Pro")
    page.theme_mode = ft.ThemeMode.LIGHT

    

    def route_change(route):
        print(page.route)
        # CLEAR ALL PAGE
        page.views.clear()
        page.views.append(
            views_handle.views(page)[page.route],
        )
        page.update()
            
    page.on_route_change = route_change
    page.go('/')

ft.app(target = main)