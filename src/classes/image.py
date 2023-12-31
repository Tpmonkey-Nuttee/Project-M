import os.path
from io import BytesIO


class Image:
    def __init__(self) -> None:
        self._images = {}
        self._bimages = {}

    def __getitem__(self, __name: str) -> BytesIO:
        if __name not in self._images:
            raise KeyError(f"Image named {__name}; not found.")

        if __name in self._bimages:
            return self._bimages[__name]

        with open(self._images[__name], "rb") as file:
            self._bimages[__name] = file.read()

        return self._bimages[__name]

    def __setitem__(self, __name: str, __value: str) -> None:
        if not os.path.isfile(__value):
            raise FileNotFoundError(f"Couldn't find {__value}")

        self._images[__name] = __value
