import os
from diffusers import StableDiffusionPipeline
import torch

if not os.path.isdir('save_images'):
    os.mkdir('save_images')

model_id = "nitrosocke/mo-di-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# prompt = "a magical princess with golden hair, modern disney style"
for i in range(10):
	prompt = "close-up of a man in a Mickey Mouse costume, 3D rendering inspired by Walt Disney, elegant standing pose, mouse people, wax figure, dark studio lighting, mouse has black shoes, mouse has a black turtleneck, mouse has red trousers, mouse smiles sweetly, symmetrical rendering of the whole body, Johnny Ives, dominant pose, restored colors, modeled"
	image = pipe(prompt).images[0]

	image.save(f"./save_images/Mickey_Mouse_{i}.png")