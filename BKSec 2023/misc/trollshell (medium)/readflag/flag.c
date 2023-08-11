#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int random_gen(){
    srand(time(NULL));
    int random_number = rand() % 999;
    return random_number;
}

int main() {
    int firstDigit, digits;
    char realflag[] = "BKSEC{restricted_shells_are_always_fun}";

    char fake1[] = "OXFRP{l0h_gu1ax_gu1f_1f_e34y_sy4t???z4lo3_z4lo3a0g}";
    char fake2[] = "BKSEC{c3VkMF94MW5fZmw0Zw==}";

    int rand = random_gen();

    /* Total number of digits - 1 */
    digits = (int)log10(rand); 

    /* Find first digit */
    firstDigit = (int)(rand / pow(10, digits)); 

    // printf("%d\n", firstDigit);

    if (firstDigit < 6)
    {
        printf("%s\n", fake1);
    }
    else if (firstDigit < 9)
    {
        printf("%s\n", fake2);
    }
    else
    {
        printf("%s\n", realflag);
    } 
}