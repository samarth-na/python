#include <stdio.h>
#include <stdlib.h>

int *quick(int arr[]) {
    int pivot = sizeof(arr) / sizeof(arr[0]) / 2;
    int lesser, equal, greater;
    for (int i = 0; i < pivot; i++) {
        if (arr[i] < pivot) {
            lesser++;
        }
        if (arr[i] == pivot) {
            equal++;
        }
        if (arr[i] > pivot) {
            greater++;
        }
    }
    int Larr[lesser], Earr[equal], Garr[greater];

    for (int i = 0; i < pivot; i++) {
        if (arr[i] < pivot) {
            Larr[i] = arr[i];
        }
        if (arr[i] == pivot) {
            Earr[i] = arr[i];
        }
        if (arr[i] > pivot) {
            Garr[i] = arr[i];
        }
    }

    Larr[lesser] = *quick(Larr);
    Larr[greater] = *quick(Garr);
    int newarr[lesser + equal + greater];
    for (int i = 0; i < lesser; i++) {
        newarr[i] = Larr[i];
    }
    for (int i = 0; i < equal; i++) {
        newarr[lesser + i] = Earr[i];
    }
    for (int i = 0; i < greater; i++) {
        newarr[lesser + equal + i] = Garr[i];
    }
    return newarr;
}

int main(int argc, char *argv[]) {

    int arr[] = {4, 3, 1, 7, 6, 2, 7, 4, 4, 6, 7, 5, 4, 2, 5, 6, 7, 3, 2, 1, 9};

    int length = sizeof(arr) / sizeof(arr[0]);
    arr[21] = *quick(arr);
    printf("Sorted array is: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    return EXIT_SUCCESS;
}
