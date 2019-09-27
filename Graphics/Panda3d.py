from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
import math

class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		
		#load model
		self.scene = self.loader.loadModel('models/environment')
		self.scene.reparentTo(self.render)
		self.scene.setScale(0.1, 0.1, 0.1)
		self.scene.setPos(-8, 42, 0)
		#spin camera
		self.taskMgr.add(self.spinCameraTask, 'SpinCameraTask')
		#load animation file
		self.pandaActor = Actor("models/panda-model", {'walk' : 'models/panda-walk4'})
		self.pandaActor.setScale(0.005, 0.005, 0.005)
		self.pandaActor.reparentTo(self.render)
		self.pandaActor.loop('walk')
		#
		
	#spin camera helper function
	def spinCameraTask(self, task):
		angleDegrees = task.time * 6.0
		angleRadians = angleDegrees * (math.pi / 180)
		self.camera.setPos(20 * math.sin(angleRadians), -20.0 * math.cos(angleRadians), 3)
		self.camera.setHpr(angleDegrees, 0, 0)
		return task.cont 
app = MyApp()
app.run()
