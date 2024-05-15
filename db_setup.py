from app import create_app
from models import db, Meter, MeterData

app = create_app()
app.app_context().push()

db.create_all()

# Adding some fake meter data
meter1 = Meter(label='Meter 1')
meter2 = Meter(label='Meter 2')

db.session.add(meter1)
db.session.add(meter2)
db.session.commit()

meter_data1 = MeterData(meter_id=meter1.id, value=100)
meter_data2 = MeterData(meter_id=meter1.id, value=150)
meter_data3 = MeterData(meter_id=meter2.id, value=200)

db.session.add(meter_data1)
db.session.add(meter_data2)
db.session.add(meter_data3)
db.session.commit()
