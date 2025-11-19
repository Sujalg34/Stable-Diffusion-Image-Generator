
# Stable Diffusion FastAPI Image Generator

This project is a **FastAPI-based Stable Diffusion API** that generates images from text prompts using the Hugging Face Diffusers library.

---

## 🚀 Features
- Text-to-image generation  
- FastAPI endpoints (`/`, `/health`, `/txt2img`)  
- Automatically saves generated images  
- CPU-friendly configuration (works on Render free tier)  
- Easy deployment on Render  

---

## 📂 Project Structure
```
project/
 ├── main.py
 ├── requirements.txt
 └── README.md
```

---

## 🛠 Installation (Run Locally)

### 1️⃣ Clone the repository
```
git clone https://github.com/Sujalg34/Stable-Diffusion-Image-Generator
cd stable-diffusion-fastapi
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the server
```
uvicorn main:app --reload
```

### 4️⃣ Open API docs
Go to:

👉 http://localhost:8000/docs  
👉 http://localhost:8000/health  

---

## 🔥 API Endpoints

### ✔ **GET /**  
Returns a welcome message.

### ✔ **GET /health**  
Health check endpoint.

### ✔ **POST /txt2img**
Generates an image from a text prompt.

#### Request Body:
```json
{
  "prompt": "a futuristic city with flying cars"
}
```

#### Response:
```json
{
  "output_image": "generated.png"
}
```

---

## 🌐 Deployment on Render

### 1️⃣ Create a new Web Service  
Go to **https://render.com**

### 2️⃣ Connect your GitHub repo

### 3️⃣ Use these settings:

- **Runtime:** Python  
- **Build Command:**  
```
pip install -r requirements.txt
```
- **Start Command:**  
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### 4️⃣ Deploy  
Render will build the API and give you a **public URL** like:

```
https://your-project-name.onrender.com/docs
```

---

## 🖼 Output Images

All generated images are saved as:

```
generated.png
```

You can modify the filename logic in `main.py` to save multiple images with timestamps.

---

## 📌 Requirements
- Python 3.8+
- FastAPI
- Diffusers
- Torch
- Uvicorn

---

## 🧑‍💻 Author
Sujal Gandhi
