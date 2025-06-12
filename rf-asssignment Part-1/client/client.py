import grpc
import rfcontrol_pb2
import rfcontrol_pb2_grpc

def run():
    try:
        # Connect to server
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = rfcontrol_pb2_grpc.RFServiceStub(channel)

            # User input
            frequency = float(input("Enter frequency (Hz): "))
            gain = float(input("Enter gain (dB): "))
            device_id = input("Enter device ID: ")

            # Create message
            config = rfcontrol_pb2.RFConfig(
                frequency=frequency,
                gain=gain,
                device_id=device_id
            )

            # Call RPC
            response = stub.SetRFSettings(config)

            # Output response from server
            print("\n Server Response:")
            print(f"Success: {response.success}")
            print(f"Status: {response.status}")

    except grpc.RpcError as e:
        # Simulate a failed response when server is not available
        print("\n Error:")
        print("Success: False")
        if e.code() == grpc.StatusCode.UNAVAILABLE:
            print("Status: Could not connect to the server. Make sure it's running on port 50051.")
        else:
            print(f"Status: gRPC Error - {e.code().name}: {e.details()}")

if __name__ == "__main__":
    run()
