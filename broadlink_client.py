"""
    Basic client to send IR signals using a Broadlink RM4 Pro device
"""

import broadlink
import base64

class BroadlinkClient:
    def __init__(self):
        self.device = None
        self.connect()

    def connect(self):
        print("Connecting to Broadlink RM4 Pro...")
        devices = broadlink.discover(timeout=3)
        
        if not devices:
            print("❌ No Broadlink device found!")
            return
        
        self.device = devices[0]
        if not self.device.auth():
            print("❌ Authentication failed!")
            self.device = None
            return
        
        print(f"✅ Connected to {self.device.host[0]}")
        self.device = self.device

    def send_ir_signal(self, b64_signal):
        if not self.device:
            print("❌ No connected device to send signal!")
            return
        
        self.device.send_data(b64_signal)