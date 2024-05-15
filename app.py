from flask import Flask, jsonify, render_template
from models import db, Meter, MeterData

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meters.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/meters/')
    def get_meters():
        meters = Meter.query.all()
        meters_list =[]
        for meter in meters:
            meters_list.append({'id': meter.id, 'label': meter.label})
        return render_template('meters.html', meters=meters_list)

    @app.route('/meters/<int:meter_id>')
    def get_meter_data(meter_id):
        meter_data = MeterData.query.filter_by(meter_id=meter_id).order_by(MeterData.timestamp).all()
        meter_data_list = [{'id': data.id, 'meter_id': data.meter_id, 'timestamp': data.timestamp, 'value': data.value} for data in meter_data]
        return jsonify(meter_data_list)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
