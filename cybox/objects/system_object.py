# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.system_object as system_binding
from cybox.common import PlatformSpecification, ObjectProperties, String, UnsignedLong, Date, DateTime, Duration, EnvironmentVariableList
from cybox.common.properties import Time
from cybox.objects.address_object import Address


class DHCPServerList(entities.EntityList):
    _binding_class = system_binding.DHCPServerListType
    _binding_var = "DHCP_Server_Address"
    _contained_type = Address
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class IPGatewayList(entities.EntityList):
    _binding_class = system_binding.IPGatewayListType
    _binding_var = "IP_Gateway_Address"
    _contained_type = Address
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class IPInfo(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.IPInfoType

    ip_address = fields.TypedField("IP_Address", Address)
    subnet_mask = fields.TypedField("Subnet_Mask", Address)


class IPInfoList(entities.EntityList):
    _binding_class = system_binding.IPInfoListType
    _binding_var = "IP_Info_List"
    _contained_type = IPInfo
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class OS(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.OSType

    bitness = fields.TypedField("Bitness", String)
    build_number = fields.TypedField("Build_Number", String)
    environment_variable_list = fields.TypedField("Environment_Variable_List", EnvironmentVariableList)
    install_date = fields.TypedField("Install_Date", Date)
    patch_level = fields.TypedField("Patch_Level", String)
    platform = fields.TypedField("Platform", PlatformSpecification)


class BIOSInfo(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.BIOSInfoType

    bios_date = fields.TypedField("BIOS_Date", Date)
    bios_version = fields.TypedField("BIOS_Version", String)
    bios_manufacturer = fields.TypedField("BIOS_Manufacturer", String)
    bios_release_date = fields.TypedField("BIOS_Release_Date", Date)
    bios_serial_number = fields.TypedField("BIOS_Serial_Number", String)


class NetworkInterface(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.NetworkInterfaceType

    adapter = fields.TypedField("Adapter", String)
    description = fields.TypedField("Description", String)
    dhcp_lease_expires = fields.TypedField("DHCP_Lease_Expires", DateTime)
    dhcp_lease_obtained = fields.TypedField("DHCP_Lease_Obtained", DateTime)
    dhcp_server_list = fields.TypedField("DHCP_Server_List", DHCPServerList)
    ip_gateway_list = fields.TypedField("IP_Gateway_List", IPGatewayList)
    ip_list = fields.TypedField("IP_List", IPInfoList)
    mac = fields.TypedField("MAC", String)


class NetworkInterfaceList(entities.EntityList):
    _binding_class = system_binding.NetworkInterfaceListType
    _binding_var = "Network_Interface"
    _contained_type = NetworkInterface
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class System(ObjectProperties):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _XSI_NS = "SystemObj"
    _XSI_TYPE = "SystemObjectType"
    _binding = system_binding
    _binding_class = system_binding.SystemObjectType

    available_physical_memory = fields.TypedField("Available_Physical_Memory", UnsignedLong)
    bios_info = fields.TypedField("BIOS_Info", BIOSInfo)
    date = fields.TypedField("Date", Date)
    hostname = fields.TypedField("Hostname", String)
    local_time = fields.TypedField("Local_Time", Time)
    network_interface_list = fields.TypedField("Network_Interface_List", NetworkInterfaceList)
    os = fields.TypedField("OS", OS)
    processor = fields.TypedField("Processor", String)
    # TODO
    # processor_architecture = fields.TypedField("Processor_Architecture", ProcessorArch)
    system_time = fields.TypedField("System_Time", Time)
    timezone_dst = fields.TypedField("Timezone_DST", String)
    timezone_standard = fields.TypedField("Timezone_Standard", String)
    total_physical_memory = fields.TypedField("Total_Physical_Memory", UnsignedLong)
    uptime = fields.TypedField("Uptime", Duration)
    username = fields.TypedField("Username", String)
