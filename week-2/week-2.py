def calculate(min, max, step):
    number = min
    sum = min
    while number + step <= max:
        number += step
        sum += number
    print(sum)


calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

print("*" * 20)


def avg(data):
    data_employees = data["employees"]
    result = []
    salary_sum = 0
    for item in data_employees:
        if item["manager"] == False:
            salary_sum += item["salary"]
            result.append("F")
    salary_number = result.count("F")
    print(salary_sum / salary_number)


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})

print("*" * 20)


def func(a):
    def f(b, c):
        print(a+(b*c))
    return f


func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)

print("*" * 20)


def maxProduct(nums):
    result = []
    for a in nums:
        for b in nums:
            if b != a:
                result.append(a*b)
    print(max(result))


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5, -1, -2, 0])
maxProduct([-5, -2])

print("*" * 20)


def twoSum(nums, target):
    i = 0
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)

print("*" * 20)


def maxZeros(nums):
    ones = 0
    result = []
    for n in nums:
        if n == 0:
            ones += 1
        result.append(ones)

        if n == 1:
            ones = 0
    print(max(result))


maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])

print("*" * 20)
