import streamlit as st
from openai import OpenAI
import base64

st.set_page_config(
    page_title="AI Vision Chatbot",
    page_icon="👁️",
    layout="centered"
)

st.title("👁️ AI Vision Chatbot")
st.caption("Upload an image and ask questions using AI-powered vision.")
st.divider()

api_key = st.secrets["OPENAI_API_KEY"]

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "webp"]
)

question = st.text_input(
    "Ask something about the image:",
    placeholder="Example: What is shown in this image?"
)

st.caption(
    "💡 Try: What is shown here? | Describe the image | "
    "What objects can you identify?"
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

if st.button("🔍 Analyze Image"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not uploaded_file:
        st.error("Please upload an image.")
    elif not question:
        st.error("Please ask a question.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            image_data = base64.b64encode(
                uploaded_file.getvalue()
            ).decode("utf-8")

            response = client.responses.create(
                model="gpt-5.6",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": question
                            },
                            {
                                "type": "input_image",
                                "image_url": f"data:{uploaded_file.type};base64,{image_data}"
                            }
                        ]
                    }
                ]
            )

            st.subheader("🤖 AI Response")
            st.write(response.output_text)

        except Exception:
            st.warning("⚠️ AI analysis is currently unavailable.")

            st.info(
                "🎯 Demo Mode: The image was uploaded successfully. "
                "In the full version, the AI Vision model analyzes the "
                "image and answers the user's question."
            )