from bokeh.plotting import figure, output_file, show
import xml.etree.ElementTree as ET
import numpy as np
import pandas
from _datetime import datetime
from dateutil.parser import parse


def load_data(filename='datalog.xml'):
    # Parse the XML
    xmltree = ET.parse(filename)
    # Output data
    data = {'currentdatetime': [],
            'humidity': [],
            'pressure': [],
            'temperature': [],
            'temperature_humidity': [],
            'temperature_pressure': []}

    # Loop through all the nodes
    for centry in xmltree.findall('.//sensordata'):
        # Append to the list
        for k,v in centry.attrib.items():
            if k != "currentdatetime":
                data[k].append(float(v))
            else:
                data[k].append(parse(v))

    # Create the data frame
    df = pandas.DataFrame(data=data)

    print(df)

    return df


def plotdata(df):
    output_file('plot_data.html')
    p = figure(tools='pan,box_zoom,reset,save',title='Sense Hat Data', x_axis_type='datetime')

    p.line(df['currentdatetime'], df['temperature'],legend='Temperature [C]', line_color='red')
    p.line(df['currentdatetime'], df['humidity'], legend='Humidity [%]', line_color='green')
    # p.line(df['currentdatetime'], df['pressure'], legend='Pressure [mbar]')

    show(p)



if __name__ == "__main__":
    df=load_data()

    plotdata(df)
