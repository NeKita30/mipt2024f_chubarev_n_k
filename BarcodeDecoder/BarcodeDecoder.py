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
                type_ = pyzxing_types.get(lib_result['format'].decode('utf-8'),
                                          lib_result['format'].decode('utf-8'))
                return DecodedBarCode(data=lib_result['parsed'],
                                      type=type_)
        return None

    @staticmethod
    def __pyzbar_decode(data, bar_type):
        lib_results = pyzbar_bar_decode(data, bar_type)
        for lib_result in lib_results:
            type_ = pyzbar_types.get(lib_result.type, lib_result.type)
            return DecodedBarCode(data=lib_result.data,
                                  type=type_)
        return None

    @staticmethod
    def __pylibdmtx_decode(data):
        lib_results = pylibdmtx_dm_decode(data)
        for lib_result in lib_results:
            return DecodedBarCode(type="data_matrix",
                                  data=lib_result.data)
        return None
