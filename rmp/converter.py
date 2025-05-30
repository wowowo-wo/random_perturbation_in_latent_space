import torch
from diffusers.models import AutoencoderKL

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse").to(device)
vae.eval()

def encode_image(x):
  with torch.no_grad():
    latent_dist = vae.encode(x)
    z = latent_dist.latent_dist.sample()
    return z * vae.config.scaling_factor
  
def decode_latent(z):
  with torch.no_grad():
    return vae.decode(z / vae.config.scaling_factor).sample
