import logging


# logging.basicConfig(level=logging.INFO, filename="lbot.log")


def strip_device_name(device, amount=3):
    # given hostname aa-bb-cc-dd-ee, this returns the last 2 (dd-ee)
    # or 3 (cc-dd-ee) sections.
    #

    # TODO: make this return the last N segments
    # TODO: select the divider, allowing to combine strip_subnet_mask function

    if amount == 3:
        index = device.find('-', device.find('-', device.find('-') + 1) + 1)
    else:
        index = device.find('-', device.find('-') + 1)

    return device[index + 1:]


if __name__ == '__main__':
    print(strip_device_name("aa-bbb-cc-ddd-ee"))

# logging.debug(stuff)
