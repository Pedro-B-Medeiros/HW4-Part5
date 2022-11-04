import data
import unittest
import math
import vector_math
import utility
from collisions import *
import cast


class TestCases(unittest.TestCase):

    def test_Point(self):
        points = data.Point(1, 2, 3)
        points2 = data.Point(7, 6, 5)
        self.assertEqual(points.x, 1)
        self.assertEqual(points.y, 2)
        self.assertEqual(points.z, 3)
        self.assertEqual(points2.x, 7)
        self.assertEqual(points2.y, 6)
        self.assertEqual(points2.z, 5)

    def test_Vector(self):
        vector = data.Vector(4, 5, 6)
        vector2 = data.Vector(7, 8, 9)
        self.assertEqual(vector.x, 4)
        self.assertEqual(vector.y, 5)
        self.assertEqual(vector.z, 6)
        self.assertEqual(vector2.x, 7)
        self.assertEqual(vector2.y, 8)
        self.assertEqual(vector2.z, 9)
        self.assertEqual(vector, data.Vector(4, 5, 6))

    def test_Ray(self):
        test_Ray = data.Ray(data.Point(1, 2, 3), data.Vector(4, 5, 6))
        test_Ray2 = data.Ray(data.Point(7, 6, 5), data.Vector(7, 8, 9))
        self.assertEqual(test_Ray.dir.x, 4)
        self.assertEqual(test_Ray.dir.y, 5)
        self.assertEqual(test_Ray.dir.z, 6)
        self.assertEqual(test_Ray2.dir.x, 7)
        self.assertEqual(test_Ray2.dir.y, 8)
        self.assertEqual(test_Ray2.dir.z, 9)
        self.assertEqual(test_Ray.dir, data.Vector(4, 5, 6))
        self.assertEqual(test_Ray.pt, data.Vector(1, 2, 3))

    def test_Sphere(self):
        test_Sphere = data.Sphere(data.Point(1, 2, 3), 5.145)
        test_Sphere2 = data.Sphere(data.Point(4, 5, 6), 8.456)
        self.assertEqual(test_Sphere.center.x, 1)
        self.assertEqual(test_Sphere.center.y, 2)
        self.assertEqual(test_Sphere.center.z, 3)
        self.assertAlmostEqual(test_Sphere.radius, 5.14, 1)
        self.assertEqual(test_Sphere2.center.x, 4)
        self.assertEqual(test_Sphere2.center.y, 5)
        self.assertEqual(test_Sphere2.center.z, 6)
        self.assertAlmostEqual(test_Sphere2.radius, 8.45, 1)
        self.assertEqual(test_Sphere2.center, data.Point(4, 5, 6))

    def test_scale_vector(self):
        vector = data.Vector(1, 2, 3)
        scaling_vector = vector_math.scale_vector(vector, 1.5)
        vector2 = data.Vector(4, 5, 6)
        scaling_vector2 = vector_math.scale_vector(vector2, 1.5)
        self.assertTrue(utility.epsilon_equal(scaling_vector.x, 1.5))
        self.assertTrue(utility.epsilon_equal(scaling_vector.y, 3))
        self.assertTrue(utility.epsilon_equal(scaling_vector.z, 4.5))
        self.assertTrue(utility.epsilon_equal(scaling_vector2.x, 6))
        self.assertTrue(utility.epsilon_equal(scaling_vector2.y, 7.5))
        self.assertTrue(utility.epsilon_equal(scaling_vector2.z, 9))

    def test_dot_vector(self):
        vector = data.Vector(4, 5, 6)
        vector2 = data.Vector(6, 7.5, 9)
        vector3 = data.Vector(1, 2, 3)
        vector4 = data.Vector(1.5, 3, 4.5)
        dotting_vector = vector_math.dot_vector(vector, vector2)
        dotting_vector2 = vector_math.dot_vector(vector3, vector4)
        self.assertTrue(utility.epsilon_equal(dotting_vector, 115.5))
        self.assertTrue(utility.epsilon_equal(dotting_vector2, 21))

    def test_length_vector(self):
        vector = data.Vector(1, 2, 2)
        vector2 = data.Vector(2, 2, 2)
        lengthing_vector = vector_math.length_vector(vector)
        lengthing_vector2 = vector_math.length_vector(vector2)
        self.assertTrue(utility.epsilon_equal(lengthing_vector, 3))
        self.assertTrue(utility.epsilon_equal(lengthing_vector2, 3.4641))

    def test_normalize_vector(self):
        vector = data.Vector(1, 2, 2)
        vector_length = vector_math.length_vector(vector)
        scale_factor = 1 / vector_length
        vector_comparing = vector_math.scale_vector(vector, scale_factor)
        vector_normalized = vector_math.normalize_vector(vector)
        vector2 = data.Vector(2, 3, 3)
        vector_length2 = vector_math.length_vector(vector2)
        scale_factor2 = 1 / vector_length2
        vector_comparing2 = vector_math.scale_vector(vector2, scale_factor2)
        vector_normalized2 = vector_math.normalize_vector(vector2)
        self.assertAlmostEqual(vector_normalized2, vector_comparing2)
        self.assertAlmostEqual(vector_normalized, vector_comparing)

    def test_difference_point(self):
        p1 = data.Point(7, 8, 9)
        p2 = data.Point(4, 5, 6)
        p3 = data.Point(3, 3, 3)
        differencing_points = vector_math.difference_point(p1, p2)
        self.assertTrue(utility.epsilon_equal(differencing_points.x, p3.x))
        self.assertTrue(utility.epsilon_equal(differencing_points.y, p3.y))
        self.assertTrue(utility.epsilon_equal(differencing_points.z, p3.z))
        p4 = data.Point(8, 9, 10)
        p5 = data.Point(3, 4, 5)
        p6 = data.Point(5, 5, 5)
        differencing_points2 = vector_math.difference_point(p4, p5)
        self.assertTrue(utility.epsilon_equal(differencing_points2.x, p6.x))
        self.assertTrue(utility.epsilon_equal(differencing_points2.y, p6.y))
        self.assertTrue(utility.epsilon_equal(differencing_points2.z, p6.z))

    def test_difference_vector(self):
        v1 = data.Vector(7, 8, 9)
        v2 = data.Vector(4, 5, 6)
        v3 = data.Vector(3, 3, 3)
        differencing_vectors = vector_math.difference_vector(v1, v2)
        self.assertTrue(utility.epsilon_equal(differencing_vectors.x, v3.x))
        self.assertTrue(utility.epsilon_equal(differencing_vectors.y, v3.y))
        self.assertTrue(utility.epsilon_equal(differencing_vectors.z, v3.z))
        v4 = data.Vector(8, 9, 10)
        v5 = data.Vector(4, 5, 6)
        v6 = data.Vector(4, 4, 4)
        differencing_vectors2 = vector_math.difference_vector(v4, v5)
        self.assertTrue(utility.epsilon_equal(differencing_vectors2.x, v6.x))
        self.assertTrue(utility.epsilon_equal(differencing_vectors2.y, v6.y))
        self.assertTrue(utility.epsilon_equal(differencing_vectors2.z, v6.z))

    def test_translate_point(self):
        point1 = data.Point(9, 0, 1)
        vector1 = data.Vector(1, 2, 2)
        point_translation = vector_math.translate_point(point1, vector1)
        point2 = data.Point(14, 4, 10)
        vector2 = data.Vector(2, 1, 9)
        point_translation2 = vector_math.translate_point(point2, vector2)
        self.assertTrue(utility.epsilon_equal(point_translation.x, 10))
        self.assertTrue(utility.epsilon_equal(point_translation.y, 2))
        self.assertTrue(utility.epsilon_equal(point_translation.z, 3))
        self.assertTrue(utility.epsilon_equal(point_translation2.x, 16))
        self.assertTrue(utility.epsilon_equal(point_translation2.y, 5))
        self.assertTrue(utility.epsilon_equal(point_translation2.z, 19))

    def test_vector_from_to(self):
        point_from1 = data.Point(7, 8, 9)
        point_to1 = data.Point(4, 5, 6)
        vector_from_to1 = vector_math.vector_from_to(point_from1, point_to1)
        point_from2 = data.Point(10, 11, 12)
        point_to2 = data.Point(4, 5, 6)
        vector_from_to2 = vector_math.vector_from_to(point_from2, point_to2)
        self.assertTrue(utility.epsilon_equal(vector_from_to1.x, -3))
        self.assertTrue(utility.epsilon_equal(vector_from_to1.y, -3))
        self.assertTrue(utility.epsilon_equal(vector_from_to1.z, -3))
        self.assertTrue(utility.epsilon_equal(vector_from_to2.x, -6))
        self.assertTrue(utility.epsilon_equal(vector_from_to2.y, -6))
        self.assertTrue(utility.epsilon_equal(vector_from_to2.z, -6))


