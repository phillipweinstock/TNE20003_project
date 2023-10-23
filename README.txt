Step 1
run pip -r requirements.txt
Step 2
then install the protobuffer compiler and runtime bindings for your system.
Linux = sudo apt install protobuf-compiler
Windows = Have fun!
Step 3
Generate Protobuffer classs
protoc --proto_path='protos' --python_out=. data.proto



Resources used in making this project
R# = resource.no
R1 = https://www.datascienceblog.net/post/programming/essential-protobuf-guide-python/ info + code

