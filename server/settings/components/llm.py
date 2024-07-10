import os

GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS", default="")
GIGACHAT_VERIFY_SSL_CERTS = os.getenv("GIGACHAT_VERIFY_SSL_CERTS", default=False)

YANDEX_FOLDER = os.getenv("YANDEX_FOLDER", default="")
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN", default="")

LOCAL_MODEL = os.getenv("LOCAL_MODEL", default="llama3")

DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", default=0.5))

SYSTEM_PROMPT = """
Исправь ошибки в тексте и убери запрещенные слова.
В выводе должен быть только исправленный текст, без какого-либо объяснения.
Используй русский язык.
"""
