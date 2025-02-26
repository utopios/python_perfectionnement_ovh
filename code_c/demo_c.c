int add_int(int a,int b){return a+b;}
float add_float(float a, float b) {return a + b;}

void add_float_ref(float *a, float *b, float *c) {
    *c = *a + *b;
}

void add_two_array(int* tab1, int* tab2, int* result, int length) {
    for(int i = 0; i < length; i++) {
    result[i] = tab1[i] + tab2[i];
    }
}