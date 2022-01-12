import io

from fastapi import HTTPException, status
from PIL import Image


async def crop_image(image: bytes, width: int, height: int) -> bytes:

    image_obj = Image.open(io.BytesIO(image))
    image_width = image_obj.size[0]
    image_height = image_obj.size[1]

    aspect = image_width / float(image_height)

    ideal_aspect = width / float(height)

    if aspect > ideal_aspect:
        new_width = int(ideal_aspect * image_height)
        offset = (image_width - new_width) / 2
        resize = (offset, 0, image_width - offset, image_height)
    else:
        new_height = int(image_width / ideal_aspect)
        offset = (image_height - new_height) / 2
        resize = (0, offset, image_width, image_height - offset)

    cropped_image = image_obj.crop(resize).resize(
        (width, height), Image.ANTIALIAS)
    img_byte_arr = io.BytesIO()
    try:
        cropped_image.save(img_byte_arr, format="PNG")
    except OSError:
        cropped_image.convert('RGB')
        cropped_image.save(img_byte_arr, format="PNG")
    except Exception as err:
        raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED,
                            'method not implemented yet')
    return img_byte_arr.getvalue()
