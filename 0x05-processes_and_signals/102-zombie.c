#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinite_while - never ending loop
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Write a C program that creates 5 zombie processes.
 * Return: displays Zombie process created, PID: ZOMBIE_PID 0 if success
 */
int main(void)
{
	int i;
	pid_t zombiepid;

	for (i = 0; i < 5; i++)
	{
		zombiepid = fork();
		if (zombiepid > 0)
			printf("Zombie process created, PID: %i\n", zombiepid);
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
