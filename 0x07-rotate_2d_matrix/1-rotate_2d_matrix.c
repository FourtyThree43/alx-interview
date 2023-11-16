#include <stdio.h>
#define N 3

/**
 * rotate_matrix - Rotates a 2D matrix 90 degrees clockwise
 * @matrix: Matrix to rotate
 *
 * Return: None
 */
void rotate_matrix(int matrix[N][N])
{
	int i, j, temp;

	for (i = 0; i < N / 2; i++)
	{
		for (j = i; j < N - i - 1; j++)
		{
			temp = matrix[i][j];

			matrix[i][j] = matrix[N - 1 - j][i];

			matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j];

			matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i];

			matrix[j][N - 1 - i] = temp;
		}
	}

}

/**
 * print_matrix - Prints a 2D matrix
 * @matrix: Matrix to print
 *
 * Return: None
 */
void print_matrix(int matrix[N][N])
{
	int i, j;

	printf("=\n");

	for (i = 0; i < N; i++)
	{
		printf("[");
		for (j = 0; j < N; j++)
		{
			printf("%d", matrix[i][j]);
			if (j < N - 1)
				printf(", ");
		}
		printf("]\n");
	}
}

/**
 * main - Main function
 *
 * Return: Exit status
 */
int main(void)
{
	int matrix[N][N] = {
		{1, 2, 3},
		{4, 5, 6},
		{7, 8 ,9}
	};
	print_matrix(matrix);

	/* Rotate matrix 90 degrees clockwise */
	rotate_matrix(matrix);
	print_matrix(matrix);

	/* Rotate matrix 90 degrees clockwise */
	rotate_matrix(matrix);
	print_matrix(matrix);

	/* Rotate matrix 90 degrees clockwise */
	rotate_matrix(matrix);
	print_matrix(matrix);

	/* Rotate matrix 90 degrees clockwise */
	rotate_matrix(matrix);
	print_matrix(matrix);

	return (0);
}
