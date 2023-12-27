import flet as ft
import math
import pyrebase
import json

fireconfig = json.load(open('fletapp/firebase/firebaseConfig.json', 'r'))
firebase = pyrebase.initialize_app(fireconfig)
auth = firebase.auth()

def send_reset_link(self):
	print(self.email_field.value)
	auth.send_password_reset_email(self.email_field.value)
	ft.page.snackbar = ft.SnackBar(
			"Reset link sent! Please check your inbox."
	)

class ForgetMain(ft.UserControl):
	def __init__(self, page):
		super().__init__()
		self.page = page

		self.email_field = ft.TextField(
			label="Email",
			text_style=ft.TextStyle(size=14, color="#000000"),
			border_radius=40, 
			border_color=ft.colors.BLACK,
			focused_border_color=ft.colors.ORANGE_700,
		)
		
		self.send_button = ft.ElevatedButton(
			"send",
			bgcolor = "red", 
			color="white", 
			width=300, 
			on_click=lambda e: send_reset_link(self)
		)

		self.ForgotPass = ft.Column([
			ft.Container(
				width=48,
				height = 40,
				border_radius = 10,
				margin=ft.margin.only(top=20),
				content=ft.IconButton(
					icon_color ="#000000",
					icon=ft.icons.ARROW_BACK_IOS_NEW_SHARP,
					on_click=lambda e: self.page.go('/login'),  
					style=ft.ButtonStyle(
						side= {
							ft.MaterialState.DEFAULT : ft.border.BorderSide(1, ft.colors.GREY)
						},
					)
				)
			),
			ft.Row([
				ft.Container(
					ft.Text("Forgot Password", 
						color = "#000000", 
						size = 30, 
						weight = "bold",
					),
					margin=ft.margin.only(top=20),
				),
			], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
			ft.Row([
				ft.Text("Please enter your email address and \nwe will email you a link to reset your password", 
					color = "#7D7C7C", 
					size=14
				),
			]),
			ft.Row([
				self.email_field,
			]),
			ft.Row([
				self.send_button
			]),
		],width = 320,)

	
	def build(self):
		return ft.SafeArea(
			ft.Container(
				alignment=ft.alignment.center,
				theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
				theme_mode=ft.ThemeMode.LIGHT,
				gradient=ft.LinearGradient(
					rotation=math.pi / 3,
					colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
					),
				width=800,
				height=760,
				border_radius=10,
				#expand=True, 
				content = self.ForgotPass       
			)	
		)
	

