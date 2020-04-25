a = 3.55
b = 4.8
c = "name"
print(a)
print(b)
x = y = z = 10
print(x, y, z)
j, k = 15, 99
print(j, k)
# booleean
status = True
msg = False
print(status, msg)
#val + chart
# is 1 concat string
print("ราคาขายต่อ", b, " บาท")
# is 2 string interpolation
print("ราคาขายต่อ %s บาท" % b)
print("ราคาขายต่อ %.2f บาท" % b)
print("ราคาขายต่อ %.2f บาท มีจำนวน %d ชิ้น" % (b, a))
# is 3 format string
print(f"ราคาขายต่อ {b} บาท มีจำนวน {a} ชิ้น")
