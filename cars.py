salesData = [
    ["Alpha Romeo", 321],
    ["BMW", 543],
    ["Chevrolet", 789],
    ["Ford", 456],
    ["Honda", 987],
    ["Hyundai", 654],
    ["Jaguar", 234],
    ["Jeep", 876],
    ["Kia", 543],
    ["Lexus", 987],
    ["Mazda", 345],
    ["Mercedes-Benz", 678],
    ["Nissan", 876],
    ["Toyota", 567],
    ["Volkswagen", 234],
    ["Volvo", 765],
    ["Audi", 456],
    ["Buick", 987],
    ["Cadillac", 876],
    ["Chrysler", 543],
    ["Dodge", 987],
    ["Fiat", 234],
    ["GMC", 876],
    ["Infiniti", 543],
    ["Land Rover", 987],
    ["Lincoln", 234],
    ["Maserati", 876],
    ["Mitsubishi", 543],
    ["Porsche", 987],
    ["Ram", 234],
    ["Subaru", 876],
    ["Tesla", 543],
    ["Acura", 987],
    ["Alfa Romeo", 234],
    ["Bentley", 876],
    ["Genesis", 543],
    ["Hennessey", 987],
    ["Isuzu", 234],
    ["Koenigsegg", 876],
    ["Lamborghini", 543],
    ["Lotus", 987],
    ["McLaren", 234],
    ["Mini", 876],
    ["Pagani", 543],
    ["Rolls-Royce", 987],
    ["Suzuki", 234],
    ["Tata", 876],
    ["Zenvo", 543]
]

average_sales = 0
num_sales = 0

for row in range(0,len(salesData)):
    for column in range(0,len(salesData[row])):
        if column == 0:
            print("Brand: ",salesData[row][column])
        else:
            print("Sales:",salesData[row][column])
            average_sales += salesData[row][column]
            num_sales += 1

average_sales = average_sales/num_sales
print(average_sales)

search_brand = input("Brand: ")
highest_brand_sales = ["Brand",0]
for brand in salesData:
    if brand[0] == search_brand:
        print(brand[1])

for i in range(len(salesData)):
    if salesData[i][1] > highest_brand_sales[1]:
        highest_brand_sales[0],highest_brand_sales[1] = salesData[i][0],salesData[i][1]
print(highest_brand_sales)