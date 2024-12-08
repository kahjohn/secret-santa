import streamlit as st
import pandas as pd

def get_name(code):
    output = pd.read_csv('/workspaces/secret-santa/santa.csv')
    # print(output)
    recepient = output[ output['Code'] == code ]['Recipient'].to_numpy()[0]
    # print(recepient)
    return 'Congratz, you are going to buy a Christmas gift for ' + recepient

# st.title("My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

st.image('/workspaces/secret-santa/santa.png')
st.title("Secret Santa")
st.subheader("Find out who you need to buy the gift for.")

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
