# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetConfig.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fGetConfig.proto\"/\n\x0fGetConfigResDTO\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\r\"\xc9\n\n\x0fGetConfigReqDTO\x12\x16\n\x0erequest_offset\x18\x01 \x01(\x05\x12\x14\n\x0crequest_time\x18\x02 \x01(\r\x12\x15\n\rlock_password\x18\x03 \x01(\x05\x12\x11\n\tlock_time\x18\x04 \x01(\x05\x12\x1b\n\x13limit_power_mypower\x18\x05 \x01(\x05\x12\x1c\n\x14zero_export_433_addr\x18\x06 \x01(\x05\x12\x1a\n\x12zero_export_enable\x18\x07 \x01(\x05\x12\x16\n\x0enetmode_select\x18\x08 \x01(\x05\x12\x16\n\x0e\x63hannel_select\x18\t \x01(\x05\x12\x18\n\x10server_send_time\x18\n \x01(\x05\x12\x11\n\twifi_rssi\x18\x0b \x01(\x05\x12\x12\n\nserverport\x18\x0c \x01(\x05\x12\x0f\n\x07\x61pn_set\x18\r \x01(\t\x12\x12\n\nmeter_kind\x18\x0e \x01(\t\x12\x17\n\x0fmeter_interface\x18\x0f \x01(\t\x12\x11\n\twifi_ssid\x18\x10 \x01(\t\x12\x15\n\rwifi_password\x18\x11 \x01(\t\x12\x1a\n\x12server_domain_name\x18\x12 \x01(\t\x12\x10\n\x08inv_type\x18\x13 \x01(\x05\x12\x0e\n\x06\x64tu_sn\x18\x14 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_model\x18\x15 \x01(\x05\x12\r\n\x05mac_0\x18\x16 \x01(\x05\x12\r\n\x05mac_1\x18\x17 \x01(\x05\x12\r\n\x05mac_2\x18\x18 \x01(\x05\x12\r\n\x05mac_3\x18\x19 \x01(\x05\x12\x13\n\x0b\x64hcp_switch\x18\x1a \x01(\x05\x12\x11\n\tip_addr_0\x18\x1b \x01(\x05\x12\x11\n\tip_addr_1\x18\x1c \x01(\x05\x12\x11\n\tip_addr_2\x18\x1d \x01(\x05\x12\x11\n\tip_addr_3\x18\x1e \x01(\x05\x12\x15\n\rsubnet_mask_0\x18\x1f \x01(\x05\x12\x15\n\rsubnet_mask_1\x18  \x01(\x05\x12\x15\n\rsubnet_mask_2\x18! \x01(\x05\x12\x15\n\rsubnet_mask_3\x18\" \x01(\x05\x12\x19\n\x11\x64\x65\x66\x61ult_gateway_0\x18# \x01(\x05\x12\x19\n\x11\x64\x65\x66\x61ult_gateway_1\x18$ \x01(\x05\x12\x19\n\x11\x64\x65\x66\x61ult_gateway_2\x18% \x01(\x05\x12\x19\n\x11\x64\x65\x66\x61ult_gateway_3\x18& \x01(\x05\x12\x0e\n\x06ka_nub\x18\' \x01(\t\x12\x10\n\x08\x61pn_name\x18( \x01(\t\x12\x14\n\x0c\x61pn_password\x18) \x01(\t\x12\x1a\n\x12sub1g_sweep_switch\x18* \x01(\x05\x12\x1a\n\x12sub1g_work_channel\x18+ \x01(\x05\x12\x13\n\x0b\x63\x61\x62le_dns_0\x18, \x01(\x05\x12\x13\n\x0b\x63\x61\x62le_dns_1\x18- \x01(\x05\x12\x13\n\x0b\x63\x61\x62le_dns_2\x18. \x01(\x05\x12\x13\n\x0b\x63\x61\x62le_dns_3\x18/ \x01(\x05\x12\x16\n\x0ewifi_ip_addr_0\x18\x30 \x01(\x05\x12\x16\n\x0ewifi_ip_addr_1\x18\x31 \x01(\x05\x12\x16\n\x0ewifi_ip_addr_2\x18\x32 \x01(\x05\x12\x16\n\x0ewifi_ip_addr_3\x18\x33 \x01(\x05\x12\r\n\x05mac_4\x18\x34 \x01(\x05\x12\r\n\x05mac_5\x18\x35 \x01(\x05\x12\x12\n\nwifi_mac_0\x18\x36 \x01(\x05\x12\x12\n\nwifi_mac_1\x18\x37 \x01(\x05\x12\x12\n\nwifi_mac_2\x18\x38 \x01(\x05\x12\x12\n\nwifi_mac_3\x18\x39 \x01(\x05\x12\x12\n\nwifi_mac_4\x18: \x01(\x05\x12\x12\n\nwifi_mac_5\x18; \x01(\x05\x12\x11\n\tgprs_imei\x18< \x01(\t\x12\x13\n\x0b\x64tu_ap_ssid\x18= \x01(\t\x12\x13\n\x0b\x64tu_ap_pass\x18> \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetConfig_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETCONFIGRESDTO']._serialized_start=19
  _globals['_GETCONFIGRESDTO']._serialized_end=66
  _globals['_GETCONFIGREQDTO']._serialized_start=69
  _globals['_GETCONFIGREQDTO']._serialized_end=1422
# @@protoc_insertion_point(module_scope)
