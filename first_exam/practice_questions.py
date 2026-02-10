class PracticeExam:

    # ===== BASIC QUESTIONS =====

        def count_odd_numbers(self, numbers):
                """Return the count of odd numbers in the list."""
                count = 0
                for num in numbers:
                        if num % 2 != 0:
                                count += 1
                return count
        


        def sum_list(self, numbers):
                """Return the sum of all numbers in the list."""
                sum = 0
                for num in numbers:
                        sum += num
                return sum



        def reverse_words_order(self, sentence):
                """Reverse the order of words in a sentence."""
                words = sentence.split()       # split sentence into words
                words.reverse()                # reverse the list of words
                return " ".join(words)         # join them back into a string


        def contains_vowel(self, text):
                """Return True if the string contains at least one vowel."""
                vowels = "aeiou"
                for char in text.lower():      # convert text to lowercase
                        if char in vowels:
                                return True
                return False


        def smallest_number(self, numbers):
                """Return the smallest number in the list or None if empty."""
            
                if not numbers:           # check for empty list
                                return None
                return min(numbers)

                # def smallest_number(numbers):
                # """Return the smallest number in the list or None if empty."""
                #         if not numbers:
                #          return None

                # smallest = numbers[0]
                # for num in numbers:
                #         if num < smallest:
                #         smallest = num
                # return smallest


        # ===== INTERMEDIATE QUESTIONS =====

        def remove_vowels(self, text):
                """Return the string with all vowels removed (case-insensitive)."""
                vowel = "aeiouAEIOU"
                for char in text:
                        if char in vowel:
                                char -= vowel
                return char
        def count_character_frequency(text):
                """Return a dictionary with character frequencies."""
                frequency = {}

                for char in text:
                        if char in frequency:
                                frequency[char] += 1
                else:
                        frequency[char] = 1

                return frequency


        def is_prime(self, n):
                """Return True if n is a prime number, otherwise False."""
                pass

        def flatten_list(self, nested):
                """Flatten a 2D list into a 1D list."""
                pass

        def longest_common_prefix(self, words):
                """Return the longest common prefix among a list of words."""
                pass


        # ===== ADVANCED QUESTIONS =====

        def fibonacci_sequence(self, n):
                """Return a list containing the first n Fibonacci numbers."""
                pass

        def max_subarray_sum(self, numbers):
                """Return the maximum sum of a contiguous subarray."""
                pass

        def valid_parentheses(self, s):
                """Return True if parentheses are valid."""
                pass

        def rotate_left(self, numbers, k):
                """Rotate the list to the left by k positions."""
                pass

        def spiral_matrix(self, n):
                """Return an n x n spiral matrix."""
                pass




exam = PracticeExam()
print(exam.sum_list([1, 2, 3]))
print(exam.count_odd_numbers([1, 2, 3]))
print(exam.remove_vowels("skyA"))   
print(exam.reverse_words_order("hello world python"))   