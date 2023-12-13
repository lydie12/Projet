import streamlit as st

def config():
    
        original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"></h1>'
        st.markdown(original_title, unsafe_allow_html=True)


        # Set the background image
        background_image = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://www.claseejecutiva.uc.cl/wp-content/uploads/2021/05/precios-dinamicos-w-min-1024x529.jpg");
            background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
            background-position: center;  
            background-repeat: no-repeat;
        }
        </style>
        """

        st.markdown(background_image, unsafe_allow_html=True)
# Dans le module util.config

    
    