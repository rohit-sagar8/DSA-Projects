import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Bubble sort algorithm
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data

# Selection sort algorithm
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        yield data

# Insertion sort algorithm
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        yield data

# Merge sort algorithm
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

        yield data

# Quick sort algorithm
def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data, low, high)
        yield from quick_sort(data, low, pivot_index)
        yield from quick_sort(data, pivot_index + 1, high)

def partition(data, low, high):
    pivot = data[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and data[left] <= pivot:
            left = left + 1
        while data[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done= True
        else:
            data[left], data[right] = data[right], data[left]

    data[low], data[right] = data[right], data[low]
    return right

# Function to generate random data for visualization
def generate_data(size=50):
    return [random.randint(1, 100) for _ in range(size)]

# Function to update the plot during animation
def update_fig(data, rects, iteration_text):
    for rect, val in zip(rects, data):
        rect.set_height(val)
    iteration_text.set_text(f"Iteration: {update_fig.iteration}")
    update_fig.iteration += 1

update_fig.iteration = 1

def main():
    sorting_methods = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "quick": lambda data: quick_sort(data, 0, len(data) - 1)
    }

    method = input("Enter sorting method (bubble/selection/insertion/merge/quick): ").lower()
    if method not in sorting_methods:
        print("Invalid sorting method.")
        return

    data = generate_data()
    fig, ax = plt.subplots()
    ax.set_title(f"{method.capitalize()} Sort Visualization")
    ax.bar(range(len(data)), data, align="edge")

    iteration_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        frames=sorting_methods[method](data.copy()),
        fargs=(ax.patches, iteration_text),
        repeat=False,
        blit=False,
        interval=50
    )

    plt.show()

if __name__ == "__main__":
    main()
