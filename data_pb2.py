# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='Data_project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndata.proto\x12\x0c\x44\x61ta_project\"\xa6\x01\n\x05Stats\x12\x11\n\tflow_rate\x18\x01 \x01(\x01\x12\x18\n\x10power_generation\x18\x02 \x01(\x01\x12\x31\n\x08op_state\x18\x03 \x01(\x0e\x32\x1f.Data_project.Operational_state\x12.\n\x0b\x65rror_state\x18\x04 \x01(\x0e\x32\x19.Data_project.Error_state\x12\r\n\x05\x65rror\x18\x05 \x01(\t\"U\n\x08Settings\x12\x11\n\tflow_rate\x18\x01 \x01(\x01\x12\x36\n\rdesired_state\x18\x02 \x01(\x0e\x32\x1f.Data_project.Operational_state*\\\n\x0b\x45rror_state\x12\x0e\n\nERROR_NONE\x10\x00\x12\x15\n\x11\x45RROR_RECOVERABLE\x10\x01\x12\x0f\n\x0b\x45RROR_FATAL\x10\x02\x12\x15\n\x11\x45RROR_MAINTENENCE\x10\x03*R\n\x11Operational_state\x12\x0f\n\x0bOP_NOTREADY\x10\x00\x12\x0c\n\x08OP_READY\x10\x01\x12\x0e\n\nOP_STANDBY\x10\x02\x12\x0e\n\nOP_RUNNING\x10\x03\x62\x06proto3'
)

_ERROR_STATE = _descriptor.EnumDescriptor(
  name='Error_state',
  full_name='Data_project.Error_state',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RECOVERABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FATAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MAINTENENCE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=284,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_ERROR_STATE)

Error_state = enum_type_wrapper.EnumTypeWrapper(_ERROR_STATE)
_OPERATIONAL_STATE = _descriptor.EnumDescriptor(
  name='Operational_state',
  full_name='Data_project.Operational_state',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OP_NOTREADY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OP_READY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OP_STANDBY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OP_RUNNING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=378,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONAL_STATE)

Operational_state = enum_type_wrapper.EnumTypeWrapper(_OPERATIONAL_STATE)
ERROR_NONE = 0
ERROR_RECOVERABLE = 1
ERROR_FATAL = 2
ERROR_MAINTENENCE = 3
OP_NOTREADY = 0
OP_READY = 1
OP_STANDBY = 2
OP_RUNNING = 3



_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='Data_project.Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flow_rate', full_name='Data_project.Stats.flow_rate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='power_generation', full_name='Data_project.Stats.power_generation', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='op_state', full_name='Data_project.Stats.op_state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='Data_project.Stats.error_state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='Data_project.Stats.error', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=195,
)


_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='Data_project.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flow_rate', full_name='Data_project.Settings.flow_rate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desired_state', full_name='Data_project.Settings.desired_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=282,
)

_STATS.fields_by_name['op_state'].enum_type = _OPERATIONAL_STATE
_STATS.fields_by_name['error_state'].enum_type = _ERROR_STATE
_SETTINGS.fields_by_name['desired_state'].enum_type = _OPERATIONAL_STATE
DESCRIPTOR.message_types_by_name['Stats'] = _STATS
DESCRIPTOR.message_types_by_name['Settings'] = _SETTINGS
DESCRIPTOR.enum_types_by_name['Error_state'] = _ERROR_STATE
DESCRIPTOR.enum_types_by_name['Operational_state'] = _OPERATIONAL_STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stats = _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
  'DESCRIPTOR' : _STATS,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:Data_project.Stats)
  })
_sym_db.RegisterMessage(Stats)

Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGS,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:Data_project.Settings)
  })
_sym_db.RegisterMessage(Settings)


# @@protoc_insertion_point(module_scope)
