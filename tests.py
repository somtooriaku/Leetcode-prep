import unittest
import sliding_window
import two_pointers

class TestTwoPointers(unittest.TestCase):
    print("Running two_pointer functions tests ")
    def test_maxSubArrayOfSizeK(self):
        self.assertEqual(sliding_window.maxSubArrayOfSizeK(2, []), 0)
        self.assertEqual(sliding_window.maxSubArrayOfSizeK(1, [1, 2, 3, 4]), 4)
        self.assertEqual(sliding_window.maxSubArrayOfSizeK(3, [2, 1, 5, 1, 3, 2]), 9)
        self.assertEqual(sliding_window.maxSubArrayOfSizeK(2, [2, 3, 4, 1, 5]), 7)
    
    def test_SmallestSubarryGivenSum(self):
        self.assertEqual( sliding_window.SmallestSubarryGivenSum( [2, 1, 5, 2, 3, 2] , 7 ), 2 )
        self.assertEqual( sliding_window.SmallestSubarryGivenSum( [2, 1, 5, 2, 8], 7 ), 1 )
        self.assertEqual( sliding_window.SmallestSubarryGivenSum( [3, 4, 1, 1, 6], 8), 3 )
        self.assertRaises(TypeError, sliding_window.SmallestSubarryGivenSum, 10, 10)

    def test_LongestSubtringofKDistinctCharacters(self):
        self.assertEqual( sliding_window.LongestSubtringofKDistinctCharacters ("araaci", 2), 4)
        self.assertEqual( sliding_window.LongestSubtringofKDistinctCharacters ("araaci", 1), 2)
        self.assertEqual( sliding_window.LongestSubtringofKDistinctCharacters ("cbbebi", 3), 5)

    def test_FruitsIntoBasket(self):
        self.assertEqual( sliding_window.FruitsIntoBasket( ['A', 'B', 'C', 'A', 'C']), 3)
        self.assertEqual( sliding_window.FruitsIntoBasket( ['A', 'B', 'C', 'B', 'B', 'C']), 5)
        self.assertEqual( sliding_window.FruitsIntoBasket( [3,3,3,1,2,1,1,2,3,3,4]), 5)
        self.assertEqual( sliding_window.FruitsIntoBasket( [0, 1, 2, 2]), 3)
        self.assertEqual( sliding_window.FruitsIntoBasket( [1, 2, 3, 2, 2]), 4)
    
    def test_NoRepeatSubstring(self):
        self.assertEqual( sliding_window.NoRepeatSubstring("aabccbb"), 3)
        self.assertEqual( sliding_window.NoRepeatSubstring("abbbb"), 2)
        self.assertEqual( sliding_window.NoRepeatSubstring("abccde"), 3)
        self.assertEqual( sliding_window.NoRepeatSubstring(""), 0)
        self.assertEqual( sliding_window.NoRepeatSubstring("abcacda"), 3)

    def test_LongestStrWithSameLettersAfterReplacement(self):
        self.assertEqual( sliding_window.LongestStrWithSameLettersAfterReplacement("aabccbb", 2), 5)
        self.assertEqual( sliding_window.LongestStrWithSameLettersAfterReplacement("abbcb", 1), 4)
        self.assertEqual( sliding_window.LongestStrWithSameLettersAfterReplacement("abccde", 1), 3)
        self.assertEqual( sliding_window.LongestStrWithSameLettersAfterReplacement("", 2), 0)
    
    def test_LongestStrWithSameOnessAfterReplacement(self):
        self.assertEqual( sliding_window.LongestStrWithSameOnessAfterReplacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), 6)
        self.assertEqual( sliding_window.LongestStrWithSameOnessAfterReplacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), 9)

    def test_find_permutation(self):
        self.assertEqual( sliding_window.find_permutation("qabqqbcaqq", "abc"), True)
        self.assertEqual( sliding_window.find_permutation("oidbcaf", "abc"), True)
        self.assertEqual( sliding_window.find_permutation("bcdxabcdy", "bcdyabcdx"), True)
        self.assertEqual( sliding_window.find_permutation("aaacb", "abc"), True)
        self.assertEqual( sliding_window.find_permutation("eidbaooo", "ab"), True)
        self.assertEqual( sliding_window.find_permutation("dcda", "adc"), True)

    def test_str_anagrams(self):
        self.assertEqual( sliding_window.findStringAnagrams("ppqp", "pq"), [1, 2])
        self.assertEqual( sliding_window.findStringAnagrams("abbcabc", "abc"), [2, 3, 4])
        self.assertEqual( sliding_window.findStringAnagrams("bcdxabcdy", "bcdyabcdx"), [0])
        self.assertEqual( sliding_window.findStringAnagrams("dbacbkhbdkrj", "bd"), [0, 7])
        self.assertEqual( sliding_window.findStringAnagrams("eidbaooo", "ab"), [3])

    def test_SmallestWindowcontainingSubstring(self):
        self.assertEqual( sliding_window.MinimumWindowSubstring("aabdec", "abc"), "abdec")
        self.assertEqual( sliding_window.MinimumWindowSubstring("abdabca", "abc"), "abc")
        self.assertEqual( sliding_window.MinimumWindowSubstring("adcad", "abc"), "")
    print("Finished running sliding window functions tests ")

class TestTwoPointers(unittest.TestCase):
    print("Running two_pointer functions tests ")
    def test_maxSubArrayOfSizeK(self):
        self.assertEqual(two_pointers.pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(two_pointers.pair_with_targetsum([2, 5, 9, 11], 13), [0, 3])


    def test_remove_duplicates(self):
        self.assertEqual(two_pointers.remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)
        self.assertEqual(two_pointers.remove_duplicates([2, 2, 2, 11]), 2)
        self.assertEqual(two_pointers.remove_duplicates([2, 2, 2, 11, 11]), 2)
    
    def test_maxSubArrayOfSizeK(self):
        self.assertEqual(two_pointers.pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(two_pointers.pair_with_targetsum([2, 5, 9, 11], 13), [0, 3])
    
    def test_maxSubArrayOfSizeK(self):
        self.assertEqual(two_pointers.pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(two_pointers.pair_with_targetsum([2, 5, 9, 11], 13), [0, 3])

    def test_maxSubArrayOfSizeK(self):
        self.assertEqual(two_pointers.backspaceCompare("xy#z", "xzz#"), True)
        self.assertEqual(two_pointers.backspaceCompare("xp#", "xyz##"), True)
        self.assertEqual(two_pointers.backspaceCompare("xywrrmp", "xywrrmu#p"), True)
        self.assertEqual(two_pointers.backspaceCompare("xy#z", "xyz#"), False)
    
    print("Finished running two pointers functions tests ")
        


if __name__ == '__main__':
    unittest.main()