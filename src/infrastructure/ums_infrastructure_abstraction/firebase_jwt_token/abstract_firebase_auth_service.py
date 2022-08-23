from abc import abstractmethod, ABC


class AbstractFirebaseAuthService(ABC):
    __metaclass__ = "ABCMeta"

    @abstractmethod
    def sign_in_access_and_refresh_token(self, received_email: str, received_password: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def refresh_token(self, received_refresh_token):
        raise NotImplementedError

    @abstractmethod
    def verify_access_token(self):
        raise NotImplementedError
