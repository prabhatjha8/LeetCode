def generate_prime_list(n):
  ansList = [1 for _ in range(n+1)]
  ansList[0] = 0
  ansList[1] = 0
  i = 0
  while i < n+1:
    if ansList[i] == 0:
      i += 1
    else:
      for j in range(i+1, n+1):
          if j%i == 0:
              ansList[j] = 0 
      i += 1

  return ansList


# Generate the list for all primes up to 1000
prime_list = generate_prime_list(1000)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        last_val = -1
        for i in range(n):
            cur_val = nums[i]

            if cur_val <= last_val:
                return False 

            else:
                j = cur_val - 1
                for j in range(cur_val - 1, -1, -1):
                    if (prime_list[j] == 1) and ((cur_val - j) > last_val):
                        break
                nums[i] = cur_val - j
                last_val = nums[i]

        return True



        