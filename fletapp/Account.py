import flet as ft
import pyrebase
import json

# Load Firebase configuration from a file
fireconfig = json.load(open('fletapp/firebase/firebaseConfig.json', 'r'))
firebase = pyrebase.initialize_app(fireconfig)
db = firebase.database()

def page_builder(self):
    # Check if the user is logged in
    if self.user is None:
        return guest_content(self)
    else:
        return user_content(self)

def guest_content(self):
    # Guest mode content
    return ft.Column([
        ft.Text(
            f"Guest mode", 
            color="#000000", 
            size=20, 
            weight=ft.FontWeight.BOLD
        ),
        ft.Text(
            "Please log in to the system or sign up for an account.\n\n", 
            color="#737373",
            size=14),
        ft.Row([
            ft.ElevatedButton("Login",
                bgcolor="red",
                color="white",
                width=120,
                on_click=lambda e: self.page.go('/login'),
            ),
            ft.ElevatedButton("Sign Up",
                bgcolor="green",
                color="white",
                width=120,
                on_click=lambda e: self.page.go('/signup'),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ])

def user_content(self):
    try:
        # Attempt to retrieve user data from the database
        user_data = db.child('users').child(self.user).get().val()

        # Check if username is available, use email if not
        if user_data and 'username' in user_data and user_data['username'] != "":
            username = user_data['username']
        else:
            username = self.user_email

        # User content
        return ft.Column([
            ft.Text(
                f"Welcome, {username}", 
                color="#000000", 
                size=20, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Text("Edit Account Information", color="#737373", size=14),
            ft.Row([
                ft.ElevatedButton("Logout",
                    bgcolor="blue",
                    color="white",
                    width=120,
                    on_click=lambda e: logout(self),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ])
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in user_content: {e}")
        # Provide a generic error message to the user
        return ft.Column([
            ft.Text("An error occurred while retrieving user data. Please try again later.", color="#FF0000", size=16),
            ft.Row([
                ft.ElevatedButton("Login",
                    bgcolor="red",
                    color="white",
                    width=120,
                    on_click=lambda e: self.page.go('/login'),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ])

def logout(self):
    # Clear user-related information from client storage
    self.page.client_storage.clear()
    self.user = None
    # Update the page
    self.page.update()
    self.page.go('/')

class AccountMain(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.user = page.client_storage.get("user_id")
        self.user_email = page.client_storage.get("user_email")

    def build(self):
        # Main container for the account page
        main_container = ft.Container(
            ft.Column(
                [
                    ft.Row([
                        ft.Text("Account", color="#000000", size=28, weight=ft.FontWeight.BOLD,),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(
                        page_builder(self),  # Pass the user to the method
                        margin=ft.margin.only(left=20, right=20),
                    ),
                ],
                width=320,
            )
        )
        # Safe area container with gradient background
        return ft.SafeArea(
            ft.Container(
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
                ),
                width=800,
                height=2000,
                expand=True,
                content=main_container,
            )
        )
