import streamlit as st
from PIL import Image

# Streamlit app layout
st.title("Image RGB to Black & White Converter")

# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert the image to black and white
    bw_image = image.convert("L")
    
    # Display the black and white image
    st.image(bw_image, caption="Black & White Image", use_column_width=True)

    # Optionally, provide a download link for the black and white image
    with st.expander("Download Black & White Image"):
        # Save the black and white image to a BytesIO object
        from io import BytesIO
        buffer = BytesIO()
        bw_image.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Create a download link
        st.download_button(
            label="Download Black & White Image",
            data=buffer,
            file_name="bw_image.png",
            mime="image/png"
        )
