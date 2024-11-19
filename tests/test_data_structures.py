import unittest
from data_structure_operations import (find_sublist_sum, rotate_list, longest_increasing_subsequence,
                                       list_partition, tuple_pair_with_sum,
                                       tuple_find_peak, tuple_to_dict, tuple_k_smallest, tuple_element_count,
                                       symmetric_difference_sets, set_cartesian_product, set_is_subset_of_any,
                                       find_missing_elements, set_frequent_elements, merge_dicts_with_sum,
                                       dict_find_key_with_max_value, reverse_lookup, dict_to_sorted_list,
                                       nested_dict_sum)

class TestListOperations(unittest.TestCase):

    def test_find_sublist_sum(self):
        self.assertEqual(find_sublist_sum([1, 2, 3, 7, 5], 12), [3, 7, 2])
        self.assertEqual(find_sublist_sum([1, 2, 3], 6), [1, 2, 3])
        self.assertIsNone(find_sublist_sum([1, 2, 3], 10))

    def test_rotate_list(self):
        self.assertEqual(rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(rotate_list([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(rotate_list([1, 2, 3], 3), [1, 2, 3])

    def test_longest_increasing_subsequence(self):
        self.assertEqual(longest_increasing_subsequence([3, 10, 2, 1, 20]), [3, 10, 20])
        self.assertEqual(longest_increasing_subsequence([3, 2]), [3])
        self.assertEqual(longest_increasing_subsequence([50, 3, 10, 7, 40, 80]), [3, 7, 40, 80])

    def test_list_partition(self):
        self.assertEqual(list_partition([3, 1, 4, 1, 5, 9], 4), [3, 1, 1, 4, 5, 9])
        self.assertEqual(list_partition([5, 2, 3, 8, 7], 5), [2, 3, 5, 8, 7])

class TestTupleOperations(unittest.TestCase):

    def test_tuple_pair_with_sum(self):
        self.assertEqual(tuple_pair_with_sum((1, 2, 3, 4, 5), 9), (4, 5))
        self.assertIsNone(tuple_pair_with_sum((1, 2, 3), 7))

    def test_tuple_find_peak(self):
        self.assertIn(tuple_find_peak((1, 3, 20, 4, 1, 0)), {20, 4})
        self.assertEqual(tuple_find_peak((1, 3, 1)), 3)

    def test_tuple_to_dict(self):
        self.assertEqual(tuple_to_dict((("a", 1), ("b", 2))), {"a": 1, "b": 2})

    def test_tuple_k_smallest(self):
        self.assertEqual(tuple_k_smallest((5, 3, 1, 4, 2), 3), [1, 2, 3])

    def test_tuple_element_count(self):
        self.assertEqual(tuple_element_count((1, 2, 2, 3, 1)), {1: 2, 2: 2, 3: 1})

class TestSetOperations(unittest.TestCase):

    def test_symmetric_difference_sets(self):
        self.assertEqual(symmetric_difference_sets({1, 2, 3}, {3, 4, 5}, {5, 6}), {1, 2, 4, 6})

    def test_set_cartesian_product(self):
        self.assertEqual(set_cartesian_product({1, 2}, {3, 4}), {(1, 3), (1, 4), (2, 3), (2, 4)})

    def test_set_is_subset_of_any(self):
        self.assertTrue(set_is_subset_of_any([{1, 2}, {3, 4}], {1, 2, 3}))
        self.assertFalse(set_is_subset_of_any([{5, 6}], {1, 2, 3}))

    def test_find_missing_elements(self):
        self.assertEqual(find_missing_elements({1, 2, 3, 4}, {2, 3}), {1, 4})

    def test_set_frequent_elements(self):
        self.assertEqual(set_frequent_elements([1, 1, 2, 3, 3, 3, 4], 2), {1, 3})

class TestDictionaryOperations(unittest.TestCase):

    def test_merge_dicts_with_sum(self):
        self.assertEqual(merge_dicts_with_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'd': 6}),
                         {'a': 6, 'b': 5, 'c': 4, 'd': 6})

    def test_dict_find_key_with_max_value(self):
        self.assertEqual(dict_find_key_with_max_value({'a': 10, 'b': 15, 'c': 5}), 'b')

    def test_reverse_lookup(self):
        self.assertEqual(reverse_lookup({'a': 1, 'b': 2, 'c': 1}, 1), ['a', 'c'])

    def test_dict_to_sorted_list(self):
        self.assertEqual(dict_to_sorted_list({'a': 3, 'b': 1, 'c': 2}), [('a', 3), ('c', 2), ('b', 1)])

    def test_nested_dict_sum(self):
        self.assertEqual(nested_dict_sum({'a': {'x': 5, 'y': 10}, 'b': 3, 'c': {'z': 2}}), 20)

if __name__ == '__main__':
    unittest.main()
