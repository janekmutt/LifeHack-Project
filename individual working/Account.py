import flet as ft
from flet import *

class ChangeNav(ft.UserControl):
      def __init__(self, page, selected_index):
        super().__init__()
        self.page = page
        self.index = selected_index

      def changetab(self):
        destinations = ['/', '/', '/', '/calculator', '/login']
        destination_url = destinations[self.index]
        self.page.go(destination_url)

      def build(self):
        print(self.index)  # Note: This print statement should be inside the build method
        return None  # You need to return something from the build method, even if it's None

def main(page):
    
    page.fonts = {
        "SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
    }
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(font_family="SF Pro")
    page.window_max_width = 410
    page.window_width = 800
    page.window_max_height = 800
    page.window_height = 800
    page.bgcolor = "#ddf7f1"
    # page.scroll ="auto"
    
    page.title = "My Account"

    # class ChangeNav(ft.UserControl):
    #   def __init__(self, page, selected_index):
    #     super().__init__()
    #     self.page = page
    #     self.index = selected_index

    #   def changetab(self):
    #     destinations = ['/', '/', '/', '/calculator', '/login']
    #     destination_url = destinations[self.index]
    #     self.page.go(destination_url)

    #   def build(self):
    #     print(self.index)  # Note: This print statement should be inside the build method
    #     return None  # You need to return something from the build method, even if it's None
    
    # name_field = ft.TextField(label="Name")
    # email_field = ft.TextField(label="Email")
    # password_field = ft.TextField(label="Password", password=True)
    
    # update_button = ft.ElevatedButton("Update Account", on_click=update_account)
    # logout_button = ft.OutlinedButton("Logout", on_click=logout)
    # login_button = ft.OutlinedButton(on_click=LoginEvent,
    #                                  text="Login", 
    #                                 # #  width=100,
    #                                 # #  border_radius=8,
    #                                 # #  border_color=ft.colors.BLUE,
    #                                 #  border_width=2,
    #                                  )

    Account = ft.Container(  
        ft.Column(
            [
                ft.Row([
                    ft.Text("Account", color = "#000000" ,size=28, weight=ft.FontWeight.BOLD,),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Text("Account", color = "#000000" ,size=28, weight=ft.FontWeight.BOLD, alignment = ft.alignment.center),
                ft.Text("Guess mode", color = "#000000" , size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Please log in to the system\n\n", color = "#737373", size=14),
                ft.Row([
                    ft.ElevatedButton("login",bgcolor = "red", color="white",
                                      width=120),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"),
                ft.Container(
                    alignment=ft.alignment.bottom_center,
                    margin=ft.margin.only(bottom=10),
                    content= ft.NavigationBar(bgcolor="#fe96a5", selected_index=2,
                    destinations=[
                        ft.NavigationDestination(icon=ft.icons.CHECK),
                        ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
                        ft.NavigationDestination(icon=ft.icons.HOME),
                        ft.NavigationDestination(icon=ft.icons.CALCULATE),
                        ft.NavigationDestination(icon=ft.icons.PERSON),
                    ],
                    on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
            ),
    )
                

                # ft.ElevatedButton("login",bgcolor = "red", color="white",
                #            on_click = login_button, width=120),
                # name_field, 
                # email_field,
                # password_field,
                # ft.Row([update_button, logout_button], alignment="spaceBetween")
            ],
            
            width = 350,
        )
    )

    # NavBAR = ft.Container(
    #     ft.Column(
    #         [
    #             ft.Container(
    #                 alignment=ft.alignment.bottom_center,
    #                 margin=ft.margin.only(bottom=10),
    #                 content= ft.NavigationBar(bgcolor="#fe96a5", selected_index=2,
    #                 destinations=[
    #                     ft.NavigationDestination(icon=ft.icons.CHECK),
    #                     ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
    #                     ft.NavigationDestination(icon=ft.icons.HOME),
    #                     ft.NavigationDestination(icon=ft.icons.CALCULATE),
    #                     ft.NavigationDestination(icon=ft.icons.PERSON),
    #                 ],
    #                 on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
    #         ),
    # )
                

    #             # ft.ElevatedButton("login",bgcolor = "red", color="white",
    #             #            on_click = login_button, width=120),
    #             # name_field, 
    #             # email_field,
    #             # password_field,
    #             # ft.Row([update_button, logout_button], alignment="spaceBetween")
    #         ],
    #         width = 350
    #     )
    # )
    
    # ft.Container(
    #         alignment=ft.alignment.bottom_center,
    #         margin=ft.margin.only(bottom=10),
    #         content= ft.NavigationBar(bgcolor="#fe96a5", selected_index=2,
    #             destinations=[
    #                 ft.NavigationDestination(icon=ft.icons.CHECK),
    #                 ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
    #                 ft.NavigationDestination(icon=ft.icons.HOME),
    #                 ft.NavigationDestination(icon=ft.icons.CALCULATE),
    #                 ft.NavigationDestination(icon=ft.icons.PERSON),
    #             ],
    #             on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
    #         ),
    # )

    c2 = ft.SafeArea(ft.Container(
                     gradient=ft.LinearGradient(
                     begin=ft.alignment.top_center,
                     end=ft.alignment.bottom_center,
                     colors=[
                         "#ddf7f1",
                         "#f2f8e6",
                         "#fff5e1",
                         "#feddda",
                         "#f1e7f5",
                     ],
                     tile_mode=ft.GradientTileMode.MIRROR,
                     #rotation=math.pi / 4,
                 ),
                 
                 width=800,
                 height=2000,
                 expand=True, 
                 content = Account
     ))
    
    page.add(ft.SafeArea(c2))
    
ft.app(target=main)