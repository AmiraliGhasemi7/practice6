def list_statistics(numbers):
    if not numbers:
        return "لیست خالی است"

    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        'min': minimum,
        'max': maximum,
        'mean': mean,
        'variance': variance
    }

# مثال:
nums = [4, 7, 2, 9, 5]
نتیجه = list_statistics(nums)
print(نتیجه)