import matrix
import light

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

        ambient_color = Light.ambient_color(ambient_light, ambient_reflection)
        r_color = ambient_color[0]
        g_color = ambient_color[1]
        b_color = ambient_color[2]
        
        for light in light_sources:
            diffuse_color = light.diffuse_color(diffuse_reflection, normal)
            specular_color = light.specular_color(specular_reflection,
                                                  view, normal)    
            r_color += diffuse_color[0] + specular_color[0]
            g_color += diffuse_color[1] + specular_color[1]
            b_color += diffuse_color[2] + specular_color[2]

        if ( r_color > 255 ):
            r_color = 255 
        if ( g_color > 255 ):
            g_color = 255 
        if ( b_color > 255 ):
            b_color = 255 
