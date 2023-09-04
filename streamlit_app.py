import streamlit as st
import requests
import json



# Load the DALL-E model
st.title('🐂 Oxen.ai Image Generator')

# Get the text input
prompt = st.text_input('Enter your text prompt here:')

# Create a button to start the generation
if st.button('Generate Image'):
    with st.spinner('Generating image...'):
        # Generate an image using an HTTP request
        response = requests.post(
            "http://192.9.151.81:8000/imagine",
            headers={'Content-Type': 'application/json'},
            json={"prompt": prompt}
        )
        print(response.text)
        response_data = json.loads(response.text)
        image_url = response_data['images'][0]['content_url']
        view_url = response_data['images'][0]['view_url']
        
        # Add some markdown and display the image
        st.markdown(f"View on Oxen.ai: [{view_url}]({view_url})")
        st.markdown(f"![{prompt}]({image_url}?width=512&height=512)")

