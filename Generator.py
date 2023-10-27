# Generator slave client
import sys
import random
import time
import enviro as env
import paho.mqtt.client as mqtt  # our Client implementation
import data_pb2 as proto  # import our protobuf definition
import shortuuid as idgen

client_id = idgen.random(10)
client = mqtt.Client(client_id)
global system_state
system_state = proto.Stats()
# global system_settings
system_settings = proto.Settings()


def on_connect(client, userdata, flags, rc):
    print(
        "Connected to Broker \n client_id: %s with response code: %s " % (client_id, rc)
    )
    client.subscribe(env.private_data.format(client_id))# subscribes to two ~~~private~~~ topics
    client.subscribe(env.private_settings.format(client_id))


def settings_handle(client, userdata, message):
    print("Recieved new configuration")
    temp_settings = proto.Settings()
    temp_settings.ParseFromString(env.black_box.decrypt(message.payload))
    print(
        f"New settings rate: {temp_settings.flow_rate} \n State: {temp_settings.desired_state}"
    )
    apply_settings(temp_settings.flow_rate, temp_settings.desired_state)


def publish_handle(client, userdata, message):
    temp_state = proto.Stats()
    temp_state.ParseFromString(env.black_box.decrypt(message.payload))
    print(f"Published Data\nFlow_rate: {temp_state.flow_rate}")
    print(f"Power Generation in Kwh: {temp_state.power_generation}")


def simulate_state():
    power_generation = 0
    system_error = proto.ERROR_NONE
    # Basic semi-implemented state machine
    match system_state.op_state:
        case proto.OP_STANDBY:
            power_generation = 0

            if system_state.flow_rate > 0:
                system_state.op_state = proto.OP_RUNNING
                system_state.error_state = proto.ERROR_NONE
            else:
                system_state.error_state = proto.ERROR_RECOVERABLE
                system_state.op_state = proto.OP_READY
        case proto.OP_NOTREADY:  # not implemented
            power_generation = 0
            system_state.error_state = proto.ERROR_MAINTENENCE
        case proto.OP_READY:
            if system_state.flow_rate > 0:
                system_state.op_state = proto.OP_RUNNING
            else:
                system_state.flow_rate = 0
                system_state.error_state = proto.ERROR_RECOVERABLE
            power_generation = 0
        case proto.OP_RUNNING:
            if system_state.flow_rate >= 100:
                system_state.flow_rate = 100
            power_generation = (
                random.normalvariate(0.8, 0.01) * system_state.flow_rate
            )  # simulate state base rate 80% efficiency +- %5 deviation
            if system_state.flow_rate <= 0:
                system_state.op_state = proto.OP_STANDBY
                system_state.flow_rate = 0

    system_state.power_generation = power_generation
    # TODO implement more robust error states


def publish_state():
    #publish data to both our public and private topics. encrypt before sending
    #this could be replaced with asymmetric encryption later on
    client.publish(env.private_data.format(client_id), env.black_box.encrypt(system_state.SerializeToString()))
    client.publish(env.public_data.format(client_id), env.black_box.encrypt(system_state.SerializeToString()))


client.on_connect = on_connect
# Add our call backs for our private topics
client.message_callback_add(env.private_settings.format(client_id), settings_handle)
client.message_callback_add(env.private_data.format(client_id), publish_handle) 
client.username_pw_set(env.usr_psd[0], env.usr_psd[1])
client.connect(env.host)


def apply_settings(flowrate=50, op_state=proto.OP_RUNNING):  # default settings
    system_state.flow_rate = system_settings.flow_rate = flowrate  # lazy crappy code
    system_state.op_state = system_settings.desired_state = op_state


apply_settings()
client.loop_start()
while True:
    # System simulation main loop
    simulate_state()
    time.sleep(2)
    publish_state()
