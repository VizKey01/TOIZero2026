# รับข้อมูลเข้า (A-Z ความยาว 5 ตัวอักษร)
data = input("ป้อนข้อมูล (A-Z ความยาว 5 ตัวอักษร): ").strip().upper()

# ตรวจสอบว่าป้อนครบ 5 ตัวตามเงื่อนไขหรือไม่
if len(data) != 5:
    print("กรุณาป้อนข้อมูลให้ครบ 5 ตัวอักษร")
else:
    encoded = ""
    count = 1
    
    # วนลูปเพื่อตรวจสอบอักขระที่อยู่ติดกัน
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            encoded += str(count) + data[i-1]
            count = 1
            
    # เพิ่มตัวอักษรชุดสุดท้ายที่มีการนับไว้
    encoded += str(count) + data[-1]
    
    # แสดงผลลัพธ์
    print(f"ข้อความ THEOS: {encoded}")
