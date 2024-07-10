from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

from server.apps.llm.providers.abstract import AbstractLLMProvider
from server.settings.components.llm import (
    DEFAULT_TEMPERATURE,
    GIGACHAT_CREDENTIALS,
    GIGACHAT_VERIFY_SSL_CERTS,
    SYSTEM_PROMPT,
)


class GigachatProvider(AbstractLLMProvider):
    """Класс для общения с LLM-провайдером GigaChat"""

    def __init__(self):
        """Инициализация провайдера"""
        self.giga = GigaChat(
            credentials=GIGACHAT_CREDENTIALS,
            verify_ssl_certs=GIGACHAT_VERIFY_SSL_CERTS,
        )

    def chat(self, message: str):
        """Запрос к LLM-провайдеру"""
        payload = Chat(
            messages=[
                Messages(
                    role=MessagesRole.SYSTEM,
                    content=SYSTEM_PROMPT,
                ),
                Messages(role=MessagesRole.USER, content=message),
            ],
            temperature=DEFAULT_TEMPERATURE,
        )
        response = self.giga.chat(payload)
        return response.choices[0].message.content
