#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <winsock.h>
// int main() {
//   int *p = (int *)malloc(sizeof(int));
//   int *q = (int *)malloc(sizeof(int));
//   int *r = (int *)malloc(sizeof(int));

//   *r = 10;
//   *p = 1;

//   for (*q = 0; *q <= *r; (*q)++) {
//     *p = *p + 1;
//     printf("p:%d q:%d r:%d\n", *p, *q, *r);
//   }
//   return 0;
// }
int main()
{
    char a[8] = {1, 2, 3, 4, 5, 6, 7, 8};

    short *ptr1 = (short *)&a[0]; // short ptr is 2 bytes
    int *ptr2 = (int *)&a[0];     // int ptr is 4 bytes

    printf("0x%X\n", *ptr1); // 16進制：201 (0x0201), LSB先放
    printf("0x%X\n", *ptr2); // 16進制：4030201 (0x04030201), LSB先放

    short b = 0x1234;    // a is a 2-byte variable.
    printf("0x%x\n", b); // Result: 0x1234.

    // printf("0x%x\n", htons(b));
    return 0;
}
