import unittest


class TestCases(unittest.TestCase):

    def test_printing(self):
        width = 512
        height = 384

        print("P3")
        print(str(width) + " " + str(height) + " " + str("\n255"))
        for y in range(height):
            for x in range(width):
                print(0)
                print(0)
                print(255)


if __name__ == '__main__':
    unittest.main()
