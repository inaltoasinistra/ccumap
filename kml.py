#!/usr/bin/env python2

'''<?xml version="1.0" encoding="UTF-8"?>
 <kml xmlns="http://earth.google.com/kml/2.0">
 <Placemark>
   <description>New York City</description>
   <name>New York City</name>
   <Point>
     <coordinates>40.714172,-74.006393,0</coordinates>
   </Point>
 </Placemark>
 </kml>'''

# placemarks
DOC_SKEL = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
%s
</kml>'''

# description, name, coordinates
PLACEMARK_SKEL = '''<Placemark>
<description>%s</description>
<name>%s</name>
<Point>
<coordinates>%s</coordinates>
</Point>
</Placemark>'''

def create_kml(data):

    # data = [
    #   {'description':'*', 'name':'*', 'Point:coordinates':'<lat>,<lng>,<h>'},
    #   {},
    # ]

    placemarks = []

    for p in data:
        placemarks.append(PLACEMARK_SKEL % (p.get('description',''),
                                            p.get('name',''),
                                            p['Point:coordinates']))

    return DOC_SKEL % '\n'.join(placemarks)


if __name__=="__main__":
    #test!
    
    test = []
    test.append({'description'})
    
    print create_kml(test)
