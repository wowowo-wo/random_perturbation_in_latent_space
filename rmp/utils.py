import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

def preprocess_image(img_path):
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  image = Image.open(img_path).convert("RGB")
  transform = transforms.Compose([
      transforms.Resize((512,512)),
      transforms.ToTensor(),
      transforms.Normalize([0.5],[0.5])
  ])
  return transform(image).unsqueeze(0).to(device)

def to_pil(tensor_img):
    img = tensor_img.squeeze().cpu()
    img = (img * 0.5 + 0.5).clamp(0, 1)
    return transforms.ToPILImage()(img)

def show_image(image):

    plt.figure(figsize=(4, 4))
    plt.imshow(to_pil(image))
    plt.axis("off")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

def show_images(original, transformed):

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(to_pil(original))
    axs[0].axis("off")

    axs[1].imshow(to_pil(transformed))
    axs[1].axis("off")
    plt.tight_layout()
    plt.show()

