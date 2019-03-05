
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import os

import grpc

import epoch_converter_service_pb2
import epoch_converter_service_pb2_grpc

grpc_host = os.environ.get("GRPC_HOST", "localhost")
grpc_channel = grpc.insecure_channel('{}:5000'.format(grpc_host))


class HttpHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        print("Got GET request!")

        try:
            ds = parse.parse_qs(parse.urlparse(self.path).query).get("ds", None)
            ds = ds[0]

            stub = epoch_converter_service_pb2_grpc.EpochConverterServiceStub(grpc_channel)
            epoch = make_request(stub, ds)
            response = "Datetime conversion result is " + epoch

            self.send_response(200)
            self.send_header("content-type", "application/text")
            self.end_headers()
            self.wfile.write(bytes("{}\n".format(response), "UTF-8"))
        except Exception as e:
            print(str(e))

            self.send_response(500)
            self.send_header("content-type", "application/text")
            self.end_headers()
            self.wfile.write(bytes("Server error!\n", "UTF-8"))

    def handle_http(self):
        return

    def respond(self):
        return


def main():

    print("Starting server...")
    httpd = HTTPServer(("0.0.0.0", 8080), HttpHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")

    httpd.server_close()


def make_request(stub, ds):
    try:
        request = epoch_converter_service_pb2.ConversionRequest(date_string=ds)

        print("Making RPC request: " + str(request))
        response = stub.ConvertDateToEpochSeconds(request)

        print("Received response!:\n" + str(response))

        response = str(response.epoch_seconds)

    except grpc.RpcError as e:
        print("Error making RPC call:\n{}: {}\n".format(str(e.code()), e.details()))

        response = "Error!"

    return response


if __name__ == "__main__":
    main()
