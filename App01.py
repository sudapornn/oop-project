import streamlit as st
from PIL import Image

def main():
    st.header("Perfect Shop")

    logo = Image.open("imaeg9.jpg")
    logo_resized = logo.resize((700, 500))
    st.image(logo_resized, use_column_width=False)

    st.markdown("""
        **SUSTAINABLE**  
        Now taking online orders. Order today and get 15% off your first order. Hurry while supplies last!
    """)

    st.markdown(" ")
    logo = Image.open("imaeg95.jpg")
    logo_resized = logo.resize((700, 500))
    st.image(logo_resized, use_column_width=False)
    st.markdown(" ")
    video_file_path = "C:\\Users\\LENOVO\\OneDrive\\Pictures\\video.mp4"
    st.video(video_file_path)

    html_content = """
        <div style='text-align: center;'>
            <h5>Product Sample Video</h5>
    """
    st.write(html_content, unsafe_allow_html=True)

    st.markdown(" ")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8= st.tabs(["Product type", "All Products", "Productpage 1", "Productpage 2", "Productpage 3", "Productpage 4", "Productpage 5", "Productpage 6"])

    st.markdown(" ")
    with tab1:
        st.subheader("Minimalist Products")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg04.jpg")
        col1.image(original1, caption="ห้องครัว Page 1", use_column_width=True)

        original2 = Image.open("imaeg06.jpg")
        col2.image(original2, caption="ห้องน้ำ Page 2", use_column_width=True)

        original3 = Image.open("imaeg03.jpg")
        col3.image(original3, caption="ห้องนอน Page 3", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("imaeg01.jpg")
        col4.image(original4, caption="ห้องนั่งเล่น Page 4", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("imaeg02.jpg")
        col5.image(original5, caption="สวนหน้าบ้าน Page 5", use_column_width=True)

        col6.markdown(" ")

        original6 = Image.open("imaeg07.jpg")
        col6.image(original6, caption="ห้องระเบียง Page 6", use_column_width=True)
        
    with tab2:
        st.subheader("All Products")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg24.jpg")
        col1.image(original1, caption="Products", use_column_width=True)

        original2 = Image.open("imaeg2.jpg")
        col2.image(original2, caption="Products", use_column_width=True)

        original3 = Image.open("imaeg3.jpg")
        col3.image(original3, caption="Products", use_column_width=True)

        col4, col5, col6 = st.columns(3)

        col4.markdown(" ")
        
        original4 = Image.open("imaeg4.jpg")
        col4.image(original4, caption="Products", use_column_width=True)

        col5.markdown(" ")

        original5 = Image.open("imaeg5.jpg")
        col5.image(original5, caption="Products", use_column_width=True)

        col6.markdown(" ")

        original5 = Image.open("imaeg6.jpg")
        col6.image(original5, caption="Products", use_column_width=True)

        col7, col8, col9 = st.columns(3)

        col7.markdown(" ")
        
        original7 = Image.open("imaeg10.jpg")
        col7.image(original7, caption="Products", use_column_width=True)

        col8.markdown(" ")

        original8 = Image.open("imaeg11.jpg")
        col8.image(original8, caption="Products", use_column_width=True)

        col9.markdown(" ")

        original9 = Image.open("imaeg12.jpg")
        col9.image(original9, caption="Products", use_column_width=True)

        col10, col11, col12 = st.columns(3)

        col10.markdown(" ")
        
        original10 = Image.open("imaeg13.jpg")
        col10.image(original10, caption="Products", use_column_width=True)

        col11.markdown(" ")

        original11 = Image.open("imaeg20.jpg")
        col11.image(original11, caption="Products", use_column_width=True)

        col12.markdown(" ")

        original12 = Image.open("imaeg1.jpg")
        col12.image(original12, caption="Products", use_column_width=True)

        col12, col13, col14 = st.columns(3)

        col12.markdown(" ")
        
        original12 = Image.open("imaeg30.jpg")
        col12.image(original12, caption="Products", use_column_width=True)

        col13.markdown(" ")

        original13 = Image.open("imaeg31.jpg")
        col13.image(original13, caption="Products", use_column_width=True)

        col14.markdown(" ")

        original14 = Image.open("imaeg32.jpg")
        col14.image(original14, caption="Products", use_column_width=True)

        col15, col16, col17 = st.columns(3)

        col15.markdown(" ")
        
        original15 = Image.open("imaeg34.jpg")
        col15.image(original15, caption="Products", use_column_width=True)

        col16.markdown(" ")

        original16 = Image.open("imaeg35.jpg")
        col16.image(original16, caption="Products", use_column_width=True)

        col17.markdown(" ")

        original17 = Image.open("imaeg36.jpg")
        col17.image(original17, caption="Products", use_column_width=True)

    with tab3:
        st.subheader("Kitchen products")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg14.jpg")
        caption1 = "Products 1 $25"  
        col1.image(original1, caption=caption1, use_column_width=True)

        if col1.button("Order Now", key="button1"):  
            col1.markdown("การสั่งซื้อ Products 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 25 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  


        original2 = Image.open("imaeg15.jpg")
        col2.image(original2, caption="Products 2 $30", use_column_width=True)

        if col2.button("Order Now", key="button2"):  
            col2.markdown("การสั่งซื้อ Products 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 30 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        original3 = Image.open("imaeg04.jpg")
        col3.image(original3, caption="Products 3 $40", use_column_width=True)

        if col3.button("Order Now", key="button3"):  
            col3.markdown("การสั่งซื้อ Products 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 40 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg14.jpg")
        caption1 = "Products 4 $25"  
        col1.image(original1, caption=caption1, use_column_width=True)

        if col1.button("Order Now", key="button4"):  
            col1.markdown("การสั่งซื้อ Products 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 25 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  


        original2 = Image.open("imaeg15.jpg")
        col2.image(original2, caption="Products 5 $30", use_column_width=True)

        if col2.button("Order Now", key="button5"):  
            col2.markdown("การสั่งซื้อ Products 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 30 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        original3 = Image.open("imaeg04.jpg")
        col3.image(original3, caption="Products 6 $40", use_column_width=True)

        if col3.button("Order Now", key="button6"):  
            col3.markdown("การสั่งซื้อ Products 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 40 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")

    with tab4:
        st.subheader("Bathroom products")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg10.jpg")
        col1.image(original1, caption="Products 1 $60", use_column_width=True)

        if col1.button("Order Now", key="button7"):  
            col1.markdown("การสั่งซื้อ Product 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 60 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg11.jpg")
        col2.image(original2, caption="Product 2 $70", use_column_width=True)

        if col2.button("Order Now", key="button8"):  
            col2.markdown("การสั่งซื้อ Product 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 70 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original3 = Image.open("imaeg12.jpg")
        col3.image(original3, caption="Product 3 $80", use_column_width=True)

        if col3.button("Order Now", key="button9"):  
            col3.markdown("การสั่งซื้อ Product 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 80 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg10.jpg")
        col1.image(original1, caption="Products 4 $60", use_column_width=True)

        if col1.button("Order Now", key="button10"):  
            col1.markdown("การสั่งซื้อ Product 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 60 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg11.jpg")
        col2.image(original2, caption="Product 5 $70", use_column_width=True)

        if col2.button("Order Now", key="button11"):  
            col2.markdown("การสั่งซื้อ Product 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 70 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original3 = Image.open("imaeg12.jpg")
        col3.image(original3, caption="Product 6 $80", use_column_width=True)

        if col3.button("Order Now", key="button12"):  
            col3.markdown("การสั่งซื้อ Product 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 80 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")

    with tab5:
        st.subheader("Bedroom products")
        st.markdown(" ")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg4.jpg")
        caption1 = "Products 1 $25"  
        col1.image(original1, caption=caption1, use_column_width=True)

        if col1.button("Order Now", key="button13"):  
            col1.markdown("การสั่งซื้อ Products 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 25 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  


        original2 = Image.open("imaeg2.jpg")
        col2.image(original2, caption="Products 1 $30", use_column_width=True)

        if col2.button("Order Now", key="button14"):  
            col2.markdown("การสั่งซื้อ Products 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 30 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        original3 = Image.open("imaeg3.jpg")
        col3.image(original3, caption="Products 1 $40", use_column_width=True)

        if col3.button("Order Now", key="button15"):  
            col3.markdown("การสั่งซื้อ Products 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 40 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg4.jpg")
        caption1 = "Products 4 $25"  
        col1.image(original1, caption=caption1, use_column_width=True)

        if col1.button("Order Now", key="button16"):  
            col1.markdown("การสั่งซื้อ Products 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 25 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg2.jpg")
        col2.image(original2, caption="Products 5 $30", use_column_width=True)

        if col2.button("Order Now", key="button17"):  
            col2.markdown("การสั่งซื้อ Products 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 30 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        original3 = Image.open("imaeg3.jpg")
        col3.image(original3, caption="Products 6 $40", use_column_width=True)

        if col3.button("Order Now", key="button18"):  
            col3.markdown("การสั่งซื้อ Products 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 40 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")

    with tab6:
        st.subheader("Living room products")
        st.markdown("")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg24.jpg")
        col1.image(original1, caption="Product 1 $90", use_column_width=True)

        if col1.button("Order Now", key="button19"):  
            col1.markdown("การสั่งซื้อ Product 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 90 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg36.jpg")
        col2.image(original2, caption="Product 2 $100", use_column_width=True)

        if col2.button("Order Now", key="button20"):  
            col2.markdown("การสั่งซื้อ Product 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 100 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original3 = Image.open("imaeg20.jpg")
        col3.image(original3, caption="Product 3 $1100", use_column_width=True)

        if col3.button("Order Now", key="button21"):  
            col3.markdown("การสั่งซื้อ Product 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 1100 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg24.jpg")
        caption1 = "Products 4 $90"  
        col1.image(original1, caption=caption1, use_column_width=True)

        if col1.button("Order Now", key="button22"):  
            col1.markdown("การสั่งซื้อ Products 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 90 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  


        original2 = Image.open("imaeg36.jpg")
        col2.image(original2, caption="Products 5 $100", use_column_width=True)

        if col2.button("Order Now", key="button23"):  
            col2.markdown("การสั่งซื้อ Products 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1) 
            total_price = 1100 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        original3 = Image.open("imaeg20.jpg")
        col3.image(original3, caption="Products 6 $40", use_column_width=True)

        if col3.button("Order Now", key="button24"):  
            col3.markdown("การสั่งซื้อ Products 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 40 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")

    with tab7:
        st.subheader("Front yard products")
        st.markdown("")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg13.jpg")
        col1.image(original1, caption="Product 1 $250", use_column_width=True)

        if col1.button("Order Now", key="button25"):  
            col1.markdown("การสั่งซื้อ Product 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 250 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg4.jpg")
        col2.image(original2, caption="Product 2 $300", use_column_width=True)

        if col2.button("Order Now", key="button26"):  
            col2.markdown("การสั่งซื้อ Product 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 300 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original3 = Image.open("imaeg5.jpg")
        col3.image(original3, caption="Product 3 $500", use_column_width=True)

        if col3.button("Order Now", key="button27"):  
            col3.markdown("การสั่งซื้อ Product 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 500 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท") 

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg13.jpg")
        col1.image(original1, caption="Product 4 $250", use_column_width=True)

        if col1.button("Order Now", key="button28"):  
            col1.markdown("การสั่งซื้อ Product 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 250 * quantity  
            col1.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original2 = Image.open("imaeg4.jpg")
        col2.image(original2, caption="Product 5 $300", use_column_width=True)

        if col2.button("Order Now", key="button29"):  
            col2.markdown("การสั่งซื้อ Product 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 300 * quantity  
            col2.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")  

        original3 = Image.open("imaeg5.jpg")
        col3.image(original3, caption="Product 6 $500", use_column_width=True)

        if col3.button("Order Now", key="button30"):  
            col3.markdown("การสั่งซื้อ Product 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 500 * quantity  
            col3.markdown(f"ราคารวมทั้งหมด: {total_price} บาท")

    with tab8:
        st.subheader("Balcony room products")
        st.markdown("")
        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg32.jpg")
        col1.image(original1, caption="Product 1 $190", use_column_width=True)

        if col1.button("Order Now", key="button31"):  
            col1.markdown("การสั่งซื้อ Product 1")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 190 * quantity  
            col1.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท")  

        original2 = Image.open("imaeg35.jpg")
        col2.image(original2, caption="Product 2 $170", use_column_width=True)

        if col2.button("Order Now", key="button32"):  
            col2.markdown("การสั่งซื้อ Product 2")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 170 * quantity  
            col2.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท")  

        original3 = Image.open("imaeg34.jpg")
        col3.image(original3, caption="Product 3 $110", use_column_width=True)

        if col3.button("Order Now", key="button33"):  
            col3.markdown("การสั่งซื้อ Product 3")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 110 * quantity  
            col3.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท") 

        col1, col2, col3 = st.columns(3)

        original1 = Image.open("imaeg32.jpg")
        col1.image(original1, caption="Product 4 $190", use_column_width=True)

        if col1.button("Order Now", key="button34"):  
            col1.markdown("การสั่งซื้อ Product 4")  
            quantity = col1.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 190 * quantity  
            col1.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท")  

        original2 = Image.open("imaeg35.jpg")
        col2.image(original2, caption="Product 5 $170", use_column_width=True)

        if col2.button("Order Now", key="button35"):  
            col2.markdown("การสั่งซื้อ Product 5")  
            quantity = col2.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 170 * quantity  
            col2.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท")  

        original3 = Image.open("imaeg34.jpg")
        col3.image(original3, caption="Product 6 $110", use_column_width=True)

        if col3.button("Order Now", key="button36"):  
            col3.markdown("การสั่งซื้อ Product 6")  
            quantity = col3.number_input("จำนวน:", min_value=1, value=1)  
            total_price = 110 * quantity  
            col3.markdown(f"**ราคารวมทั้งหมด:** {total_price} บาท")

    st.markdown('')
    st.markdown('')

    logo = Image.open("imaeg92.jpg")
    logo_resized = logo.resize((700, 500))
    st.image(logo_resized, use_column_width=False)

    menu = ["Home", "Sign In", "Create Account", "Order", "My Account", "Signup"]
    choice1 = st.sidebar.selectbox('Menu', menu)
    st.markdown("") 
    st.markdown("")
    html_content = """
        <div style='text-align: center;'>
            <h3>Questions or Concerns?</h3>
            <p>Need help selecting a product or finding a sustainable option? Send us a message!</p>
            <p><strong>Perfect Shop</strong></p>
            <p><a href="mailto:sudaphor.sa.66@ubu.ac.th">sudaphor.sa.66@ubu.ac.th</a></p>
        </div>
    """
    
    st.write(html_content, unsafe_allow_html=True)


    if choice1 == "Home":
        st.write("Welcome to the Home Page!")

    elif choice1 == "Sign In":
        st.subheader("Account sign in")

        username = st.text_input("Email")
        password = st.text_input("Password", type='password')
        
        if st.button('Sign In'):
            st.success('Sign In as {}'.format(username))

            task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
            if task == "Add Post":
                st.subheader("Add your post")
                st.write("You can add your post here.")

            elif task == "Analytics":
                st.subheader("Analytics")
                st.write("Here you can view the analytics.")

            elif task == "Profiles":
                st.subheader("User Profiles")
                st.write("View and manage user profiles here.")

    elif choice1 == "Create Account":
        st.subheader("Create Account")
        st.write("Create a new account here.")
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        email = st.text_input("Email")
        phone = st.text_input("Phone(optional)")
        new_password = st.text_input("Password", type='password')

        if st.button("Create Account"):
            st.success("You have successfully created a valid account.")
            st.info("Proceed to login to access your account.")

    elif choice1 == "Order":
        st.write("Welcome to the Order Page!")
        selected_product = st.selectbox("Select a product", ["Product A", "Product B", "Product C"])
        quantity = st.number_input("Quantity", min_value=1, value=1)
        st.write(f"You've selected {quantity} of {selected_product}.")
        if st.button("Confirm Order"):
            st.success("Your order has been placed successfully!")

    elif choice1 == "My Account":
        st.subheader("User Information")
        st.write("No user information available. Please create an account first.")

    elif choice1 == "Signup":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            st.success("You have successfully created an valid Account")
            st.info("Go to login to login")

if __name__ == "__main__":
    main()


