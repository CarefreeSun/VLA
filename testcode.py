from llm_backbone import MistralInVisionActionFeatMask
import torch
import os
from safetensors import safe_open
from transformers import AutoTokenizer
from transformers import Trainer

# tokenzier = AutoTokenizer.from_pretrained('mistral-7B-v0.1')
# va_embed 

# model = MistralInVisionActionFeatMask.from_pretrained('../mistral-7B-v0.1')
# def load_safetensors_weights(checkpoint_dir): 
#     weights_files = [f for f in os.listdir(checkpoint_dir) if f.endswith('.safetensors')] 
#     for weights_file in weights_files: 
#         weights_path = os.path.join(checkpoint_dir, weights_file) 
#         with safe_open(weights_path, framework="pt", device="cpu") as f: 
#             for key in f.keys(): 
#                 print(key, f.get_tensor(key).shape)
#     #             model.state_dict()[key].copy_(f.get_tensor(key)) 
#     # return model
# load_safetensors_weights('../model_weights')
# key = 'model.embeddings.json'
# print(key.split('model.')[-1])

model = MistralInVisionActionFeatMask.from_pretrained('asas')
model.generate()