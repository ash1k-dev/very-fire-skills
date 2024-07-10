import abc


class AbstractLLMProvider(abc.ABC):
    """Абстрактный класс провайдера для LLM"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Проверка на наличие одного единственного экземпляра провайдера"""
        if not cls._instance:
            cls._instance = super(AbstractLLMProvider, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance

    @abc.abstractmethod
    def chat(self, message: str):
        """Метод для отправки запросов к LLM"""
        pass
