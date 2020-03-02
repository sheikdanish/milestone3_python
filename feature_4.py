# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:26:35 2020

@author: sheikd
"""
# import web browser capabilities
import webbrowser
# import library for plotting.
import matplotlib.pyplot as plt
# import library for working on large, multi-dimensional arrays and matrices.
import numpy as np
# PLEASE RUN THIS COMMAND IN CONSOLE IF GMPLOT NOT INSTALLED:
# pip install gmplot
# import gmplot package
import gmplot

def feature4(data, path_lats, path_long):
    """Feature 4: Fuel Consumption Waste"""
    # Extract data of trip.
    trip = data[data['Trip Time(Since journey start)(s)'] > 0]
    print(trip)

    # Extract data of trip with mileage above 25kmpl.
    nonidle = trip[trip['Kilometers Per Litre(Instant)(kpl)'] > 25]
    print(nonidle)
    # Plot areas of mileage above 25kmpl
    plotmps(data, path_lats, path_long, nonidle)
    # Average Trip Mileage
    trip_avg = data['Kilometers Per Litre(Instant)(kpl)'].mean()
    print('Average Trip Mileage is', trip_avg, 'kmpl')

    # Plot Average Trip Mileage
    plt.plot(trip['Kilometers Per Litre(Instant)(kpl)'], '.')
    plt.title('Trip Kilometers Per Litre(kmpl)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('kmpl', fontdict=None, labelpad=None)
    plt.show()

    # Economy Mileage
    nonidle_avg = nonidle['Kilometers Per Litre(Instant)(kpl)'].mean()
    print('Average Economy Mileage is', nonidle_avg, 'kmpl')

    # Plot Economy Mileage
    plt.plot(nonidle['Kilometers Per Litre(Instant)(kpl)'], '.')
    plt.title('Economy Kilometers Per Litre(kmpl)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('kmpl', fontdict=None, labelpad=None)
    plt.show()

    # Trip Speed Average
    trip_speedavg = trip['Speed (GPS)(km/h)'].mean()
    print('Average Trip Speed is', trip_speedavg, 'kmph')

    # Plot Trip Speed Average
    plt.plot(trip['Speed (GPS)(km/h)'], '.')
    plt.title('Trip Average Speed(kmh)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('kmph', fontdict=None, labelpad=None)
    plt.show()

    # Economy Speed Average
    nonidle_speedavg = nonidle['Speed (GPS)(km/h)'].mean()
    print('Average Economy Speed is', nonidle_speedavg, 'kmph')

    # Plot Economy Speed Average
    plt.plot(nonidle['Speed (GPS)(km/h)'], '.')
    plt.title('Economy Average Speed(kmh)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('kmph', fontdict=None, labelpad=None)
    plt.show()

    # Trip RPM Average
    trip_rpm = trip['Engine RPM(rpm)'].mean()
    print('Average Trip RPM is', trip_rpm, 'rpm')

    # Plot Trip RPM Average
    plt.plot(trip['Engine RPM(rpm)'], '.')
    plt.title('Trip Average RPM(rpm)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('rpm', fontdict=None, labelpad=None)
    plt.show()

    # Economy RPM Average
    nonidle_rpm = nonidle['Engine RPM(rpm)'].mean()
    print('Average Economy RPM is', nonidle_rpm, 'rpm')

    # Plot Economy RPM Average
    plt.plot(nonidle['Engine RPM(rpm)'], '.')
    plt.title('Economy Average RPM(rpm)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('rpm', fontdict=None, labelpad=None)
    plt.show()
    # Trip Load Average
    trip_load = trip['Engine Load(Absolute)(%)'].mean()
    print('Average Trip Load is', trip_load, '%')

    # Plot Load Average
    plt.plot(trip['Engine Load(Absolute)(%)'], '.')
    plt.title('Trip Average Load(%)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('load %', fontdict=None, labelpad=None)
    plt.show()

    # Economy Load Average
    nonidle_load = nonidle['Engine Load(Absolute)(%)'].mean()
    print('Average Economy Load is', nonidle_load, '%')

    # Plot Economy Load Average
    plt.plot(nonidle['Engine Load(Absolute)(%)'], '.')
    plt.title('Economy Average Load(%)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('load %', fontdict=None, labelpad=None)
    plt.show()


    # Trip Throttle Average
    trip_thrttl = trip['Absolute Throttle Position B(%)'].mean()
    print('Average Trip Throttle is', trip_thrttl, '%')

    # Plot Trip Throttle Average
    plt.plot(trip['Absolute Throttle Position B(%)'], '.')
    plt.title('Trip Average Throttle(%)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('throttle %', fontdict=None, labelpad=None)
    plt.show()

    # Economy Throttle Average
    nonidle_thrttl = nonidle['Absolute Throttle Position B(%)'].mean()
    print('Average Economy Throttle is', nonidle_thrttl, '%')

    # Plot Economy Throttle Average
    plt.plot(nonidle['Absolute Throttle Position B(%)'], '.')
    plt.title('Economy Average Throttle(%)', fontdict=None, loc='center')
    plt.xlabel('Time (s)', fontdict=None, labelpad=None)
    plt.ylabel('throttle %', fontdict=None, labelpad=None)
    plt.show()

    print('For better mileage(Economy) of at least 25kmpl\n')
    print('Average Speed:', nonidle_speedavg, 'kmph')
    print('Average RPM:', nonidle_rpm, 'rpm')
    print('Average Load:', nonidle_load, '%')
    print('Average Throttle:', nonidle_thrttl
          , '%')


def plotmps(data, path_lats, path_long, nonidle):
    """Plot areas of mileage above 25kmpl"""
    # Declare the center of the map, and how much we want the map zoomed in.
    gmap3 = gmplot.GoogleMapPlotter(data[' Latitude'].mean(),
                                    data[' Longitude'].mean(), 14)
    # Start and stop plot on map.
    gmap3.scatter(list([path_lats[0]]), list([path_long[0]]),
                  '#00FF00', size=50, marker=False)
    gmap3.scatter(list([path_lats[-1]]), list([path_long[-1]]),
                  '#FF0000', size=50, marker=False)
                  # Plot method Draw a line in between given coordinates.
    gmap3.plot(path_lats, path_long, 'blue', edge_width=3.0)

    # Extract different latitude and longitude points.
    nonidle_lats = np.array(nonidle[' Latitude'])
    nonidle_long = np.array(nonidle[' Longitude'])
    # Plot mileage>25kmpl
    gmap3.scatter(list(nonidle_lats), list(nonidle_long), '#FFFF00',
                  size=50, marker=False)
    # Google_API_Key.
    # gmap3.apikey = "AIzaSyAXPL2nQcPiXhSkhHTwoSFXm6Vn6hyeB3Y"
    # Save to html.
    gmap3.draw(r"Mileage_25above.html")
    webbrowser.open('Mileage_25above.html', new=2)
