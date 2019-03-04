

from datetime import datetime
from concurrent import futures

import grpc

import epoch_converter_service_pb2
import epoch_converter_service_pb2_grpc


date_format = "%Y-%m-%d %H:%M:%S"
epoch_time = datetime(1970, 1, 1)


class EpochConversionService(epoch_converter_service_pb2_grpc.EpochConverterServiceServicer):
    def ConvertDateToEpochSeconds(self,
                                  request: epoch_converter_service_pb2.ConversionRequest,
                                  context
                                  ):
        print("Received request!\n" + str(request))
        ds = request.date_string

        try:
            dt = datetime.strptime(ds, date_format)

            epoch_seconds = int((dt - epoch_time).total_seconds())

            response = epoch_converter_service_pb2.ConversionResponse(epoch_seconds=epoch_seconds)

        except ValueError as e:
            print("Error parsing supplied date string!\n" + str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Date format must be " + date_format)
            response = epoch_converter_service_pb2.ConversionResponse()

        print("Returning response: " + str(response))
        return response


def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    epoch_converter_service_pb2_grpc.add_EpochConverterServiceServicer_to_server(EpochConversionService(), server)
    server.add_insecure_port('[::]:5000')

    print("Starting server...")
    server.start()
    print("Server up!")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(1)


if __name__ == "__main__":
    start()
