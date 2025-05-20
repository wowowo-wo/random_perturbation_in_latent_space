import torch
from .operator import apply_random_matrix
from .converter import encode_image, decode_latent
from .utils import preprocess_image, to_pil
import argparse
import os

def main(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    kwargs = {
        "lb": args.lb,
        "ub": args.ub,
        "density": args.density
    }
    if args.p is not None:
        kwargs["p"] = args.p

    if args.seed is not None:
        torch.manual_seed(args.seed)
        torch.cuda.manual_seed_all(args.seed)
        print(f"seed set to {args.seed}")
    else:
        print("no seed set")

    img_tensor = preprocess_image(args.img_path).to(device)
    z = encode_image(img_tensor).to(device)

    for i in range(args.n):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        z_tr = apply_random_matrix(z, args.matrix_type, **kwargs)
        img_tensor = decode_latent(z_tr)
        img_out = to_pil(img_tensor)
        img_out.save(os.path.join(output_dir, f"output_{i}.png"))

def get_parser():
    parser = argparse.ArgumentParser(description="Apply random matrix to VAE latent space and decode image.")
    parser.add_argument("--img_path", type=str, required=True, help="path to the image")
    parser.add_argument(
        "--matrix_type",
        type=str,
        default="gaussian",
        choices=["gaussian", "uniform", "orthogonal", "symmetric", "permutation", "sparse", "diagonal", "wishart"],
        help="Type of random matrix to apply to the latent vector."
    )
    parser.add_argument("--n", type=int, default=1, help="number of trials to repeat the transformation.")
    parser.add_argument("--lb", type=float, default=0.0, help="lower bound for uniform distribution")
    parser.add_argument("--ub", type=float, default=1.0, help="upper bound for uniform distribution")
    parser.add_argument("--density", type=float, default=0.1, help="density for sparse matrix.")
    parser.add_argument("--p", type=int, help="degrees of freedom for Wishart matrix.")
    parser.add_argument("--seed", type=int, default=None, help="random seed")
    return parser