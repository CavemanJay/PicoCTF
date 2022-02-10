#include <stdio.h>
// Reverse engineered source of rev binary using ghidra to rename variables
int main()
{
    size_t bytes_read;
    char flag_file_contents[23];
    char last_char;
    int bytes_read_int;
    FILE *output_file_handle;
    FILE *flag_file_handle;
    int j;
    int i;
    char current_char;

    flag_file_handle = fopen("flag.txt", "r");
    output_file_handle = fopen("rev_this", "a");
    if (flag_file_handle == (FILE *)0x0)
    {
        puts("No flag found, please make sure this is run on the server");
    }
    if (output_file_handle == (FILE *)0x0)
    {
        puts("please run this on the server");
    }
    bytes_read = fread(flag_file_contents, 24, 1, flag_file_handle);
    bytes_read_int = (int)bytes_read;
    if ((int)bytes_read < 1)
    {
        /* WARNING: Subroutine does not return */
        exit(0);
    }
    for (i = 0; i < 8; i = i + 1)
    {
        current_char = flag_file_contents[i];
        fputc((int)current_char, output_file_handle);
    }
    for (j = 8; j < 23; j = j + 1)
    {
        int comp = j & 1U;
        if (comp == 0)
        {
            current_char = flag_file_contents[j] + '\x05';
        }
        else
        {
            current_char = flag_file_contents[j] + -2;
        }
        fputc((int)current_char, output_file_handle);
    }
    current_char = last_char;
    fputc((int)last_char, output_file_handle);
    fclose(output_file_handle);
    fclose(flag_file_handle);
    return;
}