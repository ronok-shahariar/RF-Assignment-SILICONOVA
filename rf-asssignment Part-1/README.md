# RF Control gRPC Client-Server (Python)

## Requirements
```bash
pip install grpcio grpcio-tools
```

## Compile the .proto file
```bash
python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/rfcontrol.proto
```

## Run the Server
```bash
python server/server.py
```

## Run the Client (in a new terminal)
```bash
python client/client.py
```

## Run with Docker
```bash
docker build -t rf-server ./server
docker run -p 50051:50051 rf-server
```

## References

1. https://www.youtube.com/watch?v=gnchfOojMk4
2. https://www.youtube.com/watch?v=AMNWLz_f6qM&t=590s
3. https://www.youtube.com/watch?v=WB37L7PjI5k&t=78s
4. https://www.youtube.com/watch?v=E0CaocyNYKg&t=1612s
5. https://www.youtube.com/watch?v=hVrwuMnCtok&t=179s
6. https://www.youtube.com/watch?v=1yjAUY1ifUg
7. https://www.youtube.com/watch?v=fbcxm7f-Tj0&t=971s
8. https://grpc.io/docs/languages/python/quickstart/
9. https://files.ettus.com/manual/page_python.html
10. ChatGPT