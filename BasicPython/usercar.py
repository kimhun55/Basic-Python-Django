from Car import*


# สร้าง object หรือ instance by Class car
objcar1 = Car('red', 'honda', 4, 7, 195)

objcar1.printdata()

objcar2 = Car('', '', '', '', '')
objcar2.setbrand("honda")
objcar2.setcolor("md")
objcar2.setspeed("220")

objcar2.printdata()
