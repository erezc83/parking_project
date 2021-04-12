"""
file type need to be only from type: PDF, GIF, PNG, JPG, TIF, BMP
"""
import requests


def ocr_space_file(filename, overlay=False, api_key='e90ff1e75d88957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': "e90ff1e75d88957",
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )

    return r.content.decode()
