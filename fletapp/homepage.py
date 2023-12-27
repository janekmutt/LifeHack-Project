# importing the library

import flet as ft
import datetime 
import threading as th
import time

class TimeLine(ft.UserControl):
	def __init__(self):
		super().__init__()
		self.now = datetime.datetime.now()
		self.date = self.now.strftime("%A, %B, %d")
		self.time = self.now.strftime("%H:%M")

		self.field_date = ft.Text(
			self.date,
			text_align= ft.TextAlign.CENTER,
			color = 'Black',
			size = 24,
			weight = 'bold',
		)

		self.field_time = ft.Text(
			self.time,
			color = 'Black',
			weight = '300',
			size = 30,
			# weight = 'bold',
		)
	
	def update_datetime(self):
		while True:
			time.sleep(1)
			self.now = datetime.datetime.now()
			self.date = self.now.strftime("%A, %B %d")
			self.time = self.now.strftime("%H:%M:%S")
			self.field_date.value = self.date
			self.field_time.value = self.time
			self.field_date.update()
			self.field_time.update()

	def did_mount(self):
		th.Thread(target = self.update_datetime).start()
		
	def build(self):
		return ft.Container(
			ft.Column([
				ft.Container(
					self.field_date,
					alignment = ft.alignment.center
				),
			ft.Container(
				self.field_time,
					alignment = ft.alignment.center,
					margin = ft.margin.only(top = 10),
				)
			],spacing = 0),
			width = 320,
			height = 100,
			alignment = ft.alignment.center
			)

