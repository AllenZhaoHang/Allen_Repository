// Hang Zhao
// 1/20/2024
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_GAMES 5

void playGame(int gameNumber, int* totalGuesses);

int main() {
    srand(time(NULL)); // Seed for random number generation
    int totalGuesses[MAX_GAMES] = {0};

    for (int i = 0; i < MAX_GAMES; i++) {
        printf("==========================\n");
        printf("CPU Says: Pick a number 1-10\n");
        printf("==========================\n");
        playGame(i, totalGuesses);
    }

    printf("===============================\n");
    printf("| Here are the results of your guessing abilities |\n");
    printf("===============================\n");

    for (int i = 0; i < MAX_GAMES; i++) {
        printf("Game %d took you %d guesses\n", i, totalGuesses[i]);
    }

    return 0;
}

void playGame(int gameNumber, int* totalGuesses) {
    int targetNumber = rand() % 10 + 1;
    int guess;
    int guesses = 0;

    do {
        printf("Make a guess:");
        scanf("%d", &guess);
        guesses++;

        if (guess < targetNumber) {
            printf("No guess higher!\n");
        } else if (guess > targetNumber) {
            printf("No guess lower!\n");
        } else {
            printf("You got it!\n");
        }
    } while (guess != targetNumber);

    totalGuesses[gameNumber] = guesses;
}

