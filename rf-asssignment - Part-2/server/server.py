# server.py
from concurrent import futures
import grpc
import rfcontrol_pb2
import rfcontrol_pb2_grpc
from uhd_mock import MockUSRP  # Import the UHD mock

class RFServiceServicer(rfcontrol_pb2_grpc.RFServiceServicer):
    def SetRFSettings(self, request, context):
        print("\n[Server] RF Settings Received")
        print(f"Frequency: {request.frequency} Hz")
        print(f"Gain: {request.gain} dB")
        print(f"Device ID: {request.device_id}")

        # Initialize mock UHD device
        usrp = MockUSRP(request.device_id)

        # Simulate hardware actions
        usrp.set_center_freq(request.frequency)
        usrp.set_gain(request.gain)
        info = usrp.get_device_info()

        print(f"[Server] Device Info: {info}")

        return rfcontrol_pb2.RFResponse(
            success=True,
            status=f"Mock: RF settings applied successfully on {info['name']} (ID: {info['serial']})"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rfcontrol_pb2_grpc.add_RFServiceServicer_to_server(RFServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("[Server] gRPC server started on port 50051")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\n[Server] Stopped manually.")

if __name__ == "__main__":
    serve()
