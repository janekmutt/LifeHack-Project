import flet as ft
import math
import pyrebase
import json

fireconfig = json.load(open('fletapp/firebase/firebaseConfig.json', 'r'))
firebase = pyrebase.initialize_app(fireconfig)
auth = firebase.auth()

# Variable 
success_dlg = ft.AlertDialog(
	title=ft.Text("Sign in sucessfully",			
		size=16,
		color="#539165",
		text_align="center",
	), on_dismiss=lambda self: (
		print("Success Dialog dismissed!"),
		#setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update(),
		self.page.go('/account')
    )
)

wrong_dlg = ft.AlertDialog(
	title=ft.Text("Wrong email or password",		
		size=16,
		color="#C70039",
		text_align="center",
	), on_dismiss=lambda self: (
		print("Wrong Dialog dismissed!"),
	    #setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
empty_Email_and_pass = ft.AlertDialog(
	title=ft.Text("Please enter email and password",		
		size=16,
		color="#C70039",
		text_align="center",
	), on_dismiss=lambda self: (
		print("Wrong Dialog dismissed!"),
	    #setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)

def open_success_dlg(self):
	self.page.theme_mode=ft.ThemeMode.LIGHT
	print(f"Sign in sucessfully")
	self.page.dialog = success_dlg
	success_dlg.open = True
	self.page.update()
def open_wrong_dlg(self):
	self.page.theme_mode=ft.ThemeMode.LIGHT
	print(f"Wrong email or password")
	self.page.dialog = wrong_dlg
	wrong_dlg.open = True
	self.page.update()
def open_empty_Email_and_pass(self) : 
	self.page.theme_mode=ft.ThemeMode.LIGHT
	print(f"Please enter email and password")
	self.page.dialog = empty_Email_and_pass
	empty_Email_and_pass.open = True
	self.page.update()


def post(self):
	if self.Email.value == "" : 
		open_empty_Email_and_pass(self)
	else: 
		try:
			self.user = auth.sign_in_with_email_and_password(
				self.Email.value, self.password.value)
			#print(self.user)
			self.page.client_storage.set("user_id", self.user["localId"])
			self.page.client_storage.set("user_email", self.user["email"])
			value = self.page.client_storage.get("user_id")
			print(value)
			open_success_dlg(self)
		except:
		#self.add(ft.SafeArea(ft.Container(ft.Text("Wrong username or password"))))
			open_wrong_dlg(self)

		
class LoginMain(ft.UserControl):
	def __init__(self, page):
		super().__init__()
		self.page = page
		self.Email = ft.TextField(
			label="E-mail",
			text_style=ft.TextStyle(size=14, color="#000000"),
			border_radius=40,
			border_color=ft.colors.BLACK,
			focused_border_color=ft.colors.ORANGE_700,
		)

		self.password = ft.TextField(
			label="Password",
			text_style=ft.TextStyle(size=14, color="#000000"),
			password=True,
			can_reveal_password=True,
			border_radius=40,
			border_color=ft.colors.BLACK,
			focused_border_color=ft.colors.ORANGE_700,
		)

	def build(self):
		#self.page.add(self.Email)
		return ft.SafeArea(ft.Container(
		#image_src="signinbg.jpg",
		
		#image_fit=ImageFit.NONE,
		#expand=True,
		alignment=ft.alignment.center,
		gradient=ft.LinearGradient(
			rotation=math.pi / 3,
			colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
			),

		#bgcolor="#ffffff",
		border_radius=10,
		height=760,
		theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
		theme_mode=ft.ThemeMode.LIGHT,
		content=ft.Column(
			width = 320,
			controls=[
				#Container(
					#content=Image(
						#src=signinbg.jpg"
					#)
				#),
				ft.Row(
					controls=[
						ft.Container(
                        width=48,
                        height = 40,
                        border_radius = 10,
                        margin=ft.margin.only(top=20),
                        content=ft.IconButton(
                            icon_color ="#000000",
                            icon=ft.icons.ARROW_BACK_IOS_NEW_SHARP,
                            on_click=lambda e: self.page.go('/account'),  
                            style=ft.ButtonStyle(
                                side= {
                                    ft.MaterialState.DEFAULT : ft.border.BorderSide(1, ft.colors.GREY)
                                },
                            )
                        )),
						ft.Container(
							width=150,
							margin=ft.margin.only(left=120,right=10,top=20),
							content=ft.TextButton(
								"Create Account",
								style=ft.ButtonStyle(color="#7D7C7C"),
								on_click=lambda e: self.page.go('/signup'), 
							)
						),
					]
				),
				ft.Container(
					width =300,
					margin=ft.margin.only(left=90,right=10,top=20),
					content=ft.Text(
						"WELCOME",
						#text_align="center",
						size=24,
						color="#000000",
						weight="w700"
					)
				),
				ft.Container(
					width =300,
					margin=ft.margin.only(left=100,right=10,top=5),
					content=ft.Text(
						"LifeHack!",
						size=24,
						color="#000000",
						weight="w700"
					)
				),
				ft.Container(
				 width =300,
					margin=ft.margin.only(left=65,right=10,top=20),
					content=ft.Text(
						"Hack your life by lifeHack",
						#text_align="center",
						size=15,
						color="#000000"   
					)
				),
				ft.Container(
					width=300,  
					margin=ft.margin.only(left=10,right=10,top=20), 
					content = ft.Column(
						controls=[self.Email],
					),
					
				),
				ft.Container(
					width =300,  
					margin=ft.margin.only(left=10,right=10,top=5), 
					content=ft.Column(
						controls=[self.password],
					)
				),
				ft.Container(
					width=300,
					margin=ft.margin.only(left=150,right=10,top=5), 
					content=ft.TextButton(
						"Forgot Password?" ,
						style=ft.ButtonStyle(),
						on_click=lambda e: self.page.go('/forgetpass'),
					)
				),
				ft.Container(
					width=300,
					margin=ft.margin.only(left=20,right=10,top=5,bottom=20), 
					content=ft.TextButton(
						"Login" ,
						width=300,
						height=50,
						style=ft.ButtonStyle(
							color="#ffffff",
							bgcolor=ft.colors.ORANGE_700,
							shape={}
						),
        				on_click=lambda e: post(self),
					)
				)
			]
		),
	)
)