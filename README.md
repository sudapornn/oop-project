# OOP-Project
[คลิปวิดีโอของฉัน]([video.mp4](https://www.youtube.com/watch?v=HE3mJHAFqkU&list=RDHE3mJHAFqkU&start_))

# application title
  * Perfect Shop
## author: 
  * id: 66114540791
  * name: Sudaporn Sanguandee
## technology: [pygame/streamlit]
## application description:
    เป็นแอปพลิเคชันเว็บที่ใช้ Streamlit เพื่อสร้างหน้าเว็บ "Perfect Shop" ซึ่งมีฟีเจอร์ต่างๆ ดังนี้
    1. หน้าแรกแสดงโลโก้ของร้าน ("Perfect Shop") และโปรโมชั่น "SUSTAINABLE" พร้อมกับข้อความเชิญสั่งซื้อออนไลน์พร้อมโปรโมชั่น 15% สำหรับการสั่งซื้อครั้งแรก
    2. แสดงวิดีโอสำหรับตัวอย่างสินค้า
    3. แสดงแท็บที่ให้เลือกสินค้าแบบต่างๆ เช่น "Product type", "All Products", "Kitchen products" เป็นต้น
    4. ในแต่ละแท็บจะมีรายการสินค้าต่างๆ แสดงภาพและรายละเอียดสินค้า เช่น รูปภาพ, ราคา, ปุ่มสั่งซื้อ, การเลือกจำนวนสินค้า และราคารวม
    5. มีเมนูด้านข้างที่ให้เลือกการนำทางไปยังหน้าต่างๆ เช่น "Home", "Sign In", "Create Account", "Order", "My Account"
    6. หน้า "Sign In" มีฟอร์มให้กรอกอีเมลและรหัสผ่านเพื่อเข้าสู่ระบบ และมีเลือกฟังก์ชันต่างๆ เช่น "Add Post", "Analytics", "Profiles"
    7. หน้า "Create Account" มีฟอร์มให้กรอกข้อมูลสำหรับสร้างบัญชีใหม่ เช่น ชื่อ, อีเมล, รหัสผ่าน เป็นต้น
    8. หน้า "Order" มีฟอร์มให้เลือกสินค้าและปริมาณที่ต้องการสั่งซื้อ และสามารถยืนยันการสั่งซื้อได้
    9. หน้า "My Account" แสดงข้อมูลผู้ใช้ (ยังไม่มีข้อมูลผู้ใช้เนื่องจากต้องเข้าสู่ระบบก่อน)
    โดยรายละเอียดของแต่ละสินค้ารวมถึงราคาและภาพถูกนำเสนอไว้ในหน้าเว็บด้วยภาษา Python และไลบรารี Streamlit ส่วนฟอร์มสำหรับการสั่งซื้อ
    และการเข้าสู่ระบบถูกจัดการด้วย Python ด้วยการใช้งาน Streamlit
    concept OOP ที่ใช้ในโครงงาน
    1. การใช้งานคลาส
    -ใช้คลาส Image จากโมดูล PIL (Python Imaging Library) เพื่อโหลดภาพและปรับขนาดของภาพ
    -ใช้คลาส st จากโมดูล Streamlit เพื่อสร้างอินสแตนซ์ของอ็อบเจ็กต์ Streamlit เพื่อสร้างเว็บแอปพลิเคชัน
    2. การใช้งานเมทอด
    -st.header(), st.subheader(), st.markdown(), st.image(), st.video(), st.sidebar.selectbox(), st.sidebar.text_input(), st.sidebar.button(), st.sidebar.success(), 
     st.sidebar.info(), st.sidebar.write(): เป็นเมอด     ของอ็อบเจ็กต์ Streamlit ที่ใช้สร้างส่วนต่าง ๆ ของเว็บแอปพลิเคชัน เช่น ส่วนของหัวเรื่อง, ภาพ, วิดีโอ, ปุ่ม, การแสดงข้อความ เป็นต้น
    -Image.open(), resize(): เป็นเมทอดของอ็อบเจ็กต์ภาพที่โหลดจากโมดูล PIL เพื่อเปิดและปรับขนาดของภาพ
    -button(), number_input(): เป็นเมทอดของอ็อบเจ็กต์ Streamlit ที่ใช้สร้างปุ่มและช่องใส่ข้อมูลเพื่อรับค่าจากผู้ใช้
    3. การใช้ฟังชั่งหลักที่ชื่อว่า def main(): สร้างฟังก์ชันหลัก main() ซึ่งจะเป็นที่เริ่มต้นของโปรแกรม และใช้ if __name__ == "__main__": เช็คว่าโปรแกรมถูกเรียกใช้โดยตรงหรือไม่ หากถูกเรียกใช้โดยตรง main() จะถูกเรียกใช้เพื่อเริ่มการทำงานของโปรแกรมนี้ได้
## presentation:
   link [[slide/canva/etc..](https://www.canva.com/design/DAFi-3U5Cog/QR6uZRP4p0JVILM6DPra6Q/edit?utm_content=DAFi-3U5Cog&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)https://www.canva.com/design/DAFi-3U5Cog/QR6uZRP4p0JVILM6DPra6Q/edit?utm_content=DAFi-3U5Cog&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton] 
## video:
   link [[public/ubu](https://drive.google.com/file/d/1tWNlLmFpTKr74DZ3m2lkeO5OjsaMStUP/view?usp=sharing)https://drive.google.com/file/d/1tWNlLmFpTKr74DZ3m2lkeO5OjsaMStUP/view?usp=sharing]
