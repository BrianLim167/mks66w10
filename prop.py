import matrix

class Prop(object):

    def __init__( self, polygon_matrix, reflection_properties ):
        self.polygons = polygon_matrix.copy()
        self.reflections = reflection_properties[:]

    def copy( self ):
        p = Prop( self.polygons, self.reflections )
        return p

    def get_lighting(self, polygon_number, view, ambient_light, light_sources):
        return [255,0,0]
        points = self.polygons[polygon_number*3:polygon_number*3+3]

        normal = Vector.normal(*points).norm()
        view = view.norm()
        
        for light in light_sources:
            pass
