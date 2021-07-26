from matplotlib.pyplot import figure, show
import numpy

class ZoomPan:
    def __init__(self,ax):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None

        self.ctrl_press = False

        self.ax = ax
        self.zoom_factory(ax,base_scale=1.1)
        self.ctrl_key(ax)
        self.pan_factory(ax)

    def zoom_factory(self, ax, base_scale = 2.):

        def zoomX(event,scale_factor):
            cur_xlim = ax.get_xlim()
            xdata = event.xdata # get event x location
            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])

            ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
            ax.figure.canvas.draw()

        def zoomY(event,scale_factor):
            cur_ylim = ax.get_ylim()
            ydata = event.ydata # get event y location
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        def zoom(event):
            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print(event.button)

            ####### Switch zoom X or Y #########
            if self.ctrl_press:
                zoomY(event,scale_factor)
            else:
                zoomX(event,scale_factor)

        fig = ax.get_figure() # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def ctrl_key(self,ax):
        def onPress(event):
            print(event.key)
            if event.inaxes != ax: return
            if event.key == "control":
                self.ctrl_press = True
        def onRelease(event):
            print(event.key)
            if event.inaxes != ax: return
            if event.key == "control":
                self.ctrl_press = False
        
        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('key_press_event',onPress)
        fig.canvas.mpl_connect('key_release_event',onRelease)

    #def test(self,event):
    #    print(event.key)

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)

        #return the function
        return onMotion


fig = figure()

ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)

ax.set_title('Click to zoom')
x,y,s,c = numpy.random.rand(4,200)
s *= 200

ax.scatter(x,y,s,c)
scale = 1.1
zp = ZoomPan(ax)
#figZoom = zp.zoom_factory(ax, base_scale = scale)
#figPan = zp.pan_factory(ax)
#zp.ctrl_key(ax)
show()