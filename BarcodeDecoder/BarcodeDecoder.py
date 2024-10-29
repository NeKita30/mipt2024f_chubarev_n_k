from pyzbar.pyzbar import decode as pyzbar_bar_decode, ZBarSymbol
from pylibdmtx.pylibdmtx import decode as pylibdmtx_dm_decode
from pyzxing import BarCodeReader as PyzxingBarCodeReader
import numpy as np


class BarcodeDecoder:
    def decode(self, data: np.ndarray, bar_type: str = ""):
        if res := self.__pyzxing_decode(data):
            return res
        if bar_type == "data_matrix":
            return self.__pylibdmtx_decode(data)
        else:
            return self.__pyzbar_decode(data, bar_type)

    def __init__(self):
        self.pyzxing_reader = PyzxingBarCodeReader()

    def __pyzxing_decode(self, data):
        results = self.pyzxing_reader.decode_array(data)
        for result in results:
            pass

    @staticmethod
    def __pyzbar_decode(data, bar_type):
        return pyzbar_bar_decode(data, bar_type)

    @staticmethod
    def __pylibdmtx_decode(data):
        return pylibdmtx_dm_decode(data)
