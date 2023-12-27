import flet as ft
import math

class Task(ft.UserControl):
    def __init__(self, task_name,task_price, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_price = task_price
        self.task_status_change = task_status_change
        self.task_delete = task_delete

      
        

    def build(self):
        self.display_task = ft.Checkbox(
            autofocus=None,
            value=False, 
            label=f"{self.task_name} - {self.task_price}฿", 
            check_color="#FFDD94",
            fill_color= "#FA879B",
            on_change=self.status_changed,
        )
        self.edit_name = ft.TextField(expand=1 ,
            border_radius=30,color="BLACK",bgcolor="WHITE",
            border_color="#FA987B",focused_border_color="#FA987B",)
        
        
        
        

        self.display_view = ft.Container(
            width=600,
            height=80,
            border_radius=30,
            bgcolor="#ffffff",
            content =ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                #self.display_buy,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
            ),
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.CHECK,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])
    
    

    

    async def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()

    async def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        await self.update_async()

    async def status_changed(self, e):
        self.completed = self.display_task.value
        await self.task_status_change(self)

    async def delete_clicked(self, e):
        await self.task_delete(self)


class ToBuyApp(ft.UserControl):
    def build(self):


        self.new_task = ft.TextField(
            hint_text="What needs to buy?", on_submit=self.add_clicked, expand=True,border_radius=40,color="BLACK",bgcolor="WHITE",
            border_color="#FA987B",focused_border_color="#CCAB8",
                                
        )
        self.new_buy = ft.TextField(
            hint_text="price",text_align="center", on_submit=self.add_clicked, expand=False,width=90,height=60,
            border_radius=10,color="BLACK",bgcolor="WHITE",
            border_color="#FA987B",focused_border_color="#CCAB8",
                                
        )
        self.tasks = ft.Column()
        
        

        self.filter = ft.Tabs(
            divider_color="#B1B8BD",
            indicator_color="#B1B8BD",
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="all",), 
                #ft.Tab(text="active"), 
                ft.Tab(text="completed")],
        )

        self.items_left = ft.Text("0 items left")
        self.total = ft.Text("Total price = 0 ฿")

        self.total_price = 0  # Initialize total price to 0

        
        

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            alignment=ft.alignment.center,
            width=380,
            expand=True,
            #scroll="END",
            #height=1000,
            controls=[
                ft.Row(
                    [ft.Text(value="To Buy List", size=25,weight=ft.FontWeight.BOLD,)],
                    
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        self.new_task,
                        self.new_buy,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD,

                            shape=ft.CircleBorder(),
                            bgcolor="#F69CB4",
                            on_click=self.add_clicked,
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[self.total],
                )
            ],
        )
    
    

    async def add_clicked(self, e):
        if self.new_task.value:
            price_input = self.new_buy.value.strip()  # Remove leading/trailing spaces
            if price_input:
                try:
                    price = float(price_input)
                    task = Task(self.new_task.value, price, self.task_status_change, self.task_delete)
                    self.tasks.controls.append(task)
                    self.new_task.value = ""
                    self.new_buy.value = ""  # Clear the price field
                    await self.new_task.focus_async()

                # Update total price when a new task is added
                    self.total_price += price
                    self.total.value = f"Total price = {self.total_price} ฿"
                    await self.update_async()
                except ValueError:
                # Handle the case where the input is not a valid number
                # You can show an error message or take other actions as needed
                    pass
                 


    async def task_status_change(self, task):
        await self.update_async()

        # Update total price when the status of a task changes
        #self.updupdate_asyncate_total_price()

    async def task_delete(self, task):
        self.tasks.controls.remove(task)
    
    # Update total price by subtracting the deleted task's price
        self.total_price -= float(task.task_price)
        self.total.value = f"Total price = {self.total_price} ฿"

        await self.update_async()


    async def tabs_changed(self, e):
        await self.update_async()

    async def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
            # Subtract the completed task's price from the total price
                self.total_price -= float(task.task_price)
                self.tasks.controls.remove(task)

        self.total.value = f"Total price = {self.total_price} ฿"
        await self.update_async()


    
    def update_total_price(self):
        self.total_price = sum(float(task.task_price) for task in self.tasks.controls if not task.completed)
        self.total.value = f"Total price = {self.total_price} ฿"
        


    async def update_async(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count}  item(s) to buy left"
        await super().update_async()

        




async def main(page: ft.Page):
    page.title = "To Buy App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.padding = 0
    page.bgcolor = "#ddf7f1"
    page.window_max_width = 410
    page.window_width = 800
    page.window_max_height = 780
    page.window_height = 780
    
    


    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
    }

    page.theme = ft.Theme(font_family="SF Pro")



    c2 = ft.SafeArea(ft.Container(
                    alignment=ft.alignment.center,
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
                content = ToBuyApp() 
    )
            )
    page.navigation_bar = ft.NavigationBar(bgcolor="#CCABD8",selected_index=1,
            destinations=[
            ft.NavigationDestination(icon=ft.icons.CHECK,),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, ),
            ft.NavigationDestination(icon=ft.icons.HOME, ),
            ft.NavigationDestination(icon=ft.icons.CALCULATE,),
            ft.NavigationDestination(icon=ft.icons.PERSON, ),
        ]
    )




    # create app control and add it to the page
    await page.add_async(c2)


ft.app(main)