
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import os

import grpc

import epoch_converter_service_pb2
import epoch_converter_service_pb2_grpc

grpc_host = os.environ.get("GRPC_HOST", "localhost")
grpc_port = os.environ.get("GRPC_PORT", "5000")

grpc_endpoint = '{}:{}'.format(grpc_host, grpc_port)
print("Using {} as gRPC remote endpoint channel.".format(grpc_endpoint))
grpc_channel = grpc.insecure_channel('{}:{}'.format(grpc_host, grpc_port))



class HttpHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        if self.path == "/health":
            self.respond_to_health_check()
            return

        try:
            ds = parse.parse_qs(parse.urlparse(self.path).query).get("ds", None)

            if ds is None:
                self.send_response(400)
                self.send_header("content-type", "application/text")
                self.end_headers()
                self.wfile.write(bytes("Bad request! No 'ds' query parameter", "UTF-8"))
                return

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

    def respond_to_health_check(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("", "UTF-8"))

    def handle_http(self):
        return

    def respond(self):
        return


def main():

    print("Starting server...")
    httpd = HTTPServer(("0.0.0.0", 8080), HttpHandler)

    print("Server up!")
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
