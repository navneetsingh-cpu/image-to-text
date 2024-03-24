import os


from transformers import (
    pipeline,
)  # allows us to download a huggingface model into our local machine


import streamlit as st


llm_model = "gpt-3.5-turbo"


# 1. Image to text implementation (aka image captioning) with huggingface
def image_to_text(url):
    pipe = pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-large",
        max_new_tokens=1000,
    )

    text = pipe(url)[0]["generated_text"]
    print(f"Image Captioning:: {text}")
    return text


with st.sidebar:

    HUGGINFACE_HUB_API_TOKEN = st.text_input(
        "Huggingface API Key", key="hugginface_serperai_api_key", type="password"
    )
    "[Get a HugginFace API key (FREE)](https://huggingface.co/settings/tokens)"
    "[View the source code](https://github.com/navneetsingh-cpu/news-letter)"
    os.environ["HUGGINFACE_HUB_API_TOKEN"] = HUGGINFACE_HUB_API_TOKEN


if not HUGGINFACE_HUB_API_TOKEN:
    st.info("Please add your Huggingface API key to continue.")

elif HUGGINFACE_HUB_API_TOKEN:
    # llm = ChatOpenAI(temperature=0.7, model=llm_model)
    st.title("Image To Text")
    st.header("Upload an image and get a description")

    upload_file = st.file_uploader("Choose an image:", type=["jpg", "png"])

    if upload_file is not None:
        with st.spinner("Processing..."):
            file_bytes = upload_file.getvalue()
            with open(upload_file.name, "wb") as file:
                file.write(file_bytes)

            st.image(
                upload_file,
                caption="The uploaded image",
                use_column_width=True,
                width=250,
            )
            ingredients = image_to_text(upload_file.name)

            with st.expander("Description"):
                st.write(ingredients)

            st.success("Done!")


# footer
st.write("---")
st.write("Made by [Navneet](https://taplink.cc/navneetskahlon)")
