import collisions
import data
import vector_math as vm


def cast_ray(ray, sphere_list, amb_color, light, eye_point):
    list_intersections = collisions.find_intersection_points(sphere_list, ray)
    if len(list_intersections) == 0:
        return data.Color(1, 1, 1)
    else:
        nearest_inter = list_intersections[0]
        distance = vm.length_vector(vm.vector_from_to(ray.pt, nearest_inter[1]))
        for intersec in list_intersections:
            new_distance = vm.length_vector(vm.vector_from_to(ray.pt, intersec[1]))
            if new_distance <= distance:
                nearest_inter = intersec
        sph_int = nearest_inter[0]
        pt_int = nearest_inter[1]
        normal = collisions.sphere_normal_at_point(sph_int, pt_int)
        normal_scaled = vm.scale_vector(normal, 0.01)
        pe = vm.translate_point(pt_int, normal_scaled)
        ldir = vm.normalize_vector(vm.vector_from_to(pe, light.pt))
        ldir_dot_norm = vm.dot_vector(normal, ldir)
        light_behind_sphere = False
        if ldir_dot_norm <= 0:
            light_behind_sphere = True

        other_sphere_blocking = False
        pe_dist_to_light = vm.length_vector(vm.vector_from_to(pe, light.pt))
        other_intersections = collisions.find_intersection_points(sphere_list, data.Ray(pe, ldir))
        for points in other_intersections:
            distance_to_other_intersections = vm.length_vector(vm.difference_point(pe, points[1]))
            if distance_to_other_intersections < pe_dist_to_light:
                other_sphere_blocking = True

        modified_color = data.Color(sph_int.color.r, sph_int.color.g, sph_int.color.b) # sphere color
        modified_color = modified_color * amb_color # add ambient color
        modified_color *= sph_int.finish.ambient # add finish

        if light_behind_sphere is False and other_sphere_blocking is False:  # adding diffusion if light not obstructed
            light_diffuse_contribution = light.color * sph_int.color
            light_diffuse_contribution *= (vm.dot_vector(normal, ldir) * sph_int.finish.diffuse)
            modified_color = modified_color + light_diffuse_contribution

        reflection_vector = vm.difference_vector(ldir, vm.scale_vector(normal, 2 * ldir_dot_norm))  # adding specular and roughness
        v_dir = vm.normalize_vector(vm.vector_from_to(eye_point, pe))
        spec_intense = vm.dot_vector(reflection_vector, v_dir)
        if spec_intense > 0:
            specular_contribution = data.Color(light.color.r, light.color.g, light.color.b)
            specular_contribution *= (sph_int.finish.specular * (spec_intense**(1/sph_int.finish.roughness)))
            modified_color = modified_color + specular_contribution

        return modified_color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light):
    x_step = (max_x - min_x)/width
    y_step = (max_y - min_y)/height
    print('P3')
    print(width, height)
    print('255')
    for y in range(height):
        for x in range(width):
            ray = data.Ray(eye_point, data.Vector(min_x + x_step*x, max_y - y_step*y, -eye_point.z))
            #print(x, y, cast_ray(ray, sphere_list))
            color_shown = cast_ray(ray, sphere_list, amb_color, light, eye_point)
            color_255r = min(int(color_shown.r * 255), 255)
            color_255g = min(int(color_shown.g * 255), 255)
            color_255b = min(int(color_shown.b * 255), 255)
            print(color_255r, color_255g, color_255b)

'''
def cast_all_rays2(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light, file_name):
    x_step = (max_x - min_x)/width
    y_step = (max_y - min_y)/height

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("P3\n")
        f.write(str(width) + " " + str(height) + " " + str("\n255\n"))
        for y in range(height):
            for x in range(width):
                ray = data.Ray(eye_point, data.Vector(min_x + x_step*x, max_y - y_step*y, 14))
                color_shown = cast_ray(ray, sphere_list, amb_color, light, eye_point)
                color_255r = min(int(color_shown.r * 255), 255)
                color_255g = min(int(color_shown.g * 255), 255)
                color_255b = min(int(color_shown.b * 255), 255)
                f.write(str(color_255r) + " " + str(color_255g) + " " + str(color_255b) + "\n")
'''