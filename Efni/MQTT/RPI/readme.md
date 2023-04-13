### Kóði

1. Client (RPi) tenging við MQTT Broker (test.mosquitto)
2. Publisher (RPi) telemetry (birtugildi) með JSON sniðmáti.
3. Subscriber (fartölva) server kóði og birtir gildin.
4. Publisher (fartölva) server kóði með commands með JSON snimáti til Broker.
5. Subscriber (RPi) er actuator, kveikir á LED við ákveðin skilyrði.
