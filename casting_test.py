import cast
import unittest
import data

RED = data.Color(1.0, 0, 0)
BLUE = data.Color(0, 0, 1)
GREEN = data.Color(0, 1, 0)
WHITE = data.Color(1, 1, 1)
YELLOW = data.Color(1, 1, 0)
ORANGE = data.Color(1, 0.65, 0)
BLACK = data.Color(0, 0, 0)


class TestCases(unittest.TestCase):
    def test_cast_all_rays(self):
        eye_point = data.Point(0.0, 0.0, -14.0)
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 512
        height = 384
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
        sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2, BLUE, data.Finish(0.2, 0.4, 0.5, 0.05)),
                       data.Sphere(data.Point(0.5, 1.5, -3), 0.5, RED, data.Finish(0.4, 0.4, 0.5, 0.05))]
        amb_color = data.Color(1.0, 1.0, 1.0)
        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light)
#        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light)

    '''
    def test_cast_all_rays2(self):
        eye_point = data.Point(0.0, 0.0, -14.0)
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 512
        height = 384
        light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
        sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, BLUE, data.Finish(0.2, 0.4, 0.5, 0.05)),
                       data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, RED, data.Finish(0.4, 0.4, 0.5, 0.05)),
                       data.Sphere(data.Point(0, 0, 107), 100, RED, data.Finish(0.2, 0.4, 0.5, 0.05))]
        amb_color = data.Color(1.0, 1.0, 1.0)
        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light)
    '''
if __name__ == "__main__":
    unittest.main()