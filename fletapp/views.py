import flet as ft
from homepage import Home
from todo_new import ToDoMain
from tobuy_new import ToBuyMain
from calculator import Calculator
#from calendar import Calendar
from Account import AccountMain
from signup import SignupMain
from login import LoginMain
from forgetpass import ForgetMain

class ChangeNav(ft.UserControl):
    def __init__(self, page, selected_index):
        super().__init__()
        self.page = page
        self.index = selected_index

    def changetab(self):
        # Define destinations based on route URLs
        destinations = ['/todo', '/tobuy', '/', '/calculator', '/account']
        destination_url = destinations[self.index]
        self.page.go(destination_url)

    def build(self):
        # Print the selected index for debugging purposes
        print(self.index)
        return None  # You need to return something from the build method, even if it's None

def navBar(selectedIndex):
    # Navigation bar with icons and an event handler for tab changes
    return ft.NavigationBar(
        bgcolor="#fe96a5",
        selected_index=selectedIndex,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CHECK),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
            ft.NavigationDestination(icon=ft.icons.HOME),
            ft.NavigationDestination(icon=ft.icons.CALCULATE),
            ft.NavigationDestination(icon=ft.icons.PERSON),
        ],
        on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
    )

def views(page):
    # Define views for different routes along with associated controls and navigation bars
    return {
        '/': ft.View(
            route='/',
            controls=[Home(page)],
            navigation_bar=navBar(2)  # Set the selected index for the home route
        ),
        
        '/todo': ft.View(
            route='/todo/',
            controls=[ToDoMain(page)],
            navigation_bar=navBar(0)  # Set the selected index for the todo route
        ),
        '/tobuy': ft.View(
            route='/tobuy/',
            controls=[ToBuyMain(page)],
            navigation_bar=navBar(1)  # Set the selected index for the tobuy route
        ),
        '/calculator': ft.View(
            route='/calculator/',
            controls=[Calculator(page)],
            navigation_bar=navBar(3)  # Set the selected index for the calculator route
        ),
        '/account': ft.View(
            route='/account/',
            controls=[AccountMain(page)],
            navigation_bar=navBar(4)  # Set the selected index for the account route
        ),
        '/signup': ft.View(
            route='/signup/',
            controls=[SignupMain(page)]
        ),
        '/login': ft.View(
            route='/login/',
            controls=[LoginMain(page)]
        ),
        '/forgetpass': ft.View(
            route='/forgetpass/',
            controls=[ForgetMain(page)]
        ),
    }
