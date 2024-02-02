import streamlit as st
from clarifai.client.model import Model
from relevancy_check import check_question
# Set up environment variable
import os
os.environ["CLARIFAI_PAT"] = "9ef0e3a7f2ec44899b5175de6321afcc"

# Define constants
MODEL_URL = "https://clarifai.com/microsoft/text-generation/models/phi-2"

# Streamlit app starts here
st.title("Well Being and Mental Health Assistant")

# Initialize messages with a system message
messages = [{"role": "system", "content": "Well Being and Mental Health Assistant"}]

# Text input for user to provide prompt
user_input = st.text_input("Type your message here:", "")

    # Function to make prediction
def predict(prompt):
    model = Model(MODEL_URL)
    prediction = model.predict_by_bytes(prompt.encode(), input_type="text")
    return prediction.outputs[0].data.text.raw

# Button to trigger prediction
if st.button("Send"):
        # Validate if user has entered any prompt
        if user_input:
            if check_question(user_input):
                user_input = "Provide Relevant mental health information or motivational content shortly my query is " + user_input
                # Append user's message to the messages list
                messages.append({"role": "user", "content": user_input})

                # Generate response using Clarifai model
                assistant_response = predict(user_input)

                # Append assistant's response to the messages list
                messages.append({"role": "assistant", "content": assistant_response})

                # Display assistant's response
                st.text_area("Assistant:", value=assistant_response, height=300, disabled=True)
            else:
                st.warning("I only provide you the awareness about medical and health care.")
        else:
            st.write("Please enter a message.")
