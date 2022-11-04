import vector_math as vm
import math


def sphere_intersection_point(ray, sphere):
    A = vm.dot_vector(ray.dir, ray.dir)
    B = 2*(vm.dot_vector(vm.difference_point(ray.pt, sphere.center), ray.dir))
    C = vm.dot_vector(vm.difference_point(ray.pt, sphere.center), vm.difference_point(ray.pt, sphere.center)) - (sphere.radius*sphere.radius)
    delta = B*B - 4*A*C
    if delta < 0:
        return None
    else:
        t1 = (-B + math.sqrt(delta))/(2*A)
        t2 = (-B - math.sqrt(delta))/(2*A)
        if t1 > 0 and t2 > 0:
            return vm.translate_point(ray.pt, vm.scale_vector(ray.dir, min(t1, t2)))
        elif t1 < 0 and t2 < 0:
            return None
        elif (t1 >= 0 and t2 < 0) or (t2 >= 0 and t1 < 0):
            return vm.translate_point(ray.pt, vm.scale_vector(ray.dir, max(t1, t2)))


def find_intersection_points(sphere_list, ray):
    intersectionlist = []
    for sphere in sphere_list:
        intersect = sphere_intersection_point(ray, sphere)
        if intersect is not None:
            intersectionlist.append((sphere, intersect))
    return intersectionlist


def sphere_normal_at_point(sphere, point):
    return vm.normalize_vector(vm.difference_point(point, sphere.center))