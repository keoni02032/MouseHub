import os
import sys
import numpy
from PIL import Image
from kandinsky2 import get_kandinsky2

model = get_kandinsky2('cuda', task_type='text2img', model_version='2.1', use_flash_attention=False)

if not os.path.isdir('save_images'):
    os.mkdir('save_images')


for i in rnage(len(100)):
	images = model.generate_text2img(
	    "Mickey Mouse with broken proportions in black and white style, 4k photo", 
	    num_steps=100,
	    batch_size=1, 
	    guidance_scale=4,
	    h=768, w=768,
	    sampler='p_sampler', 
	    prior_cf_scale=4,
	    prior_steps="5"
	)

	images.save(f'out_{i}.jpg')