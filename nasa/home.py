import requests
import streamlit as st


api_key = "6lmkxykNtwvCNScRI4c0hNfoU6yOCFR3lvUziqFX"

url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

response1 = requests.get(url)
data = response1.json()

title = data["title"]
img_url = data["url"]
explanation = data["explanation"]

response2 = requests.get(img_url)
img_path = "nasa/img.png"
with open(img_path, "wb")as file:
    file.write(response2.content)

st.header(title)
st.image(img_path)
st.write(explanation)