#!/usr/bin/env python3
"""Example script."""

# Parse Arguments
# Import project path
import argparse
import os
import sys

# Import pyvera

sys.path.insert(1, '../pyvera')
from pyvera import VeraController


def main() -> None:
    """Run main code entrypoint."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

    parser = argparse.ArgumentParser(description="list-devices")
    parser.add_argument(
        "-u", "--url", help="Vera URL, e.g. http://192.168.1.161:3480", required=True
    )
    args = parser.parse_args()

    # Start the controller
    controller = VeraController(args.url)
    controller.start()

    try:
        # Get a list of all the devices on the vera controller
        all_devices = controller.get_devices()

        # Print the devices out
        for device in all_devices:
            print(
                "{} {} ({})".format(
                    type(device).__name__, device.name, device.device_id
                )
            )

        dv = controller.get_device_by_id(39)
        print("device")
        print(dv)
        dv.set_switch_state(1)

    finally:
        # Stop the subscription listening thread so we can quit
        controller.stop()


if __name__ == "__main__":
    main()
