from .language_detection import execute as detection_language

modules = {
    "language_classification": {
        "function": detection_language,
        "title": "Определение языка",
        "result_title": "Язык"
    },
}
