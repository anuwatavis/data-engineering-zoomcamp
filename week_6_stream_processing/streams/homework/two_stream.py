from datetime import timedelta
import faust
from taxi_rides import TaxiRide


app = faust.App('datatalksclub.stream.v5', broker='kafka://localhost:9092')

topic_1 = app.topic('datatalkclub.yellow_taxi_ride_01.json',
                    value_type=TaxiRide)

topic_2 = app.topic('datatalkclub.yellow_taxi_ride_02.json',
                    value_type=TaxiRide)

vendor_rides = app.Table('vendor_rides_windowed', default=int).tumbling(
    timedelta(minutes=60),
    expires=timedelta(hours=12),
)


@app.agent(topic_1)
async def process(stream):
    async for event in stream.group_by(TaxiRide.vendorId):
        vendor_rides[event.vendorId] += 1


@app.agent(topic_2)
async def process(stream):
    async for event in stream.group_by(TaxiRide.vendorId):
        vendor_rides[event.vendorId] += 1


if __name__ == '__main__':
    app.main()
