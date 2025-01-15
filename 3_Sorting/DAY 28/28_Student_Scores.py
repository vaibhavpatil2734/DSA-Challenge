def insertion_sort(scores):
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        
        scores[j + 1] = key
    
    return scores

if __name__ == "__main__":
    scores = [85, 95, 76, 90, 92]
    print("Original Scores:", scores)
    sorted_scores = insertion_sort(scores)
    print("Sorted Scores:", sorted_scores)

    scores = [50, 60, 45, 72, 88, 91]
    print("\nOriginal Scores:", scores)
    sorted_scores = insertion_sort(scores)
    print("Sorted Scores:", sorted_scores)
