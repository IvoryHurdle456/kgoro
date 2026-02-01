from enum import Enum


class Vendor(str, Enum):
    cx3 = "3cx"
    mikrotik = "mikrotik"
    fortinet = "fortinet"
    cisco = "cisco"
    grandstream = "grandstream"
    yealink = "yealink"
    yeastar = "yeastar"
    fanvil = "fanvil"
    flyingvoice = "flyingvoice"
    hp_aruba = "hp_aruba"
    windows = "windows"
    ubuntu = "ubuntu"
    rhel = "rhel"
    suse = "suse"
    centos = "centos"
    unix = "unix"


class DeviceType(str, Enum):
    router = "router"
    switch = "switch"
    firewall = "firewall"
    ap = "ap"
    pbx = "pbx"
    ip_phone = "ip_phone"
    printer = "printer"
    server = "server"
    workstation = "workstation"
    vm_host = "vm_host"
