import matplotlib.pyplot
import numpy

class InfiniteDrawer():
    # xCenter and yCentre are circle points
    def GetTangent(self, xCenter, yCentre, x, y):
        print(str(xCenter) + " " + str(yCentre) + " " + str(x) + " " + str(y));
        slope = (y - yCentre) / (x - xCenter);
        tangentSlope = -1 / slope;
        c = tangentSlope * x - y;

        print("Circle line equation is y = %s * x + %s" % (slope, y - slope * x));
        print("Tangent line equation on point (%s, %s) is y = %s * x + %s" % (x, y, tangentSlope, c));

        return (float(tangentSlope), float(c));

    def Plot(self, x, y):
        ax = matplotlib.pyplot.gca()
        ax.set_aspect('equal', adjustable='box')

        matplotlib.pyplot.plot(x, y);
        matplotlib.pyplot.show();

    def GetJointElements(self):
        consideredElementsForJoint = [-float(element) for element in self.x_temp if element <= self.currentDistanceFromCenter and element > self.x_beginning[-1]];
        consideredElementsForJoint = consideredElementsForJoint[::-1];

        print("Considered elements for joint: %s." % str(consideredElementsForJoint));

        return consideredElementsForJoint;

    def DisplayContent(self):
        print("Middle element is %s." % self.x_temp[self.middle]);
        print("Beginning is %s." % str(self.x_beginning));
        print("Last element of beginning is %s." % self.x_beginning[-1]);
        print("Current distance from center is %s." % self.currentDistanceFromCenter);
        print("Inversed beginning: %s" % str(-self.x_beginning[::-1]));

    def SetVariables(self, radius, numberOfPlots, stepSize):
        self.x_temp = numpy.arange(0, radius + stepSize, stepSize);
        self.y_temp = numpy.sqrt(radius**2 - self.x_temp**2);
        minimumValuesForJoint = (radius / 2) / 10;
        self.plotStepSize = (minimumValuesForJoint * 9) / numberOfPlots;
        self.middle = int(len(self.x_temp) / 2) + len(self.x_temp) % 2;
        self.x_beginning = self.x_temp[0:self.middle];
        self.y_beginning = self.y_temp[0:int(len(self.y_temp) / 2) + len(self.y_temp) % 2];
        self.currentDistanceFromCenter = self.x_beginning[-1];

        print("Plot step size is %s" % self.plotStepSize);

    # The center of it will be in (0, 0) point
    def DrawInfinite(self, radius, numberOfPlots, xSize = 1, stepSize = 0.05):
        self.SetVariables(radius, numberOfPlots, stepSize);

        for plot in range(0, numberOfPlots):
            x = self.x_temp;
            y = self.y_temp;

            self.DisplayContent();
            x_consideredElementsForJoint = self.GetJointElements();
            y_consideredElementsForJoint = y[self.middle:self.middle + len(x_consideredElementsForJoint)][::-1];

            if(len(x_consideredElementsForJoint) > 0):
                tangent = self.GetTangent(0, 0, x_consideredElementsForJoint[0], y_consideredElementsForJoint[0]);
            else:
                tangent = self.GetTangent(0, 0, -self.x_beginning[::-1][0], self.y_beginning[::-1][0]);

            x_range = tangent[1] / tangent[0];
            print("Tangent: " + str(tangent))
            print("x range: " + str(x_range))

            x = numpy.concatenate([x_consideredElementsForJoint, -self.x_beginning[::-1], x]);
            y = numpy.concatenate([y_consideredElementsForJoint, self.y_beginning[::-1], y]);
            x = numpy.concatenate([x, x[0:len(x)-1][::-1]]);
            y = numpy.concatenate([y, -y[0:len(y)-1][::-1]]);
            x = numpy.concatenate([x + (abs(x_range) - radius) + xSize, -x - (abs(x_range) - radius) - xSize]);
            y = numpy.concatenate([y, y]);
            x = numpy.concatenate([x, [x[0]]]);
            y = numpy.concatenate([y, [y[0]]]);

            self.Plot(x, y);

            self.currentDistanceFromCenter = self.x_beginning[-1] + self.plotStepSize * (plot + 1);

if __name__ == "__main__":
    infiniteDrawer = InfiniteDrawer();

    infiniteDrawer.DrawInfinite(1, 10);
    infiniteDrawer.GetTangent(2, 3, 6, 4);
