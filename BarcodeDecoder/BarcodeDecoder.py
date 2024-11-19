from pyzbar.pyzbar import decode as pyzbar_bar_decode, ZBarSymbol
from pylibdmtx.pylibdmtx import decode as pylibdmtx_dm_decode
from pyzxing import BarCodeReader as PyzxingBarCodeReader
from collections import namedtuple
import numpy as np

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
        results = []
        for lib_result in lib_results:
            if 'parsed' in lib_result:
                results.append(DecodedBarCode(data=lib_result['parsed'],
                                              type=lib_result['format'].decode('utf-8')))
        return results

    @staticmethod
    def __pyzbar_decode(data, bar_type):
        lib_results = pyzbar_bar_decode(data, bar_type)
        results = []
        for lib_result in lib_results:
            # poly = ((lib_result.rect.left, lib_result.rect.top),
            #         lib_result.rect.width, lib_result.rect.height)
            results.append(DecodedBarCode(data=lib_result.data,
                                          type=lib_result.type))
        return results

    @staticmethod
    def __pylibdmtx_decode(data):
        lib_results = pylibdmtx_dm_decode(data)
        results = []
        for lib_result in lib_results:
            results.append(DecodedBarCode(type="data_matrix",
                                          data=lib_result.data))
        return results
