For **UNIT 3**

# Part I

This part is not about Python, but about *C* instead - specifically about this code: 

```c
#include <stdio.h> 
int main(int argc, char **argv)
{
    char buf[8]; // buffer for eight characters
    printf("enter name:"); 
    gets(buf); // read from stdio (sensitive function!)
    printf("%s\n", buf); // print out data stored in buf
    return 0; // 0 as return value
}
```
[Reindented and corrected from source]

I've been running this via www.programiz.com 's C Online Compiler. 