class TestCases2(unittest.TestCase):
    def test_sphere_intersection_point1(self):
        ray1 = data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0))
        sphere1 = data.Sphere(data.Point(7, 0, 0), 4)
        intersec1 = data.Point(3, 0, 0)
        self.assertEqual(sphere_intersection_point(ray1, sphere1), intersec1)
    def test_sphere_intersection_point2(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(9.23076, 3.84615, 0))
    def test_sphere_intersection_point3(self):
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4))
        sphere = data.Sphere(data.Point(3, 12, 4), 2)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(2.53846, 10.15384, 3.38461))
    def test_find_intersection_points(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 5)
        sphere2 = data.Sphere(data.Point(10, 0, 0), 5)
        sphere3 = data.Sphere(data.Point(-10, 0, 0), 5)
        sphere4 = data.Sphere(data.Point(0, 10, 0), 5)
        sphere5 = data.Sphere(data.Point(0, -10, 0), 5)
        sphere6 = data.Sphere(data.Point(0, 0, 10), 5)
        sphere7 = data.Sphere(data.Point(0, 0, -10), 5)
        sphere_list = [sphere1, sphere2, sphere3, sphere4, sphere5, sphere6, sphere7]

        ray_list = []
        ray_list.append(data.Ray(data.Point(-25, 0, 0), data.Vector(1, 0, 0)))
        ray_list.append(data.Ray(data.Point(0, -25, 0), data.Vector(0, 1, 0)))
        ray_list.append(data.Ray(data.Point(0, 0, -25), data.Vector(0, 0, 1)))
        ray_list.append(data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4)))

        final_list = []
        for ray in ray_list:
            final_list.append(find_intersection_points(sphere_list, ray))

        inter1 = data.Point(-5, 0, 0)
        inter2 = data.Point(5, 0, 0)
        inter3 = data.Point(-15, 0, 0)
        inter4 = data.Point(0, -5, 0)
        inter5 = data.Point(0, 5, 0)
        inter6 = data.Point(0, -15, 0)
        inter7 = data.Point(0, 0, -5)
        inter8 = data.Point(0, 0, 5)
        inter9 = data.Point(0, 0, -15)
        inter10 = data.Point(1.15384615, 4.6153846, 1.5384615)
        inter11 = data.Point(1.39290320, 5.5716128, 1.8572042)

        manual_list = []
        manual_list.append([(sphere1, inter1), (sphere2, inter2), (sphere3, inter3)])
        manual_list.append([(sphere1, inter4), (sphere4, inter5), (sphere5, inter6)])
        manual_list.append([(sphere1, inter7), (sphere6, inter8), (sphere7, inter9)])
        manual_list.append([(sphere1, inter10), (sphere4, inter11)])

        self.assertEqual(final_list, manual_list)
    def test_sphere_normal_at_point(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 5)
        point1 = data.Point(5, 0, 0)
        sphere_normal = sphere_normal_at_point(sphere1, point1)
        self.assertEqual(sphere_normal, vm.normalize_vector(data.Vector(1, 0, 0)))

        point2 = data.Point(5, 5, 5)
        sphere_normal = sphere_normal_at_point(sphere1, point2)
        self.assertEqual(sphere_normal, vm.normalize_vector(data.Vector(1, 1, 1)))

        point3 = data.Point(5, -5, 5)
        sphere_normal = sphere_normal_at_point(sphere1, point3)
        self.assertEqual(sphere_normal, vm.normalize_vector(data.Vector(1, -1, 1)))

        point4 = data.Point(5, 5, -5)
        sphere_normal = sphere_normal_at_point(sphere1, point4)
        self.assertEqual(sphere_normal, vm.normalize_vector(data.Vector(1, 1, -1)))

        point5 = data.Point(5, -5, -5)
        sphere_normal = sphere_normal_at_point(sphere1, point5)
        self.assertEqual(sphere_normal, vm.normalize_vector(data.Vector(1, -1, -1)))
    def test_cast_ray(self):
        ray = data.Ray(data.Point(0, 0, -14), data.Vector(0, 0, 1))
        sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2, data.Color(255, 0, 0)), data.Sphere(data.Point(0.5, 1.5, -3), 0.5, data.Color(0, 0, 255))]
        self.assertTrue(cast.cast_ray(ray, sphere_list))


if __name__ == "__main__":
    unittest.main()
