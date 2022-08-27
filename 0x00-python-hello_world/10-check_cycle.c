#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp)
	{
		temp = temp->next;
		if (temp == NULL)
			return (0);
		if (temp == list)
			break;
	}
	return (1);
}
