import usb.core
import usb.util
import sys

dev = usb.core.find(idVendor=0x4d9, idProduct=0xa070)

if dev is None: raise ValueError("Device not found")

usb.util.claim_interface(dev, 1)
dev.set_interface_altsetting(interface=2, alternate_setting=0)

for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
    for intf in cfg:
        sys.stdout.write('\t' + \
                         str(intf.bInterfaceNumber) + \
                         ',' + \
                         str(intf.bAlternateSetting) + \
                         '\n')
        for ep in intf:
            sys.stdout.write('\t\t' + \
                             str(ep.bEndpointAddress) + \
                             '\n')

data = [0x07, 0x09, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]

#dev.ctrl_transfer(bmRequestType=0x22, bRequest=0x9, wValue=0x307, wIndex=0x1, data_or_wLength=data, timeout=1000)
dev.write(endpoint=13, data=data)

usb.util.release_interface(dev, 1)