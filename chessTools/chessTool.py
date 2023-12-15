############################
###  EXTERNAL LIBRARIES  ###
############################
import os
import sys

if sys.version_info >= (3, 8):
    from typing import Generic, TypeVar, Dict, Any, Optional, List, Iterable, Callable, Tuple, Literal
else:
    from typing import Generic, TypeVar, Dict, Any, Optional, List, Iterable, Callable, Tuple
    from typing_extensions import Literal

import yaml
############################
###  INTERNAL LIBRARIES  ###
############################


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