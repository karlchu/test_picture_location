#!/usr/bin/env python

import json
import subprocess
import sys
from PyGeoTools.geolocation import GeoLocation

file_path = sys.argv[1]
target_latitude = float(sys.argv[2])
target_longitude = float(sys.argv[3])
bound_radius = float(sys.argv[4])

p = subprocess.Popen(["exiftool", "-gpslongitude", "-gpslatitude", "-j", "-c", "%+.6f", file_path], stdout=subprocess.PIPE)
(exiftool_output, err) = p.communicate()

file_info = json.loads(exiftool_output)
if 'GPSLatitude' not in file_info[0]:
    exit(1)

picture_latitude = float(file_info[0]['GPSLatitude'])
picture_longitude = float(file_info[0]['GPSLongitude'])

target_location = GeoLocation.from_degrees(target_latitude, target_longitude)
picture_location = GeoLocation.from_degrees(picture_latitude, picture_longitude)

distance = picture_location.distance_to(target_location)

if distance > bound_radius:
    exit_code = 1
else:
    print(file_path)
    exit_code = 0

exit(exit_code)
