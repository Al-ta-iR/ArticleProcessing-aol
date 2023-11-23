# ArticleProcessing

Application for processing news (and other) articles

## Used models
Module | Model | Included in the app | Unit tests written
-|-|-|-|-
Language detection | papluca/xlm-roberta-base-language-detection | | ✔️
## Web apps

### Streamlit

#### A.Oleynik
Model: ![papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection)
Run: streamlit run streamlit_lang_detect_app.py
Details: Type the required text in the input field and press Ctrl+Enter.
The expected language of the entered text will appear below the input field.
![View of the working application](https://github.com/MyEvilpumpkin/ArticleProcessing/assets/13471304/8a4bfc0b-d6c1-48ce-977c-c26417b18556)
