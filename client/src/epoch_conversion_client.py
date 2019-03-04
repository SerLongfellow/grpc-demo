import grpc

import epoch_converter_service_pb2
import epoch_converter_service_pb2_grpc


def main():
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = epoch_converter_service_pb2_grpc.EpochConverterServiceStub(channel)

        ds = "2019-02-25 15:33:01"

        make_request(stub, ds)

        ds = "not a real date"
        make_request(stub, ds)


def make_request(stub, ds):
    try:
        print("Making RPC request with date string: " + ds)
        response = stub.ConvertDateToEpochSeconds(epoch_converter_service_pb2.ConversionRequest(date_string=ds))

        print("Received response!:\n" + str(response))
    except grpc.RpcError as e:
        print("Error making RPC call:\n{}: {}\n".format(str(e.code()), e.details()))


if __name__ == "__main__":
    main()
