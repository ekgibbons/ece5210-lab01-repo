#include "ece5210.h"

#include <stdio.h>

int16_t process_sample(int16_t sample_in)
{
    int16_t sample_out = 0;
    float sample_in_f = (float)sample_in;

    // This is just simple pass through, if you want to
    // do any signal processing, start editing here...
    float sample_out_f = sample_in_f; 

    // Convert back to int16_t
    sample_out = (int16_t)sample_out_f;
    return sample_out;
}
