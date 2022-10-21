function calculate(min, max, step) {
    let number = min;
    let sum = min;
    while (number + step <= max) {
        number += step;
        sum += number;
    }
    console.log(sum);
}
calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);

function avg(data) {
    let salary_sum = 0;
    let salary_number = 0;
    for (let i = 0; i < data["employees"].length; i++) {
        if (data["employees"][i]["manager"] == false) {
            salary_sum += data["employees"][i]["salary"];
            salary_number++;
        }
    }
    console.log(salary_sum / salary_number);
}
avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": false
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": true
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": false
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": false
        }
    ]
});

function func(a) {
    function f(b, c) {
        console.log(a + (b * c));
    }
    return f
}
func(2)(3, 4);
func(5)(1, -5);
func(-3)(2, 9);

function maxProduct(nums) {
    let result = [];
    for (let i = 0; i < nums.length; i++) {
        let a = nums[i];
        for (let j = 0; j < nums.length; j++) {
            let b = nums[j];
            if (i != j) {
                result.push(a * b);
            }
        }
    }
    console.log(Math.max(...result));
}
maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);



function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j]
            }
        }
    }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result);


function maxZeros(nums) {
    let ones = 0;
    let result = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 0) {
            ones++;
        }
        result.push(ones);
        if (nums[i] == 1) {
            ones = 0;
        }
    }
    console.log(Math.max(...result))
}

maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);































/*
employees = [
    {
        "name": "John",
        "salary": 30000,
        "manager": false
    },
    {
        "name": "Bob",
        "salary": 60000,
        "manager": true
    },
    {
        "name": "Jenny",
        "salary": 50000,
        "manager": false
    },
    {
        "name": "Tony",
        "salary": 40000,
        "manager": false
    }
];

let d = employees.filter(function (user, index) {
    return user["manager"] == false;
})

console.log(d);

*/



/*
function avg(data) {

    let d = data.employees.filter(function (user, index) {
        return user["manager"] == false;

    })

    var s = 0;
    for (var i = 0; i < d.length; i++) {
        s += d.salary[i];
    }

    console.log(s / d.length);
}

avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": false
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": true
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": false
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": false
        }
    ]
});

*/

