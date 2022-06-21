import numpy as np
import gradio as gr
import argparse
import os
from test import test
from PIL import Image




def Args():
    parser = argparse.ArgumentParser()

    # Default
    parser.add_argument('--content_dir', type=str, default='/app/content/')
    parser.add_argument('--texture_dir', type=str, default='/app/texture/')
    parser.add_argument('--color_dir', type=str, default='/app/color/')
    parser.add_argument('--out_root', type=str, default='/app/output/')
    parser.add_argument('--network', type=str, default='/app/models/net_final.pth')
    parser.add_argument('--vgg', type=str, default='/app/models/vgg_normalised.pth')
    parser.add_argument('--name', default='AAST')

    # Testing
    parser.add_argument('--test_opt', type=str, default='TC')
    parser.add_argument('--int_num', type=int, default=4)
    args = parser.parse_args()
    return args

def clear_folders():
    dir = '/app/content/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    dir = '/app/color/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    dir = '/app/texture/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
    dir = '/app/output/AAST'
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

demo = gr.Interface(init_content, inputs=[gr.Image(type='pil'),gr.Image(type='pil'),gr.Image(type='pil')], outputs="image")

demo.launch()