import numpy as np
import gradio as gr
import argparse
import os
from test import test
from PIL import Image

title = "Aesthetic-Aware Model-Optimisation-Based Style Transfer"
description = """
<center>
<div style="width: 500px;">
Transfer texture and color from your reference photos to a separate image! Use the following as inputs:
<ul>
  <li><b>Content Image</b>: The image to which the style will be transferred to</li>
  <li><b>Color Reference</b>: Reference image for your colors</li>
  <li><b>Texture Reference</b>: Reference image for your textures</li>
</ul>
</div>
</center>
"""

article = "Check out [the original paper](https://dl.acm.org/doi/abs/10.1145/3394171.3413853) that this demo is based off of."

def Args():
    import sys
    sys.argv=['']
    del sys

    parser = argparse.ArgumentParser()

    # Default
    parser.add_argument('--content_dir', type=str, default='content/')
    parser.add_argument('--texture_dir', type=str, default='texture/')
    parser.add_argument('--color_dir', type=str, default='color/')
    parser.add_argument('--out_root', type=str, default='output/')
    parser.add_argument('--network', type=str, default='models/net_final.pth')
    parser.add_argument('--vgg', type=str, default='models/vgg_normalised.pth')
    parser.add_argument('--name', default='AAST')

    # Testing
    parser.add_argument('--test_opt', type=str, default='TC')
    parser.add_argument('--int_num', type=int, default=4)
    args = parser.parse_args()
    return args

def clear_folders():
    dir = 'content/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    dir = 'color/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    dir = 'texture/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
    dir = 'output/AAST'
    for f in os.listdir(dir):
        if os.path.isfile(f):
            os.remove(os.path.join(dir, f))

def init_content(content_img, color_img, texture_img):
    clear_folders()

    content_img.save('content/input.jpg', 'JPEG')
    color_img.save('color/input.jpg', 'JPEG')
    texture_img.save('texture/input.jpg', 'JPEG')

    args = Args()
    test(args)
    output_img = Image.open('output/AAST/ct0_t0_cr0_result.png')
    
    return output_img

gr.close_all()
demo = gr.Interface(init_content, inputs=[gr.inputs.Image(type='pil'),gr.inputs.Image(type='pil'),gr.inputs.Image(type='pil')], outputs="image", enable_queue=True, title = title, description = description, article = article) 
demo.launch()