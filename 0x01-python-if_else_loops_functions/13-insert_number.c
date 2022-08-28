#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *cur;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;
	temp = *head;
	while (temp)
	{
		cur = temp;
		temp = temp->next;
		if (temp->n > number)
			break;
	}
	new->next = cur->next;
	cur->next = new;

	return (new);
}
