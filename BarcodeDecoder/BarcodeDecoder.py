from pyzbar.pyzbar import decode as pyzbar_bar_decode, ZBarSymbol
from pylibdmtx.pylibdmtx import decode as pylibdmtx_dm_decode
from pyzxing import BarCodeReader as PyzxingBarCodeReader
from collections import namedtuple
import numpy as np

from .types_translate import pyzbar_types, pyzxing_types

DecodedBarCode = namedtuple('Decoded', 'data type')


class BarcodeDecoder:
    def decode(self, data: np.ndarray, bar_type: str = ""):
        if res := self.__pyzxing_decode(data):
            return res
        if bar_type == "data_matrix":
            return self.__pylibdmtx_decode(data)
        else:
            if res := self.__pyzbar_decode(data, bar_type):
                return res
            return self.__pylibdmtx_decode(data)

    def __init__(self):
        self.pyzxing_reader = PyzxingBarCodeReader()

    def __pyzxing_decode(self, data):
        lib_results = self.pyzxing_reader.decode_array(data)
        for lib_result in lib_results:
            if 'parsed' in lib_result:
                return DecodedBarCode(data=lib_result['parsed'],
                                      type=pyzxing_types[lib_result['format'].decode('utf-8')])
        return None

    @staticmethod
    def __pyzbar_decode(data, bar_type):
        lib_results = pyzbar_bar_decode(data, bar_type)
        for lib_result in lib_results:
            return DecodedBarCode(data=lib_result.data,
                                  type=pyzbar_types[lib_result.type])
        return None

    @staticmethod
    def __pylibdmtx_decode(data):
        lib_results = pylibdmtx_dm_decode(data)
        for lib_result in lib_results:
            return DecodedBarCode(type="data_matrix",
                                  data=lib_result.data)
        return None
