from abc import ABC, abstractmethod


class ActionError(Exception):
    def __init__(self, message='Execution Failed'):
        super().__init__(message)


class ActionResult:
    def __init__(self, value=None, error=None):
        self.value = value
        self.error = error

    @property
    def succeeded(self):
        return self.error is None

    @property
    def failed(self):
        return self.error is not None


class Action(ABC):
    arguments = list()

    @abstractmethod
    def perform(self): pass

    def fail(self, message):
        raise ActionError(message)

    @classmethod
    def call(cls, **inputs):
        try:
            output = cls._handle(inputs)
            return ActionResult(value=output)
        except Exception as exc:
            exception = ActionError()
            exception.actual = exc
            exception.__cause__ = exc
            return ActionResult(error=exception)

    @classmethod
    def _handle(cls, inputs):
        instance = cls()

        for argument in instance.arguments:
            value = inputs.get(argument)
            setattr(instance, argument, value)

        return instance.perform()
