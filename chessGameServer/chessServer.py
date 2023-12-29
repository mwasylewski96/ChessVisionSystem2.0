############################
###  EXTERNAL LIBRARIES  ###
############################
import logging
import sys

from aiohttp import web, ClientResponseError
import asyncio
from copy import deepcopy
from dataclasses import dataclass
import json
import os
import pkg_resources as res
import socketio
import ssl
from typing import Type
import subprocess

############################
###  INTERNAL LIBRARIES  ###
############################
from endpoints import *
from jetson_backend.logger import Logger
from Jetson_model import Model
from JSON_examples.Jetson_Server_ENDPOINTY import *
from SocketOutputs import *
from optim_treatment_utils.config import get_jetson_aws_config
from optim_treatment_utils.tools import Result, get_process_by_name
from optim_treatment_utils.APIs.machine_learning_api.InputDTOs import UsersLoginCRMInput

jetson_aws_config = get_jetson_aws_config()


class Server(web.Application):

    def __init__(self):
        super(Server, self).__init__()

        self.model = Model()
        self.socket: socketio.AsyncServer = Server.Socket(self.model)
        self.cleanup_ctx.append(self.subprocesses)
        self.socket.attach(self)

        self.__logger = logging.getLogger(__name__)
        Logger.setup_file_handler(logger=__name__, handler_level=logging.INFO)
        Logger.setup_stdout_handler(logger=__name__, handler_level=logging.DEBUG)
        self.__logger.info("Initialising server...")

    async def subprocesses(self, app):
        self.__logger.info("Server turn on")
        self.model.hsi_methods.set_loop(asyncio.get_running_loop())
        self.model.laser_stack_methods.set_loop(asyncio.get_running_loop())
        yield
        print("Server turn off")

    class Socket(socketio.AsyncServer):

        def __init__(self, model: Model, async_mode='aiohttp'):
            super(Server.Socket, self).__init__(async_mode=async_mode, cors_allowed_origins='*')
            # self.log_where_string = f'[{type(self).__name__}] ||'

            self.__logger = logging.getLogger(__name__)

            self.default_namespace = "/"
            self.test_gui_namespace = "/test_gui"


            self.register_namespace(socketio.AsyncNamespace(namespace=self.test_namespace))


            def channel_event_decorator(
                    this_model_method: callable,
                    this_endpoint: Type[Endpoint],  # TODO: it is a class, not instance
                    socket_output: Type[SocketOutput],  # TODO: it is a class, not instance
                    server_namespace: str = '/',
                    client_namespace: str = '/'
            ):
                """

                :param this_model_method:
                :param this_endpoint:
                :param socket_output:
                :param server_namespace: particular path-like namespace on Server. Example: '/test'.
                :param client_namespace: particular path-like namespace on Client. Example: '/test'.
                :return:
                """

                def inner(
                        wrapped_fun: callable
                ):
                    """

                    :param wrapped_fun: function that will be wrapped.
                    :return:
                    """

                    self.__logger.debug(f"{self.log_where_string} Setting up `{wrapped_fun.__name__}` endpoint on namespace: `{server_namespace}`.")

                    async def wrapper(
                            sid,
                            data_dict: Optional[dict] = None
                    ) -> None:
                        self.__logger.debug(f"{self.log_where_string} `{wrapped_fun.__name__}` process started on namespace: `{server_namespace}`... data_dict: `{data_dict}`")
                        parsed_input = this_endpoint.parse_input(sid=sid, data=data_dict)
                        self.__logger.debug(f"{self.log_where_string} Acquiring data with `{parsed_input}`")
                        response = await this_model_method(endpoint_input=parsed_input)
                        if response.success:
                            self.__logger.debug(f"{self.log_where_string} {wrapped_fun.__name__} process finished successfully!")
                        self.__logger.debug(f"Emitting response to: '{wrapped_fun.__name__ + '_response'}' on namespace: '{client_namespace}'")
                        self.__logger.debug(f"Response: {response}")
                        await self.emit(
                            f"{wrapped_fun.__name__ + '_response'}",
                            response.serialize(),
                            namespace=client_namespace,
                            room=sid
                        )

                    self.on(wrapped_fun.__name__, handler=wrapper, namespace=server_namespace)
                return inner

            @channel_event_decorator(
                this_model_method=model.laser_stack_methods.reconfigure_direct_params_laser_process,
                this_endpoint=ReconfigureDirectParamsLaserProcessEndpoint,
                socket_output=ReconfigureDirectParamsLaserProcessOutput,
                server_namespace=self.laser_stack_controller_namespace,
                client_namespace=self.laser_stack_controller_namespace  # same namespace
            )
            async def reconfigure_direct_params_laser_process():
                pass

            @channel_event_decorator(
                this_model_method=model.laser_stack_methods.get_target_safety_profile_laser_process,
                this_endpoint=GetTargetSafetyProfileLaserProcessEndpoint,
                socket_output=GetTargetSafetyProfileLaserProcessOutput,
                server_namespace=self.laser_stack_controller_namespace,
                client_namespace=self.laser_stack_controller_namespace  # same namespace
            )
            async def get_target_safety_profile_server_laser_process():
                """
                This endpoint is used for emergency turning off all pwm laser stacks.
                This request can be executed all the time.
                :param:
                :return: None
                """
                pass


        async def send_time_to_end_to_gui(
                self,
                response: SendTimeToEndToGuiOutput
        ) -> None:
            """
            This method is used for sending response to gui about current passed time of epilation.
            :param response:
            :return: None
            """
            await self.emit(
                "send_time_to_end_to_gui_response",
                data=response.serialize(),
                namespace=self.laser_stack_controller_namespace
            )

#####################################################################################################################


def main():
    server = Server()
    web.run_app(server)


if __name__ == '__main__':
    main()

