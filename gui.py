import streamlit as st
from argparse import Namespace
from PIL import Image
from rmp.main import main
import tempfile
import os

st.title("random_perturbation_in_latent_space")
st.markdown("encode, add random perturbation and decode a given image.")
st.markdown(
            """
            <style>
            img {
                border-radius: 0px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    

img_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg","webp"])
if img_file is not None:
    image = Image.open(img_file)
    st.image(image, caption="Input Image", use_container_width=True)
matrix_type = st.selectbox(
    "Type of random matrix",
    ["gaussian", "uniform", "orthogonal", "symmetric", "permutation", "sparse", "diagonal", "wishart"]
)
n = st.number_input("Number of trials", min_value=1, value=1, step=1)

lb = st.number_input("Lower bound (for uniform)", value=0.0)
ub = st.number_input("Upper bound (for uniform)", value=1.0)

density = st.number_input("Density (for sparse)", value=1.0)

p = st.number_input("Degrees of freedom (for Wishart)", min_value=1, step=1, format="%d")

seed = st.number_input("Random seed", value=None, step=1, format="%d")

mode = st.selectbox("mode",
    ["default","experimental"]
)

if st.button("Apply transformation") and img_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image = Image.open(img_file)
        image.save(tmp.name)
        img_path = tmp.name

    args = Namespace(
        img_path=img_path,
        matrix_type=matrix_type,
        n=n,
        lb=lb,
        ub=ub,
        density=density,
        p=p,
        seed=seed if seed != 0 else None,
        mode=mode
    )
    main(args)

    os.remove(tmp.name)

    st.success("finished.")

if st.button("Display Results"):
    output_dir = "output"
    image_files = [
        f for f in os.listdir(output_dir)
        if f.lower().endswith((".png"))
    ]
    image_files.sort()

    if not image_files:
        st.warning("No images found in the output folder.")
    else:
        st.subheader("Generated Images")
        cols = st.columns(3)
        for idx, filename in enumerate(image_files):
            img_path = os.path.join(output_dir, filename)
            with cols[idx % 3]:
                st.image(Image.open(img_path), caption=filename, use_container_width=True)




