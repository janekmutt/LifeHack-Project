import flet as ft

class CalculatorLogic(ft.UserControl):
    def __init__(self, calculator, quantity):
        super().__init__()
        self.page = calculator.page
        self.quantity = quantity
        self.cost_per_unit_value = calculator.cost_per_unit_value
        self.product_container = calculator.product_container
        self.product_data = {}

    def cal_cost_per_unit(self, cost, unit):
        return ("%.3f" % round(cost / unit, 3))

    def calculate(self):
        self.cost_per_unit_value.value = ""
        for i, control in enumerate(self.product_container.controls, start=1):
            cost = int(control.content.controls[1].value)
            unit = int(control.content.controls[2].value)
            cost_per_unit = self.cal_cost_per_unit(cost, unit)
            self.product_data.setdefault(control.content.controls[0].value, [])
            self.product_data[control.content.controls[0].value].append({
                "cost": cost,
                "unit": unit,
                "costPerUnit": cost_per_unit,
            })
            self.cost_per_unit_value.value += (
                f"Product {i} = {cost_per_unit} Cost/Unit\n"
            )
        self.update()
        

    def reset(self):
        self.add_price(),
        self.cost_per_unit_value.value = ""
        self.update()
        # if not quantity.value:
        #     return
        # else:
        #     # Assuming you want to store the quantity in some dictionary
        #     my_dict = {"quantity": quantity.value}
        #     quantity.value = ""  # clear the value of quantity
        #     return my_dict

    
    def add_price(self):
        self.product_container.controls.clear()
        for i,x in enumerate(range(1, int(self.quantity) + 1), start=1):
            self.product_container.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    padding=10,
                    bgcolor="white",
                    border_radius=40,
                    width=300,
                    content=ft.Column([
                        ft.Text(f"Product {i}", size=24, weight="bold", color="#000000"),
                        ft.TextField(label="Cost", border_radius=40, width=200, height=50, color="#000000"),
                        ft.TextField(label="Unit", border_radius=40, width=200, height=50, color="#000000"),
                    ])
                )
            )
        self.update()
    
class Calculator(ft.UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.cost_per_unit_value = ft.Text("", size=20)
        self.product_container =  ft.ListView(expand=True, spacing=10, padding=20, height=490)
        self.calculator_logic = CalculatorLogic(self,0)
        self.page.on_resize = lambda e : self.update()
    
    def handle_slider_change(self, event):
        self.calculator_logic.quantity = event.control.value
        self.calculator_logic.add_price()
        self.update()
    
    def button_calculate(self, event):
        self.calculator_logic.calculate()
        self.update()

    def build(self):
        return ft.SafeArea(
    ft.Container(
        ft.Column([
            # Header
            ft.Row([
                ft.Container(
                    width=40,
                    margin=ft.margin.only(top=10,left=10),
                    content=ft.TextButton(
                        "<",
                        style=ft.ButtonStyle(color="#7D7C7C"),
                        on_click=lambda e: self.page.go('/'),  
                    )
                ),
                ft.Text("Price Comparison",
                    size=30, 
                    weight="bold",
                    color="#000000"
                ),
                ft.Container(
                    width=40,
                ),
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            
            ft.Row([
                ft.Slider(
                    width=300,
                    min=0,
                    max=10,
                    divisions=10,
                    value=0,
                    label="{value}",
                    on_change=lambda e: self.handle_slider_change(e),
                )
            ],alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Row([
                ft.ElevatedButton("Reset", 
                    bgcolor="white", 
                    color="#424949",
                    width=120,
                    on_click=lambda e: self.calculator_logic.reset(),
                ),
                ft.ElevatedButton("Calculate", 
                    bgcolor="red", 
                    color="white",
                    width=120,
                    on_click=lambda e: self.button_calculate(e), 
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column([
                            self.cost_per_unit_value,
                        ],spacing=10),
                        alignment=ft.alignment.center,
                        padding=0,
                        bgcolor="white",
                        border_radius=20,
                    )
                ],alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Row(
                controls=[self.product_container],
                alignment=ft.MainAxisAlignment.CENTER),
        ]),
        
        theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
        theme_mode=ft.ThemeMode.LIGHT,
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
        # width=800,
        border_radius=10,
        # height=self.page.height-100,
        #expand=True,
    ),
)

