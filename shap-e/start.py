import PIL
import torch
from PIL import Image
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import create_pan_cameras, decode_latent_images, gif_widget
import os

if not os.path.isdir('save_images'):
    os.mkdir('save_images')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

xm = load_model('transmitter', device=device)
model = load_model('text300M', device=device)
diffusion = diffusion_from_config(load_config('diffusion'))

batch_size = 5
size_image = 256
guidance_scale = 15.0
prompt = "Mickey Mouse" # disney character Mickey Mouse with broken proportions in black and white style  "a shark that looks like a banana"

latents = sample_latents(
    batch_size=batch_size,
    model=model,
    diffusion=diffusion,
    guidance_scale=guidance_scale,
    model_kwargs=dict(texts=[prompt] * batch_size),
    progress=True,
    clip_denoised=True,
    use_fp16=True,
    use_karras=True,
    karras_steps=64,
    sigma_min=1e-3,
    sigma_max=160,
    s_churn=0,
)

render_mode = 'nerf' # you can change this to 'stf'
size = size_image # this is the size of the renders; higher values take longer to render. 384

width = size_image
height = size_image
im1 = Image.new("RGBA", (width, height), (255, 0, 0))

cameras = create_pan_cameras(size, device)
for i, latent in enumerate(latents):
    images = decode_latent_images(xm, latent, cameras, rendering_mode=render_mode)
    print(type(images))
    im1.save(f"./save_images/out_{i}.gif", save_all=True, append_images=images, duration=100, loop=0)


# Example of saving the latents as meshes.
from shap_e.util.notebooks import decode_latent_mesh

for i, latent in enumerate(latents):
    t = decode_latent_mesh(xm, latent).tri_mesh()
    with open(f'./save_images/example_mesh_{i}.ply', 'wb') as f:
        t.write_ply(f)
    with open(f'./save_images/example_mesh_{i}.obj', 'w') as f:
        t.write_obj(f)