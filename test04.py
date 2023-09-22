#4.จงเขียนโปรแกรมPython ของโปรแกรมแก้สมการ y = 2x2+ 2x + 1 เมื อ x คือค่าที รับทางแป้นพิมพ์ และแสดงผลจากการแก้สมการ y ที ได้ทางหน้าจอ

def input_data ():
    x = float(input("Input X : "))
    return x
def cal(x):
    y = (( 2 * ( x ** 2 )) + ( 2 * x ) + 1 )
    return y
def showcalX ( x, y ) :
    print(f'y = ( 2  * ( {x:.0f} ** 2 )) + ( 2 * {x:.0f} ) + 1')
    print (f"แก้สมการได้ : {y:.0f}")

print ("***------------------***")
x = input_data()
print ("***------------------***")
y = cal(x)
showcalX ( x, y )
print ("***------------------***")