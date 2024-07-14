#include <iostream>
#include <vector>

using namespace std;

vector<int> quicksort(vector<int> arr) {
    int length = arr.size();

    if (length < 2) {
        return arr;
    }

    int pivot = arr[length / 2];
    // printf("Pivot: %d\n", pivot);
    vector<int> lesser, equal, greater;

    for (int i = 0; i < length; i++) {
        if (arr[i] < pivot) {
            lesser.push_back(arr[i]);
        }
        if (arr[i] == pivot) {
            equal.push_back(arr[i]);
        }
        if (arr[i] > pivot) {
            greater.push_back(arr[i]);
        }
    }

    // for (int i = 0; i < lesser.size(); i++) {
    //     std::cout << lesser[i];
    // }
    //
    // std::cout << "\n";
    // for (int i = 0; i < equal.size(); i++) {
    //     std::cout << equal[i];
    // }
    //
    // std::cout << "\n";
    // for (int i = 0; i < greater.size(); i++) {
    //     std::cout << greater[i];
    // }

    std::cout << "\n";
    vector<int> arr2;
    for (int i = 0; i < lesser.size(); i++) {
        arr2.push_back(lesser[i]);
    }
    for (int i = 0; i < equal.size(); i++) {
        arr2.push_back(equal[i]);
    }
    for (int i = 0; i < greater.size(); i++) {
        arr2.push_back(greater[i]);
    }
    return quicksort(arr2);
}
int main(int argc, char *argv[]) {

    vector<int> arr = {4, 3, 1, 7, 6, 2, 7, 4, 4, 6, 7,
                       5, 4, 2, 5, 6, 7, 3, 2, 1, 9};
    vector<int> sorted = quicksort(arr);

    for (int i = 0; i < sorted.size(); i++) {
        printf("%d ", sorted[i]);
    }
    return EXIT_SUCCESS;
}
