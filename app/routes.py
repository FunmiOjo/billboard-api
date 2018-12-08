from app import app
import billboard
from flask import jsonify, request

@app.route('/rb')
def rb():
  date = request.args.get('date')
  position = int(request.args.get('position'))
  chart = billboard.ChartData('r-b-hip-hop-songs', date)
  song = chart[position].__dict__
  return jsonify({'song': song})
