// Hang Zhao
// 2/2/2024
// CS5008 Lab03
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void removeSpace(char *str) {
    int index, k;
    index = 0;

    // Trim leading white spaces
    while (str[index] == ' ' || str[index] == '\t') {
        index++;
    }

    if (index != 0) {
        k = 0;
        while (str[k + index] != '\0') {
            str[k] = str[k + index];
            k++;
        }
        str[k] = '\0'; // Terminate string
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <assembly_file.s>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("No such file");
        return 1;
    }

    char line[256];
    int count_ADD = 0, count_SUB = 0, count_MUL = 0, count_DIV = 0;
    int count_MOV = 0, count_LEA = 0, count_PUSH = 0, count_POP = 0, count_RET = 0;
    int total_cycles = 0;

    while (fgets(line, sizeof(line), file)) {
        removeSpace(line); // Trim leading spaces for accurate comparison

        if (strncasecmp(line, "add", 3) == 0) {
            count_ADD++;
            total_cycles += 1;
        } else if (strncasecmp(line, "sub", 3) == 0) {
            count_SUB++;
            total_cycles += 1;
        } else if (strncasecmp(line, "mul", 3) == 0 || strncasecmp(line, "imul", 4) == 0) {
            count_MUL++;
            total_cycles += 3;
        } else if (strncasecmp(line, "div", 3) == 0 || strncasecmp(line, "idiv", 4) == 0) {
            count_DIV++;
            total_cycles += 24;
        } else if (strncasecmp(line, "mov", 3) == 0) {
            count_MOV++;
            total_cycles += 1;
        } else if (strncasecmp(line, "lea", 3) == 0) {
            count_LEA++;
            total_cycles += 3;
        } else if (strncasecmp(line, "push", 4) == 0) {
            count_PUSH++;
            total_cycles += 1;
        } else if (strncasecmp(line, "pop", 3) == 0) {
            count_POP++;
            total_cycles += 1;
        } else if (strncasecmp(line, "ret", 3) == 0) {
            count_RET++;
            total_cycles += 1;
        }
    }

    fclose(file);

    printf("Instruction counts:\n");
    printf("ADD: %d\n", count_ADD);
    printf("SUB: %d\n", count_SUB);
    printf("MUL: %d\n", count_MUL);
    printf("DIV: %d\n", count_DIV);
    printf("MOV: %d\n", count_MOV);
    printf("LEA: %d\n", count_LEA);
    printf("PUSH: %d\n", count_PUSH);
    printf("POP: %d\n", count_POP);
    printf("RET: %d\n", count_RET);
    printf("\nTotal Instructions: %d\n", count_ADD + count_SUB + count_MUL + count_DIV + count_MOV + count_LEA + count_PUSH + count_POP + count_RET);
    printf("Total Cycles: %d\n", total_cycles);

    return 0;
}