#!/usr/bin/env python3
"""
PixMob Red Flash
Simple script to flash red via IR signal.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from broadlink_client import BroadlinkClient
from ircodes import red

# Note: Run this script from the project root using:
#   python -m examples.flash_red


def main():
    device = BroadlinkClient()
    device.send_ir_signal(red.get_ir_signal())
    print("✅ Done! Your PixMob should have flashed red 5 times.")

if __name__ == "__main__":
    main()
