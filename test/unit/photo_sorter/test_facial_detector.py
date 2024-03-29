import unittest
import os
from photo_sorter.facial_detector import FacialDetector

test_data_dir = os.path.dirname(os.path.realpath(__file__))


class TestImaging(unittest.TestCase):
    def setUp(self):
        self.sut = FacialDetector()
        self.input_filepath = os.path.join(test_data_dir, "../../common/NickZanoElishaCuthbertKellyBrook.jpg")
        self.input_filepath_rotated = os.path.join(test_data_dir,
                                                   "../../common/NickZanoElishaCuthbertKellyBrook_rotated.jpg")
        self.sut.detect_faces(self.input_filepath)
        self.output_filepath = os.path.join(test_data_dir, "../../common/NickZanoElishaCuthbertKellyBrook_output.png")
        self.output_filepath_rotated = os.path.join(test_data_dir,
                                                    "../../common/NickZanoElishaCuthbertKellyBrook_output_rotated.png")

    def test_detect_faces_loads_correctly(self):
        self.assertIsNotNone(self.sut.loaded_img)
        self.assertIsNotNone(self.sut.rgb_img)
        self.assertIsNotNone(self.sut.face_locations)
        self.assertEqual(self.sut.face_locations, [(539, 1207, 762, 984),
                                                   (291, 786, 514, 563),
                                                   (390, 1603, 613, 1380)])

    def test_visualiser_output_file_works(self):
        self.sut.visualiser(output_filepath=self.output_filepath,
                            show_visualiser=False)

        self.assertTrue(os.path.isfile(self.output_filepath))

    def test_rotated_image_gets_detected_correctly(self):
        temp_sut = FacialDetector(detect_rotated=True)
        temp_sut.detect_faces(self.input_filepath_rotated)

        self.assertIsNotNone(temp_sut.loaded_img)
        self.assertIsNotNone(temp_sut.rgb_img)
        self.assertIsNotNone(temp_sut.face_locations)
        self.assertEqual(len(temp_sut.face_locations), 3)

    def tearDown(self):
        if os.path.isfile(self.output_filepath):
            os.remove(self.output_filepath)
        if os.path.isfile(self.output_filepath_rotated):
            os.remove(self.output_filepath_rotated)
