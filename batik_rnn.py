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

		self.mixedColorCollection = {
			'yellow_yellow' : '#F5CB4B',
			'yellow_orange' : '#EE2520',
			'yellow_red' : '#F11825',
			'yellow_brown' : '#A45139',
			'yellow_green' : '#2B553F',
			'yellow_purple' : '#C34046',
			'yellow_violet' : '#754E4D',
			'orange_yellow' : '#F03A32',
			'orange_orange' : '#F32128',
			'orange_red' : '#F0141E',
			'orange_brown' : '#8E2A1F',
			'orange_blue' : '#15131C',
			'orange_green' : '#231A1E',
			'orange_purple' : '#A42A20',
			'orange_violet' : '#6B4E4D',
			'red_yellow' : '#EA2A2B',
			'red_orange' : '#EA261E',
			'red_red' : '#E71B1E',
			'red_brown' : '#872A20',
			'red_blue' : '#151223',
			'red_green' : '#1A1719',
			'red_purple' : '#BD3123',
			'red_violet' : '#74262A',
			'brown_yellow' : '#F19148',
			'brown_orange' : '#EC2E25',
			'brown_red' : '#EC272E',
			'brown_brown' : '#8C4230',
			'brown_blue' : '#112045',
			'brown_green' : '#252421',
			'brown_purple' : '#792C28',
			'brown_violet' : '#552728',
			'blue_yellow' : '#10213F',
			'blue_orange' : '#1C141F',
			'blue_red' : '#20121F',
			'blue_brown' : '#13131E',
			'blue_blue' : '#131231',
			'blue_green' : '#111729',
			'blue_purple' : '#18152C',
			'blue_violet' : '#11142C',
			'green_yellow' : '#1C4331',
			'green_orange' : '#1E1419',
			'green_red' : '#2D181E',
			'green_brown' : '#282423',
			'green_blue' : '#111624',
			'green_green' : '#101F1F',
			'green_purple' : '#241E26',
			'green_violet' : '#0C1523',
			'purple_yellow' : '#B2383F',
			'purple_orange' : '#9E2A20',
			'purple_red' : '#B32E1F',
			'purple_brown' : '#762824',
			'purple_blue' : '#13142B',
			'purple_green' : '#15141C',
			'purple_purple' : '#902728',
			'purple_violet' : '#141017',
			'violet_yellow' : '#755152',
			'violet_orange' : '#4A1D20',
			'violet_red' : '#6B2227',
			'violet_brown' : '#4D2327',
			'violet_blue' : '#101634',
			'violet_green' : '#141E27',
			'violet_purple' : '#321927',
			'violet_violet' : '151222'
		}


class BatikColorPrediction(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)
		self.OptionParser.add_option('', '--firstcolor', action='store', type='string', dest='firstcolor', default='yellow', help='color 1 of 2 mixed color')
		self.OptionParser.add_option('', '--secondcolor', action='store', type='string', dest='secondcolor', default='yellow', help='color 2 of 2 mixed color')


	def effect(self):
		# g = inkex.etree.Element('{http://www.w3.org/2000/svg}g')

		firstColorSquarePath = 'M 23.107784,16.563749 H 86.056758 V 74.354007 H 23.107784 Z'
		secondColorSquarePath = 'm 132.56718,17.128669 h 62.94898 v 57.79026 h -62.94898 z'

		batikColor = BatikColor()

		firstColor = batikColor.collection[self.options.firstcolor]
		secondColor = batikColor.collection[self.options.secondcolor]

		mixedColorSquarePath = 'm 77.632064,100.0766 h 62.948976 v 57.79026 H 77.632064 Z'
	
		rMixedColorSquarePath = 'm 78.106018,206.09297 h 62.948972 v 57.79026 H 78.106018 Z'
		rMixedColor = batikColor.mixedColorCollection[self.options.firstcolor+'_'+self.options.secondcolor]

		# ele = inkex.etree.Element('{http://www.w3.org/2000/svg}path')
		# g.append(ele)
		# ele.set('d', simplepath.formatPath(squarePath))
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : firstColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;fill:'+firstColor})
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : secondColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;fill:'+secondColor})
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : mixedColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;'})
		inkex.etree.SubElement(self.document.getroot(), inkex.addNS('path', 'svg'), {'d' : rMixedColorSquarePath, 'style' : 'stroke:#808080; stroke-width:0.6;fill:'+rMixedColor})

		
	




if __name__ == "__main__":
	e = BatikColorPrediction()
	e.affect()