#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>

int main()
{
    int *val = mmap((void *)0x0, 4, 3, 0x21, -1, 0);
    // *val = 1000000000;
    *val = 0x3b9aca00;
    fork();
    fork();
    fork();
    fork();
    *val += 0x499602d2;
    printf("%d\n", *val);
    return 0;
}