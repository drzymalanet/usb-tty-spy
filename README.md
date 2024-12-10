# USB /dev/tty monitor

This script prints out changes in the USB TTY submodule and the /dev/tty device assigned to a given USB port.

## Example

Here is an example of running the script and attaching different USB to serial converters to a PC:

```text
USB Port :: 3-1:1.0 :: /dev/ttyACM0
USB Port :: 2-1:1.0 :: /dev/ttyACM1
USB Port :: 2-1:1.0 :: Unplugged
USB Port :: 2-1:1.0 :: /dev/ttyACM1
USB Port :: 2-1:1.0 :: Unplugged
USB Port :: 3-1:1.0 :: Unplugged
USB Port :: 3-1:1.0 :: /dev/ttyACM0
USB Port :: 3-1:1.0 :: Unplugged
USB Port :: 2-1:1.0 :: /dev/ttyACM0
USB Port :: 3-1:1.0 :: /dev/ttyACM1
USB Port :: 3-1:1.0 :: Unplugged
USB Port :: 3-1:1.0 :: /dev/ttyACM1
USB Port :: 1-4:1.0 :: /dev/ttyACM2
USB Port :: 1-4:1.0 :: Unplugged
USB Port :: 1-3:1.0 :: /dev/ttyACM2
USB Port :: 1-3:1.0 :: Unplugged
USB Port :: 3-1:1.0 :: Unplugged
USB Port :: 2-1:1.0 :: Unplugged
```

Explanation:
- `2-1:1.0` - USB Bus 2 Port 1
- `1-3:1.0` - USB Bus 1 Port 3
- `/dev/ttyACM0` - Device path to the TTY
