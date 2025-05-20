# random_perturbation_in_latent_space

<img src ="ex/ex1.jpg" width="700">

<img src ="ex/ex2.jpg" width="700">

this is an experimental and fun approach to image processing. the idea is to encode given image into latent space, apply perturbation using random generated matricies, and then decode them back. 
you can see nonlinear and random transformation of the original image.

## Usage

clone this repo and install the requirements:

```bash
git clone https://github.com/wowowo-wo/random_perturbation_in_latent_space
cd random_perturbation_in_latent_space
pip install -r requirements.txt
python3 cli.py --img_path PATH [--matrix_type type of matrix] [--steps N] [--lb lower bound for uniform float] [--ub upper bound for uniform float] [--density density for sparse float] [--p degrees of freedom for wishart N] [--seed random seed N]
```

or you can run this tool with a GUI using Streamlit:

```bash
pip install streamlit
streamlit run gui.py
```

then, open the URL shown in your brouser.

### Parameters

--img_path Path to the target image. (required)

--matrix_type Type of matrix which operates in latent space. default is gaussian. options includes gaussian, uniform, orthogonal, symmetric, permutation, sparse, diagonal, wishart.

--steps Number of steps to repeat the process with different random matricies. default is 1.

--lb Lower bound for values in uniform matricies. default is 0.0

--ub Upper bound for values in uniform matricies. default is 1.0.

--density Density for sparce matricies. default is 0.1.

--p Degrees of freedom for the wishart matrix. default is C = dimension of a latent vector.

## requirements

```bash
pip install -r requirements.txt
```