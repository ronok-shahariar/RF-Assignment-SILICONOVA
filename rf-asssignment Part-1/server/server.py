from concurrent import futures
import grpc
import rfcontrol_pb2
import rfcontrol_pb2_grpc

class RFServiceServicer(rfcontrol_pb2_grpc.RFServiceServicer):
    def SetRFSettings(self, request, context):
        print("\n RF Setting Received")
        print(f"Frequency: {request.frequency} Hz")
        print(f"Gain: {request.gain} dB")
        print(f"Device ID: {request.device_id}")

        # Mock hardware interaction with logs
        print(f"Mock: Setting RF frequency to {request.frequency / 1e6} MHz")
        print(f"Mock: Setting RF gain to {request.gain} dB on device {request.device_id}")
        print("Mock: Frequency and Gain set successfully.")

        return rfcontrol_pb2.RFResponse(
            success=True,
            status=f"Mock: RF settings applied successfully on device {request.device_id}"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rfcontrol_pb2_grpc.add_RFServiceServicer_to_server(RFServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\n Server stopped manually. Goodbye!")

if __name__ == "__main__":
    serve()
