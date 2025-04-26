import bluetooth
from micropython import const
from ubluetooth import BLE, UUID

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

class BLEManager:
    def __init__(self, ble_name="PicoW-BLE-OLED", callback=None):
        self.ble = bluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self._irq)
        self.callback = callback

        _UART_SERVICE_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
        _UART_RX_UUID = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

        self._UART_SERVICE = (
            _UART_SERVICE_UUID,
            (
                (_UART_RX_UUID, bluetooth.FLAG_WRITE | bluetooth.FLAG_WRITE_NO_RESPONSE,),
            ),
        )

        ((self._rx_handle,),) = self.ble.gatts_register_services((self._UART_SERVICE,))
        self._payload = self._advertising_payload(ble_name)
        self._advertise()

    def _advertising_payload(self, name):
        name_bytes = bytes(name, 'utf-8')
        payload = bytes((len(name_bytes) + 1, 0x09)) + name_bytes
        return payload

    def _advertise(self, interval_us=500000):
        self.ble.gap_advertise(interval_us, adv_data=self._payload)

    def _irq(self, event, data):
        if event == _IRQ_CENTRAL_CONNECT:
            print("BLE Device Connected")
        elif event == _IRQ_CENTRAL_DISCONNECT:
            print("BLE Device Disconnected")
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            conn_handle, attr_handle = data
            if attr_handle == self._rx_handle:
                message = self.ble.gatts_read(self._rx_handle)
                text = message.decode().strip()
                print("Received over BLE:", text)
                if self.callback:
                    self.callback(text)
