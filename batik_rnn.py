import os
import inkex
import sys
import simplepath




class BatikColor():
	def __init__(self):
		self.collection = {
			'yellow' : '#F9E571', 
			'orange' : '#EF2C32', 
			'red' : '#ED2134', 
			'brown' : '#9D4E3B',
			'blue' : '#0F225C',
			'green' : '#103F39',
			'purple' : '#9F2A39',
			'violet' : '#351B49'
		}

		self.mixedColor = {
			'yellow_yellow' : '#F5CB4B',
			'yellow_orange' : '#EE2520',
			'yellow_red' : '#F11825',
			'yellow_brown' : '#A45139',
			'yellow_green' : '#2B553F',
			'yellow_purple' : '#C34046',
			'yellow_violet' : '#754E4D',
			'orange_yellow' : '#EF2C32',
			'orange_orange' : ''
		}


class BatikColorPrediction(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)
		self.OptionParser.add_option('', '--firstcolor', action='store', type='string', dest='firstcolor', default='yellow', help='color 1 of 2 mixed color')
		self.OptionParser.add_option('', '--secondcolor', action='store', type='string', dest='secondcolor', default='yellow', help='color 2 of 2 mixed color')


	def effect(self):
		# g = inkex.etree.Element('{http://www.w3.org/2000/svg}g')

		firstColorSquarePath = 'M 23.107784,35.613761 H 86.056758 V 93.404019 H 23.107784 Z'
		secondColorSquarePath = 'm 132.56718,35.649514 h 62.94898 v 57.79026 h -62.94898 z'

		batikColor = BatikColor()

		firstColor = batikColor.collection[self.options.firstcolor]
		secondColor = batikColor.collection[self.options.secondcolor]





		mixedColorSquarePath = 'm 77.632064,118.06838 h 62.948976 v 57.79026 H 77.632064 Z'

		# ele = inkex.etree.Element('{http://www.w3.org/2000/svg}path')
		# g.append(ele)
		# ele.set('d', simplepath.formatPath(squarePath))
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : firstColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;fill:'+firstColor})
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : secondColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;fill:'+secondColor})
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : mixedColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;'})

		
	




if __name__ == "__main__":
	e = BatikColorPrediction()
	e.affect()