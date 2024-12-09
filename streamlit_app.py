import streamlit as st
import pandas as pd

def get_name(code):
    file_url = 'https://raw.githubusercontent.com/kahjohn/secret-santa/refs/heads/main/santa.csv'
    output = pd.read_csv(file_url)

    recepient = output[ output['Code'] == code ]['Recipient'].to_numpy()[0]
 
    text1 = 'Congratz, you are going to buy a Christmas gift for ' + recepient
    text2 = '恭喜，您将会送一份圣诞礼物给 ' + recepient

    text_ = text1 + '\n' + text2
    st.text(text_)

    # print(recepient)
    # return 'Congratz, you are going to buy a Christmas gift for ' + recepient
    return '🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄🎅🎄'

image_url = 'https://raw.githubusercontent.com/kahjohn/secret-santa/refs/heads/main/santa.png'

st.image(image_url)
st.title("Secret Santa")
st.subheader("Let's find out who you need to buy a gift for :)")

# Get the user's input
user_input = st.text_input("Key in your special code: ")
submit_button = st.button("Submit")

# Convert the input to a float (if valid)
try:
    user_input = float(user_input)

    # Generate a response
    if user_input or submit_button:
        response = get_name(user_input)
        st.write(response)

except ValueError:
    st.write("Please enter a valid number.")
