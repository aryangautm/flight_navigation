import json

from channels.generic.websocket import AsyncWebsocketConsumer


class FlightHealthConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        health_metrics = process_sensor_data(data)

        if (
            health_metrics["engine_status"] == "alert"
            or health_metrics["fuel_level"] == "low"
        ):
            alert = {"type": "alert", "message": "Flight health alert detected!"}
            await self.send(text_data=json.dumps(alert))

        await self.send(text_data=json.dumps(health_metrics))


def process_sensor_data(data):
    # Simulate the different sensor data inputs
    engine_temp = data.get("engine_temp", 0)
    fuel_level = data.get("fuel_level", 0)
    altitude = data.get("altitude", 0)
    pressure = data.get("pressure", 0)
    vibration_level = data.get("vibration_level", 0)
    hydraulic_pressure = data.get("hydraulic_pressure", 0)
    battery_voltage = data.get("battery_voltage", 0)

    # Process the data to extract health metrics
    metrics = {
        "engine_status": "normal" if engine_temp < 200 else "alert",
        "fuel_level_status": "sufficient" if fuel_level > 20 else "low",
        "altitude_status": "normal" if 0 < altitude < 40000 else "alert",
        "pressure_status": "normal" if 950 <= pressure <= 1050 else "alert",
        "vibration_status": "normal" if vibration_level < 5 else "alert",
        "hydraulic_pressure_status": "normal"
        if 2500 <= hydraulic_pressure <= 3500
        else "alert",
        "battery_status": "normal" if battery_voltage >= 24 else "low",
    }

    return metrics
