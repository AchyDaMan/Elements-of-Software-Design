import unittest
from geometry import *


class TestGeometry(unittest.TestCase):

    def setUp(self):
        # We create a bunch of points first 

        # The center of the coordinate system is called the origin
        self.origin = Point(0,0,0)
        self.one_above_origin = Point(0, 1, 0)
        self.one_under_origin = Point(0, -1, 0)
        self.out_point= Point(0, 1000, 0)

        self.one_radius_sphere = Sphere(0, 0, 0, 1)
        self.ten_radius_sphere = Sphere(0, -1, 0, 10)

        self.one_cube = Cube(0, 0, 0, 1)
        self.ten_cube = Cube(0, 0, 0, 10)

    

    def test_001_point_distance(self):
        self.assertEqual(int(self.one_above_origin.distance(self.one_under_origin)), 2)
        self.assertEqual(int(self.origin.distance(self.out_point)), 1000)


# Implement the following test cases
# create objects as needed in setup or other places 

    def test_002_point_equality(self):
        # ... Implement here and remove pass 
        self.assertEqual(self.origin, self.origin)
        
    
    def test_003_sphere_area(self):
        pass 

    
#     #TODO! Implement this 
#     def test_004_sphere_volume(self):
#         pass

#     #TODO! Implement this 
#     def test_005_sphere_is_inside_point(self):
#         pass


#     #TODO! Implement this 
#     def test_006_sphere_is_inside_sphere(self):
#         pass


#    #TODO! Implement this 
#     def test_006_cube_is_inside_point(self):
#         pass

#    #TODO! Implement this 
#     def test_007_is_inside_sphere(self):
#         pass



# Here we have the test but we do not have the implementation of the method is_inside_cube()
# 
# No need to change these tests here 
# You need to implement the method is_inside_cube()
    def test_000_is_inside_cube(self):
        self.assertTrue(self.one_cube.is_inside_cube(self.ten_cube))
        self.assertFalse(self.one_cube.is_inside_cube(self.one_cube))

    def test_000_has_same_volume(self): 
        self.assertTrue(self.one_cube.has_same_volume(self.one_cube)) 




if __name__ == '__main__':
    unittest.main()