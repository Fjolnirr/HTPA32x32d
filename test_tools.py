import unittest 
import numpy as np
import os

import tools

SAMPLE_FP = os.path.join("testing", "sample.TXT")
FRAMES_EXPECTED_FP = os.path.join("testing", "expected.npy")

class TestTxt2np(unittest.TestCase):
    def test_Result(self):
        expected_frames_shape = (3, 32, 32)
        expected_timestamps = [170.093, 170.218, 170.343]
        result = tools.txt2np(filepath = SAMPLE_FP, array_size = 32)
        frames, timestamps = result
        self.assertEqual(timestamps, expected_timestamps)
        self.assertEqual(frames.shape, expected_frames_shape)
        expected_frames = np.load(FRAMES_EXPECTED_FP)
        self.assertTrue(np.array_equal(frames, expected_frames))
    def test_Defaults(self):
        """
        Default tested: array_size = 32
        """
        expected = tools.txt2np(filepath = SAMPLE_FP, array_size = 32)
        result = tools.txt2np(filepath = SAMPLE_FP)
        expected_frames, expected_timestamps = expected
        frames, timestamps = result
        self.assertTrue(np.array_equal(frames, expected_frames))
    def test_DTYPE(self):
        expected_dtype = np.dtype(tools.DTYPE)
        result = tools.txt2np(filepath = SAMPLE_FP)
        frames, timestamps = result
        self.assertEqual(frames.dtype, expected_dtype)
    def test_array_size(self):
        expected_frames_shape = (3, 16, 16)
        expected_timestamps = [170.093, 170.218, 170.343]
        result = tools.txt2np(filepath = SAMPLE_FP, array_size = 16)
        frames, timestamps = result
        self.assertEqual(timestamps, expected_timestamps)
        self.assertEqual(frames.shape, expected_frames_shape)

class TestNp2csv(unittest.TestCase):
    def test_Result(self):
        input = np.load(FRAMES_EXPECTED_FP)
        # TODO: unit testing
        pass

class Test_flattenFrames(unittest.TestCase):
    def test_Result(self):
        input_shape = (100, 32, 32)
        expected_shape = (100, 32*32)
        input = np.arange(np.prod(input_shape)).reshape(input_shape)
        result = tools._flattenFrames(input)
        self.assertEqual(result.shape, expected_shape)
        
class Test_reshapeFlattenedFrames(unittest.TestCase):
    def test_Result(self):
        input_shape = (100, 32*32)
        expected_shape = (100, 32, 32)
        input = np.arange(np.prod(input_shape)).reshape(input_shape)
        result = tools._reshapeFlattenedFrames(input)
        self.assertEqual(result.shape, expected_shape)

class Test_reshapingFrames(unittest.TestCase):
    def test_flattenAndReshape(self):
        input = np.load(FRAMES_EXPECTED_FP)
        expected_frames_shape = (3, 32, 32)
        expected_flattened_frames_shape = (3, 32**2)
        flattened_result = tools._flattenFrames(input)
        first_frame = flattened_result[0]
        expected_first_frame = input[0].flatten()
        self.assertTrue(np.array_equal(first_frame, expected_first_frame))
        reshaped_result = tools._reshapeFlattenedFrames(flattened_result)
        self.assertTrue(np.array_equal(input, reshaped_result))