#Response client
import sys
import os
import random
import time
import paho.mqtt.client as mqtt #our Client implementation
import data_pb2 as proto #import our protobuf definition
import shortuuid as idgen
import keyboard
import threading
def cls_helper():
    match os.name:
        case 'posix':
            os.system('clear')
        case _:
            os.system('cls')
            
client_id = idgen.uuid("Generator_Controller")
client = mqtt.Client(client_id)
system_state = proto.Stats()
global system_settings
system_settings = proto.Settings()
setting_pub_msg = ''
def set_comm_msg(value):
    global setting_pub_msg
    setting_pub_msg = value
global satisfaction #super crappy oh well
satisfaction = 0
def calc_satisfaction():
   global satisfaction 
   sum = 0
   for data in output_dict.values():
       sum +=  float(data[0])
       system_total[1] = sum
       satisfaction = (100*(system_total[1]/system_total[0]))
   
global system_total
system_total = [80,0] #This is a user setting setting default to 80kwh second is current total
# Our power plant cannot output more than a certain amount so we need to keep track of how
# much each generator is outputting and temper them up or down
output_dict ={} #this will hold generator | output pairings

def print_output():#Prints our output in a human readable form
    cls_helper()
    print("Powerplant Status panel press - or + in order to change desired output\n")
    for generator, data in output_dict.items():
        print("Generator ID: {: >10} Output: {: >5.2f}Kwh State: {: >10}  Error: {: >15}  Flow Rate: {: >5.2f}%".format(generator,data[0],data[1],data[2],data[3]))
    
    print('\nCurrent system total: {: >2.2f}Kwh Desired output: {: 2.2f}Kwh  Satisfaction: {: >2.2f} %'.format(system_total[1],system_total[0],satisfaction))#
    print('\nLast command issued\n {}'.format(setting_pub_msg))
def on_connect(client,userdata,flags,rc):
    print("Connected to Broker \n client_id: %s with response code: %s " %(client_id,rc))
    calc_satisfaction()
    client.subscribe(f'102101219/+/data')

def settings_handle(client,userdata,message):
    print(f'Recieved new configurations: {message.payload.decode()} ')


def publish_settings(target):
    client.publish(f'102101219/{target}/settings',system_settings.SerializeToString())
def calc_adjustment():
    threading.Timer(3,calc_adjustment).start()
    update_generator = 0
    if len(output_dict) < 1:
        return
    
    calc_satisfaction()
    target = 0
    [low_flow, high_flow] = min(output_dict.values(), key=lambda sub: sub[3]), max(output_dict.values(), key=lambda sub: sub[3])
    [target_low, target_high] = [key for key, val in output_dict.items() if val == low_flow][0] , [key for key, val in output_dict.items() if val == high_flow][0]

    if(satisfaction <= 95):
        
        target  = target_low
        system_settings.flow_rate = output_dict[target][3] + 1 + 2*(satisfaction/100)
        
    if(satisfaction >= 105 ):
        target  = target_high
        system_settings.flow_rate = output_dict[target][3] -1 -2*(satisfaction/100)

    if((satisfaction < 95 or satisfaction > 105) and  satisfaction !=0):    
        system_settings.desired_state = proto.OP_STANDBY
        previous_rate = output_dict[target][3]
        if(system_settings.flow_rate < 0):
            system_settings.flow_rate = 0#so we don't have generators turn into motors lmao
        publish_settings(target)
        set_comm_msg('Generator: {} Adjusted from {: >2.2f}% to {: >2.2f}%'.format(target,previous_rate,system_settings.flow_rate))   

        
            
        
        
    
def process_stats(client,userdata,message):
    temp_stats = proto.Stats()
    temp_stats.ParseFromString(message.payload)
    op_state_str = ['Not Ready','Ready','Stand By','Running'][temp_stats.op_state]
    error_state_str = ['No Error','Recoverable','Fatal','Maintenence'][temp_stats.error_state]
    slave_client = message.topic.split("/")[1]
    #if((temp_stats.power_generation >= 0) and temp_stats.flow_rate >= 0):
    if(temp_stats.op_state == proto.OP_RUNNING and temp_stats.power_generation == 0):
     temp_stats.power_generation = output_dict[slave_client][0]#this is to avoid zeros after updates :)

    output_dict[slave_client] = (temp_stats.power_generation,op_state_str,error_state_str,temp_stats.flow_rate)
    #else:
    #    None
    calc_satisfaction()
    #calc_adjustment()
    print_output()


    
client.on_connect = on_connect
client.message_callback_add('102101219/+/data',process_stats)
client.username_pw_set("102101219","102101219")
client.connect("rule28.i4t.swin.edu.au")
#default settings
def default_settings():
    system_settings.flow_rate = 50
    system_settings.desired_state = proto.OP_RUNNING
    
default_settings()
calc_adjustment()
client.loop_start()
#client.loop_forever()
while True:
    
    match keyboard.read_key():
        case '+':
            system_total[0] += 0.5
        case '-':
            system_total[0] += -0.5
    if(system_total[0] <= 0):
        system_total[0]=0.1 # lets pretend we have a standby total current, lazy way to avoid 1/0 error
