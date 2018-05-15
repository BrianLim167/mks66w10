class Light(object):

    def __init__( self, location, color ):
        self.location = location
        self.color = color

    @staticmethod
    def ambient_color( ambient_light, reflection ):
        return [ ambient_light[0]*reflection[0],
                 ambient_light[1]*reflection[1],
                 ambient_light[2]*reflection[2] ]

    def diffuse_color( self, reflection, normal ):
        
