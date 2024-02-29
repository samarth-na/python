import google.generativeai
genai = google.generativeai


genai.configure(api_key="AIzaSyA25dW4h_UcxwgWkOXeq2zpONgfces3XMU")


for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("how to make cake ")


print(response.text)
