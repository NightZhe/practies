import torch
torch.__version__

print(f"{torch.backends.mps.is_available(),torch.backends.mps.is_built()}")

a=torch.rand(5).to("mps")
print(a)

