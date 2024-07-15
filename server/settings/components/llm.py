import os

GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS", default="")
GIGACHAT_VERIFY_SSL_CERTS = os.getenv("GIGACHAT_VERIFY_SSL_CERTS", default=False)
GIGACHAT_CHUNK_SIZE = os.getenv("GIGACHAT_CHUNK_SIZE", default=800)


YANDEX_FOLDER = os.getenv("YANDEX_FOLDER", default="")
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN", default="")
YANDEX_CHUNK_SIZE = os.getenv("YANDEX_CHUNK_SIZE", default=800)


LOCAL_MODEL = os.getenv("LOCAL_MODEL", default="llama3")
LLAMA_CHUNK_SIZE = os.getenv("LLAMA_CHUNK_SIZE", default=400)


DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", default=0.5))

DEFAULT_CHUNK_SIZE = int(os.getenv("DEFAULT_CHUNK_SIZE", default=255))


SYSTEM_PROMPT = """
Исправь ошибки в тексте и убери запрещенные слова.
В выводе должен быть только исправленный текст, без какого-либо объяснения.
Используй русский язык.
"""
