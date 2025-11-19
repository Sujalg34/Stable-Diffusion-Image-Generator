
from fastapi import FastAPI
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch

app = FastAPI(title="Stable Diffusion API")

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe.to("cpu")

class Txt2ImgRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Welcome to the Stable Diffusion API!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/txt2img")
def txt2img(request: Txt2ImgRequest):
    image = pipe(request.prompt).images[0]
    image_path = "generated.png"
    image.save(image_path)
    return {"output_image": image_path}
