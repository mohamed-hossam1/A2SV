# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
	def distinctPrimeFactors(self, nums: List[int]) -> int:

		result = []

		for i in range (len(nums)) :

			square_root = int(math.sqrt(nums[i]))

			for prime_num in range(2, square_root + 1) :

				if (nums[i] % prime_num == 0) :

					result.append(prime_num)

					while (nums[i] % prime_num == 0) :
						nums[i] = nums[i] 

			if (nums[i] >= 2) :
				result.append(nums[i])

		result = set(result)
		return len(result)
		