from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):

        # Test case for Dominant Emotion = JOY
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'JOY')

        # Test case for Dominant Emotion = ANGER
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'ANGER')

        # Test case for Dominant Emotion = DISGUST
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'DISGUST')

        # Test case for Dominant Emotion = SADNESS
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'SADNESS')

        # Test case for Dominant Emotion = FEAR
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'FEAR')

#calling the unit tests
if __name__ == '__main__':
    unittest.main()