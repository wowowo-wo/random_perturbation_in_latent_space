import torch

def apply_random_matrix(z, matrix_type, **kwargs):
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  B, C, H, W = z.shape
  z_flat = z.view(B, C, -1)

  if matrix_type == 'gaussian':
    A = torch.randn(C, C).to(device)

  elif matrix_type == 'uniform':
    a = kwargs.get('lb', 0.0)
    b = kwargs.get('ub', 1.0)
    A = (b - a) * torch.rand(C, C).to(device) + a

  elif matrix_type == 'orthogonal':
    A = torch.linalg.qr(torch.randn(C, C).to(device)).Q

  elif matrix_type == 'symmetric':
    A = torch.randn(C, C).to(device)
    A =  (A + A.T) / 2

  elif matrix_type == 'permutation':
    perm = torch.randperm(C)
    A =torch.eye(C)[perm].to(device)

  elif matrix_type == 'sparse':
    density = kwargs.get('density', 0.1)
    mask = (torch.rand(C, C) < density).float().to(device)
    A = torch.randn(C, C).to(device) * mask

  elif matrix_type == 'diagonal':
    diag = kwargs.get(torch.randn(C).to(device))
    A =  torch.diag(diag)

  elif matrix_type == "wishart":
    p=kwargs.get('p',C)
    x = torch.randn(C,p).to(device)
    A = x.T @ x
 
  else:
      raise ValueError(f"Unknown matrix_type: {matrix_type}")
  
  z_transformed = torch.matmul(A, z_flat)
  return z_transformed.view(B, C, H, W)