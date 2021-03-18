import pyshark

display_filter = "udp.stream eq 6"
pcap = pyshark.FileCapture('capture.pcap', display_filter=display_filter)
# pcap = pyshark.FileCapture(
#     'shark_on_wire_1/capture.pcap', display_filter=display_filter)

flag = ""
for packet in pcap:
    flag += chr(int(packet.data.data, 16))

print(flag)
