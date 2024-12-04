nums = [2,7,11,15]
target = 9


def solustion ( nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): # i+1 karena kita tidak boleh menggunakan angka yang sama
            if nums[i] + nums[j] == target:
                return [i, j]
        
solustion(nums, target)

"""
Explanations : 
1. Kita iterate dulu semua index yang ada di nums, dengan variable i ( first number )
2. Kita iterate lagi semua index yang ada di nums, dengan variable j ( second number )
3. Kita cek apakah jumlah dari nums[i] + nums[j] sama dengan target, jika iya maka kita return index dari i dan j

"""