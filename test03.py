#3.จงเขียนโปรแกรมPython ของโปรแกรมคำนวณภาษี ณ ที จ่ายของสินค้า โดยรับชื้อสินค้า และราคาสินค้า 
#ทางแป้นพิมพ์และแสดงผลภาษีที่ คำนวณได้ทางหน้าจอ ทั้งนี้ภาษีคิดที ร้อยละ 7 ของราคาสินค้า

def inputdata():
    product_name = input("กรอกชื่อรายการสินค้า : ")
    product_price = int(input("กรอกราคาสินค้า : "))
    return product_name , product_price
def cal( product_price ):
    vat = product_price * 0.07
    chackout = product_price + vat
    return vat , chackout
def calandshowproduct( product_name , product_price , vat , chackout):
    print (f"ชื่อรายการสินค้า : {product_name}")
    print (f"ราคาสินค้า : {product_price:.2f} | Vat7% : {vat:.2f} | ราคาที่ต้องชำระ {chackout:.2f}")
print ("***-------------------------------------***")
product_name , product_price = inputdata()
print ("***-------------------------------------***")
vat , chackout = cal( product_price )
calandshowproduct( product_name , product_price , vat , chackout)
print ("***-------------------------------------***")