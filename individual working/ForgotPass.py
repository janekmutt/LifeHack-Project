import flet as ft
from flet import *

def main(page: ft.page):
		
	page.fonts = {
				"SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
	}
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.theme = ft.Theme(font_family="SF Pro")
	page.window_max_width = 410
	page.window_width = 800
	page.window_max_height = 800
	page.window_height = 800
	page.bgcolor = "#000000"
	# page.scroll ="auto"

	page.title = "Password Recovery"

	page.vertical_alignment = ft.MainAxisAlignment.CENTER

	email_field = ft.TextField(label="Email", border_radius=40, 
														 color="BLACK", 
														 bgcolor="WHITE", 
														 border_color="#FA987B", 
														 focused_border_color="#CCABD8",
														)
	
	send_button = ft.ElevatedButton("send", bgcolor = "red", color="white", width=400, on_click=lambda e: send_reset_link(email_field.value))

	ForgotPass = ft.Container(
		content = ft.Column([
			ft.Row([
						ft.Text("Forgot Password", color = "#000000", size = 30, weight = "bold",),
					], alignment=ft.MainAxisAlignment.CENTER),
			
			ft.Row([
						ft.Text("Please enter your email address and \nwe will email you a link to reset your password", color = "#737373", size=14),
					]),
			email_field,
			send_button

		])
	)
	
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
								 height=800,
								 expand=True, 
								 content = ForgotPass       
		 ))
	

	page.padding = 0

	page.add(ft.SafeArea(c2))

def send_reset_link(email):
	# email = email_field.value
	# Code to send reset link to email
	ft.page.snackbar = ft.SnackBar(
			"Reset link sent! Please check your inbox."
	)



ft.app(target=main)