class Home(ft.UserControl):
	def __init__(self,page):
		super().__init__()
		self.page = page

	def build(self):
		return ft.SafeArea(
    ft.Container(
		ft.Column([
            # Top off the page
            ft.Row([
                ft.Container(
                    alignment=ft.alignment.top_left,
                    margin=ft.margin.only(left=10),
                    content=ft.Text("Hello!", color='#FFFFFF', size=32, weight="bold"),
                )
            ]),
            ft.Row([
                ft.Container(
                    alignment=ft.alignment.top_left,
                    margin=ft.margin.only(left=10, top=-10),
                    content=ft.Text("have a nice day", color='#FFFFFF', size=16),
                ),
            ]),

            # Main content
            ft.Row([
                ft.Container(
                    alignment=ft.alignment.bottom_center,
                    margin=ft.margin.only(left=8, right=8),
                    bgcolor=ft.colors.with_opacity(0.8, '#FFFFFF'),
                    border_radius=ft.border_radius.only(30, 30, 30, 30),
                    content=ft.Column([
                        ft.Row([
                            # Timeline Box
                            ft.Container(
                                content=TimeLine(),
                                alignment=ft.alignment.top_center,
                                margin=ft.margin.only(left=25, right=25, top=25),
                                height=115,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right,
                                    colors=['#86E3CE', '#D6E6A5', '#FFDD94', '#FA897B', '#CCABD8']
                                ),
                                padding=ft.padding.only(0, 15, 0, 15),
                                border_radius=10,
                            ),
                        ]),
						
                        # Button to other pages
                        ft.Row([
							ft.Column([
								ft.Container(
                                    width=160,
                                    height=200,
                                    #top=230,
                                    #left=25,
                                    margin=ft.margin.only(left=20),
                                    on_click=lambda _: self.page.go('/todo'),
                                    alignment=ft.alignment.top_center,
                                    padding=ft.padding.all(10),
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=ft.alignment.bottom_right,
                                        colors=['#86E3CE', '#D6E6A5', '#FFDD94', '#FA897B', '#CCABD8']
                                    ),
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.Column([
                                            ft.Row([
                                                ft.Image(
                                                    src="../assets/check-box_icon-icons.com_72816.png",
                                                    width=70, height=90
                                                ),
                                            ],alignment=ft.MainAxisAlignment.CENTER),
                                            ft.Row([
                                                ft.Text(
                                                    value="To Do List",
                                                    color="black",
                                                    size=15,
                                                    weight='bold',
                                                    style=ft.ButtonStyle(
                                                        color="white",
                                                        padding=10
                                                    )
                                                ),
                                            ],alignment=ft.MainAxisAlignment.CENTER),
                                            ft.Text(
                                                value = "'To Do List' is like a time management tool with a lot more fun built in.",
                                                color = "#424949",
                                                size = 11,
                                                style = ft.ButtonStyle(
                                                    color = "white",
                                                    padding = 10)
                                                ),
                                        ],
                                        spacing=1
                                    ),
                                ),
                            ]),

                            ft.Column([
                                ft.Container(
                                    width=160,
                                    height=200,
                                    #top=230,
                                    #left=208,
                                    margin=ft.margin.only(right=20),
                                    on_click=lambda _: self.page.go('/tobuy'),
                                    alignment=ft.alignment.bottom_center,
                                    padding=ft.padding.all(10),
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=ft.alignment.bottom_right,
                                        colors=['#86E3CE', '#D6E6A5', '#FFDD94', '#FA897B', '#CCABD8']
                                    ),
                                    border_radius=ft.border_radius.all(30),
                                    content=ft.Column([
                                            ft.Row([
                                                ft.Image(
                                                    src="../assets/2849824-basket-buy-market-multimedia-shop-shopping-store_107977.png",
                                                    width=90, height=90
                                                ),
                                            ],alignment=ft.MainAxisAlignment.CENTER),
                                            ft.Row([
                                                ft.Text(
                                                    value="Shopping List",
                                                    color="black",
                                                    size=15,
                                                    weight='bold',
                                                ),
                                            ],alignment=ft.MainAxisAlignment.CENTER),
                                            ft.Text(
                                                value="A shopping list: the only list that makes your wallet shed a tear",
                                                color="#424949",
                                                size=11,
                                                style=ft.ButtonStyle(
                                                    color="white",
                                                    padding=10
                                                )
                                            ),
                                        ],
                                    ),
                                ),
							]),
                        ]),
						
                        ft.Row([
							ft.Column([
                                ft.Container(
                                    width = 162,
                                    height = 200, 
                                    #top = 450,
                                    #left = 25,
                                    margin=ft.margin.only(left=20),
                                    on_click = lambda _: self.page.go('/calculator'),
                                    alignment = ft.alignment.center,
                                    padding = ft.padding.all(10),
                                    gradient = ft.LinearGradient(
                                        begin = ft.alignment.top_left,
                                        end = ft.alignment.bottom_right,
                                        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
                                    ), 
                                    border_radius= ft.border_radius.all(30),
                                    content = ft.Column([
                                        ft.Column([
                                            ft.Row([
                                                ft.Image(
                                                        src = "../assets/seo-social-web-network-internet_92_icon-icons.com_61528.png", 
                                                        width = 90, height = 90),
                                                        ], alignment=ft.MainAxisAlignment.CENTER),

                                            ft.Row([
                                                ft.Text(value = "Calculator",
                                                        color = "black",
                                                        size = 15,
                                                        weight = 'bold',
                                                        style = ft.ButtonStyle(color = "white",
                                                            padding = 10)
                                                        ),
                                            ], alignment=ft.MainAxisAlignment.CENTER),
                                        ], spacing = 1),

                                        ft.Text(value = "Your personal mathematician",
                                                        color = "#424949",
                                                        size = 11,
                                                        style = ft.ButtonStyle(
                                                            color = "white",
                                                            padding = 10)
                                                        ),
                                    ], spacing = 7
                                    ),
                                ),
                            ]),

                            ft.Column([
                                # ft.Container(
                                #     width = 162,
                                #     height = 200, 
                                #     #top = 450,
                                #     #left = 208,
                                #     margin=ft.margin.only(right=20),
								# 	on_click = lambda _: self.page.go('/'),
                                #     alignment = ft.alignment.center,
                                #     padding = ft.padding.all(10),
                                #     gradient = ft.LinearGradient(
                                #         begin = ft.alignment.top_left,
                                #         end = ft.alignment.bottom_right,
                                #         colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
                                #     ), 
                                #     border_radius= ft.border_radius.all(30),
                                #     content = ft.Column([
                                #         ft.Column([
                                #             ft.Row([
                                #                 ft.Image( 
                                #                         src = "../assets/annual_calender_day_schedule_date_time_calendar_icon_256444.png", 
                                #                         width = 70, height = 90),
                                #                         ], alignment=ft.MainAxisAlignment.CENTER),
                                        
                                #         ft.Row([
                                #             ft.Text(value = "Calendar",
                                #                         color = "black",
                                #                         size = 15,
                                #                         weight = 'bold',
                                #                         style = ft.ButtonStyle(
                                #                             color = "white",
                                #                             padding = 10)
                                #                         ),
                                #         ], alignment=ft.MainAxisAlignment.CENTER),
                                #         ], spacing = 1),
                                    

                                #         ft.Text(value = "Your calendar is your compass; let it lead you to your dreams.",
                                #                         color = "#424949",
                                #                         size = 11,
                                #                         style = ft.ButtonStyle(
                                #                             color = "white",
                                #                             padding = 10)
                                #                         ),
                                #     ], spacing = 7), 
                                # ),
							]),
                        ]),
						
                        ft.Row([
                            ft.Container(
                                height=20,
                            )
                        ])  
                    ])
                ),
            ]),
        ]),

        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#86E3CE', '#D6E6A5', '#FFDD94', '#FA897B', '#CCABD8']
        ),
        #width=480,
        height=760,
        padding=0,
        border_radius=5,
    )
)
