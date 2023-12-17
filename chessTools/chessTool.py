############################
###  EXTERNAL LIBRARIES  ###
############################
import cv2
import numpy as np
import os
import sys
import platform
if platform.system() == "Windows":
    import win32com.client

if sys.version_info >= (3, 8):
    from typing import Union, Generic, TypeVar, Dict, Any, Optional, List, Iterable, Callable, Tuple, Literal
else:
    from typing import Union, Generic, TypeVar, Dict, Any, Optional, List, Iterable, Callable, Tuple
    from typing_extensions import Literal

import yaml
############################
###  INTERNAL LIBRARIES  ###
############################
# from chessTools.chessConfig import get_chess_cameras_config TODO repair circular import


def read_yaml(
        path: os.PathLike
) -> dict:
    """
    Reads YAML file.

    :param path: absolute or relative path to YAML file.
    :return: Dictionary adequate to structure of YAML file.
    """

    with open(path) as config_stream:
        try:
            config = yaml.safe_load(config_stream)
        except yaml.YAMLError as e:
            raise Exception(f'Could not read yamlfile:{path}, e:{repr(e)}')
    return config


def write_yaml(
        data: Dict,
        path: os.PathLike
) -> None:
    """
    Writes dict to YAML file in the specified path.

    :param data: dictionary that is going to be saved.
    :param path: absolute or relative path where the YAML file will be saved.
    :return: None
    """

    with open(path, 'w') as config_stream:
        try:
            yaml.safe_dump(data, config_stream, default_style='\'', default_flow_style=False)
        except yaml.YAMLError as e:
            raise Exception(f'Could not write yamlfile:{path}, e:{repr(e)}')
    return


def stack_images(
        scale: float,
        img_array: List[List[Union[np.ndarray, List[np.ndarray]]]]
):
    """
    This function is used to pack different images on one object.
    :param scale:
    :param img_array:
    :return:
    """
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y],
                        (0, 0),
                        None,
                        scale,
                        scale
                    )
                else:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y],(
                            img_array[0][0].shape[1],
                            img_array[0][0].shape[0]
                        ),
                        None,
                        scale,
                        scale
                    )
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(
                        img_array[x][y],
                        cv2.COLOR_GRAY2BGR
                    )
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        # hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(
                    img_array[x],
                    (0, 0),
                    None,
                    scale,
                    scale
                )
            else:
                img_array[x] = cv2.resize(
                    img_array[x], (
                        img_array[0].shape[1],
                        img_array[0].shape[0]
                    ),
                    None,
                    scale,
                    scale
                )
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(
                    img_array[x],
                    cv2.COLOR_GRAY2BGR
                )
        hor = np.hstack(img_array)
        ver = hor
    return ver


def get_right_camera_index():
    system_info = platform.system()
    if system_info == 'Windows':
        detected_camera_list = []
        # config_camera_dict = get_chess_cameras_config() TODO repair circular import
        wmi = win32com.client.GetObject("winmgmts:")
        config_vid = "USB\VID"
        config_external_camera = "831DF12&0&2"
        config_internal_camera = "831DF12&0&4"
        for usb in wmi.InstancesOf("Win32_USBHub"):
            if usb.DeviceID.startswith(config_vid):
                if usb.DeviceID.endswith(config_internal_camera):
                    detected_camera_list.append(config_internal_camera)
                if usb.DeviceID.endswith(config_external_camera):
                    detected_camera_list.append(config_external_camera)

        if detected_camera_list == [config_external_camera, config_internal_camera]:
            return 0
        elif detected_camera_list == [config_internal_camera, config_external_camera]:
            return 1
        elif detected_camera_list == [config_external_camera]:
            return 0
        else:
            return None

    if system_info == 'Linux':
        return 2



T = TypeVar('T')


class Result(Generic[T]):
    def __init__(
            self,
            success: bool,
            value: T,
            error: Optional[str]
    ) -> None:
        """
        Class which is used during returning values. Enables to pass information about success or handle errors outside
        functions.

        :param success: boolean status: True - Successfully finished, False - Errors appeared.
        :param value: value which will be passed.
        :param error: error message which will be passed.
        :return: None.
        """

        self.success = success
        self.error = error
        self.value: T = value

    def __str__(
            self
    ) -> str:
        """
        Handles returning message.

        :return: string with message Success or Failure with value/error adequate.
        """

        if self.success:
            return f'[Success]: {self.value}'
        else:
            return f'[Failure] "{self.error}"'

    @classmethod
    def error(
            cls,
            error: str
    ):
        """
        Handling error.

        :param error: Error message.
        :return: Result class with error value.
        """

        return cls(False, value=None, error=error)

    @classmethod
    def success(
            cls,
            value: Any = None
    ):
        """
        Handling Success with optional value.

        :param value: optional possibility of passing value.
        :return: Result class with optional value.
        """

        return cls(True, value=value, error=None)