## Issue: Recent Kernel and Library Compatibility Issues

### Cause:
Recent kernel updates on the Raspberry Pi have altered how GPIO pins are managed. This has led to compatibility issues with the `RPi.GPIO` library, specifically causing errors with functions like `GPIO.add_event_detect()`.

### Solution: Switch to `rpi-lgpio` Library
The `rpi-lgpio` library is designed to work seamlessly with newer kernel versions and provides a similar interface to `RPi.GPIO`.

#### Steps to Transition:
1. **Uninstall `RPi.GPIO`**:
```bash
   sudo apt-get remove python3-rpi.gpio
```

2. **Install `rpi-lgpio`**:

```bash
sudo apt-get update
sudo apt-get install python3-rpi-lgpio
```

3. **Modify Your Code: Replace the import statement in your Python script**:

```Python
import lgpio as GPIO
```

The API remains largely consistent with RPi.GPIO, so minimal changes to your code should be necessary.

Reference:
[GitHub Issue: Raspberry Pi GPIO Library Issues](https://github.com/raspberrypi/linux/issues/6037)