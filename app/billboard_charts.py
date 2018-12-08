import billboard
chart = billboard.ChartData('hot-100')
rb_chart = billboard.ChartData('r-b-hip-hop-songs', '1969-11-27')
song = chart[0]
rb_song = rb_chart[25]
print(song, rb_song, type(song.__dict__))