from sense_hat import SenseHat
import xml.etree.ElementTree as etree
import datetime
import os


class SenseData:
    def __init__(self,temp=0,pres=0,humid=0,temp_pres=0,temp_humid=0):
        # Store the results.
        self.temperature = temp
        self.pressure = pres
        self.humidity = humid
        self.temperature_pressure = temp_pres
        self.temperature_humidity = temp_humid
        # Date and time stamp.
        self.currentdatetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def toxml(self):
        # Return an XML Element containing all the information.
        xmlelem = etree.Element('sensordata')
        # Set every class variable.
        for key, value in vars(self).items():
            # Serialize as an XML attribute.
            xmlelem.set(key,str(value))

        return xmlelem

    def display(self):
        senhat = SenseHat()
        senhat.show_message("T={0:.1f} P={1:d} H={2:d}".format(self.temperature, int(self.pressure), int(self.humidity)))

    @staticmethod
    def currentdata():
        # Create the sense-hat object and retrieve all the data.
        senhat = SenseHat()
        t = senhat.get_temperature()
        p = senhat.get_pressure()
        h = senhat.get_humidity()
        tp = senhat.get_temperature_from_pressure()
        th = senhat.get_temperature_from_humidity()

        return SenseData(t,p,h,tp,th)


def logdata():
    # Get the current state.
    curstate = SenseData.currentdata()
    # Open the current XML file.
    logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'datalog.xml')
    xmlroot = None
    try:
        xmlroot = etree.parse(logfile)
    except:
        # Do nothing.
        xmlroot = etree.ElementTree(etree.Element('data'))


    # Write back out.
    xmlroot.getroot().append(curstate.toxml())
    xmlroot.write(logfile)
    
    # Display temperature.
    curstate.display()

if __name__ == "__main__":
    # Call the master temperature logger.
    logdata()
