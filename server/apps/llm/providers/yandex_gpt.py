from yandexgptlite import YandexGPTLite

from server.apps.llm.providers.abstract import AbstractLLMProvider
from server.settings.components.llm import (
    DEFAULT_TEMPERATURE,
    SYSTEM_PROMPT,
    YANDEX_FOLDER,
    YANDEX_TOKEN,
)


class YandexGPTLiteProvider(AbstractLLMProvider):
    """Класс для общения с LLM-провайдером Yandex GPT"""

    def __init__(self):
        """Инициализация провайдера"""
        self.yandex = YandexGPTLite(folder=YANDEX_FOLDER, token=YANDEX_TOKEN)

    def chat(self, message):
        """Запрос к LLM-провайдеру"""
        return self.yandex.create_completion(
            prompt=message,
            system_prompt=SYSTEM_PROMPT,
            temperature=DEFAULT_TEMPERATURE,
        )
