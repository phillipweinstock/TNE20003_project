Step 1
run 
pip -r requirements.txt
or 
python3 -m pip install -r requirements.txt
Step 2
then install the protobuffer compiler and runtime bindings for your system.
Linux = sudo apt install protobuf-compiler
Windows = Have fun!
Step 3
Generate Protobuffer classs
protoc --proto_path='protos' --python_out=. data.proto
Step 4
Start PLC system 
sudo python3 Client_controller.py
Step 5
Start as many generators as your heart desired_state in different terminals
python3 Generator.py
Step 6
Play with power demand with - + hotkeys


Resources used in making this project
R# = resource.no
R1 = https://www.datascienceblog.net/post/programming/essential-protobuf-guide-python/ info + code
R2 = https://cryptography.io/en/latest/fernet/

Notes system works well with small deviations, takes much longer to reach a steady state when the deviations are larger