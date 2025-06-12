# uhd_mock.py
import logging

logging.basicConfig(level=logging.INFO)

class MockUSRP:
    def __init__(self, device_id):
        self.device_id = device_id
        logging.info(f"[UHD] Initialized Mock USRP device with ID: {device_id}")

    def set_center_freq(self, freq):
        logging.info(f"[UHD] Device {self.device_id}: Set center frequency to {freq / 1e6} MHz")

    def set_gain(self, gain):
        logging.info(f"[UHD] Device {self.device_id}: Set gain to {gain} dB")

    def get_device_info(self):
        return {
            "name": "Mock USRP",
            "serial": self.device_id,
            "fw_version": "1.0.0"
        }
