print("----------------------------")
print("# kimhun55")
print("# type exit -> end")
print("----------------------------")

sumdata = 0
count = 1

while True:
    data = input(f"enter number {count}:")
    # end exit
    if data == "0":
        break
    count = count+1
    sumdata += int(data)


print(f"sum value is : {sumdata}")
