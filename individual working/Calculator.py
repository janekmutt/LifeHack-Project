import flet as ft
from flet import *
import math



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
  page.bgcolor = "#ddf7f1"
  page.scroll ="auto"

  product_data = {}
  
  costPerUnitValue = ft.Text("",size=20)
 
  product_container = ft.Column(scroll = "auto")

  
  def add_price(e):
    product_container.controls.clear()
    for i,x in enumerate(range(1,int(e.control.value) + 1), start=1):
      product_container.controls.append(
        ft.Container(
          alignment=ft.alignment.center,
          padding = 10,
          bgcolor = "white",
          border_radius=40,
          width=300,
          
          content = ft.Column([
            ft.Text(f"Product {i}", size = 30, weight = "bold", color = "#000000"),
            ft.TextField(label = "Cost", border_radius=40, width=200, height=50, color = "#000000"), 
            ft.TextField(label = "Unit", border_radius=40, width=200, height=50, color = "#000000"), 
          ])
        )
      )
      page.update()

  my_dict = {}
  quantity = ft.TextField( hint_text = "Total of Compare product prices", 
                    on_change = add_price, 
                    border_radius=40, 
                    color="BLACK", 
                    bgcolor="WHITE", 
                    border_color="#FA987B", 
                    focused_border_color="#CCABD8",
                    width = 300,
                    )
  def reset(e):
    product_container.controls.clear()
    costPerUnitValue.value = ""
    if not quantity.value:
        page.update()
    else:
        my_dict["quantity"] = quantity.value
        quantity.value = ""  # clear the value of sstid
        page.update()

  def calCostPerUnit(cost, unit):
    return ("%.3f" % round(cost/unit,3))

  def calculate(e):
    # product_data.clear()
    # a = 0yz
    # # index = 0
    # # data_list = []
    # # temp = []
    # for i in product_container.controls:
    #   cost = int(i.content.controls[1].value)
    #   unit = int(i.content.controls[2].value)
    #   a = a + 1
    #   costPerUnit = calCostPerUnit(cost,unit)
    #   # data_list.append(float(costPerUnit))
    #   # index = index + 1
    #   product_data.setdefault(i.content.controls[0].value,[])
    #   product_data[i.content.controls[0].value].append({
    #     "cost": cost,
    #     "unit": unit,
    #     "costPerUnit": costPerUnit,
    #   })
    #   y.value = str(y.value) + str(f"Product {a}") + str(" ") + str("=") + str(" ") + str(costPerUnit) + str(" ") + str("Cost/Unit") + str("\n")
    
    # # temp = data_list
    # # sorted_temp = temp.sort()
    # # c = sorted_temp
    # # for j in range(len(data_list)):
    # #   b = j
    #   # cheaper.value = str(f"Product {a}") + str(PerCheap) + str("is cheaper")
    #   page.update()
    costPerUnitValue.value = str("")
    page.update()
    if costPerUnitValue.value == "":
      product_data.clear()
      a = 0
      for i in product_container.controls:
        cost = int(i.content.controls[1].value)
        unit = int(i.content.controls[2].value)
        a = a + 1
        costPerUnit = calCostPerUnit(cost,unit)
        product_data.setdefault(i.content.controls[0].value,[])
        product_data[i.content.controls[0].value].append({
          "cost": cost,
          "unit": unit,
          "costPerUnit": costPerUnit,
        })
        costPerUnitValue.value = str(costPerUnitValue.value) + str(f"Product {a}") + str(" ") + str("=") + str(" ") + str(costPerUnit) + str(" ") + str("Cost/Unit") + str("\n")
        page.update()

  Worthiness = ft.Container(
    ft.Stack([
      ft.Container(
        alignment=ft.alignment.center,
        content = ft.Column([
          ft.Row([
            ft.Text("Price Comparison", size = 30, weight = "bold",),
          ], alignment=ft.MainAxisAlignment.CENTER),
          
          ft.Row([
            quantity
          ], alignment=ft.MainAxisAlignment.CENTER),
          ft.Row([
            product_container,
          ], alignment=ft.MainAxisAlignment.CENTER),
          ft.Row([
            ft.ElevatedButton("Reset",bgcolor = "white", color="#424949",
                           on_click = reset, width=120),
            ft.ElevatedButton("Calculate",bgcolor = "red", color="white",
                           on_click = calculate, width=120),
                           ], alignment=ft.MainAxisAlignment.CENTER),
          costPerUnitValue,
        ])
      )
    ]),
    width = 350
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
                 height=2000,
                 expand=True, 
                 content = Worthiness            
     ))
    
  page.navigation_bar = ft.NavigationBar(bgcolor = "#fe96a5",
    destinations=[
      ft.NavigationDestination(icon=ft.icons.CHECK, ),
      ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, ),
      ft.NavigationDestination(icon=ft.icons.HOME, ),
      ft.NavigationDestination(icon=ft.icons.CALCULATE,),
      ft.NavigationDestination(icon=ft.icons.PERSON, ),
    ]
  )

  page.padding = 0
  
  page.add(ft.SafeArea(c2))
  

#starting the app
ft.app(target = main)