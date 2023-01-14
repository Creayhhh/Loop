import base64
import hashlib
import pyDes

import cv2 as cv

def resizeImageForWidget(image, widget_width, widget_height):
    """ 将传入的图片处理成符合widget匹配的大小(只要稍微大于widget就行了)
    :param image: 待处理的图像
    :param widget_width: widget的宽
    :param widget_height: widget的高
    :return: 处理好的图像
    """
    while image.shape[1] < widget_width or image.shape[0] < widget_height:
        image = cv.resize(image, (int(image.shape[1] * 1.1), int(image.shape[0] * 1.1)))

    # print("widget_width:{}, widget_height:{}".format(widget_width, widget_height))
    # print("image_w:{}, image_h:{}".format(image.shape[1], image.shape[0]))

    return image


def sha256_encryption(data):
    """将传入的data进行sha256加密
    :param data: 待加密的数据
    :return: 加密完成的数据
    """

    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def encrypt_3des(data):
    """将传入的data进行3DES加密
    :param data: 待加密的数据
    :return: 加密完成的数据
    """
    key = "LOOP_CLIENT_security_PIGPIG"
    hash_md5 = hashlib.md5()
    hash_md5.update(key.encode(encoding='UTF-8'))
    key = hash_md5.hexdigest()
    iv = key[0:8]
    key2 = key[0:24]
    k = pyDes.triple_des(key2, pyDes.CBC, IV=iv, pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data.encode())
    d = base64.b64encode(d)
    return d.decode()


def decrypt_3des(data):
    """将传入的data进行3DES解密
    :param data: 待解密的数据
    :return: 解密完成的数据
    """
    key = "LOOP_CLIENT_security_PIGPIG"
    hash_md5 = hashlib.md5()
    hash_md5.update(key.encode(encoding='UTF-8'))
    key = hash_md5.hexdigest()
    iv = key[0:8]
    key2 = key[0:24]
    k = pyDes.triple_des(key2, pyDes.CBC, IV=iv, pad=None, padmode=pyDes.PAD_PKCS5)
    data = base64.b64decode(data)
    d = k.decrypt(data)
    return d.decode()
