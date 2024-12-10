import os
import time

usb_devices_path = "/sys/bus/usb/devices/"

def get_tty_path(device_path):
    tty_submodule_path = os.path.join(device_path, "tty")
    if os.path.isdir(tty_submodule_path):
        for tty_name in os.listdir(tty_submodule_path):
            tty_path = "/dev/" + tty_name
            if os.path.exists(tty_path):
                return tty_path
    return None


def load_usb_devices(all=False):
    devices = {}
    for device in os.listdir(usb_devices_path):
        device_path = os.path.join(usb_devices_path, device)
        if os.path.isdir(device_path):
            tty_path = get_tty_path(device_path)
            if tty_path is not None:
                devices[device] = tty_path
            elif all:
                devices[device] = "not a tty"
    return devices


def monitor_usb_devices():
    previous_devices = {}

    while True:
        # Get fresh list of devices
        current_devices = load_usb_devices(all=False)

        # Compare states and detect changes
        changed_devices = set()
        for device, current_tty_path in current_devices.items():
            previous_tty_path = previous_devices.get(device, {})
            if previous_tty_path != current_tty_path:
                changed_devices.add(device)

        # Detect removed devices
        for device in previous_devices.keys():
            if not (device in current_devices.keys()):
                changed_devices.add(device)

        # Print changed devices
        for device in changed_devices:
            tty_path = current_devices.get(device, None)
            if tty_path == None:
                print(f"USB Port :: {device} :: Unplugged")
            else:
                print(f"USB Port :: {device} :: {tty_path}")

        # Update the previous state for the next iteration
        previous_devices = current_devices

        # Wait before the next check
        time.sleep(0.3)

if __name__ == "__main__":
    monitor_usb_devices()
